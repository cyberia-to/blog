#!/usr/bin/env python3
"""the beat, step one: what changed in the public repositories of cyberia-to, day by day, as a digest.

reads the GitHub API only (stdlib; the token comes from GH_TOKEN, GITHUB_TOKEN or `gh auth token`), public
repositories only, so the digest is the same for every reader and names nothing a visitor cannot open.
for each UTC day in the range it writes ~/.cache/cyber/beats/digest/YYYY-MM-DD.md with three lists, every line
carrying its link: releases published, pull requests merged, commits on each default branch (subject and body).
a day with nothing writes a digest that says so. the writer (AGENTS.md § the daily beat) works from this file.
    python3 scripts/beat_collect.py                       # yesterday, UTC
    python3 scripts/beat_collect.py --day 2026-10-07
    python3 scripts/beat_collect.py --since 2026-09-29 --until 2026-11-17 [--out DIR] [--org cyberia-to]
"""
import argparse, collections, datetime as dt, json, os, subprocess, sys, time, urllib.error, urllib.parse, urllib.request
from pathlib import Path

API = "https://api.github.com"
OUT = Path.home() / ".cache/cyber/beats/digest"
BODY = 700  # characters of a commit or pull request body kept in the digest


def token():
    for k in ("GH_TOKEN", "GITHUB_TOKEN"):
        if os.environ.get(k): return os.environ[k]
    try: return subprocess.run(["gh", "auth", "token"], capture_output=True, text=True, timeout=20).stdout.strip() or None
    except (OSError, subprocess.SubprocessError): return None


TOKEN = token()


def get(path, **q):
    """every page of one GET, as a list of items (search answers are unwrapped)."""
    url = f"{API}/{path}?{urllib.parse.urlencode({**q, 'per_page': 100})}"
    out, tries = [], 0
    while url:
        req = urllib.request.Request(url, headers={"Accept": "application/vnd.github+json", "User-Agent": "beat-collect"})
        if TOKEN: req.add_header("Authorization", f"Bearer {TOKEN}")
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                data, link = json.load(r), r.headers.get("Link", "")
        except urllib.error.HTTPError as e:
            if e.code in (404, 409): return out  # a repository gone or empty
            if e.code in (403, 429) and tries < 6:  # a rate limit: wait as long as the answer says, then ask again
                tries += 1
                wait = int(e.headers.get("Retry-After") or 0) or max(0, int(e.headers.get("X-RateLimit-Reset") or 0) - int(time.time())) + 1
                time.sleep(min(max(wait, 20), 300))
                continue
            sys.exit(f"GitHub API {e.code} on {url}: {e.read()[:200].decode(errors='replace')}")
        tries = 0
        out += data["items"] if isinstance(data, dict) else data
        url = next((p[p.index("<") + 1:p.index(">")] for p in link.split(",") if 'rel="next"' in p), None)
    return out


def excerpt(text):
    t = " ".join((text or "").split())
    return t if len(t) <= BODY else t[:BODY].rsplit(" ", 1)[0] + " …"


def collect(org, since, until):
    lo, hi = f"{since}T00:00:00Z", f"{until}T23:59:59Z"
    days = collections.defaultdict(lambda: {"releases": [], "pulls": [], "commits": collections.defaultdict(list)})
    repos = [r for r in get(f"orgs/{org}/repos", type="public") if r["pushed_at"] >= lo]
    for r in sorted(repos, key=lambda r: r["name"]):
        name = r["name"]
        for c in get(f"repos/{org}/{name}/commits", sha=r["default_branch"], since=lo, until=hi):
            if len(c["parents"]) > 1: continue  # a merge commit carries no change of its own
            at = c["commit"]["committer"]["date"]
            subject, _, body = c["commit"]["message"].partition("\n")
            days[at[:10]]["commits"][name].append((at, c["sha"][:7], subject.strip(), excerpt(body), c["html_url"]))
        for rel in get(f"repos/{org}/{name}/releases"):
            at = rel.get("published_at") or ""
            if lo <= at <= hi and not rel["draft"]:
                days[at[:10]]["releases"].append((at, name, rel["tag_name"], rel["name"] or "", excerpt(rel["body"]), rel["html_url"]))
    day = dt.date.fromisoformat(since)
    while day <= dt.date.fromisoformat(until):  # the search answers at most 1000 items, so it is asked a day at a time
        if day.isoformat() != since: time.sleep(2.5)  # the search allows 30 questions a minute
        for p in get("search/issues", q=f"org:{org} is:pr is:merged is:public merged:{day}"):
            repo = p["repository_url"].rsplit("/", 1)[1]
            at = p["pull_request"]["merged_at"]
            days[at[:10]]["pulls"].append((at, repo, p["number"], p["title"], excerpt(p["body"]), p["html_url"]))
        day += dt.timedelta(days=1)
    return days


def render(day, d):
    n = sum(len(v) for v in d["commits"].values())
    L = [f"# digest · {day} (UTC)", "",
         f"{len(d['releases'])} releases · {len(d['pulls'])} pull requests merged · {n} commits in {len(d['commits'])} repositories", ""]
    L += ["## releases", ""]
    for at, repo, tag, name, body, url in sorted(d["releases"]):
        L += [f"- {repo} `{tag}` {name} — {url}"] + ([f"  > {body}"] if body else [])
    L += ["", "## pull requests merged", ""]
    for at, repo, num, title, body, url in sorted(d["pulls"]):
        L += [f"- {repo} #{num} {title} — {url}"] + ([f"  > {body}"] if body else [])
    L += ["", "## commits on default branches", ""]
    for repo in sorted(d["commits"], key=lambda r: -len(d["commits"][r])):
        L += [f"### {repo} ({len(d['commits'][repo])})", ""]
        for at, sha, subject, body, url in sorted(d["commits"][repo]):
            L += [f"- `{sha}` {subject} — {url}"] + ([f"  > {body}"] if body else [])
        L += [""]
    return "\n".join(L).rstrip() + "\n"


def main():
    yesterday = (dt.datetime.now(dt.timezone.utc).date() - dt.timedelta(days=1)).isoformat()
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--day"); ap.add_argument("--since"); ap.add_argument("--until")
    ap.add_argument("--org", default="cyberia-to"); ap.add_argument("--out", type=Path, default=OUT)
    a = ap.parse_args()
    since = a.day or a.since or yesterday
    until = a.day or a.until or since
    days = collect(a.org, since, until)
    a.out.mkdir(parents=True, exist_ok=True)
    day = dt.date.fromisoformat(since)
    while day <= dt.date.fromisoformat(until):
        d = days[day.isoformat()]
        (a.out / f"{day}.md").write_text(render(day, d))
        print(f"{day}  {len(d['releases']):3} releases  {len(d['pulls']):3} pulls  {sum(len(v) for v in d['commits'].values()):4} commits  {len(d['commits']):3} repos")
        day += dt.timedelta(days=1)
    print(f"→ {a.out}")


if __name__ == "__main__":
    main()

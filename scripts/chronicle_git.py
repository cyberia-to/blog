#!/usr/bin/env python3
"""the chronicle, source s1 (projects/chronicle.md): every repository of cyberia-to and cybercongress as events.

metadata-only clones (--filter=blob:none, bare) into ~/.cache/cyber/chronicle/git/<org>/<repo>.git, fetched again on a
re-run; then one events.jsonl line per: a repository born (its first commit, and its creation on GitHub), archived,
each month's commits on its default branch (count, authors, three subjects), each tag. a summary per org and year.
stdlib only; gh (the owner's login) lists the repositories, private ones included.
    python3 scripts/chronicle_git.py [--orgs cyberia-to cybercongress] [--jobs 6]
"""
import argparse, collections, concurrent.futures as cf, json, subprocess, sys
from pathlib import Path

OUT = Path.home() / ".cache/cyber/chronicle/git"


def sh(*a, cwd=None, timeout=1800):
    r = subprocess.run(a, cwd=cwd, capture_output=True, text=True, timeout=timeout)
    return r.returncode, r.stdout, r.stderr


def repos(org):
    rc, so, se = sh("gh", "api", "--paginate", f"orgs/{org}/repos?type=all&per_page=100", "-q",
                    ".[] | {name, full_name, private, archived, fork, created_at, pushed_at, default_branch, description, ssh_url}")
    if rc: sys.exit(f"gh: {se.strip()}")
    return [json.loads(l) for l in so.splitlines() if l.strip()]


def fetch(r):
    d = OUT / r["full_name"].split("/")[0] / (r["name"] + ".git")
    if d.exists(): rc, _, se = sh("git", "-C", str(d), "fetch", "-q", "--tags", "origin", "+refs/heads/*:refs/heads/*")
    else:
        d.parent.mkdir(parents=True, exist_ok=True)
        rc, _, se = sh("git", "clone", "-q", "--bare", "--filter=blob:none", f"https://github.com/{r['full_name']}.git", str(d))
    return d, (se.strip()[-200:] if rc else "")


def events_of(r, d):
    ev, org = [], r["full_name"].split("/")[0]
    base = {"source": "git", "org": org, "repo": r["name"]}
    ev.append({**base, "at": r["created_at"], "kind": "repo-created", "what": r.get("description") or "", "link": f"https://github.com/{r['full_name']}", "private": r["private"], "fork": r["fork"]})
    if r["archived"]: ev.append({**base, "at": r["pushed_at"], "kind": "repo-archived", "what": "archived (the last push)", "link": f"https://github.com/{r['full_name']}"})
    rc, so, _ = sh("git", "-C", str(d), "log", r["default_branch"] or "HEAD", "--format=%H%x09%aI%x09%an%x09%s", "--no-merges")
    if rc == 0 and so.strip():
        rows = [l.split("\t", 3) for l in so.splitlines() if l.count("\t") >= 3]
        first = rows[-1]
        ev.append({**base, "at": first[1], "kind": "first-commit", "who": first[2], "what": first[3][:200], "link": f"https://github.com/{r['full_name']}/commit/{first[0]}"})
        months = collections.defaultdict(list)
        for h, at, who, subj in rows: months[at[:7]].append((who, subj, h))
        for m, cs in sorted(months.items()):
            who = collections.Counter(c[0] for c in cs)
            # inherited: a fork's upstream history, or commits older than the repository (a history imported with the code) —
            # kept as events, never counted as the team's own work
            inherited = "fork" if r["fork"] else "imported" if m < r["created_at"][:7] else ""
            ev.append({**base, "at": m + "-01", "kind": "month", "commits": len(cs), "authors": dict(who.most_common(8)), "inherited": inherited,
                       "what": " · ".join(c[1][:90] for c in cs[:3]), "link": f"https://github.com/{r['full_name']}/commits/{r['default_branch']}?since={m}-01"})
    rc, so, _ = sh("git", "-C", str(d), "for-each-ref", "refs/tags", "--format=%(refname:short)%09%(creatordate:iso-strict)%09%(subject)")
    for l in so.splitlines():
        t = l.split("\t")
        if len(t) >= 2: ev.append({**base, "at": t[1], "kind": "tag", "what": t[0] + (f" — {t[2][:120]}" if len(t) > 2 and t[2] else ""), "link": f"https://github.com/{r['full_name']}/releases/tag/{t[0]}"})
    return ev


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--orgs", nargs="+", default=["cyberia-to", "cybercongress"]); ap.add_argument("--jobs", type=int, default=6); a = ap.parse_args()
    OUT.mkdir(parents=True, exist_ok=True)
    all_r = [r for o in a.orgs for r in repos(o)]
    print(f"{len(all_r)} repositories", flush=True)
    events, failed = [], []
    with cf.ThreadPoolExecutor(a.jobs) as ex:
        for i, (r, (d, err)) in enumerate(zip(all_r, ex.map(fetch, all_r)), 1):
            if err: failed.append((r["full_name"], err)); print(f"[{i}] {r['full_name']}: {err}", flush=True); continue
            events += events_of(r, d)
            if i % 20 == 0: print(f"[{i}/{len(all_r)}]", flush=True)
    events.sort(key=lambda e: e["at"])
    (OUT / "events.jsonl").write_text("".join(json.dumps(e, ensure_ascii=False) + "\n" for e in events))
    years = collections.defaultdict(lambda: collections.Counter())
    for e in events:
        if e["kind"] == "month": years[(e["org"], e["at"][:4])]["inherited" if e["inherited"] else "own commits"] += e["commits"]
        if e["kind"] == "first-commit": years[(e["org"], e["at"][:4])]["repos born"] += 1
    summary = {"repositories": len(all_r), "failed": failed, "events": len(events),
               "by_year": {f"{o} {y}": dict(c) for (o, y), c in sorted(years.items(), key=lambda kv: (kv[0][1], kv[0][0]))}}
    (OUT / "summary.json").write_text(json.dumps(summary, indent=1, ensure_ascii=False))
    print(json.dumps(summary["by_year"], ensure_ascii=False)); print(f"{len(events)} events, {len(failed)} failed → {OUT}")


if __name__ == "__main__":
    main()

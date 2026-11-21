#!/usr/bin/env python3
"""the beat, the check: every beat and news item of a date range against the method in AGENTS.md § the daily beat.

checks, per file: frontmatter, tags and title against the file name; no bold, italics, emoji, relative time words
or headings beyond the title and `## sources`; a news item has 90 to 360 words of prose and a sources list.
across files: every news item is linked from the beat of its day and every beat link has its file.
every GitHub URL of cyberia-to exists and its repository is public. with --numbers, every number in the prose of a
news item appears in the text of a source it cites. with --site, every wiki-link that is not a news item resolves
to a published page with content: optica resolves a wiki-link by the last path segment of a page or by an alias,
and publishes a name that answers to nothing as an empty stub page, so the check reads the site's
search-index.json and counts only entries that carry an excerpt or tags.
stdlib; the token comes from GH_TOKEN, GITHUB_TOKEN or `gh auth token`; API answers are cached in
~/.cache/cyber/beats/src/. exits 1 when a problem is found.
    python3 scripts/beat_verify.py . --since 2026-09-29 --until 2026-11-17 --numbers --site https://cyberia.blog
    python3 scripts/beat_verify.py . --only '2026_11_19*'
"""
import argparse, fnmatch, hashlib, json, os, re, subprocess, sys, urllib.error, urllib.parse, urllib.request
from pathlib import Path

CACHE = Path.home() / ".cache/cyber/beats/src"
ORG = "cyberia-to"
EMOJI = re.compile("[\U0001F300-\U0001FAFF☀-➿⬀-⯿️]")
URL = re.compile(r"https?://[^\s)\]>]+")
WIKI = re.compile(r"\[\[([^\]|]+)(?:\|[^\]]*)?\]\]")
NUM = re.compile(r"(?<![\w#/.-])\d[\d,.]*\d|(?<![\w#/.-])\d")
TIME_WORDS = re.compile(r"\b(today|this morning|tomorrow|yesterday|tonight)\b", re.I)


def token():
    for k in ("GH_TOKEN", "GITHUB_TOKEN"):
        if os.environ.get(k): return os.environ[k]
    try: return subprocess.run(["gh", "auth", "token"], capture_output=True, text=True, timeout=20).stdout.strip() or None
    except (OSError, subprocess.SubprocessError): return None


TOKEN = token()


def api(path, raw=False):
    """the text of one GitHub API answer, or 'HTTP<code>'; cached on disk."""
    key = CACHE / hashlib.sha1((path + str(raw)).encode()).hexdigest()
    if key.exists(): return key.read_text()
    headers = {"User-Agent": "beat-verify",
               "Accept": "application/vnd.github.raw+json" if raw else "application/vnd.github+json"}
    if TOKEN: headers["Authorization"] = f"Bearer {TOKEN}"
    try:
        with urllib.request.urlopen(urllib.request.Request(f"https://api.github.com/{path}", headers=headers), timeout=60) as r:
            text = r.read().decode(errors="replace")
    except urllib.error.HTTPError as e:
        text = f"HTTP{e.code}"
    CACHE.mkdir(parents=True, exist_ok=True); key.write_text(text)
    return text


def public(repo):
    t = api(f"repos/{ORG}/{repo}")
    return not t.startswith("HTTP") and json.loads(t).get("private") is False


def source_text(url):
    """(ok, text) for a GitHub URL of the org; (None, '') for a URL this check does not read."""
    m = re.match(rf"https://github\.com/{ORG}/([^/#?]+)(?:/(.*))?$", url.rstrip(".,;"))
    if not m: return None, ""
    repo, rest = m.group(1), (m.group(2) or "").split("#")[0].rstrip("/")
    if not public(repo): return False, f"repository {repo} is missing or not public"
    if not rest: return True, ""
    kind, _, tail = rest.partition("/")
    if kind == "pull":
        t = api(f"repos/{ORG}/{repo}/pulls/{tail.split('/')[0]}")
        if t.startswith("HTTP"): return False, t
        j = json.loads(t); return True, f"{j['title']}\n{j.get('body') or ''}\nbase {j['base']['ref']} merged {j.get('merged_at')}"
    if kind == "commit":
        t = api(f"repos/{ORG}/{repo}/commits/{tail}")
        if t.startswith("HTTP"): return False, t
        j = json.loads(t); return True, j["commit"]["message"] + "\n" + "\n".join(f.get("patch", "")[:20000] for f in j.get("files", [])[:40])
    if kind in ("blob", "tree"):
        ref, _, path = urllib.parse.unquote(tail).partition("/")
        q = lambda p, r: api(f"repos/{ORG}/{repo}/contents/{urllib.parse.quote(p)}?ref={urllib.parse.quote(r)}", raw=(kind == "blob"))
        t = q(path, ref)
        if t.startswith("HTTP") and "/" in path:  # a branch name with a slash, e.g. release/phase1
            a, _, b = path.partition("/"); t = q(b, f"{ref}/{a}")
        return (not t.startswith("HTTP")), t
    if kind == "releases":
        t = api(f"repos/{ORG}/{repo}/releases/tags/{urllib.parse.quote(tail.split('tag/')[-1])}")
        if t.startswith("HTTP"): return False, t
        j = json.loads(t); return True, f"{j.get('name')}\n{j.get('body') or ''}\n" + " ".join(a["name"] for a in j.get("assets", []))
    if kind in ("compare", "actions"): return True, ""
    return None, ""


def slug(name): return re.sub(r"\s+", "-", name.strip().lower())


def published_names(site):
    """every name a wiki-link resolves by on the site: the last path segment and the aliases of each page with
    content. a stub page carries neither excerpt nor tags."""
    req = urllib.request.Request(site.rstrip("/") + "/search-index.json", headers={"User-Agent": "beat-verify"})
    with urllib.request.urlopen(req, timeout=120) as r: index = json.load(r)
    names = set()
    for e in index:
        if not (e.get("excerpt") or e.get("tags")): continue
        names.add(urllib.parse.unquote(e["url"].rstrip("/").rsplit("/", 1)[-1]).lower())
        names.update(slug(x) for x in e.get("aliases") or [])
    return names


def norm(s): return re.sub("[,_   ]", "", s)


def check(p, a, problems, linked, wikis):
    def bad(msg): problems.append(f"{p.parent.name}/{p.name}: {msg}")
    s = p.read_text(); isnews = p.parent.name == "news"; date = p.name[:10].replace("_", "-")
    m = re.match(r"---\ntags: ([^\n]+)\ndate: (\d{4}-\d\d-\d\d)\n---\n# ([^\n]+)\n", s)
    if not m: return bad("frontmatter or title shape")
    tags, fdate, title = m.groups()
    if fdate != date: bad(f"date {fdate} differs from the file name")
    if not tags.startswith("news, " if isnews else "blog, beat, "): bad(f"tags start: {tags}")
    if isnews and re.search(r"(^|,\s*)blog(\s*,|$)", tags): bad("a news item carries the tag blog")
    if not isnews and title != f"the beat · {date}": bad(f"beat title: {title}")
    body = s[m.end():]
    prose, _, sources = body.partition("\n## sources")
    if isnews and not sources.strip(): bad("no ## sources")
    for h in re.findall(r"^#+ .*$", body, re.M):
        if h != "## sources": bad(f"extra heading: {h}")
    if "**" in s or re.search(r"(?<![\w*])\*[^*\s][^*\n]*\*(?![\w*])", prose): bad("bold or italics")
    if EMOJI.search(s): bad(f"emoji: {EMOJI.findall(s)[:3]}")
    for w in TIME_WORDS.findall(prose): bad(f"time word: {w}")
    words = len(re.sub(r"\[\[[^\]|]+\|", "", prose).split())
    if isnews and not 90 <= words <= 360: bad(f"{words} words")
    for t in WIKI.findall(s):
        if re.match(r"\d{4}-\d\d-\d\d-", t):
            linked.add(t)
            if not (a.root / "news" / (t.replace("-", "_") + ".md")).exists(): bad(f"beat links a missing news item: {t}")
        else: wikis.setdefault(slug(t), set()).add(p.name)
    texts = []
    for u in sorted(set(u.rstrip(".,;") for u in URL.findall(s))):
        ok, text = source_text(u)
        if ok is False: bad(f"source: {u} — {text[:60]}")
        elif ok: texts.append(text)
        elif f"github.com/{ORG}" in u: bad(f"unread GitHub URL shape: {u}")
    if a.numbers and isnews:
        hay = norm("\n".join(texts) + "\n" + title)
        cited = set(re.findall(r"#(\d+)", sources)) | set(re.findall(r"/pull/(\d+)", sources))
        clean = re.sub(r"`[^`]*`", " ", re.sub(r"\[\[[^\]]*\]\]", " ", prose))
        miss = []
        for n in sorted(set(NUM.findall(clean)), key=len, reverse=True):
            k = norm(n).rstrip(".")
            if re.fullmatch(r"20\d\d-?\d*-?\d*", k) or k in cited or len(k) == 1: continue
            if k not in hay and k.replace(".", "") not in hay: miss.append(n)
        if miss: bad(f"numbers absent from the cited sources: {', '.join(miss)}")


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("root", type=Path, help="the blog checkout")
    ap.add_argument("--since", default="0000-00-00"); ap.add_argument("--until", default="9999-99-99")
    ap.add_argument("--only", help="glob over file names, e.g. '2026_11_19*'")
    ap.add_argument("--numbers", action="store_true", help="every number of a news item appears in a cited source")
    ap.add_argument("--site", help="published site whose search index resolves wiki-links, e.g. https://cyberia.blog")
    a = ap.parse_args()
    lo, hi = a.since.replace("-", "_"), a.until.replace("-", "_")
    files = sorted(p for d in ("news", "blog") for p in (a.root / d).glob("20*.md") if lo <= p.name[:10] <= hi)
    if a.only: files = [p for p in files if fnmatch.fnmatch(p.name, a.only)]
    news = {p.stem.replace("_", "-"): p for p in files if p.parent.name == "news"}
    beats = {p.stem.replace("_", "-") for p in files if p.parent.name == "blog"}
    problems, linked, wikis = [], set(), {}
    for p in files: check(p, a, problems, linked, wikis)
    for k, p in news.items():
        if k not in linked: problems.append(f"news/{p.name}: no beat links this news item")
        if k[:10] not in beats: problems.append(f"news/{p.name}: its day has no beat")
    if a.site:
        pages = published_names(a.site)
        for t, where in sorted(wikis.items()):
            if t not in pages: problems.append(f"[[{t}]] answers to no published page (stub) — {', '.join(sorted(where))}")
    print(f"{len(news)} news · {len(beats)} beats · {len(problems)} problems")
    for x in problems: print(" -", x)
    print("\nwiki-links (other than news):", ", ".join(f"{t}×{len(v)}" for t, v in sorted(wikis.items(), key=lambda kv: -len(kv[1]))))
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()

#!/usr/bin/env bash
# the alarm of cyberia.blog: one open issue labelled publish-failing in this repo.
#   alert.sh raise "<what is wrong>"   opens the issue, or comments on the open one
#   alert.sh clear                     closes it once a publish has landed and been verified
set -euo pipefail
REPO="${GITHUB_REPOSITORY:?}"
RUN="${GITHUB_SERVER_URL:-https://github.com}/${REPO}/actions/runs/${GITHUB_RUN_ID:?}"
LABEL=publish-failing
open=$(gh issue list -R "$REPO" --label "$LABEL" --state open --json number -q '.[].number')
case "${1:-}" in
  raise)
    msg="${2:-publish failed}"
    if [ -n "$open" ]; then
      for n in $open; do gh issue comment "$n" -R "$REPO" --body "$msg — $RUN"; done
    else
      gh issue create -R "$REPO" --label "$LABEL" --title "cyberia.blog is not receiving builds" --body "$msg — $RUN

This issue closes itself on the next publish whose build https://cyberia.blog/build.txt serves."
    fi ;;
  clear)
    for n in $open; do gh issue close "$n" -R "$REPO" --comment "published and verified — $RUN"; done ;;
  *) echo "usage: alert.sh raise <message> | clear" >&2; exit 2 ;;
esac

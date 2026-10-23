#!/usr/bin/env nu
# sync.nu — bootstrap a local cyber workspace.
#
# Reads subgraphs.toml, clones every declared repo as a sibling
# of this repo (under ~/cyber/<name>) if missing, fetches if present.
# A cloned repo may carry its own subgraphs.toml naming its children
# (cyberia/subgraphs.toml → cyberia-my, …); those are cloned in turn,
# so the walk covers the whole tree, not only the root census.
#
# Usage:
#   nu scripts/sync.nu                # public + private (auth via gh)
#   nu scripts/sync.nu --public-only  # skip private and local-only repos
#   nu scripts/sync.nu --fetch        # only fetch (don't clone missing)
#   nu scripts/sync.nu --shallow      # depth-1 clones (CI)
#   nu scripts/sync.nu --list         # print the tree, touch nothing

def main [
    --public-only   # skip private and local-only subgraphs
    --fetch         # only fetch existing checkouts; do not clone missing
    --shallow       # clone with --depth 1
    --list          # print what would be synced; no git
    --org: string = "cyberia-to"
] {
    let ws_root = (workspace-root)
    let parent = ($ws_root | path dirname)
    let root_name = ($ws_root | path basename)

    print $"workspace: ($parent)"

    mut queue = (active-decls (load-declarations $ws_root) $public_only | where name != $root_name)
    mut seen = [$root_name]
    mut cloned = 0
    mut fetched = 0
    mut skipped = 0
    mut listed = 0
    while ($queue | length) > 0 {
        let d = ($queue | first)
        $queue = ($queue | skip 1)
        if $d.name in $seen { continue }
        $seen = ($seen | append $d.name)
        let target = ($parent | path join $d.name)
        let result = if $list {
            print $"  ($d.name) ← ($d.under? | default "root")"
            "listed"
        } else {
            sync-one $d $target $org $fetch $shallow
        }
        if $result == "cloned" { $cloned = $cloned + 1 }
        if $result == "fetched" { $fetched = $fetched + 1 }
        if $result == "skipped" { $skipped = $skipped + 1 }
        if $result == "listed" { $listed = $listed + 1 }
        # the repo's own census, read after the clone so a fresh checkout counts
        let nested = ($target | path join "subgraphs.toml")
        if ($nested | path exists) {
            let kids = (active-decls (load-declarations $target) $public_only
                | where name != $d.name
                | each {|k| $k | merge {under: $d.name}})
            $queue = ($queue | append $kids)
        }
    }
    print ""
    if $list {
        print $"($listed) subgraphs"
    } else {
        print $"done. cloned=($cloned) fetched=($fetched) skipped=($skipped)"
    }
}

def active-decls [decls, public_only: bool] {
    $decls
        | where ($it.archived? | default false) != true
        | where ($it.orphan? | default false) != true
        | where {|d|
            if $public_only {
                (($d.visibility? | default "public") == "public") and (($d."local-only"? | default false) != true)
            } else { true }
        }
}

def sync-one [d, target: string, org: string, fetch: bool, shallow: bool] {
    let repo = ($d.repo? | default $d.name)
    if ($target | path exists) {
        if ($"($target)/.git" | path exists) {
            print $"▸ fetch ($d.name)"
            ^git -C $target fetch --quiet
            "fetched"
        } else {
            print $"  skip ($d.name) — directory exists but is not a git repo"
            "skipped"
        }
    } else if $fetch {
        print $"  skip ($d.name) — missing (re-run without --fetch to clone)"
        "skipped"
    } else {
        let url = $"https://github.com/($org)/($repo).git"
        print $"▸ clone ($d.name) ← ($url)"
        let depth_args = if $shallow { ["--depth" "1"] } else { [] }
        try {
            ^git clone --quiet ...$depth_args $url $target
            "cloned"
        } catch {
            print $"  failed to clone ($d.name) — likely private. authenticate with `gh auth login` and retry"
            "skipped"
        }
    }
}

def workspace-root [] {
    let cwd = (pwd)
    if ($"($cwd)/workspace.toml" | path exists) {
        $cwd
    } else {
        error make {msg: "workspace.toml not found; run from the cyberia-blog repo root"}
    }
}

# the census of a directory: its subgraphs.toml (the root's, or a subgraph's own)
def load-declarations [root: string] {
    let path = $"($root)/subgraphs.toml"
    if not ($path | path exists) { return [] }
    let data = (open $path)
    let key = if ($data | get -o subgraph | is-not-empty) { "subgraph" } else { "subgraphs" }
    $data | get $key | where ($it.name? | is-not-empty)
}

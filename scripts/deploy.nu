# Deploy the built graph → the front that serves cyberia.blog, /var/www/html/cyberia.blog/
#
#   nu scripts/build.nu --public-only
#   nu scripts/deploy.nu
#
# the target is the address cyberia.blog resolves to; FRONT_HOST overrides it.
# publishing goes through the Publish workflow. a hand deploy carries no build.txt stamp,
# so Watch reports the site out of step until the next publish lands.

def main [] {
  let root = (
    if ($"($env.PWD)/publish.toml" | path exists) { $env.PWD }
    else { error make {msg: "run from cyberia-blog root"} }
  )
  let build = $"($root)/build"
  if not ($"($build)/index.html" | path exists) {
    error make {msg: "build/index.html missing — run: nu scripts/build.nu --public-only"}
  }

  let host = if ($env.FRONT_HOST? | is-not-empty) { $env.FRONT_HOST } else {
    let ips = (^dig +short cyberia.blog A | lines | where {|l| $l =~ '^\d+\.\d+\.\d+\.\d+$' } | uniq)
    if ($ips | length) != 1 {
      error make {msg: $"cyberia.blog resolves to [($ips | str join ', ')]; set FRONT_HOST to the primary front"}
    }
    $ips | first
  }
  let target = $"cyber@($host):/var/www/html/cyberia.blog/"

  print $"→ rsync → ($target)"
  ^rsync -az --delete $"($build)/" $target
  print "✓ deployed → https://cyberia.blog/"
}

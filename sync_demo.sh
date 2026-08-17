#!/usr/bin/env bash
# ============================================================
# Sync the immersive demo from its source of truth into the
# deployed site, then re-apply the two deploy-only patches.
#
#   source : Trading/web-studio/          (clean, client-reusable)
#   deploy : everbuilt/demo/immersive/    (adds the "concept demo" badge)
#
# Run from the everbuilt/ directory:  ./sync_demo.sh
# ============================================================
set -euo pipefail

SRC="../web-studio/"
DEST="demo/immersive/"

[ -d "$SRC" ] || { echo "✗ source not found: $SRC"; exit 1; }

rsync -a --delete --exclude 'README.md' --exclude '.DS_Store' "$SRC" "$DEST"
echo "✓ copied $SRC → $DEST"

python3 - <<'PY'
import pathlib, sys

html = pathlib.Path("demo/immersive/index.html")
css  = pathlib.Path("demo/immersive/styles.css")

BADGE = '''<!-- DEPLOY-ONLY: this badge exists in everbuilt/demo/immersive, not in the
     Trading/web-studio source. See that README before re-syncing. -->
<a class="demo-badge" href="/work/immersive.html">
  <i></i> Concept demo &mdash; built by Everbuilt Studio
</a>

<div class="rail" aria-hidden="true"><i id="railFill"></i></div>'''

BADGE_CSS = '''/* =========================================================
   DEPLOY-ONLY: "this is a concept demo" badge + way back to
   everbuiltstudio.com. Not present in the web-studio source.
   ========================================================= */
.demo-badge{
  position:fixed;left:var(--pad);top:74px;z-index:95;
  display:inline-flex;align-items:center;gap:9px;
  font-size:10.5px;letter-spacing:.16em;text-transform:uppercase;color:var(--dim);
  background:rgba(9,9,12,.6);backdrop-filter:blur(16px);-webkit-backdrop-filter:blur(16px);
  border:1px solid var(--line);border-radius:100px;padding:8px 16px;
  transition:color .35s,border-color .35s;
}
.demo-badge i{width:5px;height:5px;border-radius:50%;background:#FF5A28}
.demo-badge:hover{color:var(--ink);border-color:var(--line-strong,rgba(242,240,236,.32))}
@media(max-width:620px){.demo-badge{font-size:9.5px;padding:7px 13px;top:66px}}

/* =========================================================
   SCENE STYLE SWITCH'''

s = html.read_text(encoding="utf-8")
anchor = '<div class="rail" aria-hidden="true"><i id="railFill"></i></div>'
if "demo-badge" in s:
    print("• badge already present in index.html")
elif anchor in s:
    html.write_text(s.replace(anchor, BADGE, 1), encoding="utf-8")
    print("✓ re-applied badge markup")
else:
    sys.exit("✗ rail anchor missing in index.html — source layout changed, patch by hand")

c = css.read_text(encoding="utf-8")
css_anchor = '''/* =========================================================
   SCENE STYLE SWITCH'''
if ".demo-badge" in c:
    print("• badge CSS already present")
elif css_anchor in c:
    css.write_text(c.replace(css_anchor, BADGE_CSS, 1), encoding="utf-8")
    print("✓ re-applied badge CSS")
else:
    sys.exit("✗ style-switch anchor missing in styles.css — patch by hand")
PY

echo "✓ demo synced. Preview: python3 -m http.server 4713 --directory ."

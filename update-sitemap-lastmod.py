# -*- coding: utf-8 -*-
"""
Rewrite <lastmod> in sitemap.xml from each page's real last-commit date in git.

Why: sitemap.xml is hand-maintained here (no build step), so its lastmod values drifted
away from reality — as of 2026-07-31, 156 of 157 entries still declared 2026-07-02/04/10
while the files had actually been rewritten on 2026-07-20 (Phase 1/2 work). Telling Google
a page hasn't changed since early July is the opposite of what you want on a site with an
indexation problem.

Git commit date is used rather than filesystem mtime: mtime gets rewritten by clones and
checkouts, git history does not.

Usage:  python update-sitemap-lastmod.py [--dry-run]
Only touches sitemap.xml in this directory.
"""
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
SITEMAP = os.path.join(ROOT, "sitemap.xml")
DRY = "--dry-run" in sys.argv

_cache = {}


def git_last_commit_date(rel_path):
    """Last commit date (YYYY-MM-DD) for a file, or None if untracked/unknown."""
    if rel_path in _cache:
        return _cache[rel_path]
    try:
        out = subprocess.run(
            ["git", "log", "-1", "--format=%cs", "--", rel_path],
            cwd=ROOT, capture_output=True, text=True, timeout=30,
        )
        date = out.stdout.strip() or None
    except Exception:
        date = None
    _cache[rel_path] = date
    return date


def local_path_for(loc):
    rel = loc.split("elitebonushub.bet/", 1)[-1].strip()
    return rel or "index.html"


def main():
    xml = open(SITEMAP, encoding="utf-8").read()
    blocks = re.findall(r"(?s)<url>.*?</url>", xml)
    changed = unchanged = skipped = 0

    def fix_block(block):
        nonlocal changed, unchanged, skipped
        loc_m = re.search(r"<loc>\s*(.*?)\s*</loc>", block, re.S)
        lm_m = re.search(r"<lastmod>\s*(.*?)\s*</lastmod>", block, re.S)
        if not loc_m or not lm_m:
            skipped += 1
            return block
        rel = local_path_for(loc_m.group(1))
        if not os.path.exists(os.path.join(ROOT, rel.replace("/", os.sep))):
            skipped += 1
            return block
        new_date = git_last_commit_date(rel)
        if not new_date:
            skipped += 1
            return block
        old_date = lm_m.group(1)
        if new_date == old_date:
            unchanged += 1
            return block
        changed += 1
        print(f"  {rel:<52} {old_date} -> {new_date}")
        return block.replace(f"<lastmod>{old_date}</lastmod>", f"<lastmod>{new_date}</lastmod>", 1)

    out = xml
    for b in blocks:
        out = out.replace(b, fix_block(b), 1)

    print(f"\nurls: {len(blocks)}  updated: {changed}  already correct: {unchanged}  skipped: {skipped}")
    if DRY:
        print("dry run - sitemap.xml not written")
        return
    if changed:
        open(SITEMAP, "w", encoding="utf-8", newline="\n").write(out)
        print("wrote sitemap.xml")
    else:
        print("nothing to write")


if __name__ == "__main__":
    main()

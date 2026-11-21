# Edit the public explanations without rewriting the science

The editable source is `content/` — **not** the generated `docs/*.html` pages.

| File | What it controls |
| --- | --- |
| `site.json` | Homepage heading, introductory paragraph, concept cards and research path |
| `home.md` | Homepage narrative |
| `matter.md` | Illustrated 2O/2I and hadron-source guide; its equations, source links and captions can be edited independently |
| `ideas.md` | Question-led introductions adapted from the X-post series; all scientific claims and source links are editable |
| `framework.md` | Main plain-language technical explanation |
| `pathways.md` | The six guided routes through the papers |
| `observables.md` | What measurements and predictions must ultimately be explained |
| `updates.md` | Current source integration, its scope and remaining obligations |
| `glossary.md` | Definition of terms for scientifically curious readers |
| `protocols/*.md` | Original verification protocol sources (not rewritten by website editing) |

The new **2O/2I matter geometry** page is generated from `content/matter.md`, with images in `docs/figures/`. The 600-cell illustration can be recreated with `python scripts/build_polyhedral_figure.py` from the exact Paper I-B quaternions.

The **Key ideas** page is generated directly from `content/ideas.md`. Headings become browseable anchors automatically. Three source-provided Hurwitz particle-split PNGs are included in `docs/figures/` with the original attribution and a clear diagnostic-vs-physical-reading note. The other X-post images remain outside the repository.

All other site material (paper catalog, audit browser, source-label anchors, geometry network, PDF files, full archives) comes from a versioned research release and should not be rewritten editorially.

## Publish text edits on GitHub

Edit a Markdown file on GitHub, commit to `main`, and the Pages Actions workflow runs `scripts/render_content.py` followed by `scripts/check_site.py`. The public HTML is rebuilt and redeployed. This requires the repository's **Settings → Pages → Source: GitHub Actions**.

For local preview:

```bash
python3 -m pip install -r requirements-edit.txt
python3 scripts/render_content.py
python3 scripts/check_site.py
python3 -m http.server 8000 --directory docs
```

Then browse `http://localhost:8000/`.

## Future scientific updates

A new source snapshot requires **all matching archive versions**. Use `scripts/refresh_framework.py` with four ZIP paths; the script checks the new manuscript inventory, verifies 31 active source/PDF hashes, matches the DAG's source/audit archive hashes and regenerates browser indices. It preserves the original files byte-for-byte. It does not rewrite these explanatory Markdown files: **revise explanations separately based on the new release notes, then increment the website filename to v1_W+1.**

The current site uses PapersMinimal v3.077 / ProofChainAudits v1.83 / DAG v1.223 / S³ network v1.49. The 55 newly added v3.077 labels are only source-integrated; they are not globally E3/E4 certified by the matching atlas.

**Writing standard:** accessible and precise, neither inaccessible academic shorthand nor childish analogy. Ask which observable is explained by an operator; preserve the theorem's domain, action/source gates and independent status. Never call a decay rate or Newton coupling 'derived' when only a conditional finite comparison has been established.

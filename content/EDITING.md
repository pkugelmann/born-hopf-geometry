# Editing the public explanations

This directory is the **editable source of public-facing explanatory content**, separate from the mathematical manuscript archive.

- `site.json` controls the homepage headline, introduction, three concept cards, explanatory path, and status summary. Edit text values only unless intentionally changing structure.
- `home.md` controls the narrative introduction below the homepage cards.
- `framework.md` controls the long guided explanation, including its source links and section titles.
- `observables.md` controls the question-led explanation of physical tests and remaining bridges.
- `glossary.md` controls the vocabulary page.

## Replacing text directly on GitHub

When GitHub Pages is configured to deploy with **GitHub Actions**, edit any Markdown file through GitHub's web editor and commit to `main`. The publishing workflow automatically regenerates the HTML and publishes the site; **no HTML editing, software installation, or manual copy of the whole archive is needed**.

For a local preview:

```bash
python3 -m pip install -r requirements-edit.txt
python3 scripts/render_content.py
python3 scripts/check_site.py
python3 -m http.server 8000 --directory docs
```

Open `http://localhost:8000/`.

## From future ChatGPT conversations

Supply the current repository ZIP or the changed `content/` files plus any new research archive. Ask: **“Update the public website from the current Born–Hopf framework; preserve the source/claim distinction; increment Paper00-GitHubPage-v1_W; provide replacement files.”** The content can then be reviewed and replaced in the GitHub repository without reconstructing the website.

The manuscript catalog is independently generated from the versioned paper archive and recorded in `docs/data/manifest.json`. Changing explanations does not rewrite paper PDF/TeX bytes or their hashes. A true research update must also refresh the paper library and provenance metadata; the narrative is **not** a substitute for the technical record.

**Editorial rule:** explain physical questions in accessible but precise language. Never infer that a geometric object has been physically realized merely because a mathematical construction exists. Keep open obligations visible, with links to the source papers. Do not use childlike analogies or present conditional calculations as measured predictions.

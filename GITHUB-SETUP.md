# Publish and maintain the Born–Hopf website on GitHub

This package includes an **automatically publishing GitHub Pages workflow**. It has not been pushed or published to a GitHub account from ChatGPT.

## First publication

1. Create a public GitHub repository named `born-hopf-geometry` (or another name), without initializing a README.
2. Extract `Paper00-GitHubPage-v1_1.zip` and open a terminal **inside** the extracted directory.
3. Use these commands, replacing `YOUR-USERNAME`:

   ```sh
   git init
   git add .
   git commit -m "Publish Born–Hopf research site and editable guide"
   git branch -M main
   git remote add origin https://github.com/YOUR-USERNAME/born-hopf-geometry.git
   git push -u origin main
   ```

4. On GitHub, open **Settings → Pages → Build and deployment → Source: GitHub Actions**. The supplied `.github/workflows/pages.yml` automatically installs the Markdown renderer, regenerates the site, checks links and manuscript SHA-256 hashes, and deploys `docs/` after a push to `main`.
5. See the actual deployment URL in **Settings → Pages** or in the workflow run. A project repository normally uses `https://YOUR-USERNAME.github.io/born-hopf-geometry/`, but verify the real URL before sharing it.

Do not choose 'Deploy from a branch' if you want Markdown changes to publish **without generating HTML yourself**. Branch mode can display the already generated `docs/`, but does not automatically rebuild pages from `content/*.md`.

## Update the explanation using GitHub itself

After the site is online, open one of the files in [`content/`](content/EDITING.md), click the GitHub pencil icon, edit the text and commit. GitHub Actions will rebuild and publish automatically. The larger paper and audit archive remains untouched.

In a future ChatGPT conversation, you can upload the current repository ZIP or relevant Markdown files and request a new website revision. Use versions `Paper00-GitHubPage-v1_2`, `v1_3`, etc., and replace the edited files in your GitHub repository. Ask for updates to source files and a new ZIP rather than having to regenerate the site by hand.

For a local preview: install `requirements-edit.txt`, run `python3 scripts/render_content.py`, then `python3 scripts/check_site.py`, and serve `docs/` with `python3 -m http.server 8000 --directory docs`.

## Updating actual papers and provenance

Do **not** paste a revised abstract into the website while leaving outdated PDF/TeX source and version metadata behind. The paper library and hashes are managed separately:

```sh
python3 scripts/refresh_manuscripts.py /path/to/Paper00-PapersMinimal-v3_059.zip
python3 scripts/render_content.py
python3 scripts/check_site.py
```

The refresh script reads the new 31-paper inventory, verifies hashes and replaces the old manuscript files; it preserves the editorial Markdown, audit archive and geometry diagrams. Review `docs/data/manifest.json` and change release metadata when new audit/DAG/network archives are adopted. A claim's verification status cannot be inferred from a filename revision.

## Original release archives

The current original `Paper00-DAGAtlas-v1_215.zip` is approximately **205 MB** and must not be committed as a normal Git blob. Add it as a **GitHub Release asset**, with the original `Paper00-PapersMinimal-v3_058.zip`. Both are enumerated with hashes in `RELEASE-ORIGINALS.md`.

Using the GitHub website: **Releases → Draft a new release → attach binaries**. Or, on a machine where GitHub CLI `gh` is authenticated and the original files exist:

```sh
gh release create v3.058 \
  ./Paper00-PapersMinimal-v3_058.zip \
  ./Paper00-DAGAtlas-v1_215.zip \
  --title "Born–Hopf Geometry source snapshot v3.058" \
  --notes "Scientific source and current proof-dependency atlas; see explicit validation scope."
```

The supplied originals might have `(1)` in their local filename. Rename a **local copy** first, or pass the actual path. Renaming does not change bytes/hashes. When release URLs exist, insert **real, verified** links into `docs/downloads.html`; the package intentionally does not invent them.

## Permissions, safety and research transparency

- Publishing and the GitHub account authorization are the owner's actions; do not share personal access tokens in chat or the repository.
- Public Pages and repository content are visible to everyone. Review the original manuscript and audit materials before publishing.
- Papers and historical audit reports keep their original versioned names and scope.
- Do not mark a claim experimentally verified merely because an operator exists or a finite computational check passes.
- The author must select licensing explicitly. No license is silently granted.

GitHub official instructions: https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site

# Publishing Born–Hopf Geometry on the existing GitHub repository

**Repository:** `https://github.com/pkugelmann/born-hopf-geometry` (branch `main`).

This is an **update**, not a new repository: `Paper00-GitHubPage-v1_2.zip` contains the complete replacement for the GitHub Pages website and research library, plus an upload script.

## One terminal upload

On macOS, Linux, or Windows with WSL/Git Bash, after downloading the ZIP into `~/Downloads`:

```bash
mkdir -p ~/born-hopf-update && unzip -o ~/Downloads/Paper00-GitHubPage-v1_2.zip -d ~/born-hopf-update && bash ~/born-hopf-update/publish.sh
```

The upload script clones the existing `main`, safely replaces only the managed site, content, scripts, workflows and root website metadata, validates hashes and internal links again, commits, and pushes. It **does not reset Git history** or delete unrelated files at the repository root. Your existing Git authentication must allow `git push` to `pkugelmann/born-hopf-geometry`. If GitHub prompts for credentials, authenticate via Git Credential Manager or `gh auth login` followed by `gh auth setup-git` (when GitHub CLI is installed); use a token rather than your GitHub account password for HTTPS.

To inspect changes without committing/pushing, use:

```bash
bash ~/born-hopf-update/publish.sh --dry-run
```

For a ZIP saved to another location, substitute its actual path. Only archives you explicitly downloaded locally are accessed; the script does not fetch an unpublished project archive.

## Enable GitHub Pages once

In your repository, open **Settings → Pages**. Under **Build and deployment**, select **GitHub Actions** as the Source. The included `.github/workflows/pages.yml` installs the Markdown renderer, regenerates public HTML, validates the paper and archive hashes and deploys `docs/`. A separate workflow validates pull requests.

When the Actions workflow succeeds, the expected published address is `https://pkugelmann.github.io/born-hopf-geometry/`. Publishing is performed by GitHub; creating this ZIP alone does not make the site live.

If the workflow does not appear, check that the hidden `.github/workflows/` directory was committed. The terminal upload includes hidden files automatically.

## Editable text and scientific snapshots

**Replace explanations:** edit `content/site.json`, `content/framework.md`, `content/home.md`, `content/observables.md`, `content/pathways.md`, `content/updates.md` and `content/glossary.md`. Committing to `main` triggers a website rebuild and deployment. The PDF/TeX scientific sources are not rewritten by this editorial step.

**Refresh the current framework later:** supply new versioned ZIPs to `scripts/refresh_framework.py` using `--papers`, `--audits`, `--dag`, and `--geometry`. The script validates all 31 paper pairs and checks that the DAG points to the exact source and audit archive bytes. Then run `python3 scripts/render_content.py` and `python3 scripts/check_site.py`, update public explanatory text and version markers, and commit.

The current full archives are direct site downloads (`docs/data/`): PapersMinimal v3.077, ProofChainAudits v1.83, DAG Atlas v1.223 and S³ Structure Network v1.49. Every single file is under GitHub's 100 MiB normal-blob limit; Git LFS is not required for this release. Future archives may be larger and should be screened before adding them to Git.

**Evidence limitation:** website validation checks file integrity, labels and links. It is not an independent global E3/E4 mathematical audit or a new physical source/measurement certificate.

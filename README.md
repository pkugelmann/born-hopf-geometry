# Born–Hopf Geometry

**A geometry-first research programme connecting mathematical structure to physical observables.**

Author: **Peter Kugelmann** · Manuscripts: **PapersMinimal v3.058**, 20 November 2026 · Proof audits: **v1.79** · DAG Atlas: **v1.215** · Geometry network: **v1.41** · Website package: **Paper00-GitHubPage-v1_1**.

This repository contains a public-friendly research website, the current **31 source PDFs and LaTeX manuscripts**, proof-chain audit reports, geometric diagrams and integrity metadata. It is designed so the **explanatory website text can be replaced without touching the mathematical source archive**.

## Read the website

- [Start here](docs/index.html) — readable, research-level introduction.
- [Framework explained](docs/framework.html) — how G0, GP1–GP3, S³, M₈, dynamics, quantum states, matter, gravity and QCD relate.
- [What must be explained](docs/observables.html) — masses, decays, forces, gravitational coupling, cosmology, hadronic readouts.
- [Glossary](docs/glossary.html) — concepts explained without removing technical meaning.
- [Manuscript library](docs/papers.html) — 31 papers, each PDF and LaTeX, exact version and SHA-256.
- [Verification archive](docs/verification.html) — full separate proof-chain records, not a blanket 'verified' status.
- [Download provenance](docs/downloads.html) — audit and diagram archive sources, plus large DAG Atlas release instructions.

## Replace public-facing content

**Edit Markdown, not HTML.** All human-readable research explanations live in [`content/`](content/EDITING.md):

| File | Controls |
| --- | --- |
| `content/site.json` | Homepage heading, introductory paragraph, cards, reading pathway, and status note |
| `content/home.md` | Narrative introduction |
| `content/framework.md` | Full guided explanation |
| `content/observables.md` | Testable physical questions and unresolved bridges |
| `content/glossary.md` | Definitions |

With **GitHub Pages → Source: GitHub Actions**, editing these files on GitHub and committing to `main` automatically rebuilds and publishes the website. No editing of generated `docs/*.html` pages and no re-uploading the large paper ZIP are required.

The checked-in HTML can also be previewed immediately. To build locally:

```sh
python3 -m pip install -r requirements-edit.txt
python3 scripts/render_content.py
python3 scripts/check_site.py
python3 -m http.server 8000 --directory docs
```

Open `http://localhost:8000` and review the layout. The rendering library is `mistune==3.2.1`. The public site itself is static HTML, CSS and JavaScript; it has no server dependency.

## Update the scientific corpus

The manuscript files are not silently overwritten when the public explanation changes. To replace the **entire papers snapshot** with a new versioned archive, run:

```sh
python3 scripts/refresh_manuscripts.py /path/to/Paper00-PapersMinimal-v3_059.zip
python3 scripts/render_content.py
python3 scripts/check_site.py
```

The refresh tool validates 31 paper entries against the source inventory and regenerates the manuscript manifest and searchable paper catalog with exact hashes. Review any changed conceptual explanations and external archive/release data before publishing. Older paper files are removed so the repository holds the current papers only.

## Research status

This archive deliberately separates **exact mathematical construction**, **same-action/source physical realization**, **measurement mapping** and **experimental validation**. Not every proposed bridge has been closed. The v3.058 release notes explicitly retain open questions concerning a realized charged source, physical interacting poles and the microscopic Newton-action/measurement match. For claims consult the exact manuscript hypotheses and the separate proof-chain status reports.

## Publish

Follow [`GITHUB-SETUP.md`](GITHUB-SETUP.md). GitHub access is required to create the actual repository; this ZIP is a complete prepublication package.

The original 205 MB DAG Atlas archive exceeds GitHub's 100 MiB normal Git-blob limit. It belongs in a **GitHub Release**, not the Git repository. See [`RELEASE-ORIGINALS.md`](RELEASE-ORIGINALS.md).

Citation metadata is in `CITATION.cff`. **No public reuse license is implied by this package**; the author should choose licensing deliberately.

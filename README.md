# Born–Hopf Geometry

**A geometry-first mathematical physics research programme: from admissible structure to measurable observables.**

Author: **Peter Kugelmann**. This repository hosts both the public research website and byte-preserved primary sources, so scientific claims can be traced from an accessible explanation to a specific manuscript and its versioned audit record.

## Current source edition (20 November 2026)

| Component | Version | Source presentation |
|:--|:--|:--|
| Papers I–VII, 31 active manuscripts | **PapersMinimal v3.077** | 31 current PDF/TeX pairs, source index |
| Proof-chain audits | **v1.83** | 45 readable Markdown/HTML reports, 130 retained obligation rows |
| Dependency graph | **DAG Atlas v1.223** | 14,366 current source labels; 7,667 inherited nodes |
| S³ exact finite-geometry network | **v1.49** | 13 diagrams, complete network ZIP |
| Website | **Paper00-GitHubPage-v1_5** | Editable Markdown + browser indexes |

The v3.077 source adds **55 scoped mathematical source labels** across five papers. The current DAG source overlay links these statements to their new line numbers but does **not** promote them to independently verified global E3/E4 status or physical occurrence. The audit archive is versioned and source-dependent; not every new paper has been independently re-audited.

## Read and browse

- [Start](docs/index.html) — the research question in clear, technically serious language.
- [Framework explained](docs/framework.html) — from G0/GP1–3 to S³, M₈, dynamics, particles, gravity and QCD.
- [Guided reading paths](docs/pathways.html) — follow a question to the relevant proofs and physical bridges.
- [Search the research index](docs/research.html) — all 14,366 current source labels; 7,667 inherited DAG nodes; 130 retained proof obligations; 45 reports; 13 diagrams.
- [31-paper library](docs/papers.html) — searchable, each paper viewable as an embedded PDF, with TeX and related audit.
- [Verification](docs/verification.html) — source-specific evidence, protocols, formal scope and audit records.
- [Current updates](docs/updates.html) — mathematical additions and unclosed source-action/measurement bridges.
- [Original archive downloads](docs/downloads.html) — four released ZIPs and SHA-256 hashes.

## Updating the site

The explanatory pages can be updated **without touching the scientific PDFs**: edit `content/*.md` and `content/site.json`, commit to main and let the GitHub Actions Pages workflow rebuild the HTML. Read [the editorial guide](content/EDITING.md).

For a new scientific archive, run `python3 scripts/refresh_framework.py --papers ... --audits ... --dag ... --geometry ...`, then `python3 scripts/render_content.py` and `python3 scripts/check_site.py`. The release-matching and source-hash checks prevent mixing a new paper snapshot with an unrelated atlas.

To install this version over the existing GitHub repository from the versioned ZIP, follow [GITHUB-SETUP.md](GITHUB-SETUP.md) or run the bundled `publish.sh`. It clones your existing repository, replaces the managed website paths and pushes a normal commit; it does not force-push or replace Git history.

## Research and licence status

Mathematical construction, action/source selection, propagation, measurement and independent validation are different claims. Source-integrated does **not** mean globally independently proved. Original manuscripts and full audit records govern the detailed hypotheses.

Citation metadata: `CITATION.cff`. No open-source licence is implied unless the author publishes one explicitly.

## Key ideas

[Question-led research explanations](docs/ideas.html) adapted from Paper00-XPosts-v1_12. Edit `content/ideas.md` to revise the public prose without altering the scientific manuscripts.


## Exceptional particle and hadron geometry (v1.4)

Open [2O / 2I and the geometry of matter](docs/matter.html). The explanatory source lives in `content/matter.md` and the reproducible exact-coordinate SVG generator is `scripts/build_polyhedral_figure.py`. Mathematical splits, working physical roles, and remaining hadron-current/pole obligations are kept distinct.

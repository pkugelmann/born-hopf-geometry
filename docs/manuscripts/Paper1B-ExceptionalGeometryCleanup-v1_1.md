# Paper I-B — Exceptional-geometry editorial revision v1.22

**Release date:** 20 November 2026  
**Input:** `Paper1B-ExceptionalGeometry-v1_21.tex` in PapersMinimal v3.054  
**Output:** `Paper1B-ExceptionalGeometry-v1_22.tex` in PapersMinimal v3.055

## Outcome

The paper now reads as an organized, comprehensive exceptional-geometry treatise.
The 7, rather than 8, numbered parts remove the empty-Part-III issue. The full
Kleinian/ADE quotient, Dirac/Hodge/eta/heat/torsion, modular, cubature and graph
material has been promoted to the **main narrative**. The specialist root,
Clifford, Hurwitz, triality, Petersen and certificate computations are retained
as **39 technical appendices** after the subject chapters. All 47 substantive
sections precede the appendix marker; the old layout had 68 appendix sections,
including four entire subject parts.

The first part now introduces the classical exceptional groups, their subgroup
lattice, invariant-ring and polytope foundations before the more advanced
Petersen/completion results. Paper I-A is the round S³ parent; I-B owns the
binary exceptionals and finite constructions. No S³-compendium mathematics was
silently deleted or reallocated to another paper.

## Verified conservation

- Original formal objects: **574**; revised formal objects: **574**.
- Original proof environments: **431**; revised proof environments: **431**.
- Unique scientific label identifiers: **805**, with **identical label set**.
- Removed source-only historical/editorial comments: **281**. Their original
  source lines are preserved in the accompanying annotation ledger, outside
  the manuscript.
- Historical release-numbered section headings: **9 → 0**.
- Spurious empty numbered part: **1 → 0**.
- Source-only proposed/pending integration declarations: removed; their
  theorems remain with their mathematical restrictions intact.
- Obvious TeX defects corrected: malformed Hurwitz unit superscript
  `\mathcal H^\times`, math heading that printed `§3`, the 47 broken `Spin(4)`
  spellings, and outdated imports of I-C/I-D.
- Conditional distinctions preserved: unselected 2I completion, group versus
  coset, non-lumpable finite walks, scalar versus spinorial operators, unsigned
  support-counting versus signed triality coefficients, and mathematical graph
  readouts versus action-owned physical observables.

## Mathematical-body preservation by environment

| Environment | Count retained | Byte-identical after comments are excluded | Edited notation or scoped wording |
|---|---:|---:|---:|
| theorem | 207 | 200 | 7 |
| proposition | 115 | 108 | 7 |
| corollary | 120 | 114 | 6 |
| lemma | 4 | 4 | 0 |
| definition | 32 | 28 | 4 |
| remark | 96 | 89 | 7 |
| proof | 431 | 423 | 8 |

The edited formal blocks consist of notation repairs (`Spin(4)`) and a small
number of explicitly recorded scope/history clarifications. This conservation
check is **not** an independent verification that all mathematical theorems
are correct.

## Compilation and graphical checks

- LaTeX build exit: **0**, with BibTeX; final PDF: **295 pages**.
- Compiled scientific labels: all **805** present in current I-B AUX.
- Undefined references or citations: **0**; LaTeX errors: **0**.
- Overfull boxes: **0**; missing glyph warnings: **0**.
- Rendered inspections of the front matter, finite-subgroup theorem,
  contents hierarchy and technical appendix boundary passed.
- The current AUX alias registry was regenerated from the revised I-B AUX
  so that versioned external imports use the revised label data.

## Cross-paper dependency note

The preceding v1.21 analysis found 27 direct consumers of I-B labels.
Current source inspection detects **281** reference calls to I-B
labels across **27** unchanged consumer sources (unique labels:
**159**). Their labels are all preserved.
**Important:** Those 30 other PDFs are byte-preserved from v3.054, not rebuilt.
Because the editorial reorganization necessarily changes printed section,
theorem and appendix numbering, those PDFs can retain old printed numeric
references until their separately versioned publication refreshes. This
archive fixes their future LaTeX cross-reference resolution; it does not
pretend their existing PDF displays were regenerated.

The separate proof-chain audit and DAG archives have not been modified by
this editorial release. Legacy label names that contain strings such as `v561`
remain unchanged for downstream compatibility; they are identifiers, not
public-facing descriptions of historical development.

## Integrity

- Original I-B SHA-256: `c1203fa2617400956e80de94cca82a15a560c79ba9fa709e77301d557134cdb1`
- Revised I-B SHA-256: `40eed3943a135269e06f384ac5d0e9ca0a679cdda1d7ce02cea25328d1937da0`
- Updated macro dependency: `Macros-v2_190.tex` (I-B v1.22 import).
- All 30 other sources and their PDFs remain byte-identical to their v3.054 versions.

This update is an editorial/typesetting/ownership clean-up, **not a new
proof-chain audit or physical identification**. External computational
certificates named within the source are not automatically included in the
minimal-paper archive; consult the existing proof and DAG audit packages
for evidence and outstanding verification status.

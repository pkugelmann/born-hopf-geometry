# Paper III-D — applied preservation-first editorial revision v1_1

**Paper revision:** `Paper3D-RunningResponse-v1_167` → `Paper3D-RunningResponse-v1_168`.
**Framework revision:** PapersMinimal v3.071 → v3.072.
**Parent:** the current project-based `Paper00-PapersMinimal-v3_071.zip`.
**Scope:** source-based editorial refactoring, cross-paper owner correction, PDF compilation and latest-only framework integration. This is not a new mathematics audit.

## What changed

1. Removed the 46-line opening series-revision chronology and all remaining standalone source history/comment lines. All **70 original standalone comment lines** are retained verbatim in the reversible `Paper3D-RemovedSourceAnnotations-v1_1.csv` ledger.
2. Reorganized the long reciprocal-response chapter into properly nested subsections for Born reduction, endpoint-calibrated two-root coupling, Laurent characterization, positive-part junction/carrier, Born-symmetric normalization, Hopf conjugation and the optional curvature-clock comparison. This removes `3.0.x` headings without merging distinct mathematical hypotheses.
3. Moved the grade-four action-incidence corollary, Petersen no-running proposition and static radius/curvature compatibility counterexample (with their proofs and scope notes) before a single final conclusion. The bibliography is now the last substantive element of the manuscript.
4. Corrected nine Laurent/Euler narrative references to **Paper I-D** (actual owner of `p1b:thm:laurent-family` and `p1b:thm:born-euler-anticommutation`) while retaining historical theorem label IDs.
5. Corrected the trace-coordinate citation to **Paper I-C** (`p1b:prop:trace-coordinate` physically lives in I-C). The static homothety theorem cited by the terminal counterexample also lives in I-C; its original label is unchanged.
6. Corrected seven references to technical appendices actually declared in **Paper III-G**, rather than implying these appendices belong to III-D.
7. Added a new accurate `Kugelmann2026Paper1C` bibliography entry in `Born-v6_60.bib` and used the already accurate `Kugelmann2026Paper1D` key. **Did not repurpose** the misleading legacy `Kugelmann2026Paper1B` key, which other papers may still use. `Born-v6_59.bib` remains unchanged for those papers.
8. Updated the current source registry to `Macros-v2_198.tex` with only III-D/current-bibliography bindings changed; regenerated current-owner AUX aliases.
9. Reworded a few obsolete development-stage labels (including the v2.219 theorem title), while keeping optional least-support and first-actual-carrier criteria mathematically distinct.

## Formal-preservation checks

| Item | Before | After |
|---|---:|---:|
| Theorems | 23 | 23 |
| Propositions | 12 | 12 |
| Lemmas | 5 | 5 |
| Corollaries | 15 | 15 |
| Definitions | 13 | 13 |
| Remarks | 30 | 30 |
| **Formal objects** | **98** | **98** |
| Proof environments | 54 | 54 |
| Additional `proofsteps` environment | 1 | 1 |
| Original label IDs | 157 | 157 preserved + 1 organizational label |
| Recognized mathematical spans | 1,254 | 1,254 (identical multiset) |
| Standalone comment lines in source | 70 | 0; all 70 archived |

**Proofs:** 45/54 normalized proof blocks are unchanged. Nine carry only corrected mathematical ownership or editorial historical wording. The explicit proof differences are in `Paper3D-ProofAttributionDiff-v1_1.csv`; changes to source lines are in `Paper3D-FormalTextChanges-v1_1.csv`. The revision script independently reproduces the new source byte-for-byte.

The source specifically retains the corrected Laurent junction (constant trace versus independently glued distributional representative), distinct `REG_sigma` scheme character branches, `FLAG` and native active-depth differences, `RED`/root calibration and optional absolute scale, complete action first/second jet/Schur contacts, and the limited static-radius compatibility test. No beta function, physical action coefficient, actual source or decay law is inferred merely from finite geometry.

## Compilation and release certification scope

- The new PDF was rebuilt using `pdflatex`, `/usr/bin/bibtex.original`, then two additional `pdflatex` passes. **51 pages** (previously 50).
- Final build log: no LaTeX errors, unresolved citations or cross-references, overfull boxes, or missing glyphs. The TOC and the final two pages were visually inspected.
- The current bibliography displays a valid **I-C** and **I-D** entry, not the earlier ambiguous I-B/I-C hybrid.
- The complete project-based framework ZIP contains one current TeX/PDF pair for each of **31** logical papers; only Paper III-D is replaced. The other **30 manuscript TeX/PDF pairs** remain byte-for-byte identical to v3.071. The shared macro/BibTeX registry and AUX compatibility files are updated as named build metadata.
- Every former III-D label used by downstream papers remains resolvable. Static source-wide reference/manifest checks and ZIP CRC/SHA-256 validation are recorded in the release's build-verification file.

## Remaining scope

The supplied historical III-D proof-chain audit is for v1.159 with a later source-integration addendum for v1.166. Independent **source-version-matched E3/E4 mathematical certification of v1.168 remains pending**; editing and compilation are not a replacement. The other 30 PDFs were not recompiled.

## Files provided in the focused revision package

Original and revised paper TeX/PDF, reversible source-edit script, mathematical-preservation and proof-diff ledgers, archived comments, source ownership/bibliography changes, the earlier audit-compatibility report, a separate verification-status record, and the complete editorial change report.

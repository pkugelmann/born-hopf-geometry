# Paper I-D — Technical Material cleanup and verification report

**Revised manuscript:** `Paper1D-TechnicalMaterial-v1_69.tex` / `Paper1D-TechnicalMaterial-v1_69.pdf`
**Source:** `Paper1D-TechnicalMaterial-v1_68.tex` from PapersMinimal v3.056
**Release:** PapersMinimal v3.057 — 20 November 2026
**Task:** editorial and structural cleanup; **not an independent mathematical proof audit**.

## Completed editorial changes

1. Removed the opening chronological revision log and 653 standalone source annotations, exporting their literal text with original line numbers to `Paper1D-RemovedSourceAnnotations-v1_1.csv`. Source-level mathematical caveats were checked before removal; the whole-annulus parity limitation has been stated explicitly in rendered prose. Inline TeX percent-signs required by macro syntax remain unchanged.
2. Corrected the paper's role to the technical proof and computational companion for I-A ($S^3$), I-B (exceptional geometry), and I-C ($M_8$), without changing the ownership of the primary mathematical constructions.
3. Replaced the lone historical “Part I / relocated from I-A” heading with an actual `\appendix` boundary. The late technical comparison, Clifford, Hurwitz, Petersen, F40, $E_8$, and certificate calculations now have lettered appendices. All primary proof sections remain in their established mathematical order.
4. Removed repeated headings and a tripled introductory sentence. The manuscript's section and abstract descriptions now use mathematical topics rather than research/import chronology.
5. Replaced 76 rendered references to old research Batch numbers, including ranges, with references to the matching existing `rtproof29`–`rtproof63` mathematical subsections. Corrected “Appendix” cross-references when the referenced subsection is in the main paper. No label was renamed.
6. Rebound the active external references to I-A v5.180, I-B v1.22 and I-C v1.144, removing stale registry entries and obsolete I-D self-import.
7. Kept all eleven independently supplied rank/gauge/character/complex/spectral/quotient/Hessian calculations in I-D, with subject-based headings and their original quantitative expressions. Exported their original candidate/partial issue-status words and the eleven-issue report verbatim to `Paper1D-IndependentVerificationRecord-v1_1.md`. The later source-relative seven formal statements remain in I-D; the closing remark preserves mathematical scope guards without mixing in administrative verdicts.

## Source preservation

| Measure | Source v1.68 | Revision v1.69 |
|---|---:|---:|
| Theorems | 117 | 117 |
| Propositions | 76 | 76 |
| Lemmas | 45 | 45 |
| Corollaries | 31 | 31 |
| Definitions | 3 | 3 |
| Remarks | 7 | 7 |
| **Formal statements total** | **279** | **279** |
| Proof environments | 268 | 268 |
| Original `\label` anchors | 1,405 | 1,405 |
| Additional subject-appendix label | — | 1 |
| Longtables | 5 | 5 |
| Display-math `\[` blocks | 1,495 | 1,495 |
| Standalone `%` source annotations | 653 | 0 |

The before/after patch and annotation ledger make the editorial migration reversible. Preservation of numbered statements, proofs and labels is not by itself a proof of their mathematical correctness; math-level review and independent audit status have not changed.

## Build and downstream reference validation

- PDF rebuild: **PASS**, 313 pages, using `latexmk`/`pdflatex` and installed `bibtex.original` through an executable shim.
- Undefined citations / undefined references / LaTeX errors / missing glyphs / overfull boxes: **0** in the final build.
- Benign diagnostics remaining: 7 underfull boxes and 14 hyperref PDF-bookmark token sanitizations (math in headings); visible mathematical text and equations compile.
- Source labels: **1,406 / 1,406** available in the new canonical `.aux`. All original 1,405 anchors preserved, with one new appendix anchor.
- Label ownership: no duplicate I-D label in the other 30 sources. Earlier downstream analysis records 205 direct references from 19 paper sources to 117 I-D labels. Their source targets are retained, and the old I-D AUX aliases now point to compiled v1.69 values.
- Other 30 shipped PDFs **not recompiled**; they may display pre-v1.69 theorem/appendix numbers, although the source-side aliases are current. Re-typesetting would require a coordinated paper-version release.

## Reproducibility and evidence limits

The 22-entry dependency ledger names 16 executable/JSON artifacts. **9 of 16** were located in the provided DAG Atlas snapshot; the other **7** were not found in the four supplied snapshots by the cited filenames. They are not fabricated or claimed executed. They should be restored or linked by stable machine-readable evidence locators in a later DAG evidence release.

The four prior “candidate” and seven “partial” independent verification-status labels remain **unadjudicated by this editorial revision**. The separate DAG and ProofChainAudits archives are unchanged. Results conditional on specified native sources, restrictions, finite tests, framing, or candidate mappings remain conditional; no particle-physics occurrence or decay prediction is promoted.

## Files in focused package

- Updated LaTeX source and compiled PDF
- This report and the independent-verification status record
- Removed source annotation ledger and complete original-to-new patch
- Source-preservation metadata and the certificate dependency ledger
- Reproducible editing script (requires original v1.68 as input)

**Status:** Editorial revision finished; compiled manuscript and current-source alias registry verified. Formal proof audit and missing certificate provision are separate tasks.

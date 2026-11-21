# Paper III-E v1.204 — Source-preserving editorial change report

**Baseline:** project release v3.072, III-E v1.203, source SHA256 `429efc8d50d6d82fff0e61dbe8b7373c3adedff3e99909fb26e100d7a8a2b184`.
**Revised:** III-E v1.204, source SHA256 `b76d35f9d9a46ff0cdbdaa826b8c270c10a60422d3db1688d1be79624bc73fb5`.

## Applied improvements

1. Removed/archived the 50-line revision chronology and all 101 standalone source comments in a reversible CSV.
2. Updated the manuscript date/release edition and replaced the 24-stale-binding `Macros-v2_188` import with 31/31-current `Macros-v2_199`.
3. Rebuilt a mathematical chapter hierarchy, correcting all four Section 3 `3.0.x` subsection paths and giving large gravitational/action material stable mathematical headings.
4. Moved the full local-to-global response corollary/proof from the premature conclusion into the hierarchy-response chapter.
5. Integrated the post-bibliography rooted conormal cap and Schur source certificates into a dedicated source-realization chapter. Hypotheses about actual Dirichlet-to-Neumann data, source orientation and amplitude transport remain explicit.
6. Grouped the first-jet whole-action Newton test and finite Gibbs/Gaussian quantum-reduction conditions. Kept raw 1/96 action mismatch separate from an actual physical projection.
7. Placed Petersen no-gravity-promotion, independent momentum-to-EH scale family, and conditional exceptional-triad cap together. Retained `ET-OWNER` and its three undischarged subconditions.
8. Consolidated one final conclusion and references after all results. Both original conclusion labels remain unchanged.
9. Corrected I-B/I-C/I-D theorem owners, replacing the wrong shared `Kugelmann2026Paper1B` reference with the dedicated I-C and I-D bibliography keys. Identified nine technical appendices as belonging to Paper III-G.
10. Replaced selected release-stage headings (rank-two countercomparison, figure deferral, local-phase-volume scope, smooth MRESP) with mathematical domain statements, keeping the counterexamples and conditions.

## Preservation and source verification

- Formal objects: **152/152** (41 theorems, 27 propositions, 4 lemmas, 36 corollaries, 11 definitions, 33 remarks).
- Proof environments: **96/96**; 91 text-identical, 5 source-owner text corrections only.
- Existing labels: **253/253**; four new section labels = **257 total**.
- Mathematical spans: **2047/2047** canonical equality; one in-display source-edition phrase was updated, no mathematical operator changed.
- All original non-comment LaTeX source lines copied once (except deliberately relocated `\printbibliography` and redundant `\subsection{Conclusion}`); 68 source-anchored editorial changes listed in CSV.
- Incoming III-E references: **79 from 18 other papers** retained, outgoing: **320**; 31-paper corpus: 14293 unique labels, 11602 resolved reference uses, no collisions.
- Other 30 TeX/PDF pairs byte-identical to the v3.072 project parent.
- New III-E PDF: 91 pages; BibTeX entries and rendered first/TOC/final reference pages inspected.

## Mathematical scope explicitly not promoted

The exact scalar/graded response identities, roots U/C, conditional local Laurent and heat flow, source-cap Schur identities, and finite ET geometry do not suffice to assert a physical Newton action, physical source orientation, a selected cosmology, or an actually populated transition. The full independent E3/E4 proof-chain audit remains pending; see `Paper3E-VerificationStatusRecord-v1_1.md`.

## Reproducibility

`edit_p3e.py` transforms the exact source v1.203 to v1.204 with source-line assertions, records edits and checks all statements/proofs/labels and symbolic expressions. `build_release.py` requires the SHA-verified parent ZIP, edits only III-E, rebuilds current AUX aliases, checks all 31 roots and hashes, and creates the next release. `Paper3E-SourcePreservation-v1_1.json` records the comparison counts. A focused ZIP contains both source revisions, both PDF revisions, patch, scripts and ledgers.

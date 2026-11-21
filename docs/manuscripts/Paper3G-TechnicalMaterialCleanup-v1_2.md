# Born--Hopf Geometry III-G v1.58 — editorial implementation and proof-preservation report

**Report:** `Paper3G-TechnicalMaterialCleanup-v1_2.md`  
**Authorized change:** apply the 51 source-anchored analysis actions to the user-uploaded `PapersMinimal v3.075` parent and release `v3.076`.  
**Authoritative parent ZIP SHA-256:** `a46ca6a315d85edbf5e74df082eb75f8d2189f1f0cd3f2bef237b72d6a8623e1`.  
**Parent source:** III-G `Paper3G-TechnicalMaterial-v1_57.tex`, SHA-256 `b816daa50d8d88a48ee934f89b3f6e466cb5942e82ec460534b983c499d0e340`.  
**Revised source:** III-G `Paper3G-TechnicalMaterial-v1_58.tex`, SHA-256 `1c6a431f1aefcf16c133550cd0064d8db8485ffdb94bb4647b38c219ebcf1537`.  
**Reference:** `Paper3G-CleanMainPaperAnalysis-v1_1.md` and `Paper3G-CleanupActionPlan-v1_1.csv`.

## Scope, sections, and attribution

The manuscript remains the technical proof companion of Papers III-A--III-F. Its actual mathematical claims, countermodels and precise conditional scopes are preserved; technical proofs are not moved to other owners. Historic version/process text has been removed from publication prose or reformulated as mathematical scope. The abstract is now a scientific synopsis rather than a transfer/revision history. The previous 13 top-level sections become seven coherent major sections; final finite benchmarks are collected as subordinate sections, including a properly leveled local Maxwell subsection and a paper-wide scope conclusion immediately before the bibliography.

Imported owner corrections are resolved using current I-B v1.26, I-C v1.146, I-D v1.69 and II-F v1.71 texts and source labels. All 22 instances of the misleading `Kugelmann2026Paper1B` key are rebound individually to I-C or I-D, not replaced globally in the shared bibliography. No bibliography entry was changed. The corrected printed PDF cites both current I-C and I-D.

## Full source-preservation tests

| Constraint | Result |
|---|---|
| Formal mathematical statements | 184 original / 184 new; exact type ordering and labels |
| Formal result mathematical expressions | All unchanged per object |
| Formal result text changes | 28 recorded prose/owner/caption adjustments; all their full diff data in claim evidence |
| Outer proof environments | 125 retained in original order and with same preceding formal-claim identities |
| Nested `proofsteps` | One retained |
| Full proof bodies | 32 changed prose/owner attributions, 94 of all 126 proof-related blocks text-identical; exact differences preserved in `Paper3G-FullProofDiff-v1_2.json` |
| Raw mathematical spans | 3036 identical in their original occurrence order |
| Labels | 375 original labels retained, unique and in the same order |
| Outgoing references | 293 original uses retained and in the same order |
| Source-line tracking | 9170 original lines mapped or intentionally archived |
| Comments | 155 complete original comment records archived, including four inline |
| Logged text edit events | 188 exact before/after events; all reversible against frozen source |
| Added scientific synthesis | A new scope paragraph, not a formal claim or new assumption |
| Page count | 115 A4 pages; LaTeX build passed |

No theorem was made unconditional or an optional spectral/mass/decay/gravity certificate upgraded to physical occurrence. The source comment archive is complete in `Paper3G-RemovedSourceAnnotations-v1_2.csv`; every rewritten original line has a mapped source location. The edit script takes the original SHA-frozen source and fails if a line differs.

## Reproducibility boundary

The original manuscript referenced `Paper3G-PetersenDynamics-v1_1-verify.py`; that exact file was not present in the inspected current project and DAG bundles. A new `Paper3G-PetersenMoments-v1_1-verify.py` checks exactly the ten axes and the second/fourth/sixth polynomial moments in symbolic arithmetic over the golden-ratio field. It executed successfully. **That checks the moment identities only.** The separate two-core `T/B` matrix statements, 15-edge projector, and off-diagonal E36 congruence are not certified by the replacement moment replay; the full verifier remains a supporting-artifact limitation rather than an asserted false theorem.

The meron/zeta proposition retains the analytic theta argument; its historical path to a different numeric verifier was removed from publication prose. The previous `Paper00-MultiGapClosures-v1_1-verify.py` is separately present in the supplied DAG Atlas and is not part of this changed paper source.

## Compatibility and epistemic limits

The new macro registry is `Macros-v2_202.tex`, forked from the user's `Macros-v2_201.tex` only to point at the new III-G stem. Older macros used by other papers remain in the release. All old III-G AUX basename aliases will be made to contain the current v1.58 AUX bytes; they are compatibility handles, not old theorem versions. The 30 non-III-G current TeX/PDF pairs are SHA-identical to the uploaded v3.075 parent. Their precompiled PDFs may display historical imported theorem numbers; future complete recompilation is needed to refresh those printed references, but the source label identities and current AUX target mapping remain intact.

**Verification statuses:** `EDITORIAL_SOURCE_UPDATED`, `BUILD_VERIFIED`, source-preservation checked. `MATHEMATICAL_AUDIT_PENDING`. This report is not a new E3/E4 rigorous audit and makes no changes to the ProofChainAudits or DAG Atlas.

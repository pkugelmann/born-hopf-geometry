# Paper I-C — M8 compendium cleanup and preservation report

**Input:** `Paper1C-M8Geometry-v1_143.tex` in PapersMinimal v3.055  
**Output:** `Paper1C-M8Geometry-v1_144.tex` in PapersMinimal v3.056  
**Date:** 20 November 2026.

## Result

The revised manuscript is a complete \(M_8\) reciprocal-geometry compendium
with **seven mathematically titled parts**, rather than an unstructured first
11 sections followed by a historically titled import part. Its final section
sequence contains **24 mathematical sections** (previously 25 numbered sections, including an empty
release heading, and one unnumbered verification-status insert). The late genuine reciprocal, Dirac/boundary, polygon and finite
spectral material remains part of the scientific text, with no technical
mathematics removed simply to shorten the paper.

- **518/518 formal statements and remarks retained**: 238 theorems, 115
  propositions, 93 corollaries, 20 lemmas, 11 definitions, 41 remarks.
- **440/440 proofs retained**; **1,096/1,096 distinct labelled objects**
  preserved with their names and ordering; **28/28 longtables** retained.
- **One corollary and its proof** have internal-reference terminology
  corrected from "appendix" to "subsection", and **one further proof** loses
  a sentence about a separate exact-arithmetic certificate. The mathematical
  steps and resulting claims are otherwise unchanged.
- Source-only historical comments removed from I-C: **472**; all exported
  with original line numbers in the attached source-annotation ledger.
- The independent verification supplement is preserved as a separate exact
  LaTeX evidence transcription, with **4 candidate certificates pending** and
  **7 partial/open checks**; no proof gate is upgraded.
- A spurious empty "verified source geometry" section was removed. Stale
  source-history prose, the late "imported from Paper I-A" part, release
  markers, internal export/status tags and incorrectly described appendix
  references were corrected.
- Current external LaTeX AUX imports were rebound to the active versions of
  Papers I-A, I-B, I-D, II-F, III-B, III-E and III-F. Legacy `p1b:` label
  prefixes remain **unchanged** because later papers depend on them.

## Verification

- Rebuilt I-C with `latexmk -pdf -g` and a working BibTeX executable:
  **success**, **358 PDF pages** (previous edition: 359 pages).
- Final compile log: **0 undefined references; 0 undefined citations; 0 LaTeX
  errors; 0 overfull boxes; 0 missing glyphs; 0 PDF bookmark warnings**.
- **2 nonblocking pre-existing amsmath legacy syntax warnings** (formulae
  containing `\atopwithdelims` and `\over`), left as-is to preserve the
  original mathematical source.
- All 1,096 labels appear in the generated current I-C AUX; historical
  I-C AUX basenames map to the same current source numbering.
- All **462 direct reference uses from all other 30 papers**, representing
  **233 individual I-C labels**, remain resolvable in the current AUX.
- No name collision among all 31 manuscript label sets; I-C's own reference
  commands have a defined owner in the current source collection.
- The 30 other paper sources and PDFs are byte-identical to v3.055. Their
  **published PDFs were not rebuilt**; their printed external theorem numbers
  may therefore be stale until each is separately recompiled against these
  current AUX files.

## Exact mathematical scope preserved

The product and exchange structure, Cartan and bi-Hopf geometry, topology,
complex and invariant metrics, representations, all-level carrier families,
exhaustion catalogue, primitive reductions, rooted Clifford/triality,
principal-SU(2) descent and its **unevaluated full classification fibres**,
mathematical versus physical occurrence conditions, and 120/720/12720/60000
finite sampling comparisons retain their stated mathematical domains.

The appendix references to `p1b:app:g17`, `p1b:app:m8-substructures`, and
`p1b:app:v233-support-countermodels` are correctly described as I-C
subsections; separate I-D technical appendices remain attributed to I-D.
The revised source does not invent a `\appendix` command, because these
specialized calculations are already part of the \(M_8\) compendium, not
separate anonymous appendices. I-D remains the distinct technical companion.

## Residual work and limits

This release changes **editorial ownership only**. It does not re-prove any
mathematical theorem or change prior independent-verification statuses;
proof-chain/DAG archive updates are separate tasks. To display *new* I-C
cross-paper theorem numbers, the other 30 PDF outputs require versioned
rebuilds. The source-level labels and current-AUX compatibility links are
ready for that work. Existing conditional constructions remain conditional.

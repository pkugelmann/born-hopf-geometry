# Paper II-F — technical manuscript cleanup and verification v1_1

**Input:** `Paper2F-TechnicalMaterial-v1_70.tex` from `PapersMinimal-v3_064` (SHA-256 `81ed2c9c568103bdc4824be8ac68b98b04424db8811607fe5d4189e94e031939`).
**Output:** `Paper2F-TechnicalMaterial-v1_71.tex` in `PapersMinimal-v3_065` (SHA-256 `a7d091ce67c74dc3ddb5a477a99a68d7e02d2e9805ccad4472b3be27f8ee8a8c`).

## Applied editorial changes

1. Archived 110 standalone historical/provenance source comments verbatim with original line numbers.  Replaced the out-of-date source-extraction abstract and framework date with a domain-accurate account of the technical contents and their physical non-occurrence guards.
2. Updated the current-source LaTeX registry to `Macros-v2_195.tex`.  The ten stale explicit `\BHExternalRefs` lines were removed because the current macro imports all 31 current owners automatically while excluding the logical current paper.
3. Split the 2,790-line opening proof section into four navigable mathematical sections: exactness/countermodels, compact-Lie/elliptic consequences, conditional (FD)+(LR) regularity, and finite-readout descent. Added three new **section labels**, retained all original theorem labels.
4. Replaced deferred/legacy development-stage headings with precise mathematical scope descriptions.  Optional and countermodel hypotheses remain explicit; proof calculations and the word-stage non-implications were not deleted.
5. Moved the complete independent finite radius/spectral/readout certificate chapter next to the POVM/moment-radius calculations without altering its mathematical content.
6. Corrected 15 textual I-A/I-B attributions of genuine binary-exceptional, Petersen, Hurwitz, and finite-equivariance results against the actual I-B theorem declarations.  General round $S^3$, Hopf and intrinsic parent references continue to belong to I-A.
7. Placed the two centre-even descent and matched-$A_5$ propositions (with both proofs and original labels) before a single final bibliography.
8. Recorded the source-version gap to the prior II-F proof-chain audit rather than assigning any new mathematical verification status.

## Preservation and build results

- **226/226 formal objects**, **179/179 proof environments**, **306/306 original labels**, plus 3 new section labels.
- **176 exact normalized proof-text matches**; the other **3** change only I-A to I-B owner references. No proof calculation or mathematical expression was altered.
- **296 original outgoing references / 296 revised uses**; the exact set of referenced labels is unchanged (175 distinct), and all revised targets resolve.
- **156 incoming references** from 17 other papers still target 99 original II-F labels; **zero cross-paper duplicate labels** after cleanup.
- PDF **116 pages**; successfully compiled using `pdflatex`, `bibtex.original`, then two further `pdflatex` passes. Diagnostics: `{'LaTeX errors': 0, 'undefined commands': 0, 'undefined references': 0, 'undefined citations': 0, 'overfull boxes': 0, 'missing characters': 0}`.
- Other 30 current manuscript TeX/PDF pairs byte-identical to v3.064.
- Canonical and compatibility AUX files now reference the current v1.71 source; aliases are *not* preservation of historical proof evidence.

## Limits

This is source/LaTeX reference verification and an editorial mathematical-preservation comparison, **not** a new independent mathematical proof audit.  The other 30 PDFs and the separate DAG/proof-chain records were not re-typeset or re-adjudicated; old PDFs may still show obsolete theorem numbers.  All conditional qualifications remain active.

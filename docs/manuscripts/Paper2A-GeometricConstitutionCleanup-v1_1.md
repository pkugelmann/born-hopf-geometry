# Paper II-A — clean scientific manuscript revision v3.227

**Input:** `Paper2A-GeometricConstitution-v3_226.tex` from PapersMinimal v3.059.  
**Output:** `Paper2A-GeometricConstitution-v3_227.tex` and compiled 171-page PDF.  
**Framework release:** PapersMinimal v3.060 (20 November 2026).  
**Nature of work:** editorial/theorem-preserving cleanup, not a new rigorous proof audit.

## Editorial result

Paper II-A remains the constitutional treatment of G0, GP1–GP3, exact host realization, whole-candidate least selection, typed co-realization, and conditional application/physical-occurrence boundaries. The primary principles are preserved in their original formal environments; no principle has been weakened or strengthened through editorial surgery.

1. **Abstract and front matter:** replaced a roughly 290-line source abstract with a concise scoped abstract. The 18-line release-numbered master-rule paragraph was integrated into the introduction under its mathematical subject. Its theorem references remain available in the body. Current edition metadata replaces a stale framework version.
2. **Historical materials:** all **172** standalone source comments, including the 57-line release chronology, are removed from the maintained TeX and archived verbatim with their original line numbers. An original abstract copy is also archived as an editorial comparison source.
3. **Reordered mathematics:** the four formal finite-band/coset diagnostic objects previously placed inside the conclusion are now under a dedicated mathematical section. The global-cover $SU(2)/SO(3)$ theorem and remark now immediately follow compact-parent selection. The marked conormal source subsection is integrated with action applications, and the finite rank-two and conditional complete-$2O$ applications are placed before the final conclusion. Scientific statements no longer follow the bibliography.
4. **Application organization:** the former 28-subsection application cluster has five subject-oriented sections covering finite descendant operations; owner-resolved action inputs; physical/readout limits; rooted relations and successor transport; and exact observable/action-incidence certificates. Inherited 3.0.1-style subsubsection hierarchy and TOC numbering are corrected.
5. **Paper ownership:** exceptional finite subgroup constructions and the Petersen–Hopf proof source are correctly attributed to Paper I-B. General $S^3$/Hopf/Spin(4) mathematics remains attributed to Paper I-A. The printed bibliography entries for I-A and I-C no longer repeat stale transfer/version history.
6. **Mathematical scope retained:** the complete-$2O$ particle-response carrier remains a conditional **working interpretation**, not an asserted particle occurrence. The projective rank-two packet and finite subgroup/spectral tests still require the frozen role antecedents stated in the paper. No dynamics, measurement, physical source, mass or calibration is inserted by the cleanup.

## Preservation evidence

| Measurement | v3.226 | v3.227 |
|---|---:|---:|
| Formal theorem/definition/remark/postulate/principle objects | **306** | **306** |
| Proof environments | **173** | **173** |
| Original labels retained | **371** | **371** |
| Added subject-section labels | 0 | **5** |
| Distinct locally used reference targets | **246** | **246** |
| Ordinary reference mentions | **498** | **495** (three redundant mentions removed from condensed abstract) |
| Standalone historical annotations | **172** | **0** (verbatim archive) |
| PDF page count | **174** | **171** |

A complete normalized formal/proof-block comparison shows that all objects are retained with **only three explicit textual edits**:
- Remark `p2a:rem:v270-covariant-readout-ledger`: removed the release identifier from its title.
- Remark `p2a:rem:v3102-no-new-gp`: replaced publication-history wording with its already stated chronology consequence, without changing the condition.
- Proof of theorem `p2a:thm:v318-petersen-same-owner-descent`: changed the mathematical citation owner from I-A to I-B; no inferential step changed.

The original abstract contains more descriptive source text than the new abstract. That removed material remains in `Paper2A-OriginalAbstract-v1_1.tex.txt` for traceability; this is a rewrite of explanatory material, not a proof deletion. The theorem and proof comparison ledger provides exact text diffs of the only formal-object edits.

## Build and cross-paper verification

- PDF: **171 pages**, pdfLaTeX/BibTeX compilation success; no undefined citations, undefined references, missing glyphs, LaTeX errors, or overfull boxes. Existing nonfatal underfull-box diagnostics remain.
- Cross-paper: **272** direct incoming references from **24** other papers continue to target preserved II-A labels. The entire 31-source corpus has **14,192** globally distinct labels with zero source-label collisions.
- Cross-document AUX registry: **158** current-source/compatibility aliases, including the original II-A v3.226 basename now containing bytes of the compiled v3.227 AUX. This supports subsequent builds; the unchanged 30 PDF files were not re-typeset and may still print old section numbers.
- Bibliography: no citation keys were renamed; four Paper-I bibliographic fields were corrected or dehistoricized in the existing shared `Born-v6_59.bib` filename for compatibility. The former bibliography file is included in the focused provenance package.

## Exact source hashes

- Original II-A TeX: `6f730fe5ca615c44520f8ccf667503bff12713c785aa031f1f78ea7619f723d7`
- Revised II-A TeX: `863d7e2efde76d8156ddd384cb9febd81b53cc1d5f0fd7911968508c346128a9`
- Revised II-A PDF: `79e37ad924347f49a325c70c4668e9753942b6b76b34c2eaeb1485acbc7498f0`
- Shared bibliography after metadata corrections: `27ebe2fc096f86bd9d922826e807296523426dca0c33bbdc444adff992e20159`
- Current II-A AUX: `ae70142b14ced08256a07bcde150b5ccea62b633e6d8b1018ff662bd599d7e11`

## Unchanged limitations

1. The earlier Paper II-A proof-chain audit was performed against an older manuscript and has **not** been independently rerun for v3.227. Editorial parity is not mathematical proof verification.
2. The other 30 PDFs were not recompiled. Their archived source text is unchanged and their print reference numbers can differ from the current AUX aliases when a theorem number moved.
3. The separate DAG Atlas and ProofChainAudits packages were not modified. No certificate has been upgraded and no physical conditional-to-unconditional promotion was made.
4. The shared bibliography has corrected metadata, but the previous Paper-I citation *keys* and 30 unchanged PDF bibliography impressions remain for compatibility until those papers are next rebuilt.

**Reproduction:** The focused package includes the source transformation script and the original II-A source. The complete PapersMinimal archive includes all necessary 31 current sources, macros, bibliography, canonical cross-reference AUX aliases and the build verification materials.

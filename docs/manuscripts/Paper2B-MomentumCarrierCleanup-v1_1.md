# Paper II-B — editorial cleanup and build verification

**Revision:** `Paper2B-MomentumCarrier-v2_146.tex` → `Paper2B-MomentumCarrier-v2_147.tex` (20 November 2026).  
**Framework source package:** `Paper00-PapersMinimal-v3_061.zip`, parent v3.060.  
**Boundary:** editorial/reorganization and reference/build verification. This is **not** an independent mathematical proof audit.

## Mathematical material preserved

- All **80 previous formal objects** survive. One additional proposition, `p2b:prop:derived-d01-pointwise-extension`, wraps the existing D01 pointwise-product claim before its unchanged original proof; total now **81 formal objects**.
- All **51 proof environments** survive. Two proof bodies have only the corrected I-A → I-B source attribution: the smooth-model theorem and Petersen representation.
- All **105 original labels** survive. The new D01 proposition and the dedicated generated-host section add precisely two labels, for **107 total**.
- Both longtables survive. The historical comments (81 standalone source lines) are preserved in `Paper2B-RemovedSourceAnnotations-v1_1.csv`.
- The **89 direct incoming references** from **10 other paper sources** still have targets, and all **107 explicit outgoing references** resolve to the corpus. The 31-paper corpus has **14,194 unique labels** with no cross-paper collisions.

## Structural and editorial changes

1. A concise abstract replaces the development-stage long abstract; the generation and comparison domains remain explicit.
2. The round-parent and Spin(4) geometry precede a newly promoted **generated six-type momentum-host** section, which distinguishes the bracket constructor, GP2 type-support, $m_p=1$, and GP3 comparison frontier.
3. The subsequent representation, finite-product and recovery mathematics retain their statements and references. The existing mathematical finite-algebra and process-capacity section moves to the main body before inverse/action diagnostics and the final conclusion.
4. The D01 product statement is now a formally labeled proposition, not proved prose with an orphan proof.
5. The duplicate matrix-unit verification is kept as an explicitly alternative constructive derivation; it is not used as a new GP2-generation theorem.
6. Historical source comments, pre-contents release banner, old version headings and post-conclusion mathematics have been removed or relocated. Scientific hypotheses, countermodels, and obstructions remain.
7. Actual I-A/I-B mathematical ownership is distinguished: I-A supplies intrinsic round $S^3$/Spin(4) structures, while existing finite smooth-model and Petersen theorem labels live in I-B.
8. The revised paper uses **`Macros-v2_191.tex`**, which imports the exact current paper roots from v3.060 plus II-B v2.147. Other papers' macros and PDFs are untouched.

## Limits and reproducibility

The universal GP3 physical endpoint-multiplicity comparison remains open under the original three added hypotheses. Finite state or native finite-ancilla tests do not themselves discharge it. This revision adds neither new physical occurrence claims nor measured rates.

- LaTeX compile (`latexmk`/`bibtex.original`): **pass**; **45 pages**.
- Build diagnostics: **0** LaTeX errors; **0** undefined refs; **0** undefined citations; **0** overfull boxes; **0** missing glyphs. Nonfatal underfull warnings may remain.
- `Paper00-MaterializeXrefAliases-v1_20.py` rebuilds **159 canonical/current-source aliases**; old AUX filenames are compatibility paths, not historical theorem evidence.
- Only Paper II-B was rebuilt and changed; the other 30 paper source and PDF pairs remain unchanged from v3.060. They may still show older printed theorem numbering until separately re-typeset.
- Proof-chain audit v1.8 concerns earlier II-B v2.144; source-bound rigorous re-audit and synchronized DAG/proof-chain ownership records remain pending.

## Files for reproduction

Use `apply_p2b_cleanup.py` with `Paper2B-MomentumCarrier-v2_146.tex` from the focused package in an extracted v3.060 release directory (as `release/`); run `verify_p2b_source.py` before removal of the old source, then compile `Paper2B-MomentumCarrier-v2_147.tex` using its shared macros and bibliography. `Paper2B-SourceChanges-v1_1.diff` records the full diff. `Paper2B-CleanupOperations-v1_1.json` and the comment ledger record source provenance outside the main manuscript.

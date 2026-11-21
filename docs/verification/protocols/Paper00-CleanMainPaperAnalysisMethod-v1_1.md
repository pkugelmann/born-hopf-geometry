# Born–Hopf Geometry — Clean Main-Paper Analysis and Preservation Protocol

**Protocol:** `Paper00-CleanMainPaperAnalysisMethod-v1_1.md`  
**Purpose:** reproducible, source-based examination and editorial cleanup of each Born–Hopf Geometry paper without discarding mathematics, weakening derivations, promoting assumptions, or confusing source-integrity checks with independent proof verification.  
**Scope:** Papers I–VII and their technical companions; applies to both a request to **analyze** a paper and a later, separate request to **apply changes**.  
**Version convention:** `PaperXY-Theme-vU_W`; on an update to an existing theme increment the revision counter `W` to `W+1`. For manuscript versions and framework releases, advance the actual current version from the authoritative parent.  
**Current example only:** the uploaded PapersMinimal archive is `Paper00-PapersMinimal-v3_074(1).zip`, with Paper III-F v1.280. These numbers are not fixed protocol inputs; inspect the user's latest project archive each time.

---

## 1. Mission and non-negotiable principles

The main papers must read as **finished mathematical and physical theories**, not as records of their historical development. Remove release chronologies, prior attempts, superseded selector stories, status bookkeeping, migration notes, implementation comments, and repeated explanations **when they are only editorial history**. Place genuinely useful background, long computations, alternative conditional models, counterexamples, exact certificates, and technical proofs in an appropriate appendix or separately owned technical paper **only if relocation is justified and references remain intact**.

**Preserve the mathematics by default.** The task is not to shorten a manuscript by eliminating results; it is to assign each mathematical result its natural logical position. Every stated condition, type, domain, non-implication, countermodel, equation and proof step is part of the content until shown otherwise.

The governing question is **which observable, physical distinction or mathematical result must be explained**, not which conventional Standard Model, general-relativistic or other standard mechanism must be reproduced. A mathematically available object is not automatically a physically occurring one.

Adhere to the framework's own constitutional inputs and terms. Dimensional normalization, G0, GP1–GP3 and their source-specific meaning must not be replaced by an invented stronger assumption. In particular, do not confuse:

- a mathematical construction with a GP2-generated structure or a GP3-selected whole candidate;
- an established role/type support with universal physical endpoint uniqueness;
- an actual G0 occurrence with a mathematical existence or an available test operator;
- a scalar or finite trace coefficient with an observed coupling or complete physical action;
- a generated law, certified flow and actual physical history;
- a conditional Schur/heat/finite-source certificate with a physical source, detector, kinetic process, decay width or lifetime;
- a numerical calibration with an uncalibrated prediction;
- a correct conditional theorem with a failed unconditional proof.

**Two tasks must remain separate:**

1. **Editorial/source analysis:** identify what belongs where, preserve the content, map source owners, describe suggested corrections. This task does *not* modify the paper.
2. **Independent mathematical proof-chain audit:** check derivations, assumptions, counterexamples and typed DAG edges using the actual current source and `Paper00-RigorousVerificationDAGWorkProtocol`. Editorial integrity alone neither proves nor refutes a theorem, nor upgrades its audit status.

Proceed to **applying the cleanup only after the user asks for changes**, unless the original request explicitly includes editing.

## 2. Authoritative source selection and freeze

### 2.1 Establish the actual latest baseline

1. Inspect the **latest accessible project-folder/user-uploaded framework archive**. Do not silently substitute an older assistant-generated conversation ZIP with the same or a higher-looking label. Compare source trees and release parentage whenever ambiguity exists.
2. Find the **one active TeX/PDF pair** for the requested paper. Record paper code, full stem, source version, framework version, ZIP identity, SHA-256 for ZIP/TeX/PDF, and physical source/PDF page counts.
3. Inspect the archive's release notes, current macro registry, bibliography, `xref/` AUX bank, paper inventory and verification manifest. Record their versions, but treat them as release metadata, *not* mathematical proof.
4. Record the corresponding proof-chain audit and DAG Atlas versions, including the **exact manuscript revision** they certify. Preserve any mismatch as a source-version mismatch.
5. If a relevant file is missing or two candidates remain ambiguous, explicitly report the limitation; do not invent content or choose a source merely from a filename guess.
6. Freeze the original byte sequence before analysis. All source line numbers, hashes and object identifiers in the analysis must refer to this immutable baseline.

**Source-of-truth hierarchy:** exact current `.tex` text and original PDF for rendering; actual imported current paper sources and theorem bodies; release-level metadata; source-version-matched proof-audit evidence; historical audits and conversational notes as leads only. A historic theorem-label prefix such as `p1b:` **does not determine ownership**.

### 2.2 Build a source corpus, not just one document

Open the 31 current paper `.tex` roots (or the actual current count, if the framework grows) and build a mapping of **every declared label → paper/version/line**. Build a separate map of references **from** the target and **to** it. Store all source paths relative to the archive; avoid hardcoding the temporary filesystem location or assuming previously generated files survive into a new session.

Retain old AUX *basenames* only as compatibility aliases when appropriate; they are not old paper versions or historical theorem proofs.

## 3. Exhaustive single-paper inventory

Read the **entire source**, not just the abstract and first or last pages. Generate machine-readable inventories and manually check special LaTeX cases:

| Inventory | Required fields / checks |
|---|---|
| Paper identity | paper code/stem; framework/source/PDF hashes; page and source-line counts |
| Section hierarchy | every `\part`, `\section`, `\subsection`, `\subsubsection`, optional heading, start/end lines; section count and nesting |
| Formal objects | every theorem, proposition, lemma, corollary, definition, remark, principle or paper-specific environment; optional title, exact line span, labels, mathematical domain and body hash |
| Proofs | every proof/proofsteps/other proof environment, exact start/end, body hash, nearest or explicitly linked result |
| Labels | every original `\label`, exact declaration source/line, duplicates, labels that appear within a proof or unusual environment |
| Outgoing references | every `\ref`, `\eqref`, `\autoref`, `\cref`, `\Cref`, `\pageref`, `\nameref` and relevant custom reference command; resolved owner and target |
| Incoming references | all current other papers whose references resolve to a target label; number of uses, distinct papers and distinct target labels |
| Citations | every citation key and its **actual printed bibliography entry**, plus nearby cited labels and their true declaring papers |
| Comments/provenance | complete standalone comments, contiguous blocks and meaningful inline comments; distinguish history from proof qualifications |
| Structure after ending | every mathematical object/proof after a supposed conclusion and after `\printbibliography`, including PDF rendering |
| Optional inputs and results | exact conditional, no-go, physical owner, regularity, localization, calibration and occurrence boundaries |

Count *formal objects* separately from proof environments. Record missing or unusual environment types rather than silently omitting them. Deduplicate labels by actual declarations, **not** by textual mention.

**Parsing cautions:** simplistic regular expressions may mis-handle nested optional theorem titles, TeX comments, escaped `%`, multiline commands, a comma-separated `\cref` argument, `\label` inside comments, starred forms or macros that expand into references. Use a brace-aware scanner for headings, a TeX-aware comment filter, and manually inspect exceptions. Source scan counts are a first-stage integrity check, not a proof audit.

## 4. Section-by-section editorial and mathematical diagnosis

For each numbered section, record:

- original heading and line range, formal-object and proof counts, primary mathematical job;
- prerequisites consumed from other sections/papers and where these are proved;
- actual mathematical output and observable/readout interface, **not** merely the standard formalism it resembles;
- every conditional physical realization, operator, source/action, measurement, calibration, limit, regularity and boundary guard;
- whether its current position is logical, duplicated in prose, misowned, misplaced after conclusion/bibliography, or only named by historical status;
- a recommended disposition: `KEEP`, `RENAME`, `SPLIT`, `MOVE_WITH_PROOFS`, `MERGE_EXPOSITION`, `ARCHIVE_HISTORY`, `REATTRIBUTE`, `KEEP_CONDITIONAL`, or `REVIEW_TRANSFER_TO_TECHNICAL_OWNER`.

A section that is very long is not automatically bad. Split it at **mathematical dependency boundaries**, not arbitrary line counts. Keep proofs adjacent to the results they establish. A technical-companion paper may legitimately be substantially longer and contain countermodels or auxiliary calculations that are inappropriate in a clean main paper.

### 4.1 Structural diagnostics

Check for:

- a conclusion that appears before later scientific sections, theorem blocks or proofs;
- a bibliography followed by scientific content;
- numbering such as `3.0.1` from subsubsections without a subsection;
- an unexplained counter reset or pseudonymous `AA`/appendix chapters inserted in the middle of the main body;
- repeated “new theorem”, “legacy”, “deferred”, “formerly”, “current release”, “not yet integrated”, “batch” or old-version language in mathematical titles/prose;
- contradictory comment status (e.g., a compiled theorem called “not yet integrated”);
- misleading “Appendix” references to a **separate technical paper**;
- a conclusion that restates release history instead of deriving the final theorem-level scope;
- an old framework/date/macro import inconsistent with the current source;
- title/TOC/bookmark overflow, fonts, missing glyphs, split equations and bibliography disorder in the PDF.

Record exact source lines. Do not infer these defects from a screenshot alone.

### 4.2 Decide what belongs in the main paper

The clean main text should contain the essential definitions, mathematical constructors, theorems, precise hypotheses, core proofs required to establish its advertised claims, negative results that constrain interpretation, and the interface to actual observables.

An appendix or technical companion may contain **long independent calculations**, finite matrices, exact rank/Gram spectra, algorithms, alternative optional constructions, edge-case countermodels, independent verification scripts, technical regularity estimates and supplemental proof methods.

**Transfer rule:** never move content to another paper just because it is specialized. First identify the real owner, consumer links, source labels, exact proof block, import/definition requirements, and possible duplication. Preserve the canonical theorem label and downstream links or explicitly implement an alias/owner migration. Do not insert duplicate independent assumptions into the destination.

## 5. Actual theorem ownership and bibliography verification

**Do not use paper title, chronological origin or label prefix as the owner test.** For a cited statement:

1. Find its exact current `\label{...}` declaration across all paper sources.
2. Read the actual theorem/proposition and nearby hypotheses; confirm that it supports the use, not just that the label exists.
3. Compare the narrative paper attribution with the **declaring paper**.
4. Compare the `\cite{...}` key with the **printed title and author fields** of the current bibliography entry. Legacy keys can print another paper's title.
5. Correct the paper name and citation key **only at the affected use**, retaining established theorem labels unless a separately verified migration demands otherwise.
6. Never globally repurpose a bibliography key used by other current papers without checking their uses and rebuilding the affected papers.
7. For `Appendix~\ref{...}`, determine whether the target is local or in a technical companion; name the actual owner explicitly.

Output a correction table: source line, claimed owner, label, actual declaring paper/version/line, bibliography key and printed title, proposed wording, and evidence confidence (`EXACT-LABEL`, `CONTEXTUAL-REVIEW`, `UNRESOLVED`).

## 6. Mathematical and physical scope discipline

Before proposing **any** editorial replacement, record the claim's actual quantifiers, parameter range, stage, normalization, source owner and physical readout boundary.

Use a source-bound scope ledger with at least these categories:

- `MATHEMATICAL_CONSTRUCTION`: representation, invariant, operator, finite projector, exact symmetry/Gram/rank identity;
- `GENERATED_GEOMETRY`: structures licensed by the actual upstream G0/GP1–GP3 proof chain;
- `CONDITIONAL_REALIZATION`: requires a named marked action, REG scheme, metric, measure, regularity, finite carrier, spectral window, completion or source word;
- `PHYSICAL_OCCURRENCE`: actual state/history/source/field event requires its explicit G0 and source-incidence map;
- `OBSERVABLE_READOUT`: apparatus, detector, response, physical projection, calibration and measurement protocol;
- `NEGATIVE_OR_NONIMPLICATION`: rigorous obstruction/countermodel, not dispensable history;
- `TECHNICAL_COMPARISON`: optional candidate family, exact numerical certificate or toy/conditional comparison;
- `IMPORT`: earlier theorem with exact mathematical and physical domain;
- `AUDIT_PENDING`: missing current independent verification, **not automatically a theorem gap**.

Do not re-open established type-support or `m_p=1` merely because universal whole-GP3 endpoint selection remains conditional. Do not convert finite spectral geometry into a physical mass, Newton coupling, decay mechanism or lifetime without the exact missing source/action/observable bridge. Do not demand a conventional vertex, metric or gauge theory when a different native construction explains the stated observable.

**Negative results are high-value content.** A no-go result or counterexample that separates an intrinsic result from a stronger physical conclusion normally belongs in the paper or its clearly linked technical proof, not in the deleted history.

## 7. Audit compatibility — strictly separate from editorial review

Inspect the latest relevant `PaperXY-ProofChainAudit` and DAG layer and record their **source file and hash**, not just their version and final status. Determine whether the latest full E1/E3/E4 proof audit was source-matched or only accompanied by a later source-integration addendum.

For each inherited audit issue, distinguish:

1. **Historical issue on old source**;
2. **Source-level repair now present**, with exact current lines;
3. **Independent re-verification of the repaired theorem**, if it actually exists;
4. **Not-source-matched / pending** when no new full proof check exists.

A source repair does not automatically close the issue, and a frozen old `OPEN` status does not automatically refute the repaired current statement. A release validator or successful TeX compilation does **not** count as mathematical E3/E4 correctness.

Use the separate `Paper00-RigorousVerificationDAGWorkProtocol-v2_4` when the user requests a mathematical audit. Preserve canonical DAG IDs, conditionality, provenance, and historical status; do not change proof-chain or DAG archives as a side effect of editorial work.

## 8. Source-anchored action plan and analysis deliverables

For each proposed change issue a machine-readable action record:

| Field | Meaning |
|---|---|
| `action_id` | Stable `PXY-E-###` within this analysis version |
| `priority` | `P0/HIGH`, `P1/MEDIUM`, or lower with reason |
| `original_line_start/end` | Exact frozen-source range, not estimated PDF pages |
| `problem` | Specific structural, bibliographic or ownership defect |
| `recommended_disposition` | KEEP / MOVE / RENAME / ARCHIVE / REATTRIBUTE / etc. |
| `intended_location` | The mathematical chapter/technical owner that should hold the intact content |
| `original_labels` | All labels in the affected block |
| `math_preservation_guard` | What must **not** change mathematically or physically |
| `evidence` | Source excerpt / declaring theorem / PDF page / versioned audit |
| `acceptance_test` | Formal count, proof hash, label and reference checks to pass |
| `audit_impact` | `NONE`, `SOURCE-MATCH-REVIEW`, or user-requested independent audit action |

**Minimum analysis deliverables** (versions use the naming convention, ordinarily `v1_1` on first issuance):

- `PaperXY-CleanMainPaperAnalysis-v1_1.md` — complete report, executive findings, source identity, section map, mathematical boundaries, action plan;
- `PaperXY-EditorialClaimMatrix-v1_1.csv` — every formal statement, type, title, label, lines, owner, SHA-256 and proposed location;
- `PaperXY-FormalProofLedger-v1_1.csv` — every proof, source span, exact hash and associated claim;
- `PaperXY-SectionDisposition-v1_1.csv` — each main section with formal/proof count and recommended editorial disposition;
- `PaperXY-CleanupActionPlan-v1_1.csv` — all identified actions, exact source lines and safeguards;
- `PaperXY-LabelInventory-v1_1.csv`, `PaperXY-OutgoingReferenceMap-v1_1.csv`, `PaperXY-DownstreamReferenceMap-v1_1.csv`;
- `PaperXY-SourceCommentLedger-v1_1.csv` — all comments with line numbers, including ones requiring mathematical review;
- `PaperXY-OwnershipBoundary-v1_1.csv`, `PaperXY-AppendixOwnerMap-v1_1.csv`, and bibliography/source-binding ledger;
- `PaperXY-AuditCompatibility-v1_1.md` — which older audit applies to which exact source;
- `PaperXY-ProjectMergePlan-v1_1.md` — precise parent/project baseline and protected files for a possible later update;
- **one integrity-checked analysis ZIP**, containing the original TeX/PDF, supporting tables, visual evidence, reproducibility scripts, report and checksum manifest.

Do not create an edited manuscript, new framework release, or mathematical audit status during a request that only says **analyze**.

## 9. Applying corrections — only when explicitly requested

### 9.1 Pre-edit freeze

1. Reconfirm the **latest actual project archive**; a later uploaded project ZIP overrides an obsolete hard-coded parent. If the target manuscript has advanced, **rebase the analysis** rather than applying stale line-indexed replacements.
2. Freeze the original TeX/PDF bytes and SHA-256 and copy the complete parent release to an isolated workspace.
3. Confirm all requested dispositions against the current source; do not blindly execute every exploratory candidate in the analysis matrix.
4. Set successor manuscript version (`vU_{W+1}` on that paper's actual sequence), successor framework version, and associated new macro/alias metadata versions. Never manufacture an independent proof-audit version upgrade.

### 9.2 Reversible source transformation

- Work on the **original source**. Use a clear script recording exact old source line ranges and original/replacement text, or a parser capable of moving balanced LaTeX environments. Preserve source anchor provenance for every move.
- Move **whole mathematical blocks** with their definitions, formal statements, proofs, equations, remarks and associated labels. Never split a theorem from its proof or silently change its assumptions.
- Archive all standalone historical comments verbatim with original line numbers. For inline comments, remove only identified provenance, never a TeX command, equation, label or real mathematical guard.
- Remove research-revision history from the rendered manuscript; use timeless mathematical names for headings.
- Fix source owner and bibliography references case by case. Preserve all existing labels; new *organizational* section labels may be added if unique.
- Remove orphan appendix and section-number resets. Finish with **one coherent mathematical conclusion followed by the bibliography**, with no new science afterward.
- Keep technical companion mathematics where it belongs; don't move the entire proof bank to an appendix just because it is long.

### 9.3 Formal preservation tests — stronger than merely counting

Minimum checks, **all required** before claiming preservation:

1. **Object conservation:** every original formal environment count by type retained. Compare each original formal object by stable label, body hash and complete textual diff. Unlabelled objects require a content-based multiset or a tracked block ID.
2. **Proof conservation:** every original proof environment retained, associated with its correct theorem. Compare **full normalized proof texts** (not just the number of proofs). Report every changed proof with an exact diff. If a proof changes outside attribution/typography, stop for review.
3. **Mathematical-expression conservation:** compare all raw and normalized inline/display math expressions, including equation/align and custom operator environments. A count or multiset alone is **necessary but not sufficient**: confirm no expression was moved into a different logical claim, its assumptions were not altered, and operator type/normalization is intact. Explicitly log any justified change.
4. **All original labels retained** and unique. Verify exact label-to-result identity, not only existence.
5. **No lost/duplicated source blocks:** preserve an original-line-to-revised-location map. Every original noncomment mathematical span must be accounted for exactly once. Track removed comments and intentionally replaced editorial lines separately.
6. **Original citation target set preserved**, except explicit corrected ownership/citation actions. Every new/changed reference resolves; inspect moved theorem numbering and imported AUX bytes.
7. **All physical and mathematical guards retained**, including optional conditions and negative results. Manual semantic review is mandatory; regex tests do not prove semantic equivalence.
8. **Theorem/role types:** the physical observable, action owner, measure, source word, regularity and actual occurrence must not have been upgraded by replacing history words such as `conditional`, `selected` or `optional`.

If a guard or substantive proof has changed unexpectedly, **do not claim a clean editorial preservation**. Repair or clearly disclose the deviation.

### 9.4 LaTeX/PDF compilation and review

Rebuild the revised paper from its complete current source tree. Typical build:

```sh
pdflatex -interaction=nonstopmode -halt-on-error PaperXY-Theme-vU_W.tex
bibtex PaperXY-Theme-vU_W   # or the actual available BibTeX executable
pdflatex -interaction=nonstopmode -halt-on-error PaperXY-Theme-vU_W.tex
pdflatex -interaction=nonstopmode -halt-on-error PaperXY-Theme-vU_W.tex
```

Use the actual bibliography and build strategy imported by the manuscript. In these environments `/usr/bin/bibtex.original` may be available when the `bibtex` alias is not; check rather than assuming. Run additional passes if warnings require them. Check:

- LaTeX errors, undefined commands, labels, citations, overfull boxes and missing glyphs;
- no bibliography placed before remaining scientific text;
- actual title/version, PDF page count and table of contents;
- first pages, each newly inserted chapter transition, final theorem/proof, conclusion and final bibliography;
- PDF bookmarks, headings/numbering, equations, tables and page breaks;
- actual displayed author/source titles rather than trusting `\cite` key spellings.

If available, independently extract rendered text or build a second time from the **released ZIP itself** and compare outputs. Document any remaining nonfatal underfull warnings separately.

## 10. Framework ZIP release — no regressions

Create the next release **only from the latest authoritative project baseline**, not from a superseded chat fork. The standard editorial release changes only:

1. the target paper's active `.tex` and `.pdf`;
2. the narrowly necessary current macro registry, bibliography entries and source-current AUX/compatibility aliases;
3. release metadata, manifest, inventory, build-verification and the specific cleanup report.

The other **current paper** TeX/PDF pairs must be SHA-256 **byte-identical** to the parent unless separately authorized. If that invariant fails, investigate; never silently overwrite newer I-B, VI, VII or other results.

Release validation:

- **One current TeX/PDF pair per logical paper**; no competing historical manuscript versions. Historical AUX basename aliases are permitted and must point to the *current owner*.
- Current macro registry contains the exact current paper stems. Handle self-imports correctly.
- No duplicate source labels in the whole collection; all ordinary current references resolve; report **incoming uses to edited paper** and their owner papers.
- The ZIP passes CRC/integrity checks and the entry-by-entry SHA-256 manifest matches the packaged bytes.
- The released TeX source reproduces from the source-edit script and original source hash. If possible, the released PDF independently rebuilds with no unresolved warnings.
- The final release notes state precise changed files, old/new paper version, old/new framework version, counts, checks, limitations and what has **not** been independently re-audited.

Provide: complete latest-only `Paper00-PapersMinimal-vNEXT.zip`, revised target `.tex`/`.pdf`, focused reversible cleanup ZIP, detailed `PaperXY-...Cleanup-vU_W.md` and separate source-version-specific verification-status record.

## 11. Honest status reporting and failure modes

Use the following distinct status words:

- `ANALYSIS_COMPLETE` — full source inventory, ownership/reference/structure map and action plan exist; no files edited.
- `EDITORIAL_SOURCE_UPDATED` — source refactored with recorded text and proof diffs; not necessarily compiled.
- `BUILD_VERIFIED` — PDF compiles and current refs/citations resolve; not proof correctness.
- `FRAMEWORK_RELEASE_VERIFIED` — ZIP is complete, current and parent-preserving with manifest/alias checks.
- `MATHEMATICAL_AUDIT_PENDING` — no source-matched independent correctness check of the current new version.
- `MATHEMATICAL_AUDIT_SOURCE_MATCHED` — use only when the separate rigorous protocol has truly adjudicated the exact version and produced its evidence.
- `PARTIAL / BLOCKED` — explicitly describe which check failed, which artifacts are reliable, and the remaining conditions.

Never say **“all proofs preserved”** merely because the counts match; qualify whether their actual content and associations were compared. Never say **“all problems fixed”** when only editorial/source errors were repaired. Do not infer a mathematical theorem from a release validator, a PDF build, a historical DAG status flag, or a familiar physical formula.

## 12. Compact reusable invocation

When the user says **“Analyze Paper XY”**:

> Read the complete latest project Paper XY source and matching PDF. Apply `Paper00-CleanMainPaperAnalysisMethod-v1_1.md`. Preserve all mathematics and existing status boundaries. Inventory every formal object, proof, label, comment and incoming/outgoing reference, trace actual owners and citations, identify historical narrative and structural flaws, and deliver a complete source-anchored action plan, classification tables, audit compatibility and integrity-checked analysis ZIP. Do not modify source or framework files.

When the user says **“Apply the changes”**:

> Reopen the newest authoritative project archive and the original analysis. Rebase if the source has changed. Apply the preservation-first cleanup with a reversible edit ledger, retain all mathematical results/proofs/labels and conditional physical boundaries, rebuild the paper, run source and PDF checks, and produce the next latest-only framework release preserving the other current papers byte-for-byte. Do not upgrade independent mathematical audit status.

---

## 13. Definition of success

A clean paper is one in which a reader can follow **what is constituted, what is generated, what is proved, what is conditional, how the mathematics is normalized, and which observable is actually explained**, without reading a history of the author's discovery or the framework's release sequence.

A successful analysis has **complete source coverage**, a credible mathematical ownership map, and an executable editorial plan. A successful edit adds **source integrity, reproducibility and release compatibility**. Neither step replaces the independent proof-chain verification protocol.

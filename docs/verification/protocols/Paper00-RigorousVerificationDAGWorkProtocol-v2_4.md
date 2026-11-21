# Born–Hopf Geometry — Single-Paper Multi-Agent Correctness Audit and Global DAG Completion Protocol

**Protocol file:** `Paper00-RigorousVerificationDAGWorkProtocol-v2_4.md`  
**Protocol revision:** 2.4 — Work-mode adaptation of the supplied rigorous verification/adjudication protocol v2.3  
**Operating environment:** ChatGPT Work mode, using multiple coordinated agents when available  
**Audit unit:** exactly **one user-designated paper/manuscript** per run  
**Persistent artifact:** one updated, backward-compatible Born–Hopf **DAG Atlas ZIP**  
**User-visible report:** **all issues found, in chat**  
**Mathematical remit:** verify existing claims rigorously; **do not develop or repair the theory**  
**Presentation remit:** source-level correctness only; **no PDF compilation, rendering, or appearance review**  
**Source authority:** the most recent corpus explicitly supplied/designated for this run; source contents outrank filenames and old summaries.

> **Binding mission.** Conduct a rigorous, full mathematical/physical correctness audit of **one selected paper**, while multiple agents work on distinct evidence functions for that *same* paper. Maintain a single global theorem/constructor/assumption/gap DAG covering the already-audited framework. Verify existing proof steps, including independent and adversarial checks; do **not** derive new framework results, introduce new axioms, add mechanisms, close gaps by inventing lemmas, or rewrite papers. Introduce each distinct condition/assumption **once**, at its earliest established occurrence. All later uses inherit it through verifiable dependency paths. After adjudication, deliver **(1) every identified issue in chat and (2) an updated DAG Atlas ZIP**. A genuine open mathematical gap does not prevent finishing the audit; it must be represented accurately in both outputs.

## A. Activation, boundaries, and priority

1. This protocol activates only when the user's **current request** explicitly asks to audit/verify a **specified paper** using it. Uploading, discussing, or revising the protocol alone does **not** activate an audit.
2. A run audits **one paper** (normally one `PaperXA`/`PaperXB`/... `.tex` manuscript and its directly controlling included mathematical inputs). “Paper III” does not silently authorize a full audit of III-A through III-G. If the user explicitly designates a combined manuscript as one unit, freeze that bounded unit in the run record; never add other manuscripts opportunistically.
3. Other papers may be read to trace or verify **specific imported prerequisites, exact downstream references, and affected interfaces**, but are **not** independently declared audited. A remote imported theorem can be checked to the extent indispensable for the target; log that narrower coverage.
4. Retain the full rigorous correctness standard from protocol v2.3: source-first theorem object, statement layers, type/quantifier/domain checks, constitutional boundary, physical constructor grammar, independent `E3` evidence, applicable adversarial `E4`, issue/challenge adjudication, and propagation. Restrictions in this protocol take precedence over v2.3 passes that otherwise generate new theory.
5. **Disabled:** frontier-consequence discovery/closure (`Pass 5C` as derivation work), optional extensions (`Pass 6`), speculation, new hypotheses, new proofs of previously unstated physical claims, and mathematical gap-repair activity. **Enabled:** alternative computations, exact checks, independent proof *of an existing claimed result*, and counterexample searches necessary to determine whether that existing result is correct.
6. Do not modify any supplied paper, TeX source, mathematical content, macro, bibliography, or original ZIP. Update the DAG archive only. Record recommended repairs as **issues**, never implement them without a separate instruction.
7. No PDF generation/compilation, visual inspection, typography, or document-design work. Existing PDFs inside the incoming archive may be retained unchanged as *historical* files; do not present them as regenerated or recertified by this audit.
8. Work within the actual claimed mathematical and physical domains. Do not demand that a result reproduce a conventional mechanism merely because the framework is nonstandard. Ask which defined **observable or theorem** is claimed and whether the existing proof justifies that claim.

### Nonnegotiable distinction

- **Verification** can replay a derivation, independently check the same mathematical proposition by a different route, test a claimed numerical identity, and search for counterexamples.
- **Theory development** would add a new theorem, independent physical mechanism, stronger conclusion, new axiom, or replacement proof to repair missing mathematics. **It is forbidden in this run.**
- An unproved edge is reported as a **gap with source evidence**. The agents never silently fill it, weaken the conclusion, drop the original result, or redefine the target.
- Missing DAG linkage, missing source location, missing verification evidence, and genuine logical failure are **four different issue classes**. None implies another without proof.

## B. Supplied data and source precedence

The usual project inputs are:

1. Current papers archive (for example `Paper00-PapersMinimal-v2_356.zip`): the **authoritative current `.tex` source**, includes/macros, bibliography, and claim definitions.
2. Current DAG archive (for example `Paper00-DAGAtlas-v1_12.zip`): `DAG/Paper00-TheoremDAG.json`, its `.schema.json`, `DAG/CurrentSourceAnchorMap-*.json`, proof/constructor/strict/citation/scope edges, derived records, observables, issue/review material, scripts, manifests and provenance.
3. The current rigorous verification/adjudication protocol v2.3, incorporated here for technical correctness gates.
4. `Paper00-ProofChainAuditProtocol-v1_1.md` and earlier audit artifacts, used to prevent false gap creation and to locate existing checked proof chains; their **gap-closing instructions are overridden** by this no-new-theory protocol.

**Source rule.** The user-designated current `.tex` controls what the theorem states. The latest source-anchor map is a locator, not proof. In the provided DAG v1_12 archive, `Sources-v2_356/` is current and `Sources/` is historical; the canonical `DAG/Paper00-TheoremDAG.json` was carried forward without a global mathematical reproof. Do not silently use old `Sources/` to judge new `Sources-v2_356/` results. On a later input archive, **re-discover** the current source directory rather than hardcoding these names.

**Authority ordering:** (i) selected current manuscript and its controlling files, (ii) its exact imported theorem statements and proofs in current peer corpus, (iii) existing DAG/evidence ledgers as traceability guides, (iv) previous audit reports and scripts as evidence subject to rechecking, (v) external primary mathematical literature for checking imported claims, (vi) secondary sources only as explicitly qualified support. Prior conversations and summaries are leads, never proof substitutes.

Before audit, inventory all available files, source roles, target identity, label/alias map, archive structure, schema, source anchors, and existing audit evidence. Hashes may be retained for reproducibility, not used as mathematical correctness evidence. A mismatch in a historical filename or revision marker is not a mathematical issue. Missing **controlling mathematical content** is an issue.

### Foundational interpretation guard

Read G0, GP1–GP3, dimensional normalization, constituted seeds, canonical classes and the actual role/constructor vocabulary from current source. The intended G0 formulation in the project's proof-chain protocol is *“Nontrivial complete geometry exists”*; the framework's GP1 (finite and bounded), GP2 (exact and faithful), GP3 (irreducible and least) have source-specific **typed** meanings. Do not replace GP3's comparison preorder by naive smallest-dimension selection, GP2's licensed closure by ambient closure, or constituted geometry by an unstructured host. Treat previously checked `S^1/S^3`, `\mathcal H_1` on `S^3_1`, and `m_p=1` statements as **source-verification checkpoints**, not an invitation to reconstruct them from scratch. A source-established status is preserved until contrary **claim-matched evidence** warrants a challenge.

## C. Single-paper coverage contract

An audit is **full for the target** only if every mathematically substantive result in that paper has a source-bound disposition:

- Explicit definitions, constitutive clauses, assumptions and theorem scope.
- All named theorem, proposition, lemma, corollary, claim and relevant formal remark statements.
- Material unnamed results and equations **consumed by a proof**.
- Calculations, numerical constants, normalization/readout steps and physical claims actually asserted.
- Every indispensable imported premise, proof step, cross-reference, constructor/physical-realization clause and observables interface used by those results.
- Source-proved alternatives, conditional results and explicit exclusions, without treating conditions as automatic defects.

A statement-only citation is not a proof-use edge. A paper's claims may be **audited but unresolved**; that does not make the audit incomplete. Conversely, unexamined claims must remain explicitly **not audited** and bar the label “full audit.”

For each selected claim freeze the exact **SOURCE-AS-PRINTED**, any distinct **INTERPRETED** branches, and any already-present **REPAIRED** wording *as separate objects*. No agent writes a new repair theorem. Record type signature, logical form, exact quantifiers, domain, side conditions, boundary/regularity, approximation regime, selection status, normalization, and physical-identification status.

## D. Agent architecture in Work mode

Use separate agents for **different evidence functions** on the **same target paper**. The coordinator may subdivide one function by theorem groups, but all results must be merged by one registry. If true separate agents are unavailable in a given Work execution, use separately recorded review passes and disclose the limitation; do **not** claim simulated independent agents.

| Responsibility | Authorized work | Required return object |
|---|---|---|
| **Coordinator / registry owner** | Freeze paper, sources, work packages, IDs, acceptance gates; adjudicate integration | Run manifest and central registries |
| **Source and claims extractor** | Exhaustive target-source inventory, labels, proof spans, macros, source premises | Claim/definition manifest with coverage |
| **Proof replayer** | Check the exact source argument line by line, types and consumed hypotheses | `E1` replay/evidence records and candidate gaps |
| **Independent verifier** | `E3`: distinct mathematical checks of **existing** claims; no new theoretical results | Independent certificates with lineage |
| **Adversarial verifier** | `E4`: exact-negation attacks, boundary cases, counterexamples matched to actual hypothesis/grammar | Valid/invalid/unresolved witness records |
| **Assumption and boundary registrar** | Canonicalize first appearance of every actual assumption/condition, trace discharges and scopes, `BND` semantics | One global premise register + typed use edges |
| **Dependency and interface mapper** | Confirm proof-use edges, conditional routes, cross-paper imports, observed descendants | Provenance-backed graph edge proposals |
| **Graph integrator / release verifier** | Merge reviewed records and evidence, test schema/graph completeness, verify ZIP after writing | Updated DAG ZIP, integrity and coverage report |

**Independence is epistemic, not a headcount.** Two agents that import the same disputed step do not furnish independent `E3` evidence. Keep independent-verifier inputs to the theorem object, necessary source definitions and declared premises—not the earlier agent's verdict or expected test output—until a provisional result is recorded. The adversarial agent attacks the *same* theorem object and domain. Every proposed adverse finding is reviewed against the exact current source before adjudication.

### Safe parallelism and integration

1. The coordinator makes **read-only snapshots** of input files and allocates **globally unique IDs** and disjoint work packages.
2. Parallel agents create **proposal files**; they do not independently edit the canonical graph or source ZIP.
3. The assumption registrar has single-writer authority for canonical condition identities; other agents propose aliases/uses.
4. Graph integration is single-writer and deterministic. Resolve overlapping records, alternative proof routes, duplicate claims, contradictory status proposals and stale source locators **before** writing the new archive.
5. The coordinator records who checked each proposition, what evidence each agent used, conflicts, and the eventual verdict. No consensus/majority vote can replace a proof or refutation certificate.

## E. Correctness evidence, statuses and mandatory challenge gates

Preserve the v2.3 epistemic statuses:

`REPORTED`, `FORMALIZED`, `REPRODUCED`, `VERIFIED`, `VERIFIED-CONDITIONAL`, `INCONSISTENT`, `REFUTED`, `UNRESOLVED`, `OUT-OF-SCOPE`.

Track lifecycle separately: `ACTIVE`, `UNDER-CHALLENGE`, `STALE`, `SUPERSEDED`, `RETIRED`. An inherited status remains evidence-backed only if its source and proof lineage remain applicable. New source-content changes invalidate affected evidence, not unrelated established results.

Use these evidence levels, **not** a vote or confidence percentage:

- `E0 INTEGRITY`: file, label, edge/index, archive or state checks; **not mathematical verification**.
- `E1 REPLAY`: reproduce the source proof/calculation; not independent.
- `E2 CORROBORATION`: special cases, dimensional checks or supporting literature sharing the disputed premise; not sufficient alone.
- `E3 INDEPENDENT`: a separate exact calculation, theorem application, representation, independent oracle or proof of the **same stated result** that does not import the disputed step.
- `E4 ADVERSARIAL`: exact-negation attack, structurally valid counterexample search, boundary or mutation test, and scrutiny of premise/quantifier/normalization.

A material ordinary central claim may be called `VERIFIED` only with a complete `E1` replay and applicable `E3`. High-impact nodes—default: three or more central downstream results, constitution/physical-realization bottlenecks, or observables boundaries—also require an adequate `E4` challenge. The auditor may not self-certify by checking that a script reprints the intended status. Preserve valid and invalid attack histories. If a decisive check cannot be completed, use the appropriate lower status, record the exact missing evidence, and **still include the finding in the DAG**.

### Mandatory theorem-boundary gate

Before alleging a hidden assumption, illegitimate selector, false finiteness claim, missing seed, overgeneration, or an unlicensed operation, create/refresh a source-anchored `BND-nnn` record:

1. Source clause that **constitutes**, **generates**, **realizes**, **minimizes**, **classifies**, **derives**, **interprets**, or **calibrates** the disputed item.
2. Its chronological stage, exact mathematical/physical sort, frozen prior inventory, actual candidate class and relevant completeness scope.
3. What constructors and partial evaluations are licensed, their domains/codomains, output retention/reuse/iteration, and what belongs only to the **ambient host mathematics**.
4. Separation of existence `E`, uniqueness `U`, canonicality `C`, physical realization `R`, and interpretation `I`; no arrow among these is automatic.
5. Exact quantifier domain (global/stage, fixed/varying carrier/action, boundary and equivalence classes) of both theorem and downstream consumer.
6. Whether a word such as “first,” “lowest,” or “intrinsic” is a descriptor, actual physical selector, constructor, classification, or host-only fact.

Use provenance tags `[CONST]`, `[FROZEN]`, `[GEN]`, `[REAL]`, `[MIN]`, `[DER]`, `[CLASS]`, `[HOST]`, `[ID]`, `[CAL]` with ordered histories. Do not demand a downstream rule regenerate explicitly constituted content; do not promote ambient mathematics to a physical constructor; do not accept “intrinsic” as proof of a bridge theorem. For leakage/closure disputes, require a **typed physical-constructor word** with licensed retention and reuse at each step. Without such a record, classify the issue `UNRESOLVED / boundary review required`, not established refutation.

### Mathematical and physical checks

For every material proof: exact statement, quantifiers, premises, types and codomains; algebra/signs/factors; local/global and limit exchanges; convergence, boundary conditions and regularity; circularity; exact/approximate distinctions; equality/isomorphism; conditions for imported theorems; calibrated versus predicted constants; gauge/symmetry and physical occurrence; normalization, trace carrier and denominator; operator versus scalar and projection versus multiplication; finite-carrier versus ambient host. Independently test edge cases and known soluble controls where applicable. A proof of a conditional result is not a proof of its antecedent, but is not a defect merely for being conditional.

**Refutation rule.** A `REFUTED` verdict requires a certificate identifying the exact target and negation, witness type, valid hypotheses/domain, matching seeds/constructors/completeness scope, explicit failure calculation, positive control and independent replay. A counterexample to a stronger or different proposition must **not** refute the source claim.

## F. Canonical assumptions and conditions — **one introduction only**

### F1. Single-node rule

**Each distinct mathematical/physical condition, hypothesis, constitutive principle or restriction is a first-class DAG node introduced exactly once** at its earliest identifiable **logical** appearance in the current source-verified framework. This is the one canonical occurrence; later papers may have **use edges** to it but must never redefine it as another assumption node.

Identity is based on the **normalized predicate together with its types, quantified domain, parameter regime, strength, and provenance**, not on spelling. An assumption such as `compactness of X`, `compactness of X under Y`, and a stronger global compactness claim are not automatically identical. Conversely, notational aliases of the **same** fully typed premise are one node. Merge only when equivalence is already supported by checkable evidence; otherwise flag `POSSIBLE-ALIAS` and do not silently equate distinct predicates.

The canonical assumption registry is **global across papers and audits**, not recreated in each paper's report. Stable IDs (e.g. `BH-A-000123`) are never reused. Source aliases and local labels map to the canonical ID.

### F2. Required assumption record

For the **single introduction node**, store:

- canonical ID and normalized statement (prefer logical or mathematical notation, not just a prose label);
- precise type, variables, quantifiers, value/domain ranges, regularity, boundary and stage/role scope;
- earliest validated source identifier, label, equation/proof span and, if partial ordering is insufficient, `FIRST-KNOWN` rather than falsely claiming absolute priority;
- category: `FOUNDATIONAL`, `CONSTITUTIVE`, `MATHEMATICAL`, `DOMAIN`, `REGULARITY`, `BOUNDARY`, `SELECTION`, `NORMALIZATION`, `APPROXIMATION`, `PHYSICAL-IDENTIFICATION`, `EMPIRICAL-CALIBRATION`, `EXTERNAL-THEOREM`, or other explicitly typed kind;
- epistemic status: `STIPULATED`, `PROVED-UPSTREAM`, `DERIVED-FROM-RECORDED-CLAIM`, `CONDITIONAL`, `UNRESOLVED`, `REFUTED`, or `NOT-YET-LOCATED`; with separate lifecycle;
- whether assumed, asserted, proved, independently verified, calibrated, or merely scoped, and the exact evidence for that classification;
- its **direct** prerequisites, existing proof of discharge (if any), alternative established discharge paths, and relevant `BND` record;
- assumptions/claims explicitly depending on it as **direct** edges; all **transitive** influence must be computed, not stored as repeated assumption declarations;
- any unverified equivalence, stronger/weaker variant, or source-provenance conflict.

A condition logically introduced by a verified earlier theorem may have status `PROVED-UPSTREAM` and remain visible as its own node; it must **not** be counted as an *open* assumption. G0 and GP1–GP3 have explicit constitutional provenance, not default missing-proof classifications. A later proof relying on a previously discharged condition gets a path to the upstream proof, not a new condition.

### F3. First-appearance and inheritance algorithm

1. Collect explicit and **actually consumed implicit** conditions from every step of the target paper, plus the necessary imported scopes. Do not invent hypothetical conditions unrelated to an actual proof use.
2. Normalize their exact types, strength and scope; look up the global canonical registry and all proven aliases.
3. When already registered, attach an explicit **direct `REQUIRES`/`USES-CONDITION` edge only where the dependency is not already carried by the actual proof path**. The same condition node remains the sole source.
4. When new, locate the first occurrence in the framework's established dependency ancestry. Do not infer a logical order merely from filename or paper number. Record `FIRST-KNOWN` and a relocation/alias action if earlier evidence is not presently accessible.
5. Distinguish an explicitly stated hypothesis from an inference prerequisite implicit in a computation; link the latter to the exact step and mark it `INFERRED-CONDITION` for adjudication.
6. Compute the **condition ancestry** for every target claim/observable by following **verified material dependency edges** and per-proof-route guards. Never duplicate assumptions as downstream nodes or paste their full statements onto every descendant.
7. If a claim has **alternative proofs (OR)**, list assumptions **per certified proof route**. An assumption required by only one route is not globally necessary when a valid independent bypass exists. All inputs to a single proof route/constructor (AND) must be satisfied together.
8. A verified upstream theorem may discharge a condition, but cite the **specific discharge edge**; never infer discharge from matching words, repeated use, or status flags.
9. When a source introduces a distinct **stronger**, **weaker**, or **specialized** predicate, allocate a distinct canonical node, and record the mathematically supported implication, if any. Unproved equivalences remain issues, not automatic merges.
10. After each correction, recompute inherited conditions for all affected downstream routes; do not alter unaffected upstream meanings.

**Invariant:** for a downstream observable `O`, the DAG query `conditions(O)` produces exactly the union of active conditions on each source-supported proof route, with scopes and discharge status. `descendants(A)` enumerates all currently known claims whose **actual** dependency routes use assumption `A`, including cross-paper consumers. The graph must support a concrete trace from `A` to `O`; resemblance or citation alone does not establish that trace.

## G. Typed DAG: existing atlas + auditable new layer

### G1. Preserve the existing canonical graph

Start from the supplied `DAG/Paper00-TheoremDAG.json` and schema. Preserve existing graph IDs, proof flags, claim statuses, constructors, source manifolds, role nodes, legacy proof/strict/constructor/scope/derivation/citation edges, and historical source locators. Use the source-anchor map for **current** locations. The current archive contains separate evidence classes; they must **not** be flattened into one undifferentiated `depends_on` edge set.

**Historical rule:** a citation edge is navigation, a source-reported proof-use link is a **candidate** until semantically reviewed, and an `E0` synchronization success is not `E3` verification. Existing quarantined candidates remain quarantined unless *this audit* resolves them with a real source-matched certificate. Never upgrade all inherited graph edges or statuses as a bulk convenience.

### G2. Add a namespaced audit layer, not a competing DAG

The successor archive MUST integrate a current **audit layer** into the global graph while preserving backward compatibility of its documented core keys. Prefer machine-readable files under `DAG/AuditLayer/`, registered from the canonical graph by a backward-compatible `graph_layers`/audit-index entry (or an equivalent documented extension that existing validators tolerate):

- `AssumptionRegistry.json`: single canonical node per condition plus aliases and first-appearance evidence;
- `GapRegistry.json`: single canonical gap/issue origin with material dependency and effect paths;
- `AuditClaimLedger.json`: target-paper claims, precise status/lifecycle, evidence lineage and coverage;
- `TypedDependencyEdges.json`: `from`, `to`, typed relation, proof route, AND/OR group, source evidence, review status and domain guard;
- `ProofEvidenceLedger.json`: exact source locators, replay, `E3`, `E4`, negative and failed checks;
- `AuditRuns.json`: selected target, source freeze, agent assignments, challenges, adjudications, provenance and version ancestry;
- `ImpactIndex.json`: derived direct/transitive affected routes, verified bypasses and unresolved remote coverage;
- `CoverageAndValidation.json`: coverage denominator, excluded items, graph checks, artifact write certificate and archive integrity.

Names may adapt to the actual existing schema, but **the semantic objects and graph links are mandatory**. These sidecars MUST be indexable as **one combined DAG** with the existing theorem graph, not unlinked reports. Prefer updating existing canonical records/indices **only** when semantically justified and when backward-compatible validation succeeds. If a legacy renderer cannot accept assumption/gap node types, retain them in the linked typed audit layer and update the query/index integration rather than corrupting the old schema. Record precisely which layer is authoritative for which edge kind.

### G3. Edge semantics and proof-route logic

Every edge MUST specify its type and provenance. At minimum distinguish:

| Edge | Meaning |
|---|---|
| `PREMISE_OF` / `REQUIRES` | Indispensable premise actually consumed by a specific proof route |
| `PROVES` / `DISCHARGES` | An identified proof establishes a condition/target at the recorded scope |
| `IMPORTED_PROOF` | Target proof uses a specific earlier theorem, with source-use evidence |
| `CONSTRUCTOR_INPUT` | Licensed physical constructor argument, with its contract and retention policy |
| `SCOPE_GUARD` | The theorem is valid only within this condition/domain/branch |
| `NORMALIZATION_CHOICE` | Explicit readout, measure, trace or coefficient branch |
| `INTERPRETATION_OF` | A physical label assigned to a mathematical result, *not* a proof edge |
| `EVIDENCE_FOR` | Replay, independent check or attack supporting a verdict |
| `ALTERNATIVE_ROUTE` | Independently checked proof/constructor path with explicit OR semantics |
| `ISSUE_AT` / `BLOCKS_ROUTE` | Gap located at a precise step, affecting only routes that consume it |
| `CITATION_ONLY` / `CANDIDATE_LINK` | Reference or suspected dependency **not authorized** for theorem propagation |

Orient material edges consistently (premise/source `→` consumer/target); for a formal hyperedge with several required inputs, use an explicit route/constructor object and an **AND** input group. Distinct routes for one target form **OR** alternatives. The graph must not infer that one of several hypothetical possibilities is physically selected. Cross-paper links must have a source-use witness and quantifier/type compatibility check.

### G4. Graph invariants

1. Every new claim, assumption, issue and reviewed edge has a stable, unique ID and current source/evidence locator.
2. Every activated status has a supporting evidence record and lineage; status labels alone are not certificates.
3. Every **material** edge has a typed, claim-matched proof-use witness and explicit scope guard. Citation/candidate edges cannot promote a claim.
4. Every assumption is introduced once; aliases are references, never independent copies. Every downstream inherited condition is reachable by graph traversal in the correct proof route.
5. Every unresolved issue has an exact target step and an upstream/backward plus downstream/forward path **as far as verified records permit**.
6. Every direct edge imported from another paper has source/current-label resolution; missing or ambiguous imports are separate coverage/locator issues.
7. Alternative routes are never collapsed into one conjunction; one route's weakness does not automatically invalidate a valid bypass.
8. Every mathematical cycle among supposed foundational proof dependencies is flagged for review; definitional equivalences, simultaneous systems and citations must not be mislabeled as ordinary acyclic proof ancestry.
9. No unsupported status promotion, no automatic global closure, no duplicate assumption node, no dangling required material edge, no silent overwrite of a source claim or earlier adjudication.
10. Every issue's listed downstream effects can be regenerated from paths in the graph; speculative effects are explicitly tagged `POSSIBLE / UNCONFIRMED`, not asserted dependencies.

## H. Gaps, issues and downstream impact

**Every found issue becomes a uniquely located, persistent, typed DAG object.** The issue first appears at the **earliest demonstrably defective/unresolved material step**, not at each later theorem that inherits the problem. Preserve later occurrences as affected paths or separate issues only if they introduce a distinct defect.

Mandatory issue classes include:

- `LOGICAL_GAP`: indispensable implication missing or not validly supported.
- `INCORRECT_STEP`: algebra, sign, factor, theorem application, circularity or logical invalidity.
- `COUNTEREXAMPLE`: exact in-domain refutation, with full certificate.
- `MISSING_CONDITION`: consumed hypothesis not stated or discharged.
- `CONDITIONAL_FRONTIER`: valid result with open antecedent or a not-yet-established physical realization.
- `TYPE_OR_DOMAIN`: object/operation, quantifier, boundary, action/carrier or local/global mismatch.
- `NORMALIZATION_OR_READOUT`: choice of trace, measure, physical coefficient, calibration or unproved identification.
- `CONSTITUTION_OR_SELECTION`: source-demonstrated boundary/role or canonicality/realization issue, only after `BND` warrant.
- `CROSS_PAPER_CONFLICT`: true content conflict after checking types, domains, macros and conventions.
- `MISSING_EVIDENCE`: source proof not rechecked, missing independent check, absent controlling mathematical data.
- `DAG_COVERAGE`: missing or wrong graph edge/node, historical anchor, alias, source location or unsupported status.
- `DAG_INTEGRITY`: stale index, collision, invalid schema, broken source link or cycle.

Do **not** conflate a legitimate assumption with a gap. A theorem is not defective for making its conditional scope explicit; the unresolved antecedent remains a graph-visible condition and, where applicable, a **frontier obligation** for the stronger downstream physical claim.

### H1. Issue certificate — required for every finding

Each `BH-G-xxxxxx` / `I-nnn` record must include:

```yaml
issue_id: BH-G-000001
class: LOGICAL_GAP
severity: critical | major | moderate | minor
lifecycle: OPEN | UNDER_CHALLENGE | RESOLVED | SUPERSEDED
first_origin:
  paper: PaperXY
  theorem_id: exact-source-label
  step_locator: source-file:lines-or-equation-label
  source_excerpt: short-exact-quotation
statement_layer: SOURCE-AS-PRINTED | INTERPRETED | EXISTING-REPAIRED
exact_obligation: "Premise P -> conclusion Q, in source's domain"
source_replayed: true | false
independent_evidence: [EV-id]
adversarial_evidence: [EV-id]
constitution_boundary: BND-id | null
conditions_consumed: [BH-A-id]
conditions_open: [BH-A-id]
issue_status: established | unresolved | conditional | invalidated
upstream_material_paths: [explicit-node-paths]
downstream_verified_paths: [explicit-node-paths]
other_papers_affected: [paper-and-node-ids]
possible_unconfirmed_impacts: [node-ids]
verified_bypass_routes: [route-ids]
why_it_matters: "what source claim or observable is affected"
resolution_requirement: "exact missing proof/evidence/choice; NO invented repair"
audit_scope_limit: "what was not checked"
```

Severity is determined by logical/physical consequence and verified reach, not by how surprising the finding sounds. A missing documented proof edge is **not** proof that the mathematical implication fails. All attempted counterexamples that do not meet the target hypothesis go in the negative evidence ledger; they cannot support a `REFUTED` status.

### H2. Impact propagation

For an issue or open condition, trace all **certified** downstream material paths already in the global DAG. Classify each result/route as:

- `DIRECTLY_BLOCKED` — every currently certified indispensable route consumes a failed/unresolved step;
- `INHERITS_CONDITION` — a live proof route remains correct only under a specific condition;
- `INDEPENDENT_BYPASS` — an established route avoids the issue;
- `POSSIBLY_AFFECTED` — plausible or citation-only connection **not** certified as a dependency;
- `NO_PROVEN_IMPACT` — no current evidence-backed path.

If a problem in the selected paper reaches an earlier or later paper, display the exact **path**, affected claim IDs, and limits of remote audit coverage. Do **not** label an unaudited remote theorem `REFUTED` simply because a possible dependency exists; place it under impact/challenge if the particular route is verified. When an alternative route exists, preserve it and its own conditions. Propagate assumption and epistemic statuses per **route**, not by indiscriminately taking the minimum over all incoming edges.

## I. Mandatory run sequence (single paper, multiple agents)

### Pass 0 — Freeze target and archive

- Record the one target manuscript, requested coverage, current authoritative files, macros/includes, bibliography and matching current source anchors.
- Read DAG README, schema, existing status/evidence conventions, known quarantined candidates and review history. A previously indexed claim or a green synchronization test is not presumed reverified.
- Allocate central IDs, create read-only source snapshot and assign parallel agent packages.
- Establish a **baseline ledger/count** of existing nodes/edges/assumptions/gaps and current source identities. Never begin by rewriting the whole graph.

### Pass 1 — Exhaustive target claim census

- Source-extractor inventories all substantive statements and relevant unnamed proof inputs in **the selected paper**; include technical appendices and source-defined physical readouts if part of that manuscript.
- Coordinator assigns proof groups so every census item has an audit owner and independent challenge allocation where required.
- Mark any unlocated/missing controlling text. The paper cannot be declared fully audited while a substantive item has no disposition.

### Pass 2 — Source-bound formalization + boundary mapping

- Freeze exact statement layer, types, quantifiers, mathematical conventions and precise scope for each target claim.
- Resolve the source's constitution/realization hierarchy and typed constructor grammar before criticizing missing selectors, generated closures or physical occurrence.
- Assumption registrar inventories **all actually used** conditions and links them to existing canonical nodes, or creates a **single first-occurrence record** after checking global ancestry.
- Graph mapper proposes each candidate dependency from source proof-use evidence—not from a bare citation.

### Pass 3 — Parallel correctness checks

- Replayer verifies source derivation step by step (`E1`).
- Independent verifier seeks source-independent check **of the identical existing target**, not a new theorem (`E3`).
- Adversarial verifier targets the same formal negation, actual seeds/operators/conditions and boundary (`E4`).
- Record every unresolved indispensable step and every invalid as well as valid attack. No new theory, gap repair, optional generalization or observable prediction work.

### Pass 4 — Imported dependencies and precise cross-paper interfaces

- Verify or read the **specific** prerequisite and exact scope needed by the selected target, consulting other papers only within this bounded task.
- Classify prior dependency as `FOUNDATION`, `CONSTITUTED`, `EARLIER_PROVED`, `DEFINITION`, `CONDITION_DISCHARGED`, `CONDITION_OPEN`, `EVIDENCE_MISSING`, `INVALID`, or `NOT_RELEVANT_TO_TARGET_SCOPE`.
- Reconcile imported assumptions through the global canonical register and attach only necessary direct use edges.
- Follow forward paths into other papers **for impact mapping only**, without auditing those papers as a new target.

### Pass 5 — Adjudication and gap certification

- Independently assess each proposed `VERIFIED`, `VERIFIED-CONDITIONAL`, `INCONSISTENT`, `REFUTED`, or `UNRESOLVED` result.
- Require full constitution/typed-word certificates before accepting a closure/selector refutation; distinguish source-as-printed and interpretation branches.
- For every issue, identify the **earliest actual** missing/failed material transition and exact necessary conditions. Check it was not already discharged by an earlier framework proof or bypass.
- Resolve contested status proposals by checkable evidence, never by consensus. Preserve rejected allegations and reasons in the audit history.

### Pass 6 — DAG completion and assumption inheritance

- Integrator adds the target claims and reviewed dependencies, condition identities, scope guards, evidence, gap nodes and per-route proof semantics to the **existing global DAG**.
- Preserve source identities, correct previously erroneous links **only with source-matched evidence**, and leave unrelated historical material untouched.
- Regenerate backward (`prerequisites`), forward (`descendants`), assumption-inheritance and gap-impact indices across the combined graph.
- Record issue impacts on other papers without promoting or retroactively auditing their claims.

### Pass 7 — Independent audit-completeness and graph-consistency review

A reviewer independent of the graph integrator compares the final candidate against the **original target source and baseline**:

1. Every substantive target claim has a status, exact source locator, relevant evidence and audit coverage.
2. Every actually consumed assumption/condition has precisely one canonical origin and a reachable use/discharge path.
3. Every target dependency edge agrees with a material source proof use, typed domain and relevant branch; no citation was promoted by accident.
4. E3/E4 proof independence is real, not inherited verdicts or self-confirming scripts.
5. Every candidate gap is correctly distinguished from a documented conditional theorem, missing graph link or ambient-host-only construction.
6. Every confirmed gap has a single source origin, known ancestry, impacted descendants and a defined next resolution requirement.
7. Cross-paper effects and observable ancestry follow the **real** routes, including verified bypasses and `POSSIBLE` branches.
8. The archive can be queried to show the complete per-route inherited conditions for any checked claim and observable.
9. Existing unrelated statuses, proof flags, source files and historical provenance have not been corrupted.
10. The new archive passes JSON/schema, references, uniqueness, index-reconciliation, archive-integrity and applicable existing validator checks. **Do not run PDF-dependent/visual checks as a release gate.**

### Pass 8 — Release artifacts and post-write verification

- Generate the next DAG Atlas archive version according to `PaperXY-Theme-vU_W`, increasing `W` by **one** for each successor of that artifact. Example: input `Paper00-DAGAtlas-v1_12.zip` → output `Paper00-DAGAtlas-v1_13.zip`. Never overwrite the supplied ZIP or silently skip a revision.
- Preserve all relevant original archive contents; include the integrated global graph and linked audit layer with source anchors, evidence and validation files. Preserve unchanged source copies and historical PDFs as historical—not newly audited or rebuilt.
- Reopen the **exact newly written ZIP**, read back every mandatory entry, validate JSON, issue counts, registries, source/edge locators, first-occurrence uniqueness, changed nodes/edges and a sample of forward/backward impact queries. Record `WRT-nnn`/artifact-write certificate including the actual output identity and archive hash.
- Deliver **every found issue in chat**, then the verified download link to the new **DAG ZIP**. The audit report and the archive must contain matching issue IDs and counts. Do not substitute an issue-file link for the chat report.

## J. Release output contract — exactly two primary user deliverables

### J1. Chat: **all identified issues**

The final Work response MUST contain:

1. The one paper audited; current source set; coverage count (substantive claims checked/total); outcome counts by evidence-backed status, separately from issue counts.
2. **Every found issue**, even minor ones, in chat. Each entry gives its stable issue ID, category, severity, exact theorem/equation/source locator, explanation of the failure or uncertainty, conditions/assumptions involved (using canonical IDs), immediate upstream source, proven cross-paper/observable impact paths, and precise remaining obligation. Group related manifestations under their **one earliest-root issue**, but show all distinct defects. Include link-free `POSSIBLY_AFFECTED` items separately from proven impact.
3. A separate concise distinction between (a) mathematical defects, (b) valid but conditional claims/open assumptions or physical interfaces, (c) verification/evidence gaps, and (d) DAG-only integrity/coverage defects. A condition is not called a mathematical error just because its antecedent remains open.
4. The target paper's final audit classification: `FULLY_AUDITED` or `PARTIALLY_AUDITED`, and separately `WITH_OPEN_GAPS` / `WITHOUT_CONFIRMED_OPEN_GAPS`. Do not call the framework globally verified after one paper.
5. A direct link to the **one updated DAG ZIP** and a compact statement of its validation result. No mandatory standalone PDF, paper rewrite, second audit archive, or separate downloadable issue report.

**No summary-only issue list.** If there are many findings, use compact entries and grouped sections but enumerate **all distinct issue IDs in chat**. Reflect every ID verbatim inside the ZIP's `GapRegistry.json`. Do not substitute “see attached file for other issues.” If the chat channel imposes an actual message-length limit, send the remaining enumerated issues in the available continuation mechanism rather than falsely claiming a complete report.

### J2. ZIP: complete **updated DAG Atlas**

The ZIP MUST contain the **revised global graph**, not just a standalone paper-level audit addendum. It MUST preserve existing graph/provenance data, make target audit changes queryable, and include at minimum:

- updated canonical graph/index or a documented backward-compatible global graph + registered audit-layer combination;
- all checked claims/steps and their source/evidence status;
- all existing and newly found canonical assumptions and scoped condition edges, **without duplicating assumptions downstream**;
- all identified gap nodes with exact origin, assumptions and impact paths;
- verified material dependencies, alternative routes/bypasses and non-promoting citation/candidate references;
- cross-paper interfaces and observable-impact traversals supported by real graph paths;
- audit coverage, challenge/revision history, evidence-lineage registry and integrity checks;
- README documenting how to query assumptions for any theorem/observable, forward impacts of any gap, and which graph layer contains each kind of node/edge;
- preservation of original archives' mathematically controlling source content and named provenance where applicable, with versioned artifact-write verification.

A DAG archive with only a list of issues, a graph picture, an unlinked `audit.json`, or unchecked generated edges **fails** this requirement.

### J3. Honest completion states

- `FULLY_AUDITED_WITH_OPEN_GAPS`: every target claim has been examined/classified, and precise unresolved proof obligations remain. **Valid completion**.
- `FULLY_AUDITED_NO_CONFIRMED_GAPS`: every target claim was examined/classified; **does not imply global mathematical completeness** or absence of possible undetected error.
- `PARTIALLY_AUDITED`: some target claims, evidence gates, or controlling sources could not be examined. Report exact omissions; do not label the audit complete. Still produce an appropriately labeled updated DAG ZIP whenever safe.
- `ARTIFACT_NOT_VERIFIED`: ZIP write/readback/schema validation failed. Do **not** claim an updated ZIP was delivered; report the precise failure and retain available issue findings in chat.

## K. Minimal machine-readable record rules

These are semantic field requirements; actual serialization may follow the incoming atlas structure.

```json
{
  "assumption": {
    "id": "BH-A-000001",
    "statement": "fully typed and quantified predicate",
    "category": "DOMAIN",
    "status": "CONDITIONAL",
    "first_occurrence": {"paper": "PaperXY", "source_label": "exact label", "locator": "source:line"},
    "canonical_aliases": [],
    "proved_or_discharged_by": [],
    "direct_prerequisites": [],
    "lifecycle": "ACTIVE"
  },
  "material_edge": {
    "from": "BH-A-000001",
    "to": "Pxx-Cnnn",
    "kind": "REQUIRES",
    "proof_route_id": "ROUTE-0001",
    "logic_group": "AND",
    "scope_guard": "exact bounded claim scope",
    "source_use_locator": "proof label/line",
    "reviewed": true,
    "evidence_id": "EV-0001"
  },
  "gap": {
    "id": "BH-G-000001",
    "first_origin": "exact theorem/step",
    "issue_class": "MISSING_CONDITION",
    "condition_ids": ["BH-A-000001"],
    "affected_route_ids": ["ROUTE-0001"],
    "proven_impact_paths": [],
    "possible_unconfirmed_impacts": [],
    "status": "OPEN",
    "source_evidence": ["EV-0002"],
    "next_required_certificate": "specific proof, source evidence, or decision"
  }
}
```

For any graph algorithm, **prove its input edge class**: `CITATION_ONLY`, candidate, scope, and interpreted bridges cannot accidentally enter theorem proof ancestry. Use the current source anchors for location repair, not as evidence that a new proof edge is mathematically sound. Record exact negative results: missing edges from an automated extractor are not automatically missing theorem premises.

## L. Final acceptance scenarios

A run fails the protocol if any of the following happens:

1. An agent starts a full audit of an untargeted neighboring paper or launches an open-ended mathematical extension.
2. An E3 agent develops a new physical theorem rather than independently checking the target's existing claim.
3. `m_p=1`, `\mathcal H_1`, S¹/S³, or another source-established checkpoint is reopened on the basis of a remembered objection rather than the actual matched proof.
4. A constitution/seed claim is challenged by a host-only mathematical operation that has no licensed physical-constructor word.
5. A valid conditional theorem is treated as false solely because the antecedent has not yet been established for physical occurrence.
6. The same assumption is inserted as a new node in Papers IV, V, and VII when its canonical first appearance is in Paper II; downstream links must resolve to that one node.
7. A more restrictive condition is silently merged with a weaker assumption, or an inferred assumption is silently labeled as source-stipulated.
8. A target with two verified alternative routes is marked blocked even though one route bypasses the challenged assumption.
9. A citation/reference to another paper is promoted to a proof edge without semantic proof-use and domain evidence.
10. A gap is reported independently at ten descendant claims rather than once at its real origin with ten traceable effect paths.
11. A source locator is stale but the theorem is declared refuted without resolving what the current source says.
12. Every target result is called verified because the JSON/schema and scripts passed.
13. The issue report in chat omits minor, conditional, evidence or DAG integrity findings that were recorded in the archive.
14. The supplied atlas is returned unchanged with a new name, a paper-local delta only, or a ZIP whose edited contents were not read back and verified.
15. A revised Atlas PDF is advertised despite no mathematical and source-identity-compatible regeneration (PDFs are not produced by this protocol).

### Satisfying end-to-end scenario

Select one paper (e.g. a `Paper5C` manuscript). Multiple Work agents independently extract, replay, verify and attack **all its material claims**, checking only the exact imported theorem scopes from other papers. `BH-A-...` conditions already constituted or introduced in Paper II are **referenced, not reintroduced**. One missing step in Paper5C becomes one gap node with the exact failed edge and condition IDs. The new DAG exposes every supported path from that gap into later Paper VI/VII targets and observable readouts, while retaining source-limited uncertainty and any alternative bypasses. The final **chat lists all issues**, and `Paper00-DAGAtlas-v1_13.zip` (when v1_12 was the input) is read back and verified with its updated global graph and linked auditable records. No new mathematics or paper edits are produced.

## M. Suggested Work-mode invocation

> Apply `Paper00-RigorousVerificationDAGWorkProtocol-v2_4.md` to **[exactly one selected paper]** from the attached current Born–Hopf papers archive, using the attached current DAG Atlas ZIP. Coordinate multiple agents to verify the existing mathematics and physics, including independent and adversarial checks, while completing the paper's global dependency mappings. Do **not** derive new framework results or repair the paper. Create every genuinely new assumption/condition node only at its earliest verified logical appearance and inherit it downstream through typed DAG paths. For each gap, record its exact first failed/undischarged step and supported impact paths to the rest of the framework and its observables. Deliver **all found issues directly in chat** and **one updated, validated, version-incremented DAG Atlas ZIP**. Do not compile PDFs or alter paper sources.

---

**Binding final instruction:** **Audit exactly one paper. Verify existing claims rigorously; do not extend the theory. Store every condition exactly once at first occurrence, trace all downstream dependencies through the global proof-route-aware DAG, retain every identified gap at its origin, propagate only evidenced cross-paper impacts, and finish with *all issues in chat* plus *one post-write-verified updated DAG ZIP*.**

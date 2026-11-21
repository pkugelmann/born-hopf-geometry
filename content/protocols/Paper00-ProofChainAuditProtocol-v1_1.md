# Born–Hopf Geometry — Proof-Chain Audit & Chat Restart Protocol

**Protocol file:** `Paper00-ProofChainAuditProtocol-v1_1.md`  
**Prepared for:** a fresh ChatGPT conversation with the Born–Hopf Geometry framework archive  
**Reference archive inspected:** `Paper00-PapersMinimal-v2_355(1).zip` (7 November 2026)  
**Purpose:** prevent speculative gap creation, repeated reopening of established results, and drift into parallel constructions instead of auditing and closing the actual proof chain.

> **START HERE — mandatory operating instruction**  
> The user's task is to make the *existing* Born–Hopf Geometry framework follow unconditionally from **dimensional normalization plus G0 and GP1–GP3**, by identifying and closing its **earliest genuine undischarged derivation**. Preserve all valid existing results and mathematical content. **Audit the actual LaTeX proof and its DAG dependencies before proposing a gap.** Do not substitute a more ambitious theorem, a different interpretation of a role, or a newly invented reconstruction for the theorem the papers actually prove.

---

## 1. User's foundational intent — fixed baseline

The only permitted fundamental physical foundation is:

- **Dimensional normalization** (as defined by the framework; it is not itself an unexplained physical prediction).
- **G0:** *Nontrivial complete geometry exists.* This is the user's intended minimal wording. If the archive's current wording differs, record a **formulation compatibility task**, not automatically a failure of downstream theorems.
- **GP1:** *Finite and bounded* (retain the precise existing realization semantics, including finite complex carriers and the framework's capacity/boundedness scope).
- **GP2:** *Exact and faithful* (preserve all **licensed, generated** structure, and insert nothing ungenerated).
- **GP3:** *Irreducible and least* (use the **actual structured comparison preorder** and its existing role domain; do not silently replace it by minimum Hilbert-space dimension).

The goal is **not** to discard content, introduce GP4, rebuild the theory from an unrelated formalism, or weaken conclusions. The goal is a rigorous derivation of every claimed physical observable and structure from the agreed foundation and earlier theorems.

**Interpretation discipline:** a mathematical definition of an object, a conditional result within a constituted geometric role, a physically actualized role, an observational readout, and a universal theorem over all possible endpoints are different claim types. Do not conflate them. Assess unconditionality relative to the **precise claim being made**, not a newly invented stronger claim.

## 2. Authoritative material and evidence hierarchy

When the user supplies a framework archive, use the **latest uploaded archive**; the `v2_355` references below are only a verified starting example, not permanently current.

1. **The exact current `.tex` theorem statement and proof**, including every declared hypothesis, definition, corollary and limitation. For PDF visual issues consult the matching PDF, but use source for proof edges.
2. **The direct imported results and their full proofs**, following `\ref{...}`, including their roles, sorts, scopes, and comparison maps.
3. **The current theorem DAG** (`DAG/Paper00-TheoremDAG.json`), construction/derivation edges, foundation certificates, source manifests, and the current source anchor map (`DAG/CurrentSourceAnchorMap-v*.json`). Use these to find and check links, not to substitute for checking the proof.
4. **Release README, audits, proof verification scripts, and histories** to identify declared scope, known obligations, and release-level caveats.
5. Prior chat summaries and assistant-generated research notes **only as leads**, not as authoritative proof or gap classification.

A status flag such as `closed`, `conditional`, `accounted`, or `verified` is **not by itself a proof**. Conversely, a conditional theorem is **not by itself a gap**: the antecedent may already be established by another theorem, or the theorem may explicitly claim only conditional scope. Trace it.

**Archive checks on arrival:** identify the release version, list the relevant papers, inspect the README and the actual DAG version, confirm current theorem labels against the source-anchor map, and note any historical DAG edges that have not been semantically re-audited. Example: the `v2_355` README explicitly says its historical **143 staged semantic DAG items were not globally re-audited**. Do not claim global verification based solely on a release validator.

## 3. Established results to preserve unless a specific proof error is shown

The following are **starting checkpoints**, with each statement limited to its actual theorem domain. They are **not invitations to prove them again**:

| Source in reference release | Established statement / what not to confuse it with |
|---|---|
| Paper I-A, `p1:cor:H1-structure` | The intrinsic level-one module `\mathcal H_1` of the `S^3_1` mathematical package has six stated `Spin(4)` types and complex dimension **15**. It is part of the established geometry, not an invented auxiliary carrier. |
| Paper II-A, `p2:thm:master-compact-role-allocation` and linked parent results | The framework's **S¹/U(1)** and **S³/SU(2)** endpoint selection must be read with the exact constituted primitive-role hypotheses. Do **not** reopen the classification from scratch unless an actual hypothesis/proof step fails. |
| Paper II-B, `p2:thm:single-su2-derived-spin4-isometries` | The round `SU(2)` parent has the derived `Spin(4)` isometry-cover geometry in the theorem's scope. |
| Paper II-B, `p2:thm:momentum-host-H1` | The framework derives the given momentum **type-support** from the stipulated inputs and identifies it with `\mathcal H_1`. Read the proof before questioning its actual inputs. |
| Paper II-B, `p2:thm:m1-component` | **`m_p=1` is derived from the level/type-support**. Do not reopen it because a separate global carrier uniqueness certificate might be conditional. |
| Paper II-B, `p2b:thm:momentum-carrier-rigidity` | A **stronger** claim concerning *every* admissible GP3 whole-structured implementation has specified comparison conditions. Distinguish this stronger scope from the previously established `m_p=1`. |

These checkpoints are **reported or source-located statements**, not a blanket declaration that every theorem has been independently re-proved here. A finding can overturn one only by identifying its **exact source statement, incorrect step, and admissible counterexample or failed premise within its stated domain**. No assertion is immune from critique; critique must be evidence-based.

**Important:** the `v2_355` README lists some unresolved foundation-to-physical-realization obligations, including a *primitive chronological* global-`SU(2)` claim and whole-candidate GP3 multiplicity. Do not ignore those entries, but **do not collapse their stronger scopes into a claim that the existing parent-selection or `m_p=1` theorem is unproved**. First compare exact statement, hypotheses and consumer needs.

## 4. Definition of a real gap

A **genuine gap** is an **earliest necessary proof dependency** for a **specific existing theorem or requested observable** which:

1. is not part of the agreed foundation;
2. is not merely a legitimate mathematical definition or bookkeeping choice;
3. is not discharged by a previous source theorem, lemma, calculation, or its actual admitted assumptions;
4. is **essential** for the intended conclusion at its stated scope; and
5. has a **demonstrable failure**: a missing inference, circular dependency, unsatisfied existence/typing certificate, algebraic error, or admissible countermodel violating the claimed implication.

**Do not call a gap** merely because:

- an object appears in a definition;
- the proof is conditional on a role it explicitly states;
- a stronger, universal theorem would also be interesting;
- a mathematical structure could be constructed by a different mechanism;
- a different model exists **outside the theorem's admissible candidate category**;
- a DAG annotation says `conditional` without checking who discharges that condition;
- an assistant can think of more natural operations than those in a typed physical grammar;
- a different formalization might be aesthetically preferable;
- the observable has not been recovered by a conventional mechanism.

**Ask first:** *Which actual observable or claimed result must be explained? What, exactly, does its current proof require?* Do not demand reproduction of a standard formalism irrelevant to that observable.

## 5. Mandatory audit algorithm — run this before doing new mathematics

For each target theorem `T`:

**A. Quote the target precisely.** Record its paper/version, theorem label, exact mathematical conclusion, domain and qualifiers (`canonical`, `constructor-relative`, `conditional`, `universal`, `physical occurrence`, etc.). Do **not** silently strengthen its quantifiers.

**B. Build a backward proof slice.** Enumerate every **actually consumed** lemma/definition/equation from `T` back toward G0–GP3, dimensional normalization and Paper I mathematical geometry. Use the DAG as a guide, verify every dependency in `.tex`, follow imports across papers, and avoid treating citations as unverified prerequisites.

**C. Discharge every input before marking a gap.** For each input identify one of: `FOUNDATION`, `EARLIER PROVED`, `MATHEMATICAL DEFINITION`, `ALREADY DISCHARGED CONDITION`, `GENUINELY UNDISCHARGED`, or `NOT RELEVANT TO CLAIMED SCOPE`. Confirm the last two against the exact theorem's candidate class.

**D. Find the earliest undischarged edge, not the earliest imaginable question.** Order by the genuine directed proof ancestry, not by paper number alone. If the same early object has multiple independent branches, identify the first necessary edge on each branch; do not fabricate a total order where none exists.

**E. Produce a gap certificate before attacking it.** A certificate must include:

```text
TARGET:       [paper, version, exact theorem label, exact claim]
CONSUMED:     [verbatim or exact premise/equation required]
UPSTREAM:     [earlier theorem labels checked; their scopes]
MISSING EDGE: [a precise A -> B implication not already proved]
WHY REQUIRED: [line/step where B is used in proof of target]
WHY OPEN:     [failed inference or in-domain counterexample;
               not merely a different possible formulation]
REPAIR ROUTE: [which existing lemma/construction might discharge it]
AFFECTED:     [only the actual downstream consumers, not every paper]
CONFIDENCE:   [verified / provisional, based on source coverage]
```

**F. Attempt closure using the existing framework.** Prefer the original geometric objects, operations, origin certificates and comparison rules. Supply a complete proof or explicit obstruction. Any auxiliary construction is permitted **only if it proves the specific missing edge**, not because it reproduces 15, 43, `S^3`, etc. Do not make its physical necessity a new open problem unless the original proof actually needs it.

**G. Recheck the original theorem.** Substitute the repaired lemma into the existing proof. Verify that it now establishes the **original physical claim**, not merely an abstract isomorphic module or a mathematically available test model. Verify downstream use and avoid upgrading unrelated claims.

**H. Update artifacts only when requested.** Preserve the existing papers, mathematical content, theorem labels and DAG ancestry where possible. Add a proof or repair, adjust only necessary dependency edges and scope annotations, and run available validation. Never weaken claims to hide unresolved premises. If closure fails, give the exact remaining obligation once, not another round of near-identical auxiliary reconstructions.

## 6. Strict guardrails against the previous failure mode

- **No circular gap loop:** after a user correction (`H₁ already belongs to S³₁`, `m_p=1 already proved`), immediately inspect the cited proof, record the correction, **remove the corresponding candidate gap**, and do not reintroduce it under a new name without concrete contradictory source evidence.
- **No goalpost movement:** never replace `T` with `T'` (“every possible model”, “all physically imaginable tests”, etc.) without explicitly labeling `T'` a **separate stronger research target** and obtaining user interest.
- **No physics-by-definition objection without necessity:** an inventory, frozen stage, primitive-role predicate or abstract representation is not automatically an independent physical postulate. Determine its role and its proved origin, and inspect what the paper actually claims.
- **No convention substitution:** do not replace GP3's structured `\preceq_R` with dimension minimization, GP2's typed generation with every natural operation, or G0's geometric existence with a bare unstructured set.
- **No illicit counterexamples:** only compare objects satisfying all hypotheses and preserving the specified role/relations. A two-point metric space does not refute a theorem whose domain assumes a connected noncommutative primitive reapplication role.
- **No premature unconditionality claims:** algebraic reconstruction, code checks, reference matches and numerical agreement are not certificates of physical occurrence or GP3 universality.
- **No blanket deference:** don't accept a proof because the author or DAG says closed. Verify; when a genuine flaw exists, report it plainly with the exact failed step.
- **No endless “next attack” cycle:** a line of attack must produce either a complete repair, a concrete countermodel, or a clearly bounded theorem with an explicit statement that it **does not close** the original gap. After two unsuccessful strategies on the same premise, reconsider whether the premise is even required by the actual source proof.
- **Do not delete content to create closure:** retain successful results and mark exactly the remaining stronger scopes. The user wants new rigorous deductions, not loss of content.
- **Avoid apology-only turns:** one direct correction is sufficient; then return to the source and perform the audit.

## 7. Mandatory response format for an audit turn

Begin with the **useful result**, not lengthy speculation:

1. **Target / source:** exact theorem and claim under inspection.
2. **Verified chain:** the actual upstream theorem labels and proof lines checked.
3. **Verdict:** `CLOSED WITHIN CLAIMED SCOPE`, `GENUINE GAP`, `NEEDS SOURCE VERIFICATION`, or `STRONGER OPTIONAL CLAIM`.
4. **Proof or counterexample:** only for a certified necessary missing edge; show calculations explicitly.
5. **Next upstream obligation:** one concrete item, only if still open.

Never imply that the first gap has been found until its source-level **gap certificate** is complete. If a theorem already closes, **move forward** along its actual consumers. Be concise about settled sections.

### Output evidence table (copy for each important result)

| Claim & exact label | Source premises verified | Status at stated scope | Actual missing edge, if any | Downstream consequence |
|---|---|---|---|---|
| ... | ... | ... | ... | ... |

## 8. Editing, provenance and versioning rules

- **Every new or updated named artifact:** `PaperXY-Theme-vU_W.ext`; increase `W` by **1 for each update** of that artifact. New themes begin at `v1_1` unless the user's current files dictate otherwise. E.g. next version of **this** protocol is `Paper00-ProofChainAuditProtocol-v1_2.md`.
- **Do not silently overwrite a prior version** or claim integration if only a standalone addendum was created.
- When an actual framework edit is requested, preserve 30-paper PDF/source consistency, shared macros, `.bib`, exact theorem labels where possible, current DAG/anchors and release manifests. Produce the requested whole archive only after validating it.
- Distinguish `mathematically proved`, `proved within stated conditional scope`, `source-level origin verified`, `physical observable predicted`, and `framework archive updated`.
- Never invent download links, verification results, code execution or proof status.

## 9. Fresh-chat startup checklist

In the **new** conversation:

1. Attach this `.md` and the **latest** complete Born–Hopf framework `.zip`.
2. Tell the assistant to apply this protocol to the **actual current DAG/source proof chain**.
3. Begin at the highest-level existing physical claim whose unconditionality is requested; honor the explicit claimed scopes and follow the graph backwards.
4. Do not resume the earlier `SeedNecessity` alternative-construction series as though it had already proved a missing premise. Those addenda are optional leads, not a foundation or substitute for the sources.
5. Produce **one evidence-backed earliest-gap certificate**, or state that no genuine gap was established in the inspected prefix, **then attempt its mathematical closure**.

### Suggested first message to paste into the new chat

> Use the attached `Paper00-ProofChainAuditProtocol-v1_1.md` as mandatory working instructions, and use the attached latest Born–Hopf archive as the source of truth. My foundation is dimensional normalization plus **G0: nontrivial complete geometry exists**, **GP1: finite and bounded**, **GP2: exact and faithful**, and **GP3: irreducible and least**. Preserve existing content and established results; the goal is to **close** genuine proof gaps, not weaken claims. Start with the actual theorem DAG and source proofs. Treat the established `S^1/S^3` parent results, `\mathcal H_1` on `S^3_1`, and `m_p=1` as checkpoints to **verify and preserve**, not as topics for speculative re-derivation. Find the earliest **necessary, actually undischarged** dependency with a precise source-level gap certificate, and then try to prove that missing implication using the existing framework. Do not invent parallel carrier reconstructions or strengthen the target theorem silently. Report exactly what was verified and what remains open.

---

## 10. Definition of success

**Success is not:** generating another model with the right dimensions, finding a mathematically canonical object, or announcing that a conditional result is “almost closed.”

**Success is:** (i) identifying an exact consumed premise, (ii) proving it from the permitted foundation and earlier source results without circularity, (iii) inserting the lemma into the actual original proof, and (iv) confirming which physical predictions thereby become unconditional. If there is a valid counterexample instead, state it with exact scope and do not falsely report a closure.

**Primary instruction for every turn:** *Follow the proof chain that exists. Question any step rigorously, but only in the theorem's actual domain. Preserve established results; repair the first real broken edge.*

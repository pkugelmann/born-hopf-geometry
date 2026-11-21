# Source migration and repair-integration addendum — Paper4C-ProofChainAudit-v1_3.md

**Integration release:** `Paper00-PapersMinimal-v3_007.zip`, 14 November 2026.
**Current paper source:** `Paper4C-TechnicalMaterial-v1_49.tex`.
**Status:** `SOURCE_INTEGRATED; GLOBAL_SOURCE_REAUDIT_PENDING`. An inherited historical audit is not a correctness certificate for the newer current manuscript.
**Evidence policy:** Local algebraic proofs and scoped tests do not discharge physical source/observable interfaces or automatically alter the canonical proof DAG.

---

## Historical source-bound audit: Paper4C-ProofChainAudit-v1_2.md
# Repair addendum — Paper IV-C / 13 November 2026

**Current manuscript:** `Paper4C-TechnicalMaterial-v1_43.tex` (SHA-256 `ca2e6f83a061c29d88095c9e18b553dbc681bb74a4efaed4db57cebdd6475623`)  
**Historical report preserved:** `Paper4C-ProofChainAudit-v1_1.md` verbatim below.  
**Scope/status:** source repaired; scoped E3/E4 controls recorded; no blanket proof/physical status promotion.

| Audit finding | Current source locator | Correction | Remaining proof gate |
|---|---|---|---|
| `BH-G-000102` | `Paper4C-TechnicalMaterial-v1_43.tex:3076` | Higher-degree CCR occupation margin; word-level leakage or n<=N-d guard | Actual licensed refinement/localizer/dynamical transport not proved |
| `BH-G-000103` | `Paper4C-TechnicalMaterial-v1_43.tex:3462` | C3/C1 regularity for positive differentiable nonstationary frequency | Physical mode origin and background-specific domain remain separate |
| `BH-G-000104` | `Paper4C-TechnicalMaterial-v1_43.tex:4209` | Nonautonomous finite unitary recurrence claim withdrawn | No Markovian reservoir/kinetic limit inferred |
| `BH-G-000105` | `Paper4C-TechnicalMaterial-v1_43.tex:6632` | Detector-specific vanishing interference does not imply dephasing | Which-path/dephasing requires state/measurement protocol |
| `BH-G-000106` | `Paper4C-TechnicalMaterial-v1_43.tex:10919` | Nonzero-coefficient hypothesis; all-zero cumulants separately handled | Realized finite mode/detector selection remains a separate port |

**Verification:** `Paper00-AuditRepairBatch-v1_4.md`; 57/57 scoped checks in the atlas. Source line and version citations within the preserved historical baseline refer to the **old edition** and original OPEN flags remain valid at their original audit time.

---

## Historical audit baseline (verbatim)

# Paper IV-C — rigorous proof-chain verification audit (final)

**Audit unit:** `Paper4C-TechnicalMaterial-v1_42.tex` (10,934 lines; SHA-256 `db4933305c7acd0a67ac9c81ba219d051cbad95777a9848514ce4ce0e4e57626`).
**Method:** `Paper00-RigorousVerificationDAGWorkProtocol-v2_4`; source-first E1, scoped independent E3, adversarial E4, condition-preserving global DAG integration.
**Source release:** `Paper00-PapersMinimal-v2_371`; no paper sources were changed.

## Coverage and verdict

**FULLY_AUDITED_WITH_OPEN_GAPS**: all **186/186** named objects examined across seven complete, nonoverlapping batches; E1 sequential proof-step scan and material unnamed step checks; all seven batch reports and machine ledgers archived. Dispositions: **65 VERIFIED, 73 VERIFIED-CONDITIONAL, 29 FORMALIZED, 15 REPRODUCED, 4 UNRESOLVED**. **261/261 independent and adversarial scoped controls completed**. All-source theorem verification is **not** implied by these finite controls; in particular reservoir all-order convergence, physical realization and the 128-dimensional time-dependent charge certificate are not automatically upgraded.

## All identified open issues (source-as-printed)

1. **BH-G-000102 — Moderate, UNDER_CHALLENGE, MISSING_CONDITION/LOGICAL_GAP.** `p4:thm:approximate-microcausality` (3069–3072; proof 3145–3154): elementary compressed CCR control alone does not quantify higher-degree polynomial commutators after intermediate occupation excursions. A finite two-mode boundary example shows failure of the *intermediate implication* even when elementary defects vanish, but does not instantiate every spatial-localizer hypothesis of the full theorem. Needs degree-relative occupation margin or a directly checked word-level leakage estimate; CAR/Weyl branches unchanged.
2. **BH-G-000103 — Moderate, OPEN, MISSING_CONDITION.** `p4:thm:v245-nonstationary-hessian-bogoliubov-source` (3443–3490): `m in C²` and continuous `ell` allow `Omega_eff` merely continuous. With `m=1, ell=1+|t|`, `dot Omega_eff` and the asserted pointwise Nambu law fail at 0. Exact pointwise law needs suitable frequency differentiability, or an explicitly formulated almost-everywhere version. Affects the cited defect corollary; does not refute independent CAR or finite squeeze construction.
3. **BH-G-000104 — Minor, OPEN, INCORRECT_STEP.** Reheating/GKLS auxiliary recurrence sentence at line 4191: a fixed finite block is not necessarily recurrent under arbitrary time-dependent unitary driving. A smooth two-level finite rotation supplies countercontrol. Main finite CPTP identity and conditional GKLS limits remain unaffected.
4. **BH-G-000105 — Minor, OPEN, INCORRECT_STEP/TYPE_OR_DOMAIN.** Double-slit discussion line 6613: vanishing of cross terms for a particular detector effect does not imply dephasing; a path-diagonal POVM eliminates observed interference without destroying off-diagonal state coherence. The four-term Born probability formula is unchanged; qualify the detector/generalization.
5. **BH-G-000106 — Minor, OPEN, MISSING_CONDITION/TYPE_OR_DOMAIN.** `p4c:thm:v349-multimode-first-cumulant` (10893–10919): if every real coefficient `c_a` is zero, the defined minimum `m=min_{a:c_a≠0}(N_a+1)` is undefined and all cumulants vanish, contrary to the unqualified strict negativity statement. At least one nonzero coefficient is required; no source edit performed.

## Independent evidence and scope guard

Batches 1–7 individually record respectively 16, 28, 33, 35, 39, 54 and 56 passed controls, including adversarial successes that corroborate *issues* rather than universal theorems. The tested identities cover finite CAR/CCR, mixed spectral and reconstruction interfaces, source/path cumulants, entropic information balance, transfer spectra, and 120 signed Petersen permutations. No new upstream paper is claimed audited. Conventional mechanism reproduction is not a test of correctness; only the source-defined observable and its hypotheses are considered.

## DAG integration and release

The new audit layer at `DAG/AuditLayer/Paper4C-v1_1` contains exact claim/evidence ledgers, reviewed and quarantined dependencies, first-known inferred regularity/occupation/coefficient conditions, 5 gap objects, scoped proof routes and impact traversal. The global canonical graph, combined material edge index, query index, condition/gap registries and composite release references are updated without changing prior-paper proofs or statuses. Citation-only and E0 source-anchor links never enter theorem ancestry.

**Artifacts:** `Paper00-DAGAtlas-v1_109.zip` and `Paper00-ProofChainAudits-v1_26.zip`. Only one active latest-version entry per artifact/theme is retained.

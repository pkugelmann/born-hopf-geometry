# Source migration and repair-integration addendum — Paper6C-ProofChainAudit-v1_4.md

**Integration release:** `Paper00-PapersMinimal-v3_007.zip`, 14 November 2026.
**Current paper source:** `Paper6C-TechnicalMaterial-v1_51.tex`.
**Status:** `SOURCE_INTEGRATED; GLOBAL_SOURCE_REAUDIT_PENDING`. An inherited historical audit is not a correctness certificate for the newer current manuscript.
**Evidence policy:** Local algebraic proofs and scoped tests do not discharge physical source/observable interfaces or automatically alter the canonical proof DAG.

---

## Historical source-bound audit: Paper6C-ProofChainAudit-v1_3.md
# Paper6C — v2.372 source repair addendum (13 November 2026)

**Successor:** `Paper6C-ProofChainAudit-v1_3.md`.  
**Current source:** `Paper6C-TechnicalMaterial-v1_44.tex`.  
**Current SHA-256:** `bb3a8751dee4a8d8f29e99c0d4d5a69cdfe22e5738ac94f75fb7a5234cf81905`.  
**Historical audit:** `Paper6C-ProofChainAudit-v1_2.md`.  
**Source repair scope:** 5 distinct issue(s); 8 textual corrections.  
**Disposition:** `SOURCE_REPAIRED_WITH_SCOPED_CHECKS; FORMAL_REAUDIT_PENDING` for only the listed IDs. Other issues and all original evidence statuses unchanged.

| Issue ID | New source line(s) | Repaired issue |
|---|---|---|
| `BH-VIC-G-0138` | 2773, 2785 | Use S³ eigen-wavenumber sqrt[k(k+2)] instead of identifying mode index k with momentum. |
| `BH-VIC-G-0141` | 4036, 4045 | Compute 2.9588×10⁹·(3/5)^(1/4) ≈ 2.6041×10⁹; do not use 2.96×10⁹ as the product. |
| `BH-VIC-G-0143` | 4942 | The normalized Reeb return sum has y>0 domain; acceleration may extend continuously to y=0 even though the multiplier does not. |
| `BH-VIC-G-0147` | 6416, 9929 | C56 equals ℛ56², not ℛ56²/U; repair primary equality and downstream reuse without altering its physical readout. |
| `BH-G-000152` | 10051 | SymPy verification snippet uses the prescribed 1/(4π) factor. |

The historical report below refers to the previous source version and explicitly marks those same issue IDs as `OPEN` **as of that old version**. Those specific historical labels are superseded only as source-edit dispositions by the addendum above; the original audit text is retained to prevent loss of evidence or false global certification. Other issues are unchanged. Recheck the updated source theorem and its proof/use dependencies before promoting an issue to closed in the canonical DAG.

---

## Historical predecessor audit (unchanged text; former source version)

> **Merge-only ID reconciliation (v1_2, 2026-11-13).** This report retains the original VI-C audit mathematics, source spans, dispositions, and proof evidence. The concurrent VII-A audit used the same numerical IDs `BH-G-000134`–`BH-G-000148` for distinct findings. Consequently, VI-C references to those fifteen historical local IDs are globally disambiguated to `BH-VIC-G-0134`–`BH-VIC-G-0148` here. Original v1_1 report and independent verification scripts remain preserved in `Provenance/IssueIDCollision-v1_119/`. No issue was closed, duplicated as a canonical root, or verified anew by this administrative change. The unchanged VI-C issues `BH-G-000149`–`BH-G-000152` retain their IDs.

# Paper VI-C — complete rigorous proof-chain audit

**Artifact:** `Paper6C-ProofChainAudit-v1_1.md` · **Target:** `Paper6C-TechnicalMaterial-v1_43.tex` · **Source SHA256:** `95584cae4b46ce8aef588f664b2b91e1ae6e60c4703a305e720672d1fa82efbc` · **Method:** Paper00 rigorous verification/DAG v2.4.

## Verdict

**FULLY_AUDITED_WITH_OPEN_GAPS.** The full 10,448-line source has been inspected across six non-overlapping batches, with 247 unique formal statement dispositions and **19 distinct unresolved issues** (15 moderate, four minor). Full source coverage does **not** imply 247 independent mathematical proofs: **106** have independent verification at the stated often conditional scope. Other statements carry source replay, dependency tracing, partial tests or explicit gaps. No paper source was edited.

The mathematically primary objects and verified conditional identities are not equated with observational/physical occurrence without an action, owner and boundary certificate. Optional MRESP, optional Reeb static interpolation, historical K48/local-L firewall, and native S+T deep RAR are kept as distinct branches.

## Coverage and evidence

| Batch | Source lines | Formal statements | New findings |
|---|---:|---:|---:|
| 01 | 80–1374 | 32 | 3 |
| 02 | 1375–3157 | 53 | 2 |
| 03 | 3158–5295 | 59 | 5 |
| 04 | 5296–6887 | 29 | 4 |
| 05 | 6888–8897 | 42 | 3 |
| 06 | 8898–10448 | 32 | 2 |
| **Total** | **80–10,448** (opening conventions separately reviewed) | **247** | **19** |

The independent reproducibility checks cover harmonic and representation algebra, optional inflation interpolation, reheating ledgers, phase-space measure projectors, tensor Dirac poles, finite-collar Dirichlet-to-Neumann response, strong-field geometric identities, and final validation countermodels. Failed proof links are not interpreted as failure of all conditional calculations.

## All 19 issue certificates

### BH-VIC-G-0134 — MODERATE · Batch 1

**First-known target origin:** `Paper6C-TechnicalMaterial-v1_43.tex:415-430`.

**Finding:** A covariant V:H1(E9⊕L6)→V_pair kills L6 only if the equivariant target has no (1,0) or (0,1) representation; the target type and covariance of the actual mode-map must be established.

**Unmet proof obligation:** Trace the actual action/ordered-mode pair-vertex module to the E9 target with correct quantifiers or make 415 conditional on the explicitly proved later statement. No source repair performed.

**Cross-paper/observable impact status:** No supported outgoing material impact path beyond source proof uses. The recorded possible consumers remain unconfirmed.

### BH-VIC-G-0135 — MODERATE · Batch 1

**First-known target origin:** `Paper6C-TechnicalMaterial-v1_43.tex:612-643`.

**Finding:** On the comoving single-clock scalar reduction, require H_E≠0 and φdot_E≠0 for a nonsingular curvature-variable/canonical oscillator interval; M_k=C_E γ_k>0 in 647-713 requires φdot_E≠0; regularity of derivatives as needed.

**Unmet proof obligation:** Record/scoped proof of rolling nonzero-H interval, patch with valid alternative gauge at a bounce/turning point, or explicitly restrict these kernel/oscillator statements. Do not infer from F>0,fRR>0.

**Cross-paper/observable impact status:** No supported outgoing material impact path beyond source proof uses. The recorded possible consumers remain unconfirmed.

### BH-VIC-G-0136 — MODERATE · Batch 1

**First-known target origin:** `Paper6C-TechnicalMaterial-v1_43.tex:968-982`.

**Finding:** On the same active REG0 K16 junction with [F]16=[χ]16=0 and R+ = R− = C2, positive χ(C2), the one-sided χ ratio and m_alg ratio must both equal 1. If displayed nonunit values are historical, identify the separate branch precisely.

**Unmet proof obligation:** Show the explicit comparator/historical action, branch labels and non-conflicting K16 endpoint for the quoted nonunit ratios, or withdraw them from the current branch. No edit made.

**Cross-paper/observable impact status:** No supported outgoing material impact path beyond source proof uses. The recorded possible consumers remain unconfirmed.

### BH-VIC-G-0137 — MODERATE · Batch 2

**First-known target origin:** `Paper6C-TechnicalMaterial-v1_43.tex:2125-2153`.

**Finding:** From fixed-rank theta_k=8/k and the background sharp spectral frontier, together with activated scalar perturbations, show an actual typed operator/physical-source map which identifies the first unresolved observable scalar perturbation band and makes its response the eight-slot module. "No additional subscale" does not by itself define such a map.

**Unmet proof obligation:** Locate a same-owner perturbation source/initial-condition-to-first-band response operator and prove its eight-slot identification, with explicit domain, or downgrade 2125-2153 to a conditional phenomenological first-band ansatz; no new mechanism inserted by audit.

**Cross-paper/observable impact status:** No supported outgoing material impact path beyond source proof uses. The recorded possible consumers remain unconfirmed.

### BH-VIC-G-0138 — MODERATE · Batch 2

**First-known target origin:** `Paper6C-TechnicalMaterial-v1_43.tex:2771-2780`.

**Finding:** For actual closed-S³ degree k_MS, horizon eigen-wavenumber scales as sqrt[k_MS(k_MS+2)], not k_MS. Even if H is exactly constant, exact shell endpoints satisfy sqrt[k2(k2+2)/(k1(k1+2))]=e^{Delta N}, not k2/k1. If k denotes continuous comoving eigen-wavenumber, define it separately and state finite integer-shell rounding and slow-roll accuracy; if H≈const rather than constant equality is approximate.

**Unmet proof obligation:** Declare the k=aH variable as continuous eigen-wavenumber and qualify leading slow-roll approximation, or express the exact closed-degree window as sqrt[k2(k2+2)/k1(k1+2)] with integer endpoint rounding; keep ell transfer separate.

**Cross-paper/observable impact status:** No supported outgoing material impact path beyond source proof uses. The recorded possible consumers remain unconfirmed.

### BH-VIC-G-0139 — MODERATE · Batch 3

**First-known target origin:** `Paper6C-TechnicalMaterial-v1_43.tex:3178-3194 (physical source law), :3243-3279 (theorem)`.

**Finding:** Connect the Paper V-B one-real-scalar PARTIAL width coefficient to a physically declared TOTAL scalaron handoff width or explicitly stipulate the total one-real-scalar-equivalent rate on the optional comparison branch, with its channel multiplicity/nonminimal-coupling/anomaly content.

**Unmet proof obligation:** Source-match an actual channel-summed total-rate theorem or state a distinct total-width interface premise; preserve optional-vs-active branch scope.

**Cross-paper/observable impact status:** No supported outgoing material impact path beyond source proof uses. The recorded possible consumers remain unconfirmed.

### BH-VIC-G-0140 — MODERATE · Batch 3

**First-known target origin:** `Paper6C-TechnicalMaterial-v1_43.tex:3386-3416; compare :3512-3533`.

**Finding:** From total covariant conservation and the chosen normalization I16 alone, establish epsilon_ord^prod <= I16 on the exact handoff interval, or import the later pure-I16-transfer ledger as a separate indispensible premise.

**Unmet proof obligation:** Connect first use to the precise pure-transfer normalized handoff condition or source-prove the energy inequality for the actual initial and final state.

**Cross-paper/observable impact status:** No supported outgoing material impact path beyond source proof uses. The recorded possible consumers remain unconfirmed.

### BH-VIC-G-0141 — MINOR · Batch 3

**First-known target origin:** `Paper6C-TechnicalMaterial-v1_43.tex:4020-4035`.

**Finding:** The printed equation must multiply at its displayed precision, or explicitly keep the unrounded T0=2.9588e9 GeV in the multiplication.

**Unmet proof obligation:** Use full-precision input or correct the rounded product as a presentation/accuracy issue; audit does not edit source.

**Cross-paper/observable impact status:** No supported outgoing material impact path beyond source proof uses. The recorded possible consumers remain unconfirmed.

### BH-VIC-G-0142 — MODERATE · Batch 3

**First-known target origin:** `Paper6C-TechnicalMaterial-v1_43.tex:4333-4353; compare :3420-3424 and :3862-3867`.

**Finding:** The joint antecedent Xi16_delta: xi16dyn=delta_geom and DEM15 with eps_dep=1: xi16dyn=3/5 is inconsistent for one same-owner transfer variable; demonstrate a separately typed pre-split coefficient, or remove the claimed simultaneous saturated-democratic member.

**Unmet proof obligation:** Distinguish a pre-visibility unsplit source coefficient from xi16dyn with a verified typed normalization, or keep the historical numerical comparison explicitly non-co-realizable.

**Cross-paper/observable impact status:** No supported outgoing material impact path beyond source proof uses. The recorded possible consumers remain unconfirmed.

### BH-VIC-G-0143 — MINOR · Batch 3

**First-known target origin:** `Paper6C-TechnicalMaterial-v1_43.tex:4927-4947; compare :4788-4794 and :4837-4840`.

**Finding:** The scalar normalized return sum is finite only for y>0; specify this domain (as the earlier general-envelope proposition does) and distinguish the y=0 limit of the physical acceleration product.

**Unmet proof obligation:** Use y>0 for the normalized kernel, and state an explicit continuous extension of g_obs at y=0 if needed.

**Cross-paper/observable impact status:** No supported outgoing material impact path beyond source proof uses. The recorded possible consumers remain unconfirmed.

### BH-VIC-G-0144 — MODERATE · Batch 4

**First-known target origin:** `Paper6C-TechnicalMaterial-v1_43.tex:5732-5746`.

**Finding:** Nonnegative scalar boundary quadratic form and coercivity imply invertibility, but NOT a positive inverse without a positivity-preserving/Markov boundary condition, as consumed by G_env1>0 and normalized source Green selection.

**Unmet proof obligation:** Locate an actual local Markov/Robin/Dirichlet scalar boundary theorem or certify positive semigroup for the actual nonlocal boundary; not enough to cite quadratic coercivity.

**Cross-paper/observable impact status:** No supported outgoing material impact path beyond source proof uses. The recorded possible consumers remain unconfirmed.

### BH-VIC-G-0145 — MODERATE · Batch 4

**First-known target origin:** `Paper6C-TechnicalMaterial-v1_43.tex:6092-6115;6135-6154`.

**Finding:** A radial scalar RAR law g_obs=nu(g_b/a*)g_b is used as the local nonspherical vector force g_resp=nu(|grad Phi_b|/a*)grad Phi_b and then as gradient of the lensing scalar potential; a spatially varying a* generally creates nonzero curl, so the force-to-potential step is not justified by taking its divergence.

**Unmet proof obligation:** Trace a sourced scalar Helmholtz/Poisson response operator directly from the native action, or establish curl-free condition in declared merger domain; do not add a new physical mechanism in the audit.

**Cross-paper/observable impact status:** No supported outgoing material impact path beyond source proof uses. The recorded possible consumers remain unconfirmed.

### BH-VIC-G-0146 — MODERATE · Batch 4

**First-known target origin:** `Paper6C-TechnicalMaterial-v1_43.tex:6158-6178`.

**Finding:** K radial positive decreasing and D≫ell do not alone ensure separated selector maxima when component positive weights Wg,Wc can be arbitrarily imbalanced; two-peak conclusion requires additional weight/profile control.

**Unmet proof obligation:** Require a quantitative relative weight/profile condition for bimodality or treat morphology as case-dependent; leave standalone Renv field intact.

**Cross-paper/observable impact status:** No supported outgoing material impact path beyond source proof uses. The recorded possible consumers remain unconfirmed.

### BH-VIC-G-0147 — MINOR · Batch 4

**First-known target origin:** `Paper6C-TechnicalMaterial-v1_43.tex:6393-6399`.

**Finding:** Current owner defines C56=R56²=U alpha^-7, whereas the second printed a0 equality uses R56²/U; these differ by factor 1/U inside the square root, making the second expression dimensionally wrong.

**Unmet proof obligation:** Align the displayed secondary equality and later reuse with current VI-A definition without changing physically correct primary a0 value; report only, no source edit.

**Cross-paper/observable impact status:** No supported outgoing material impact path beyond source proof uses. The recorded possible consumers remain unconfirmed.

### BH-VIC-G-0148 — MODERATE · Batch 5

**First-known target origin:** `7775-7810`.

**Finding:** VI-C reprints K48/RAR firewall as though the physical β48 map and every deep RAR export remain unprovided; VI-C 7431-7437 and 7677-7687 expressly state β48 is now generated locally and native S+T deep RAR is independently closed. VI-B 4153-4176, 4183-4205 explicitly scopes those earlier theorems to historical local-L/Schur/Calderón/G26-GLOBAL. An unqualified terminal/current branch reading is inconsistent with active ancestry.

**Unmet proof obligation:** Explicitly inherit current VI-B route restriction on reprinted firewalls and separate current β48 local owner, current native S+T deep law, and optional historical local-L/G26-GLOBAL completion; do not postulate a new mechanism.

**Cross-paper/observable impact status:** Verified paths only via material edges in accompanying ImpactIndex; wider implications unconfirmed.

### BH-G-000149 — MODERATE · Batch 5

**First-known target origin:** `8149-8173`.

**Finding:** Constant F and vacuum trace root establish Rμν=(R_ext/4)gμν; stationary-axisymmetry alone does not force Kerr-(A)dS nor absence of all exterior multipoles or NUT/acceleration-like charges. The theorem supplies no global uniqueness/horizon/asymptotic hypotheses.

**Unmet proof obligation:** State and source the exact boundary/horizon/asymptotic hypotheses under which a Kerr(-dS) uniqueness theorem applies, or type the Kerr family as one allowed solution; audit records only, no source repair.

**Cross-paper/observable impact status:** No supported outgoing material impact path beyond source proof uses. The recorded possible consumers remain unconfirmed.

### BH-G-000150 — MODERATE · Batch 5

**First-known target origin:** `8021-8077`.

**Finding:** The printed coupled two-marginal solution, residual <2e-13, transversality derivatives, positivity, and sixth-order constraint buffers rely on four explicitly named numerical files not included in the supplied paper or DAG archives. The inputs, normalization and ODE integration cannot be independently rerun from those archives.

**Unmet proof obligation:** Supply the cited frozen scripts/json and full source-state packet, rerun with checksum/result tolerances and independent solver/constraints; no claim of numerical refutation.

**Cross-paper/observable impact status:** No supported outgoing material impact path beyond source proof uses. The recorded possible consumers remain unconfirmed.

### BH-G-000151 — MODERATE · Batch 6

**First-known target origin:** `[9946, 9999]`.

**Finding:** To advertise the displayed ν_Reeb(y)=1/(1−exp(−sqrt(y))) as the native selected static RAR response requires the actual R1/R2/same-action scalar stiffness and return-ownership certificates; the current manuscript only grants that kernel an enlarged comparison-branch status.

**Unmet proof obligation:** Explicitly scope all Reeb example headings, documentation and code as a conditional (R1/R2) comparison, or provide existing same-action owner certificates; do not replace native S+T with the example.

**Cross-paper/observable impact status:** No supported outgoing material impact path beyond source proof uses. The recorded possible consumers remain unconfirmed.

### BH-G-000152 — MINOR · Batch 6

**First-known target origin:** `[10023, 10034]`.

**Finding:** Numerical a_0 code must divide by 4π to reproduce the immediately preceding displayed a0=c² sqrt(2 Λ_eff)/(4π) and printed 1.146×10^-10 m/s².

**Unmet proof obligation:** Correct the printed verification code independently of any theory work; retain native and optional branch distinction.

**Cross-paper/observable impact status:** No supported outgoing material impact path beyond source proof uses. The recorded possible consumers remain unconfirmed.

## Canonical conditions, material edges and source integrity

- Reviewed typed dependency uses: 93; accepted material source-use edges: 49; quarantined unsupported/citation edges: 44.
- Global conditions/axioms are not duplicated: inherited references remain canonical and newly asserted local aliases with unresolved earliest origins stay pending in the condition-use ledger.
- Claims retain source-as-printed verbatim excerpts and SHA256; source statuses are not upgraded merely by package integration.
- Original upstream graph, historical provenance, claims and source files are retained; combined forward/backward indexes are extended only through reviewed material proof-use edges.
- Final release includes `DAG/AuditLayer/Paper6C-v1_1/`, its six evidence JSON files, reproducibility scripts, source claims, gaps and queryable routes.

## Method limits and final acceptance

This is a source-complete verification audit, **not** a clean proof certification. `BH-G-000150` cannot be closed without the missing numerical ODE witness files. `BH-G-000151` keeps the optional Reeb comparator distinct from the native S+T RAR. The failed code snippet in `BH-G-000152` is not used as a proof of a different acceleration scale.

All 19 gaps remain OPEN. Any later source repair must be checked against its own first-origin and route, rather than treating an audit finding as a theorem repair.

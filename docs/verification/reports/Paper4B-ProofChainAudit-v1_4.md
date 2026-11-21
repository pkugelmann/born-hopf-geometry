# Paper4B — CC18 current-source scope rebase (Paper4B-ProofChainAudit-v1_4.md)

**Latest source:** `Paper4B-QuantumResponse-v1_51.tex`; SHA-256 `ee68e1edfd7834515a337cd2d4734671ddf3949ce222ebf0cf5281cb570b4693`.  **Framework release:** `Paper00-PapersMinimal-v3_019.zip` based on v3.018.  **DAG release:** `Paper00-DAGAtlas-v1_155.zip` based on v1.154.  **Audit collection:** `Paper00-ProofChainAudits-v1_68.zip` based on v1.67.

**Scope and grade:** `SOURCE_INTEGRATED_LOCAL_MATH_CHECKS / NEW_CLAIMS_NOT_FULLY_AUDITED`.  The historical audit below remains valid only for the original source body and the exact original manuscript version it names.  The added CC18 proof statements have formal source labels, precise dependency owners and reproducible finite/exact checks, but **not a fresh exhaustive E3/E4 audit for this entire revised paper**.  No old issue, open physical obligation, or conditional status is silently closed.  No physical occurrence/observable was promoted.

New source-labelled mathematical result(s):
- `p4b:thm:cc18-nonet-su3-obstruction` — source-integrated auxiliary comparison, no physical-owner certificate.
- `p4b:thm:cc18-rankone-haar-twirl` — source-integrated auxiliary comparison, no physical-owner certificate.

**Local evidence:** `DAG/SourceUpdates/DAGCrossConnections-v1_9/` contains the independent exact-cubature, exact-block, independent facet-geometry and independent nonet reconstruction scripts from supplement v1.9; the release manifest records their replay status and the exact updated source anchors.  The predecessor audit, source text before the appended CC18 block, and all predecessor issue ledgers are preserved as provenance; source hash changed and must not be mistaken for E0 equality to the old manuscript.

---

## Historical audit retained verbatim (not current-version re-certification)

# Source migration and repair-integration addendum — Paper4B-ProofChainAudit-v1_3.md

**Integration release:** `Paper00-PapersMinimal-v3_007.zip`, 14 November 2026.
**Current paper source:** `Paper4B-QuantumResponse-v1_49.tex`.
**Status:** `SOURCE_INTEGRATED; GLOBAL_SOURCE_REAUDIT_PENDING`. An inherited historical audit is not a correctness certificate for the newer current manuscript.
**Evidence policy:** Local algebraic proofs and scoped tests do not discharge physical source/observable interfaces or automatically alter the canonical proof DAG.

---

## Historical source-bound audit: Paper4B-ProofChainAudit-v1_2.md
# Repair addendum — Paper4B / 13 November 2026

**Current manuscript:** `Paper4B-QuantumResponse-v1_43.tex` (SHA-256 `7e34acf99133089396835891bcad540d337e899e385da6c8654aa621f7fd967d`)  
**Historical report preserved:** `Paper4B-ProofChainAudit-v1_1.md` verbatim below.  
**Disposition:** Scoped source repairs, not complete independent mathematical re-audit; all prior DAG proof/physical statuses unchanged.  

| Issue | Current source line(s) | Change | Disposition |
|---|---|---|---|
| `BH-G-000100` | `Paper4B-QuantumResponse-v1_43.tex:2922`, `Paper4B-QuantumResponse-v1_43.tex:2934`, `Paper4B-QuantumResponse-v1_43.tex:2943`, `Paper4B-QuantumResponse-v1_43.tex:2959`, `Paper4B-QuantumResponse-v1_43.tex:2979` | Corrected restricted-composition Cauchy leap; a determining full-real or dense additive composition-domain certificate is now explicit. | SOURCE_CORRECTED; REAUDIT PENDING / IMPORTED GATE RETAINED |
| `BH-G-000101` | `Paper4B-QuantumResponse-v1_43.tex:4553`, `Paper4B-QuantumResponse-v1_43.tex:4569`, `Paper4B-QuantumResponse-v1_43.tex:4584` | Equilibrium is characterized by all additive collision invariants; Gibbs form follows only if the actual positive-rate collision-invariant space is complete. | SOURCE_CORRECTED; REAUDIT PENDING / IMPORTED GATE RETAINED |

See `Paper00-AuditRepairBatch-v1_3.md` and the 28/28 scoped controls in the current atlas. Source hashes and line numbers appearing in the original text below refer to its **previous source edition**; original OPEN flags are historical and have not been changed or globally promoted.

---

## Historical audit baseline (unaltered original text)

# Paper IV-B — Full Rigorous Proof-Chain Audit (all four batches)

**Artifact:** `Paper4B-ProofChainAudit-v1_1.md` | **Audit protocol:** `Paper00-RigorousVerificationDAGWorkProtocol-v2_4.md`
**Status:** `FULLY_AUDITED_WITH_OPEN_GAPS`, under source-as-printed finite/conditional proof interpretation; no framework-wide certificate.
**Authoritative source:** `Paper4B-QuantumResponse-v1_42.tex` (framework v2.371); SHA256 `11b93140dc5c53854a382763fde536862e8d979f65ba8e37c1af562b23bdab6f`; 12149 lines. Predecessor audits/atlas left immutable.
**Result:** 227/227 named theorem/lemma/proposition/corollary/definition/remark statements; 176/176 proof environments; 119/119 scoped independent checks; two source-implication defects originating in Batch 2.

## Evidence methodology and precise classification
- E1: every named statement and its source-located proof environment compared against the *current* TeX. Proof environments not directly attached to named statements are inventoried separately in Batch 3.
- E2/E3: 119 passing independent finite matrix/CAR/instrument/response controls, plus positive controls and bounded countermodels. They verify the exact tested branches, not universal quantified claims beyond the finite owner.
- E4: adversarial counterexample attempts and source-domain firewall. The two issues below are established countermodels to the *implications as printed*, not automatically to the actual physical operator or untested source selection.
- Imported upstream assertions are read at relevant exact scopes only. This single-paper audit does not independently re-audit earlier works.
- Multiple separately written replay, computational and boundary checks were executed by one coordinating analyst; an independent multi-agent run is **not** claimed.
- All conditional upstream physical occurrences, actualized states, common-source normalizations, quasiparticle collision kernels and thermodynamic subnet assumptions remain conditional on their stated hypotheses.
- Source-classified verdicts: **VERIFIED 12**, **VERIFIED-CONDITIONAL 136**, **REPRODUCED 37**, **FORMALIZED 40**, **INCONSISTENT 2**. These are proof/evidence statuses, not 227 claims universally independently proved.

## Every identified mathematical issue
### BH-G-000100 — Major, missing condition in global Euclidean exponential-weight rigidity
- **Origin:** `p4:thm:euclidean-weight-rigidity`, lines 2913–2942, proof 2937–2942. The printed hypothesis gives positive continuous `w:R→R+` and multiplicativity when two actions occur in relation-free composed subsystems; its proof then treats this as the Cauchy relation for all `x,y∈R`.
- **Failure certificate:** If admissible composition values are nonnegative integers, `w(x)=exp(-x+sin(2πx)/20)` is positive, continuous and strictly decreasing; `w(n+m)=w(n)w(m)` for all admitted integer pairs, but it is not globally `exp(cx)`. Full-real action composability, or a determining dense set plus extension argument, is an undischarged additional condition `BH-IVB-A-0001`.
- **Scope:** Ordinary continuous additive Cauchy theorem holds when its premise really is valid for all real pairs; positive finite Euclidean integrals with an *explicitly supplied* `exp(-S_E/ħ)` weight are not refuted.
- **Material downstream:** `p4:thm:euclidean-weight-rigidity → p4:def:generated-finite-euclidean-quantum-ray → p4:cor:finite-generated-quantum-constructor` uses the rigidity assertion for the no-extra-selector conclusion. No certified cross-paper impacted proof path asserted. Earlier source: `p2:post:GP2` role-composition grammar; it does **not** discharge action-coordinate coverage.
- **Resolution obligation:** Source-verified composability/density for the actual action-coordinate domain with continuous extension; no axiom added and no source changed.

### BH-G-000101 — Moderate, missing collision-invariant completeness for unique Gibbs equilibrium
- **Origin:** `p4:thm:v496-quantum-kinetic-h`, lines 4537–4563. The nonnegative collision entropy production is valid. But connectedness of the reversible reaction graph need not exhaust additive collision invariants.
- **Failure certificate:** Eight fermionic momentum cells in four opposite pairs, with only the three positive-rate opposite-pair exchange reactions sharing a reference pair, form a connected microreversible total-charge/energy-momentum sector. Occupancies 1/2 on the six axis cells, 3/4 on `+u` and 1/4 on `−u` yield zero entropy production because opposite-pair log-odds sums vanish. No single printed affine Gibbs log-odds parameter fits both axis and `±u` values.
- **Scope:** The inequality `(X−Y) log(X/Y)≥0` remains correct; this countermodel is a permitted abstract collision kernel, **not** a test of the actually generated Born–Hopf Standard Model collision network. The thermal/KMS interface retains its own independently stated conditions.
- **Direct impact:** Gibbs-uniqueness clause of `p4:thm:v496-quantum-kinetic-h`; no certified universal downstream proof route attached. Additional collision-invariant completeness `BH-IVB-A-0002` is required. Later cosmological kinetic consumers are POSSIBLY_AFFECTED, not claimed proved dependent.
- **Resolution obligation:** Check and certify full additive-collision-invariant classification on the *actually admitted* quasiparticle kernel/sector; no assumption manufactured.

## Mathematical issue vs conditional physical interface
- **Established proof-scope defects:** exactly the two IDs above. No additional source-as-printed defect established in Batches 1, 3, 4.
- **Legitimate conditional statements:** finite KMS/global KMS accumulation, full interacting H source-visible pole, dynamical detector/source actualization, finite-to-asymptotic scattering, chosen lepton and Petersen source incidents, and cosmological source work. These are not classified as incorrect merely because the paper explicitly requires their inputs.
- **Evidence scope:** finite computation on a sample owner cannot certify all quantified possible source words; follow-up physical data may be needed even after the mathematical source theorem is correct.
- **DAG coverage:** reviewed material edges are explicitly promoted only with source-matched use witnesses and AND routes. Citation-only candidates remain quarantined. Two first-known inferred predicates are entered as single condition nodes; existing constituted checkpoints are inherited, not duplicated.

## Four bounded batches and their retained exact ledgers
| Batch | Source lines | Named statements | Proofs | Passing scoped checks | New issues |
|---|---:|---:|---:|---:|---|
| 1 | 65–2240 | 39 | 29 | 14 | none |
| 2 | 2241–4710 | 57 | 36 | 26 | BH-G-000100, BH-G-000101 |
| 3 | 4711–7996 | 53 | 46 | 32 | none |
| 4 | 7997–12149 | 78 | 65 | 47 | none |

## Full 227-claim source disposition ledger
| # | Source line | Type | Exact label | Verdict | Has proof |
|---:|---:|---|---|---|:---:|
| 1 | 352 | PROPOSITION | `p4:prop:native-qft-status` | REPRODUCED | yes |
| 2 | 404 | REMARK | `p4:rem:qft-postulate-boundary` | FORMALIZED | — |
| 3 | 475 | PROPOSITION | `p4:prop:bare-algebra-one-particle-no-selector` | VERIFIED | yes |
| 4 | 494 | THEOREM | `p4:thm:stationary-positive-frequency-mode-space` | VERIFIED-CONDITIONAL | yes |
| 5 | 546 | THEOREM | `p4:thm:v245-hessian-kahler-projective-geometry` | VERIFIED-CONDITIONAL | yes |
| 6 | 651 | PROPOSITION | `p4:prop:no-exact-ccr` | VERIFIED | yes |
| 7 | 674 | THEOREM | `p4:thm:v245-finite-free-vacuum-covariance` | VERIFIED-CONDITIONAL | yes |
| 8 | 737 | PROPOSITION | `p4:prop:paired-berezin-determinant-line` | VERIFIED-CONDITIONAL | yes |
| 9 | 767 | COROLLARY | `p4:cor:v489-fixed-carrier-gauge-jacobian-cancellation` | VERIFIED-CONDITIONAL | yes |
| 10 | 792 | REMARK | `p4:rem:v489-fixed-versus-chiral-line` | FORMALIZED | — |
| 11 | 802 | THEOREM | `p4:thm:parallel-line-trivialization` | REPRODUCED | yes |
| 12 | 833 | REMARK | `p4:rem:parallel-line-chiral-firewall` | FORMALIZED | — |
| 13 | 842 | COROLLARY | `p4:cor:doubled-pfaffian-presentation` | VERIFIED | yes |
| 14 | 860 | THEOREM | `p4:thm:finite-fermion-clock-real-form` | VERIFIED-CONDITIONAL | yes |
| 15 | 908 | THEOREM | `p4:thm:finite-energy-source-certificate` | VERIFIED-CONDITIONAL | yes |
| 16 | 936 | COROLLARY | `p4:cor:finite-constrained-energy-duality` | VERIFIED-CONDITIONAL | yes |
| 17 | 985 | THEOREM | `p4:thm:v4106-functional-hilbert-response` | REPRODUCED | yes |
| 18 | 1061 | COROLLARY | `p4:cor:v4106-moving-carrier-contact` | REPRODUCED | yes |
| 19 | 1106 | THEOREM | `p4:thm:v4106-canonical-stress-ward` | REPRODUCED | yes |
| 20 | 1207 | THEOREM | `p4:thm:v4118-passive-clock-pullback` | REPRODUCED | yes |
| 21 | 1286 | THEOREM | `p4:thm:v4118-homogeneous-time-ward` | REPRODUCED | yes |
| 22 | 1343 | COROLLARY | `p4:cor:v4118-homogeneous-source-work` | REPRODUCED | yes |
| 23 | 1400 | PROPOSITION | `p4:prop:v2174-occupation-phase-moment` | VERIFIED-CONDITIONAL | yes |
| 24 | 1448 | REMARK | `UNLABELED:Paper4B:remark:1448` | FORMALIZED | — |
| 25 | 1465 | THEOREM | `p4:thm:gp1-bosonic-occupation-boundary` | VERIFIED-CONDITIONAL | yes |
| 26 | 1528 | COROLLARY | `p4:cor:occupation-cutoff-saturation` | VERIFIED-CONDITIONAL | yes |
| 27 | 1614 | DEFINITION | `p4:def:intrinsic-finite-spectral-block` | FORMALIZED | — |
| 28 | 1629 | REMARK | `p4:rem:reeb-polarization-not-time-frequency` | FORMALIZED | — |
| 29 | 1647 | LEMMA | `p4:lem:positive-frequency-generator-from-euclidean-block` | VERIFIED-CONDITIONAL | yes |
| 30 | 1728 | DEFINITION | `p4:def:minimal-uninserted-free-scalar-cover-domain` | FORMALIZED | — |
| 31 | 1783 | LEMMA | `p4:lem:second-order-free-collapse` | REPRODUCED | yes |
| 32 | 1819 | LEMMA | `p4:lem:scalar-cover-speed-normalization` | VERIFIED-CONDITIONAL | yes |
| 33 | 1858 | COROLLARY | `p4:cor:finite-inherited-operational-speed` | REPRODUCED | — |
| 34 | 1877 | THEOREM | `p4:thm:finite-one-particle-dispersion` | VERIFIED-CONDITIONAL | yes |
| 35 | 1993 | THEOREM | `p4:thm:pure-scalar-factor-representation` | VERIFIED-CONDITIONAL | yes |
| 36 | 2029 | COROLLARY | `p4:cor:stationary-free-law-dyn-law-closure` | REPRODUCED | — |
| 37 | 2048 | THEOREM | `p4:thm:stationary-quadratic-real-form-pair` | VERIFIED-CONDITIONAL | yes |
| 38 | 2140 | THEOREM | `p4:thm:v244-action-generated-schrodinger-form` | VERIFIED-CONDITIONAL | yes |
| 39 | 2206 | COROLLARY | `p4:cor:v244-generated-green-operators` | VERIFIED-CONDITIONAL | — |
| 40 | 2248 | PROPOSITION | `p4:prop:coordinate-source-work` | VERIFIED-CONDITIONAL | yes |
| 41 | 2285 | PROPOSITION | `p4:prop:spherical-free-dirac-source` | REPRODUCED | yes |
| 42 | 2338 | COROLLARY | `p4:cor:spherical-free-positive-constituent` | VERIFIED-CONDITIONAL | yes |
| 43 | 2362 | COROLLARY | `p4:cor:spherical-dirac-trace-source-work` | VERIFIED-CONDITIONAL | yes |
| 44 | 2388 | PROPOSITION | `p4:prop:spherical-dirac-retarded-kernel` | VERIFIED-CONDITIONAL | yes |
| 45 | 2433 | COROLLARY | `p4:cor:common-flow-dynamic-tests` | VERIFIED-CONDITIONAL | yes |
| 46 | 2459 | COROLLARY | `p4:cor:finite-tt-source-response` | REPRODUCED | yes |
| 47 | 2522 | THEOREM | `p4:thm:v2190-car-euler-derivation` | VERIFIED-CONDITIONAL | yes |
| 48 | 2583 | THEOREM | `p4:thm:v2190-complete-finite-propagator` | VERIFIED-CONDITIONAL | yes |
| 49 | 2619 | COROLLARY | `p4:cor:v2190-frame-constraint-transport` | VERIFIED-CONDITIONAL | yes |
| 50 | 2683 | THEOREM | `p4:thm:finite-thermal-kms-kinetic-interface` | VERIFIED | yes |
| 51 | 2726 | REMARK | `p4:rem:finite-kms-kinetic-boundary` | FORMALIZED | — |
| 52 | 2756 | THEOREM | `p4:thm:finite-channel-scattering-lsz-interface` | REPRODUCED | yes |
| 53 | 2818 | THEOREM | `p4:thm:external-fermion-line-generated-closure` | VERIFIED-CONDITIONAL | yes |
| 54 | 2873 | REMARK | `UNLABELED:Paper4B:remark:2873` | FORMALIZED | — |
| 55 | 2885 | THEOREM | `p4:thm:finite-reference-integration-ray` | VERIFIED-CONDITIONAL | yes |
| 56 | 2913 | THEOREM | `p4:thm:euclidean-weight-rigidity` | INCONSISTENT | yes |
| 57 | 2944 | DEFINITION | `p4:def:generated-finite-euclidean-quantum-ray` | FORMALIZED | — |
| 58 | 2964 | COROLLARY | `p4:cor:finite-generated-quantum-constructor` | REPRODUCED | — |
| 59 | 2974 | COROLLARY | `p4:cor:v2140-relative-determinant-weights` | VERIFIED-CONDITIONAL | yes |
| 60 | 3033 | THEOREM | `p4:thm:finite-euclidean-path-integral-status` | VERIFIED-CONDITIONAL | yes |
| 61 | 3084 | REMARK | `p4:rem:finite-interaction-versus-geometric-vertex` | FORMALIZED | — |
| 62 | 3116 | THEOREM | `p4:thm:hurwitz-link-finite-support-import` | REPRODUCED | yes |
| 63 | 3213 | COROLLARY | `p4:cor:v204-quantum-sampled-transport` | VERIFIED-CONDITIONAL | yes |
| 64 | 3249 | REMARK | `p4:rem:no-scalene-carrier-triangle` | FORMALIZED | — |
| 65 | 3255 | COROLLARY | `p4:cor:hurwitz-finite-operator-algebras` | REPRODUCED | yes |
| 66 | 3325 | THEOREM | `p4:thm:finite-gauge-constraint-closure` | VERIFIED-CONDITIONAL | yes |
| 67 | 3343 | REMARK | `p4:rem:v176-finite-gauge-noether-typing` | FORMALIZED | — |
| 68 | 3367 | PROPOSITION | `p4:prop:explicit-finite-ccr-boundary-defect` | VERIFIED | yes |
| 69 | 3394 | REMARK | `p4:rem:ccr-defect-meaning` | FORMALIZED | — |
| 70 | 3432 | THEOREM | `p4:thm:finite-wick-quasifree-calculus` | VERIFIED-CONDITIONAL | yes |
| 71 | 3513 | REMARK | `p4:rem:finite-wick-downstream-support` | FORMALIZED | — |
| 72 | 3529 | THEOREM | `p4:thm:car-source-variance` | VERIFIED | yes |
| 73 | 3575 | COROLLARY | `p4:cor:bounded-source-connected-return` | VERIFIED-CONDITIONAL | yes |
| 74 | 3601 | THEOREM | `p4:thm:v4100-exact-graded-eaa` | REPRODUCED | yes |
| 75 | 3640 | REMARK | `p4:rem:v4100-graded-eaa-scope` | FORMALIZED | — |
| 76 | 3699 | PROPOSITION | `p4:prop:framework-scattering-window` | VERIFIED-CONDITIONAL | yes |
| 77 | 3744 | REMARK | `p4:rem:scattering-smatrix` | FORMALIZED | — |
| 78 | 3785 | LEMMA | `p4:lem:derived-scattering-plateau` | VERIFIED-CONDITIONAL | yes |
| 79 | 3907 | LEMMA | `p4:lem:finite-window-scattering-cauchy-criterion` | VERIFIED-CONDITIONAL | yes |
| 80 | 3934 | THEOREM | `p4:thm:moller-bridge` | REPRODUCED | yes |
| 81 | 4129 | THEOREM | `p4:thm:finite-resonance-reduction` | VERIFIED-CONDITIONAL | yes |
| 82 | 4176 | REMARK | `p4:rem:finite-resonance-status` | FORMALIZED | — |
| 83 | 4186 | REMARK | `p4:rem:resonance-meaning` | FORMALIZED | — |
| 84 | 4232 | REMARK | `p4:rem:scattering-spectroscopy-bridge` | FORMALIZED | — |
| 85 | 4280 | THEOREM | `p4:thm:minimal-finite-temperature-seesaw-interface` | REPRODUCED | yes |
| 86 | 4430 | REMARK | `p4:rem:thermal-interface-status` | FORMALIZED | — |
| 87 | 4440 | LEMMA | `p4:lem:uniform-finite-trace-efficiency` | VERIFIED-CONDITIONAL | yes |
| 88 | 4457 | PROPOSITION | `p4:prop:sphaleron-and-photon-conversion` | VERIFIED-CONDITIONAL | yes |
| 89 | 4519 | PROPOSITION | `p4:prop:v496-depth-not-beta` | VERIFIED-CONDITIONAL | — |
| 90 | 4537 | THEOREM | `p4:thm:v496-quantum-kinetic-h` | INCONSISTENT | — |
| 91 | 4565 | REMARK | `p4:rem:v496-local-not-global-kms` | FORMALIZED | — |
| 92 | 4580 | PROPOSITION | `p4:prop:v497-internal-response-positive-frequency` | VERIFIED-CONDITIONAL | — |
| 93 | 4602 | COROLLARY | `p4:cor:v497-state-not-saturation` | VERIFIED-CONDITIONAL | — |
| 94 | 4623 | THEOREM | `p4:thm:v498-no-charge-production` | VERIFIED-CONDITIONAL | yes |
| 95 | 4665 | PROPOSITION | `p4:prop:v4103-real-pair-response-no-new-phase` | VERIFIED-CONDITIONAL | yes |
| 96 | 4694 | REMARK | `p4:rem:v4103-relative-sector-cp` | FORMALIZED | — |
| 97 | 4766 | THEOREM | `p4:thm:sector-compatible-observables` | VERIFIED-CONDITIONAL | yes |
| 98 | 4820 | COROLLARY | `p4:cor:sector-vs-mixing-observables` | VERIFIED-CONDITIONAL | yes |
| 99 | 4841 | PROPOSITION | `p4:prop:trace-neutral-finite-word-selection` | VERIFIED-CONDITIONAL | yes |
| 100 | 4869 | REMARK | `p4:rem:trace-neutral-selection-status` | FORMALIZED | — |
| 101 | 4908 | PROPOSITION | `p4:prop:finite-family-factors` | VERIFIED-CONDITIONAL | yes |
| 102 | 4949 | COROLLARY | `p4:cor:rank-three-family-sectors` | VERIFIED-CONDITIONAL | yes |
| 103 | 4994 | PROPOSITION | `p4:prop:finite-sector-transition` | VERIFIED-CONDITIONAL | yes |
| 104 | 5021 | REMARK | `p4:rem:sector-transition-meaning` | FORMALIZED | — |
| 105 | 5060 | PROPOSITION | `p4:prop:finite-threshold` | VERIFIED-CONDITIONAL | yes |
| 106 | 5098 | REMARK | `p4:rem:effective-threshold-language` | FORMALIZED | — |
| 107 | 5117 | THEOREM | `p4:thm:finite-multiplet-mixing` | VERIFIED-CONDITIONAL | yes |
| 108 | 5175 | COROLLARY | `p4:cor:v4101-generated-pair-member-handoff` | REPRODUCED | yes |
| 109 | 5217 | REMARK | `p4:rem:v4101-exact-charge-scope` | FORMALIZED | — |
| 110 | 5240 | THEOREM | `p4:thm:v4102-pair-charge-source` | VERIFIED-CONDITIONAL | yes |
| 111 | 5295 | THEOREM | `p4:thm:v4102-finite-car-charge-propagation` | VERIFIED-CONDITIONAL | yes |
| 112 | 5348 | REMARK | `p4:rem:v4102-charge-propagation-scope` | FORMALIZED | — |
| 113 | 5360 | COROLLARY | `p4:cor:v498-phase-locked-pairing-invariant` | VERIFIED-CONDITIONAL | yes |
| 114 | 5398 | REMARK | `p4:rem:v4102-relative-phase-scope` | FORMALIZED | — |
| 115 | 5426 | LEMMA | `p4:lem:v2167-pair-commutator` | VERIFIED | yes |
| 116 | 5442 | THEOREM | `p4:thm:v2167-inherited-pair-coefficients` | VERIFIED-CONDITIONAL | yes |
| 117 | 5488 | COROLLARY | `p4:cor:v2167-returned-pair-kernel` | VERIFIED-CONDITIONAL | yes |
| 118 | 5549 | PROPOSITION | `p4:prop:v2168-stationary-source-quotient` | VERIFIED-CONDITIONAL | yes |
| 119 | 5634 | THEOREM | `p4:thm:v2168-dynamical-fidelity` | VERIFIED-CONDITIONAL | yes |
| 120 | 5681 | COROLLARY | `p4:cor:v2168-positive-source-leakage` | VERIFIED-CONDITIONAL | yes |
| 121 | 5722 | THEOREM | `p4:thm:v2168-stationary-family-fidelity` | VERIFIED-CONDITIONAL | yes |
| 122 | 5888 | THEOREM | `p4:v2169:b11:thm:normalstate` | VERIFIED-CONDITIONAL | yes |
| 123 | 5940 | REMARK | `p4:rem:v239-gibbs-support-scope` | FORMALIZED | — |
| 124 | 5981 | THEOREM | `p4:v2169:b11:thm:weakslater` | VERIFIED-CONDITIONAL | yes |
| 125 | 6173 | THEOREM | `p4:v2169:b12:thm:adjacentnumber` | VERIFIED-CONDITIONAL | yes |
| 126 | 6230 | COROLLARY | `p4:v2169:b12:cor:onefermion` | VERIFIED-CONDITIONAL | yes |
| 127 | 6370 | THEOREM | `p4:v2171:thm:fullcharge` | VERIFIED-CONDITIONAL | yes |
| 128 | 6427 | THEOREM | `p4:v2171:thm:flow` | VERIFIED-CONDITIONAL | yes |
| 129 | 6494 | THEOREM | `p4:v2171:thm:capcommutator` | VERIFIED-CONDITIONAL | yes |
| 130 | 6546 | PROPOSITION | `p4:prop:v2219-uv-bogoliubov` | REPRODUCED | — |
| 131 | 6563 | REMARK | `UNLABELED:Paper4B:remark:6563` | FORMALIZED | — |
| 132 | 6580 | COROLLARY | `p4:cor:v228-charged-bilinear` | VERIFIED-CONDITIONAL | yes |
| 133 | 6603 | PROPOSITION | `p4b:prop:v240-protected-chiral-source-splitting` | REPRODUCED | yes |
| 134 | 6624 | THEOREM | `p4b:thm:v240-complete-one-source-stieltjes` | VERIFIED-CONDITIONAL | yes |
| 135 | 6699 | THEOREM | `p4:thm:v2168-bilinear-source-commutators` | VERIFIED-CONDITIONAL | yes |
| 136 | 6755 | PROPOSITION | `p4:prop:v2168-coefficient-pairing` | VERIFIED | yes |
| 137 | 6791 | THEOREM | `p4:thm:v2168-commuting-port-memory-gram` | VERIFIED-CONDITIONAL | yes |
| 138 | 6856 | PROPOSITION | `p4:prop:v2168-equivariant-charge-reduction` | VERIFIED-CONDITIONAL | yes |
| 139 | 6934 | THEOREM | `p4:thm:v2168-faithful-stationary-poles` | VERIFIED-CONDITIONAL | yes |
| 140 | 7012 | COROLLARY | `p4:cor:v2168-support-family-visibility` | VERIFIED-CONDITIONAL | yes |
| 141 | 7057 | THEOREM | `p4:thm:v2168-regular-gap-root-bound` | VERIFIED-CONDITIONAL | yes |
| 142 | 7198 | THEOREM | `p4:v2169:b7:thm:closure` | VERIFIED-CONDITIONAL | yes |
| 143 | 7248 | THEOREM | `p4:v2169:b7:thm:poles` | VERIFIED-CONDITIONAL | yes |
| 144 | 7420 | THEOREM | `p4:v2169:b10:thm:support` | VERIFIED-CONDITIONAL | yes |
| 145 | 7637 | COROLLARY | `p4:cor:v2174-full-ground-degree-bound` | VERIFIED-CONDITIONAL | yes |
| 146 | 7715 | LEMMA | `p4:lem:v2186-exact-source-cyclic-action` | VERIFIED-CONDITIONAL | yes |
| 147 | 7756 | THEOREM | `p4:thm:v2186-common-source-cyclic-polynomial` | VERIFIED-CONDITIONAL | yes |
| 148 | 7815 | COROLLARY | `p4:cor:v2186-source-cyclic-residue-scope` | VERIFIED-CONDITIONAL | yes |
| 149 | 7837 | COROLLARY | `p4:cor:v2186-scalar-center-pole-invisibility` | VERIFIED-CONDITIONAL | yes |
| 150 | 8056 | THEOREM | `p4:thm:weak-monitoring-diffusive` | VERIFIED-CONDITIONAL | yes |
| 151 | 8251 | PROPOSITION | `p4:prop:weak-value-ozawa-domain` | VERIFIED-CONDITIONAL | yes |
| 152 | 8345 | PROPOSITION | `p4:prop:pure-dephasing-rates` | VERIFIED-CONDITIONAL | yes |
| 153 | 8416 | COROLLARY | `p4:cor:pointer-operational` | VERIFIED-CONDITIONAL | yes |
| 154 | 8507 | THEOREM | `p4:thm:v2203-gaussian-physical-work` | VERIFIED-CONDITIONAL | yes |
| 155 | 8551 | PROPOSITION | `p4:prop:v2203-gaussian-functional-work` | VERIFIED-CONDITIONAL | yes |
| 156 | 8585 | PROPOSITION | `p4:prop:v2203-time-dependent-chart-work` | VERIFIED-CONDITIONAL | yes |
| 157 | 8635 | THEOREM | `p4:thm:v2203-causal-mean-response-noise` | VERIFIED-CONDITIONAL | yes |
| 158 | 8673 | PROPOSITION | `p4:prop:v2203-gaussian-connected-noise` | VERIFIED-CONDITIONAL | yes |
| 159 | 8726 | COROLLARY | `p4:cor:v2203-gaussian-linear-even-parity` | VERIFIED-CONDITIONAL | yes |
| 160 | 8750 | PROPOSITION | `p4:prop:v2203-quantum-schur-nonduplication` | VERIFIED-CONDITIONAL | yes |
| 161 | 8787 | THEOREM | `p4:thm:v2203-gaussian-cold-tail` | VERIFIED-CONDITIONAL | yes |
| 162 | 8863 | THEOREM | `p4:thm:v2209-passive-work-capacity` | VERIFIED-CONDITIONAL | yes |
| 163 | 8906 | THEOREM | `p4:thm:v2217-monotone-free-loading` | VERIFIED-CONDITIONAL | yes |
| 164 | 8952 | PROPOSITION | `p4:prop:v2209-compact-bloch-source` | VERIFIED-CONDITIONAL | yes |
| 165 | 8988 | REMARK | `p4:rem:v2209-noise-energy-witness` | FORMALIZED | — |
| 166 | 9006 | THEOREM | `p4:thm:v2209-controlled-excitation-survival` | VERIFIED-CONDITIONAL | yes |
| 167 | 9054 | COROLLARY | `p4:cor:v2209-native-tail-retention` | REPRODUCED | yes |
| 168 | 9082 | PROPOSITION | `p4:prop:v2209-inherited-mixedness-gap` | VERIFIED-CONDITIONAL | yes |
| 169 | 9113 | COROLLARY | `p4:cor:v2212-massive-conformal-shape-kernel` | REPRODUCED | yes |
| 170 | 9244 | REMARK | `p4:rem:v2212-conformal-shape-scope` | FORMALIZED | — |
| 171 | 9282 | THEOREM | `p4:thm:quasilocal-thermodynamic-bridge` | REPRODUCED | yes |
| 172 | 9369 | REMARK | `p4:rem:thermo-conditionality` | FORMALIZED | — |
| 173 | 9386 | REMARK | `p4:rem:v490-local-kinetic-versus-kms` | FORMALIZED | — |
| 174 | 9404 | PROPOSITION | `p4:prop:v236-thermal-atlas` | REPRODUCED | — |
| 175 | 9431 | PROPOSITION | `p4:prop:v236-scattering-atlas` | REPRODUCED | — |
| 176 | 9455 | THEOREM | `p4:thm:v2109-finite-root-restrictions` | VERIFIED-CONDITIONAL | yes |
| 177 | 9500 | THEOREM | `p4:thm:v2114-neutral-fock-unit` | REPRODUCED | yes |
| 178 | 9546 | THEOREM | `p4:thm:v2114-positive-family-ground-source` | VERIFIED-CONDITIONAL | yes |
| 179 | 9586 | THEOREM | `p4:thm:v2109-finite-evolution-error` | VERIFIED-CONDITIONAL | yes |
| 180 | 9636 | THEOREM | `p4:thm:v2109-euclidean-weight-support` | VERIFIED | yes |
| 181 | 9672 | THEOREM | `p4:thm:v164-action-hessian-pole-owner` | REPRODUCED | — |
| 182 | 9687 | THEOREM | `p4:thm:v164-finite-gibbs-vacuum-no-thermalization` | VERIFIED-CONDITIONAL | — |
| 183 | 9764 | COROLLARY | `p4:cor:v491-fermion-factor-source-multiplication` | VERIFIED-CONDITIONAL | yes |
| 184 | 9960 | THEOREM | `p4:thm:v2210-lit-instrument-mixing` | VERIFIED-CONDITIONAL | yes |
| 185 | 10014 | COROLLARY | `p4:cor:v2211-finite-event-resolvent-certificate` | VERIFIED-CONDITIONAL | yes |
| 186 | 10083 | COROLLARY | `p4:cor:v2211-event-frequency-strong-law` | VERIFIED-CONDITIONAL | yes |
| 187 | 10125 | THEOREM | `p4:thm:v255-sharp-event-frequency` | VERIFIED-CONDITIONAL | yes |
| 188 | 10284 | PROPOSITION | `p4:prop:v255-periodic-persistent-records` | VERIFIED-CONDITIONAL | yes |
| 189 | 10343 | THEOREM | `p4:thm:v258-nonstationary-frequency-law` | VERIFIED-CONDITIONAL | yes |
| 190 | 10506 | COROLLARY | `p4:cor:v258-asymptotic-frequency-povm` | VERIFIED-CONDITIONAL | yes |
| 191 | 10559 | COROLLARY | `p4:cor:v258-stationary-frequency-recovery` | VERIFIED-CONDITIONAL | yes |
| 192 | 10586 | PROPOSITION | `p4:prop:v258-frequency-law-diagnostics` | VERIFIED-CONDITIONAL | yes |
| 193 | 10661 | PROPOSITION | `p4:prop:v2210-lit-frequency-obstructions` | VERIFIED-CONDITIONAL | yes |
| 194 | 10691 | PROPOSITION | `p4:prop:v2210-lit-markov-window` | VERIFIED-CONDITIONAL | yes |
| 195 | 10729 | THEOREM | `p4:thm:v2216-zero-excitation-dynamic-response` | VERIFIED-CONDITIONAL | yes |
| 196 | 10797 | REMARK | `p4:rem:v2216-qroot-dynamic-scope` | FORMALIZED | — |
| 197 | 10817 | THEOREM | `p4:thm:v2216-graded-matter-uv` | REPRODUCED | yes |
| 198 | 10882 | REMARK | `p4:rem:v2216-graded-matter-scope` | FORMALIZED | — |
| 199 | 10914 | PROPOSITION | `p4:prop:v2216-finite-heat-integrability` | REPRODUCED | yes |
| 200 | 10959 | REMARK | `p4:rem:v2216-finite-heat-domain` | FORMALIZED | — |
| 201 | 10986 | THEOREM | `p3f:thm:v247-car-influence-determinant` | VERIFIED | yes |
| 202 | 11041 | COROLLARY | `p3f:cor:v247-car-logdet-jets` | VERIFIED-CONDITIONAL | yes |
| 203 | 11065 | PROPOSITION | `p3f:prop:v247-car-source-jets` | VERIFIED-CONDITIONAL | yes |
| 204 | 11118 | PROPOSITION | `p3f:prop:v247-car-influence-frame-transport` | VERIFIED-CONDITIONAL | yes |
| 205 | 11151 | THEOREM | `p4:thm:v247-native-source-factorization` | VERIFIED-CONDITIONAL | yes |
| 206 | 11263 | COROLLARY | `p4:cor:v247-native-source-work-cumulants` | VERIFIED-CONDITIONAL | yes |
| 207 | 11351 | PROPOSITION | `p4:v251:prop:symmetry-transport` | REPRODUCED | yes |
| 208 | 11380 | PROPOSITION | `p4:v251:prop:finite-response-symmetry` | VERIFIED-CONDITIONAL | yes |
| 209 | 11428 | THEOREM | `p4:v251:thm:lepton-cyclic-response` | REPRODUCED | yes |
| 210 | 11493 | COROLLARY | `p4:v251:cor:required-noncyclic-content` | VERIFIED-CONDITIONAL | yes |
| 211 | 11596 | THEOREM | `p4b:thm:v254-in-in-charge-detector-covariance` | VERIFIED-CONDITIONAL | yes |
| 212 | 11641 | COROLLARY | `p4b:cor:v254-ward-operator-residual` | VERIFIED-CONDITIONAL | yes |
| 213 | 11670 | PROPOSITION | `p4b:prop:v254-same-action-angular-flux` | REPRODUCED | yes |
| 214 | 11696 | REMARK | `UNLABELED:Paper4B:remark:11696` | FORMALIZED | — |
| 215 | 11715 | THEOREM | `p4b:thm:v266-native-instrument` | REPRODUCED | yes |
| 216 | 11746 | COROLLARY | `p4b:cor:v266-quadratic-repeat` | VERIFIED-CONDITIONAL | yes |
| 217 | 11781 | THEOREM | `p4b:thm:v320-chiral-auxiliary-poles` | VERIFIED-CONDITIONAL | yes |
| 218 | 11831 | COROLLARY | `p4b:cor:v320-complement-phase-gauge` | VERIFIED-CONDITIONAL | yes |
| 219 | 11855 | THEOREM | `p4b:thm:v320-z2-loop-interference` | VERIFIED-CONDITIONAL | yes |
| 220 | 11892 | PROPOSITION | `p4b:prop:v320-source-incidence-boundary` | REPRODUCED | yes |
| 221 | 11931 | THEOREM | `p4b:thm:v347-onebody-criterion` | VERIFIED-CONDITIONAL | yes |
| 222 | 11972 | COROLLARY | `p4b:cor:v347-retarded-criterion` | VERIFIED-CONDITIONAL | yes |
| 223 | 11999 | PROPOSITION | `p4b:prop:v347-three-mode-response-obstruction` | VERIFIED | yes |
| 224 | 12032 | THEOREM | `p4b:thm:v347-majorana-hierarchy` | VERIFIED-CONDITIONAL | yes |
| 225 | 12064 | PROPOSITION | `p4b:prop:v347-odd-transfer-witness` | VERIFIED-CONDITIONAL | yes |
| 226 | 12100 | THEOREM | `p4b:thm:v356-current-visible-krylov` | VERIFIED | yes |
| 227 | 12137 | REMARK | `p4b:rem:v356-current-krylov-scope` | FORMALIZED | — |

## Global DAG and reproducibility handoff
- Global audit layer: `DAG/AuditLayer/Paper4B-v1_1/Index.json`, linked in `DAG/Paper00-TheoremDAG.json`, `DAG/CombinedGraphIndex-v1_108.json` and `DAG/Paper00-CompositeAuditIndex-v1_108.json`.
- Full original LaTeX statements, exact proof text, proof witnesses and source locator links: `AuditClaimLedger.json`. All local test scripts and raw results are included inside the atlas under `Evidence/Paper4B/`.
- Typed proof edge semantics: `TypedDependencyEdges.json`; conditional AND routes: `ProofRoutes.json`; two exact gap certificates: `GapRegistry.json`; first-known inferred premises: `AssumptionRegistry.json`; traversal/impact: `ImpactIndex.json`.
- The general DAG query script handles `node`, `conditions`, `descendants`, `prerequisites`, `issue`, `checks`, `staged` and `source`. No claim is made that all 5100+ historical claims are newly reverified here.
- **Output packages:** updated global atlas `Paper00-DAGAtlas-v1_108.zip` and the latest-only audit collection `Paper00-ProofChainAudits-v1_25.zip` (15 audit reports: 14 inherited and Paper4B).

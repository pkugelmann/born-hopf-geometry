# Source migration and repair-integration addendum — Paper3D-ProofChainAudit-v1_3.md

**Integration release:** `Paper00-PapersMinimal-v3_007.zip`, 14 November 2026.
**Current paper source:** `Paper3D-RunningResponse-v1_166.tex`.
**Status:** `SOURCE_INTEGRATED; GLOBAL_SOURCE_REAUDIT_PENDING`. An inherited historical audit is not a correctness certificate for the newer current manuscript.
**Evidence policy:** Local algebraic proofs and scoped tests do not discharge physical source/observable interfaces or automatically alter the canonical proof DAG.

---

## Historical source-bound audit: Paper3D-ProofChainAudit-v1_2.md
# Paper 3D — current source repair addendum (v1.2)

Date: 13 November 2026. Repair batch 5. Historical proof-chain audit is preserved verbatim below; the old line positions and OPEN/disposition assertions apply to their original frozen source, not the revised manuscript.

- **Repaired current source:** `Paper3D-RunningResponse-v1_160.tex` (SHA-256 `fd67ab4b01b49c1f90e840d100703f76f3a2c2954a10fba7cfa172dd610ef4d8`).
- **Original finding IDs addressed:** `BH-IIID-HATJUNC-001`, `BH-IIID-DCHARPORT-002`.
- **Verification:** `Proofs/Paper00-AuditRepairBatch5-v1_1-verify.py` (41/41 scoped exact checks, one execution environment); full standalone derivations in `DAG/RepairLayer/Paper00-AuditRepairBatch-v1_5.md`.
- **Provenance:** no new whole-paper independent-audit assertion, no original statuses changed, no global DAG status promotion.
- **Conditional physical matters retained:** action-owned P4 incidence and physical junction (III-D); solder occurrence, actual full neutral-current amplitudes and baryon source/history (V-C).

## Source repair summary

The constant terminal Laurent trace still has zero distributional Hessian; an explicit, separately typed piecewise representative produces the positive Dirac jump. The grade-four coefficient is a positive character evaluation on the existing PQTI coefficient line; no physical metric-action insertion is inferred.

---

## Historical original audited report (unchanged below this heading)

# Paper III-D — cumulative rigorous verification and proof-chain DAG audit

## Controlling sources and scope

- **Paper:** `Paper3D-RunningResponse-v1_159.tex` from unchanged `Paper00-PapersMinimal-v2_370(1).zip`, SHA-256 `573e1830d1b486e7842743e9cb4141f0c25ef11e6e49ef27c97e54c84fc146b4`.
- **Method:** `Paper00-RigorousVerificationDAGWorkProtocol-v2_4(1).md`, three sequential comprehensive batches. Source-level proof E1, independent analytical/numerical E3, adversarial E4; upstream imports checked at exact consumed clauses.
- **Base global DAG:** `Paper00-DAGAtlas-v1_101(1).zip`; **base audit archive:** `Paper00-ProofChainAudits-v1_19(1).zip`. Both are frozen inputs, not source repairs.
- **Final classification:** **FULLY_AUDITED_WITH_OPEN_GAPS**. No source modifications or inferred physical-occurrence certifications.

## Coverage and disposition census

- **3,674/3,674** manuscript lines; **98/98** source objects; **68/68** formal declarations (23 theorems, 12 propositions, 5 lemmas, 15 corollaries, 13 definitions) and **30/30** remarks.
- **54/54** printed proof environments checked; **55** proof-bearing formal results (one explicitly without separate proof environment).
- Source dispositions: VERIFIED=14, VERIFIED-CONDITIONAL=39, FORMALIZED=43, UNRESOLVED=2.
- 97 source-reviewed typed premise/scope edges; 13 distinct first-origin condition nodes; 2 open source-local issue certificates.
- All 137 cross-paper reference uses (91 distinct labels) resolved in the current source anchor map; no unresolved local bibliography labels in source-reference scan.
- Three batches: lines 1–1,236; 1,237–2,501; 2,502–3,674. All reviewed source objects have explicit dispositions.

## Finding 1 — `BH-IIID-HATJUNC-001` (minor, open)

- **Origin:** lines 1743–1753, `p3d:thm:canonical-nonnegative-laurent-projection`.
- The text assigns nonzero distributional Hessian/junction measure to `\widehat{\mathcal H}_j` while identifying it with the constant terminal trace `C_j`. A constant has zero distributional derivatives. A separate piecewise-glued representative is needed for the displayed jump.
- **Safe subclaims:** positive-part Laurent algebra and the active-sector Hessian remain independently verified.
- **Repair obligation:** define the piecewise function and one-sided derivatives in the paper itself; no audit-only replacement counts as a source repair.
- **Dependency status:** later Paper VI-A cites algebraic/active pieces; no defective downstream path established for the ambiguous junction clause.

## Finding 2 — `BH-IIID-DCHARPORT-002` (moderate, open)

- **Origin:** lines 1835–1862, `p3d:thm:v2219-carrier-four-dressing`.
- The grade-four actual-carrier selection `j=4` is supported by the exact upstream III-C carrier statement. The additional coefficient amplitude `D_4(R)=Q_\sigma^{n_4^+(R)}` requires a typed coefficient owner and normalization not defined or discharged within the III-D theorem.
- **Safe subclaims:** carrier selection and rank-character exponents; Paper III-F/III-G contain separately scoped coefficient-owner material, not retroactive unconditional proofs of this source clause.
- **Repair obligation:** import the exact coefficient-owner premise at the origin, or type the displayed amplitude as conditional.
- **Dependency status:** no verified propagation of the missing coefficient as an unconditional physical prediction; conditional downstream carrier use remains valid.

## Previously open issue retained without duplication

- `BH-IIIC-DEPTHARG-002` remains an upstream Paper III-C issue. III-D explicitly uses a depth coordinate; the earlier flow/depth parameter confusion is not independently recreated.

## Every source object (canonical ID, lines, disposition)

| # | Batch | Claim/remark ID | Kind | Source lines | Disposition | Evidence |
|---:|---:|---|---|---:|---|---|
| 1 | 1 | `p3:def:effective-damping-ordering` | definition | 291–296 | **FORMALIZED** | E1:definition-scope-type-read |
| 2 | 1 | `p3:def:reeb-phase-contact-residue-distance` | definition | 298–314 | **FORMALIZED** | E1:definition-scope-type-read, E3-HOPF-C2 |
| 3 | 1 | `p3:def:protected-rank-quotient` | definition | 330–345 | **FORMALIZED** | E1:definition-scope-type-read |
| 4 | 1 | `Paper3D:unnamed:remark:347` | remark | 347–353 | **FORMALIZED** |  |
| 5 | 1 | `p3:lem:rank-atom-hopf-trace-localization` | lemma | 355–373 | **VERIFIED** | E1-IIID-B1-001, E3-HOPF-C2, E3-MULT-CHAR |
| 6 | 1 | `p3:lem:primitive-hopf-cell-normalization` | lemma | 389–410 | **VERIFIED-CONDITIONAL** | E1-IIID-B1-002, E3-HOPF-C2, E3-MULT-CHAR, E3-SCHEME-SIGN |
| 7 | 1 | `p3:thm:reeb-universal` | theorem | 438–479 | **VERIFIED-CONDITIONAL** | E1-IIID-B1-003, E3-MULT-CHAR, E3-SCHEME-SIGN |
| 8 | 1 | `p3:def:active-support-response` | definition | 494–534 | **FORMALIZED** | E1:definition-scope-type-read |
| 9 | 1 | `p3:lem:unit-trace-forces-reciprocal-active-fraction` | lemma | 536–548 | **VERIFIED** | E1-IIID-B1-004, E3-TRACE-DENSITY, E4-STATE-NONLINEAR |
| 10 | 1 | `p3:thm:eight-mode-harmonic-response` | corollary | 589–606 | **VERIFIED** | E1-IIID-B1-005, E3-TRACE-DENSITY, E4-STATE-NONLINEAR |
| 11 | 1 | `p3d:cor:generated-active-support-inheritance` | corollary | 617–640 | **VERIFIED-CONDITIONAL** | E1-IIID-B1-006, E3-TRACE-DENSITY, E4-SCOPE-TESTS |
| 12 | 1 | `Paper3D:unnamed:remark:642` | remark | 642–647 | **FORMALIZED** |  |
| 13 | 1 | `p3:rem:no-hidden-inverse-trace-axiom` | remark | 649–664 | **FORMALIZED** |  |
| 14 | 1 | `p3d:cor:unit-boundary-normal-form` | corollary | 666–681 | **VERIFIED** | E1-IIID-B1-007, E3-TRACE-DENSITY |
| 15 | 1 | `Paper3D:unnamed:remark:696` | remark | 696–709 | **FORMALIZED** |  |
| 16 | 1 | `p3:prop:ordering-versus-step-size` | proposition | 711–720 | **VERIFIED-CONDITIONAL** | E1-IIID-B1-008, E3-MULT-CHAR, E4-SCOPE-TESTS |
| 17 | 1 | `p3:thm:sequential` | theorem | 734–769 | **VERIFIED-CONDITIONAL** | E1-IIID-B1-009, E3-MULT-CHAR, E3-CLOCK-DEPTH, E4-SCOPE-TESTS |
| 18 | 1 | `Paper3D:unnamed:remark:810` | remark | 810–816 | **FORMALIZED** |  |
| 19 | 1 | `p3:rem:pseudoscalar-diagnostic-pointer` | remark | 818–828 | **FORMALIZED** |  |
| 20 | 1 | `p3:def:reduced-response-branch` | definition | 843–884 | **FORMALIZED** | E1:definition-scope-type-read |
| 21 | 1 | `p3:prop:one_parameter_reduction` | theorem | 906–921 | **VERIFIED-CONDITIONAL** | E1-IIID-B1-010, E3-BORN-REFLECTION, E4-SCOPE-TESTS |
| 22 | 1 | `p3:rem:no-hidden-beta-system` | remark | 966–973 | **FORMALIZED** |  |
| 23 | 1 | `p3:def:reciprocal-quotient-coordinate` | definition | 975–1002 | **FORMALIZED** | E1:definition-scope-type-read |
| 24 | 1 | `p3:lem:reduced-born-reciprocity` | lemma | 1004–1027 | **VERIFIED-CONDITIONAL** | E1-IIID-B1-011, E3-BORN-REFLECTION |
| 25 | 1 | `p3d:thm:born-seven-depth-reflection` | theorem | 1056–1079 | **VERIFIED-CONDITIONAL** | E1-IIID-B1-012, E3-BORN-REFLECTION, E4-SCOPE-TESTS |
| 26 | 1 | `p3d:cor:born-operational-scale-inversion` | corollary | 1093–1117 | **VERIFIED-CONDITIONAL** | E1-IIID-B1-013, E3-BORN-REFLECTION |
| 27 | 1 | `p3:def:visible-reciprocal-sector-weights` | definition | 1130–1170 | **FORMALIZED** | E1:definition-scope-type-read |
| 28 | 1 | `p3:lem:spectral-trace-sector-valuation` | lemma | 1172–1184 | **VERIFIED-CONDITIONAL** | E1-IIID-B1-014, E3-ROLE-TRACE, E4-SCOPE-TESTS |
| 29 | 1 | `Paper3D:unnamed:remark:1220` | remark | 1220–1227 | **FORMALIZED** |  |
| 30 | 1 | `Paper3D:unnamed:remark:1230` | remark | 1230–1235 | **FORMALIZED** |  |
| 31 | 2 | `p3:def:scalar-response-readout-normalization` | definition | 1237–1256 | **FORMALIZED** | E1-IIID-B2-SCOPE-READ |
| 32 | 2 | `p3:def:uv-ir-calibration-pair` | definition | 1258–1276 | **FORMALIZED** | E1-IIID-B2-SCOPE-READ |
| 33 | 2 | `p3:thm:geff_from_reciprocity` | theorem | 1278–1304 | **VERIFIED-CONDITIONAL** | E1-IIID-B2-SOURCE-REPLAY, E3-IIID-B2-ROOT-CAL |
| 34 | 2 | `p3d:cor:primitive-unit-quadratic-response` | corollary | 1334–1352 | **VERIFIED-CONDITIONAL** | E1-IIID-B2-SOURCE-REPLAY, E3-IIID-B2-EULER |
| 35 | 2 | `p3d:cor:two-scale-response-normalizations` | corollary | 1362–1386 | **VERIFIED-CONDITIONAL** | E1-IIID-B2-SOURCE-REPLAY, E3-IIID-B2-EULER |
| 36 | 2 | `p3d:cor:born-euler-response-pair` | corollary | 1394–1414 | **VERIFIED-CONDITIONAL** | E1-IIID-B2-SOURCE-REPLAY, E3-IIID-B2-EULER |
| 37 | 2 | `p3d:thm:minimal-born-laurent-characterization` | theorem | 1426–1459 | **VERIFIED** | E1-IIID-B2-SOURCE-REPLAY, E3-IIID-B2-LAUR-UNIQUE |
| 38 | 2 | `p3d:cor:rank-character-laurent-family` | corollary | 1479–1556 | **VERIFIED-CONDITIONAL** | E1-IIID-B2-SOURCE-REPLAY, E3-IIID-B2-SECANT |
| 39 | 2 | `p3d:thm:v285-calibration-free-hierarchy-dip` | theorem | 1576–1614 | **VERIFIED-CONDITIONAL** | E1-IIID-B2-SOURCE-REPLAY, E3-IIID-B2-DIP |
| 40 | 2 | `p3d:cor:born-midpoint-shell-coordinate` | corollary | 1642–1682 | **VERIFIED-CONDITIONAL** | E1-IIID-B2-SOURCE-REPLAY, E3-IIID-B2-DIP |
| 41 | 2 | `p3d:thm:canonical-nonnegative-laurent-projection` | theorem | 1698–1754 | **UNRESOLVED** | E1-IIID-B2-SOURCE-REPLAY, E3-IIID-B2-TRACE-JUNC |
| 42 | 2 | `p3d:thm:least-support-n2-dressing` | theorem | 1778–1808 | **VERIFIED-CONDITIONAL** | E1-IIID-B2-SOURCE-REPLAY, E3-IIID-B2-DRESS |
| 43 | 2 | `Paper3D:unnamed:remark:1824` | remark | 1824–1832 | **FORMALIZED** | E1-IIID-B2-SCOPE-READ |
| 44 | 2 | `p3d:thm:v2219-carrier-four-dressing` | theorem | 1835–1855 | **UNRESOLVED** | E1-IIID-B2-SOURCE-REPLAY, E3-IIID-B2-DRESS |
| 45 | 2 | `Paper3D:unnamed:remark:1864` | remark | 1864–1871 | **FORMALIZED** | E1-IIID-B2-SCOPE-READ |
| 46 | 2 | `p3d:rem:response-normalization-invariance` | remark | 1874–1899 | **FORMALIZED** | E1-IIID-B2-SCOPE-READ |
| 47 | 2 | `p3:rem:geff_status` | remark | 1902–1910 | **FORMALIZED** | E1-IIID-B2-SCOPE-READ |
| 48 | 2 | `p3:cor:fully_derived_one_parameter_trajectory` | corollary | 1912–1933 | **VERIFIED-CONDITIONAL** | E1-IIID-B2-SOURCE-REPLAY, E3-IIID-B2-DIP |
| 49 | 2 | `p3:rem:riccati_from_geff` | remark | 1963–1966 | **FORMALIZED** | E1-IIID-B2-SCOPE-READ |
| 50 | 2 | `p3d:rem:dimensionless-hierarchy-handoff` | remark | 1969–1987 | **FORMALIZED** | E1-IIID-B2-SCOPE-READ |
| 51 | 2 | `p3d:rem:anchored-reg-hierarchy-import` | remark | 1990–2000 | **FORMALIZED** | E1-IIID-B2-SCOPE-READ |
| 52 | 2 | `p3:thm:exact-reciprocal-freeze-interface` | theorem | 2005–2021 | **VERIFIED-CONDITIONAL** | E1-IIID-B2-SOURCE-REPLAY, E3-IIID-B2-ROOT-CAL |
| 53 | 2 | `p3:rem:forward-transport-normalization` | remark | 2028–2036 | **FORMALIZED** | E1-IIID-B2-SCOPE-READ |
| 54 | 2 | `p3d:thm:v222-born-phase-conjugation` | theorem | 2051–2076 | **VERIFIED-CONDITIONAL** | E1-IIID-B2-SOURCE-REPLAY, E3-IIID-B2-PHASE |
| 55 | 2 | `p3d:thm:v222-primitive-phase-twist` | theorem | 2093–2128 | **VERIFIED-CONDITIONAL** | E1-IIID-B2-SOURCE-REPLAY, E3-IIID-B2-PHASE |
| 56 | 2 | `p3d:rem:v222-phase-nonaction-firewall` | remark | 2151–2167 | **FORMALIZED** | E1-IIID-B2-SCOPE-READ |
| 57 | 2 | `p3d:prop:v223-curvature-clock` | proposition | 2173–2201 | **VERIFIED-CONDITIONAL** | E1-IIID-B2-SOURCE-REPLAY, E3-IIID-B2-CAP |
| 58 | 2 | `p3d:rem:v223-log-asinh` | remark | 2212–2228 | **FORMALIZED** | E1-IIID-B2-SCOPE-READ |
| 59 | 2 | `p3:eq:geff_def` | definition | 2245–2271 | **FORMALIZED** | E1-IIID-B2-SCOPE-READ |
| 60 | 2 | `p3:rem:reduced_variables_status` | remark | 2273–2288 | **FORMALIZED** | E1-IIID-B2-SCOPE-READ |
| 61 | 2 | `p3d:rem:v263-exponent-character-pullback` | remark | 2290–2312 | **FORMALIZED** | E1-IIID-B2-SCOPE-READ |
| 62 | 2 | `p3:thm:riccati` | theorem | 2314–2327 | **VERIFIED-CONDITIONAL** | E1-IIID-B2-SOURCE-REPLAY, E3-IIID-B2-DIP |
| 63 | 2 | `p3:prop:n_closed` | proposition | 2338–2353 | **VERIFIED-CONDITIONAL** | E1-IIID-B2-SOURCE-REPLAY, E3-IIID-B2-SECANT |
| 64 | 2 | `p3:def:active-reduced-window` | proposition | 2362–2371 | **VERIFIED-CONDITIONAL** | E1-IIID-B2-SOURCE-REPLAY, E3-IIID-B2-SECANT |
| 65 | 2 | `p3:thm:exact-calibrated-secant-range` | theorem | 2381–2402 | **VERIFIED-CONDITIONAL** | E1-IIID-B2-SOURCE-REPLAY, E3-IIID-B2-SECANT |
| 66 | 2 | `p3:def:neutral-visibility-readout` | definition | 2414–2439 | **FORMALIZED** | E1-IIID-B2-SCOPE-READ |
| 67 | 2 | `p3:thm:basis-neutral-entropy-lift` | theorem | 2441–2477 | **VERIFIED-CONDITIONAL** | E1-IIID-B2-SOURCE-REPLAY, E3-IIID-B2-ENTROPY |
| 68 | 3 | `p3d:rem:mresp-derived-later-state` | remark | 2502–2514 | **FORMALIZED** | E1-IIID-B3-CLAUSE-READ |
| 69 | 3 | `p3d:thm:v2211-excess-character-certificate` | theorem | 2532–2577 | **VERIFIED-CONDITIONAL** | E1-IIID-B3-SOURCE-REPLAY, E3-IIID-B3-EXCESS-ODE, E3-IIID-B3-EXCESS-JET, E4-IIID-B3-LOCAL-GLOBAL |
| 70 | 3 | `p3d:thm:v173-fixed-depth-laurent-excess-jet` | theorem | 2591–2623 | **VERIFIED-CONDITIONAL** | E1-IIID-B3-SOURCE-REPLAY, E3-IIID-B3-LOCAL-JET-BOUND, E3-IIID-B3-LOCAL-JET-END, E4-IIID-B3-LOCAL-GLOBAL |
| 71 | 3 | `p3d:prop:v2211-excess-jet-counterfamily` | proposition | 2634–2654 | **VERIFIED** | E1-IIID-B3-SOURCE-REPLAY, E3-IIID-B3-EXCESS-JET, E3-IIID-B3-EXCESS-ODE |
| 72 | 3 | `p3d:rem:v173-three-n7-sorts` | remark | 2663–2670 | **FORMALIZED** | E1-IIID-B3-CLAUSE-READ |
| 73 | 3 | `p3d:thm:v2216-complete-action-jets` | theorem | 2684–2723 | **VERIFIED** | E1-IIID-B3-SOURCE-REPLAY, E3-IIID-B3-ACTION-CHAIN, E3-IIID-B3-DIAG-TWOJET |
| 74 | 3 | `p3d:rem:v2217-density-matching-import` | remark | 2736–2745 | **FORMALIZED** | E1-IIID-B3-CLAUSE-READ |
| 75 | 3 | `Paper3D:unnamed:remark:2748` | remark | 2748–2764 | **FORMALIZED** | E1-IIID-B3-CLAUSE-READ |
| 76 | 3 | `p3d:thm:v2216-exjet-global-obstruction` | theorem | 2766–2796 | **VERIFIED** | E1-IIID-B3-SOURCE-REPLAY, E3-IIID-B3-EXJET-GLOBAL, E4-IIID-B3-LOCAL-GLOBAL |
| 77 | 3 | `p3d:cor:v2216-raw-euler-nongluing` | corollary | 2811–2818 | **VERIFIED-CONDITIONAL** | E1-IIID-B3-SOURCE-REPLAY, E3-IIID-B3-EXJET-GLOBAL |
| 78 | 3 | `p3d:prop:v226-response-coefficients` | proposition | 2827–2839 | **VERIFIED-CONDITIONAL** | E1-IIID-B3-SOURCE-REPLAY, E3-IIID-B3-DIAG-TWOJET, E3-IIID-B3-TOMOGRAPHY-DUAL |
| 79 | 3 | `p3d:cor:v227-running-frequency` | corollary | 2857–2863 | **VERIFIED-CONDITIONAL** | E1-IIID-B3-SOURCE-REPLAY, E3-IIID-B3-DIAG-TWOJET, E3-IIID-B3-ENERGY-SAMPLES |
| 80 | 3 | `p3d:thm:v2216-positive-born-provider` | theorem | 2892–2932 | **VERIFIED** | E1-IIID-B3-SOURCE-REPLAY, E3-IIID-B3-MEASURE-MASS, E3-IIID-B3-MEASURE-RESOLVENT, E3-IIID-B3-MEASURE-TERMINAL, E3-IIID-B3-MEASURE-INFINMOM, E3-IIID-B3-SCHUR-MIN, E4-IIID-B3-NOT-ACTION |
| 81 | 3 | `p3d:cor:v2216-born-positive-approximation` | corollary | 2971–2988 | **VERIFIED** | E1-IIID-B3-SOURCE-REPLAY, E3-IIID-B3-FINITE-SLOPE |
| 82 | 3 | `Paper3D:unnamed:remark:2999` | remark | 2999–3013 | **FORMALIZED** | E1-IIID-B3-CLAUSE-READ |
| 83 | 3 | `p3d:thm:v2216-finite-born-second-jet` | theorem | 3015–3053 | **VERIFIED** | E1-IIID-B3-SOURCE-REPLAY, E3-IIID-B3-FINITE-PHI-NONNEG, E3-IIID-B3-PHI-FIRST-JET, E3-IIID-B3-FINITE-THIRD-JET, E4-IIID-B3-NEUTRAL-SOURCE, E4-IIID-B3-NOT-ACTION |
| 84 | 3 | `p3d:prop:v2216-finite-born-limits` | proposition | 3078–3099 | **VERIFIED** | E1-IIID-B3-SOURCE-REPLAY, E3-IIID-B3-FINITE-THIRD-JET, E3-IIID-B3-FINITE-PHI-NONNEG, E3-IIID-B3-FROZEN-GLOBAL-SIGN |
| 85 | 3 | `Paper3D:unnamed:remark:3123` | remark | 3123–3138 | **FORMALIZED** | E1-IIID-B3-CLAUSE-READ |
| 86 | 3 | `p3d:cor:v2216-second-jet-transgression` | corollary | 3140–3153 | **VERIFIED-CONDITIONAL** | E1-IIID-B3-SOURCE-REPLAY, E3-IIID-B3-ACTION-CHAIN, E3-IIID-B3-TRANS-INTEGRAL |
| 87 | 3 | `p3d:def:v2218-finite-orbit-value` | definition | 3179–3197 | **FORMALIZED** | E1-IIID-B3-CLAUSE-READ |
| 88 | 3 | `p3d:prop:v2218-finite-orbit-contacts` | proposition | 3199–3226 | **VERIFIED** | E1-IIID-B3-SOURCE-REPLAY, E3-IIID-B3-PHI-FIRST-JET, E3-IIID-B3-PHI-SECOND-JET, E3-IIID-B3-PHI-COINCIDENCE, E3-IIID-B3-FINITE-REFLECTION |
| 89 | 3 | `p3d:prop:v2218-diagonal-cancellation` | proposition | 3243–3264 | **VERIFIED** | E1-IIID-B3-SOURCE-REPLAY, E3-IIID-B3-FINITE-THIRD-JET, E3-IIID-B3-FINITE-PHI-NONNEG, E3-IIID-B3-DIAGONAL-TANGENT |
| 90 | 3 | `p3d:def:v2218-fixed-momentum-candidate` | definition | 3284–3316 | **FORMALIZED** | E1-IIID-B3-CLAUSE-READ |
| 91 | 3 | `p3d:thm:v2218-fixed-candidate-endpoints` | theorem | 3340–3366 | **VERIFIED-CONDITIONAL** | E1-IIID-B3-SOURCE-REPLAY, E3-IIID-B3-CANDIDATE-CUBIC, E3-IIID-B3-FINITE-REFLECTION, E3-IIID-B3-UV-TRACE-BOUND, E4-IIID-B3-UV-RESTRICTION |
| 92 | 3 | `p3d:prop:v2218-finite-value-junction` | proposition | 3406–3426 | **VERIFIED-CONDITIONAL** | E1-IIID-B3-SOURCE-REPLAY, E3-IIID-B3-DRESS-JUMP |
| 93 | 3 | `p3d:rem:v2218-fixed-candidate-status` | remark | 3438–3454 | **FORMALIZED** | E1-IIID-B3-CLAUSE-READ |
| 94 | 3 | `p3d:rem:v229-actual-gravitational-incidence` | remark | 3552–3571 | **FORMALIZED** | E1-IIID-B3-CLAUSE-READ |
| 95 | 3 | `p3d:cor:v286-protected-grade-four-incidence-test` | corollary | 3576–3596 | **VERIFIED-CONDITIONAL** | E1-IIID-B3-SOURCE-REPLAY, E3-IIID-B3-GRADE4-GRAM, E4-IIID-B3-GRADE4 |
| 96 | 3 | `p3d:prop:v319-petersen-no-running` | proposition | 3617–3629 | **VERIFIED-CONDITIONAL** | E1-IIID-B3-SOURCE-REPLAY, E3-IIID-B3-GRADE4-GRAM, E3-IIID-B3-RG-DISCONNECT |
| 97 | 3 | `Paper3D:unnamed:remark:3638` | remark | 3638–3646 | **FORMALIZED** | E1-IIID-B3-CLAUSE-READ |
| 98 | 3 | `p3d:prop:v229-static-radius-test` | proposition | 3653–3660 | **VERIFIED-CONDITIONAL** | E1-IIID-B3-SOURCE-REPLAY, E3-IIID-B3-STATIC-OBSTRUCTION, E4-IIID-B3-REG-ROLE |

## Canonical scoped conditions — one first origin each

| Condition ID | Status and sort | Source first origin | Exact requirement |
|---|---|---|---|
| `BH-IIID-A-0001` | SOURCE-DECLARED / DOMAIN / G0-BOUNDARY | `p3:def:active-support-response`:494–531 | For a fixed protected-state conditioning use a nonzero orthogonal P∈End_R(A_prot), rank(P)=k∈{1,...,8}; a physical fixed P has its supported G0 occurrence/mark when not an invariant generated constituent. |
| `BH-IIID-A-0002` | CONDITIONAL / PHYSICAL-IDENTIFICATION | `p3:def:active-support-response`:524–531 | (UNIT): on a fixed physical support P, adopt the unique normalized conditioned regular trace state as the reduced scalar-response readout; no inverse-trace action law asserted. |
| `BH-IIID-A-0003` | CONDITIONAL / DOMAIN / RESPONSE-CLASS | `p3:def:reduced-response-branch`:843–886 | (RED): fixed common f, Λ, overall normalization, phase/ground projection, Spin(4)-equivariant shellwise coarse graining, one fixed Born product leaf ab=s_B²>0, positive scalar role outputs a,b. |
| `BH-IIID-A-0004` | CONDITIONAL / NORMALIZATION / OWNER-SCOPE | `p3d:thm:born-seven-depth-reflection`:1056–1080 | For the owner-placed physical response-root reflection, positive common U,C with U>C and α_σ>1; C/U=α_σ^{-7}, s_B²=UC and same-owner ancestry of generated determinant depth. |
| `BH-IIID-A-0005` | SOURCE-DECLARED / CALIBRATION / RED | `p3:def:uv-ir-calibration-pair`:1258–1276 | Two-root endpoint calibration: fixed reduced response owner, positive distinct roots 0<C<U and g_eff(C)=g_eff(U)=1; physical occurrence/scale choice separate from algebraic uniqueness. |
| `BH-IIID-A-0006` | CONDITIONAL / OWNER-PLACEMENT / RESPONSE | `p3d:cor:rank-character-laurent-family`:1479–1486 | Optional rank-character response placement of all designated C_j/U=alpha_sigma^-j on a single owner, alpha_sigma>1, j=1..7; no claim that every j is an actual nonzero spectral carrier. |
| `BH-IIID-A-0007` | CONDITIONAL / OPTIONAL-ROLE-COMPARISON | `p3d:thm:least-support-n2-dressing`:1778–1795 | Optional coefficient-role selector conditions D1 (turnover after inflation), D2 (freeze no later than K32), D3 (least support among complete admissible candidates), with 1/2<q_end<1. |
| `BH-IIID-A-0008` | CONDITIONAL / COEFFICIENT-ROLE-SELECTOR | `p3d:thm:v2219-carrier-four-dressing`:1835–1844 | First actual nonzero carrier in active protected spectrum is required as coefficient-source rank; this rule replaces optional D3 and consumes the generated III-C spectral grades {0,4,5,7}. |
| `BH-IIID-A-0009` | CONDITIONAL / METRIC-COMPARISON / CAP-ANCHOR | `p3d:prop:v223-curvature-clock`:2173–2201 | Optional metric curvature comparison R=R[g]>0, fixed positive upper anchor P, anchored REG0 L, declared cap anchors B_U,B_I and sigma=B_I R_s. |
| `BH-IIID-A-0010` | CONDITIONAL / ACTUAL-SOURCE-JET / CONDITION | `p3d:thm:v2211-excess-character-certificate`:2532–2565 | (EXJET_7): independently owned and evaluated C¹ local action-source excess with E_barR(barR)=Delta(barR), frozen w=1+n7(barR), and actual Ward defect W_barR(barR)=0 at a specified active barR>C. |
| `BH-IIID-A-0011` | CONDITIONAL / ACTUAL-SOURCE-INTERVAL / STRONGER CONDITION | `p3d:thm:v2211-excess-character-certificate`:2554–2565 | (EXCHAR_7): on the actual local positive source interval, W_barR(r)=0 throughout (not merely at barR), with fixed w and independently owned E_barR; stronger than EXJET_7. |
| `BH-IIID-A-0012` | CONDITIONAL / SOURCE-GRAM / PHYSICAL-NORMALIZATION | `p3d:thm:v2216-finite-born-second-jet`:3049–3052 | For a chosen finite invariant Born source word, the independently evaluated Gram/source incidence satisfies beta_R*kappa_R^2=4 Delta(R) in the actual local configuration chart; matching cannot be defined by retrofitting the proposed susceptibility. |
| `BH-IIID-A-0013` | SOURCE-DECLARED / DEFINED-CANDIDATE / BRANCH | `p3d:def:v2218-fixed-momentum-candidate`:3284–3316 | Fixed-momentum composed candidate branch: choose positive alpha>1 and U>C=U alpha^-7, Q=8sqrt(alpha) held constant across C≤R≤U, and choose the generated visibility norm k(R)*zeta(R)^2 as the finite invariant source section. |

**Non-equivalence:** `(EXCHAR_7)` at one background/source interval implies the local `(EXJET_7)` at that background, not conversely. `(RED)`, `(UNIT)`, `(FLAG)`, `(PQTI)` and physical source/action incidence are separately typed and are not imported as universal truths.

## Explicit source-consumed dependency and branch ledger

| Edge ID | Premise/source | Consuming claim | Kind | Exact use location |
|---|---|---|---|---|
| `BH-IIID-EDGE-B12-0001` | `p3:thm:rank-one-hopf-localization` | `p3:lem:rank-atom-hopf-trace-localization` | `IMPORTED_PROOF` | Paper3D:375-385 |
| `BH-IIID-EDGE-B12-0002` | `p3:thm:Vlog` | `p3:lem:primitive-hopf-cell-normalization` | `IMPORTED_PROOF` | Paper3D:418-426 |
| `BH-IIID-EDGE-B12-0003` | `p3:thm:D1-primitive-smooth-uniqueness` | `p3:lem:primitive-hopf-cell-normalization` | `IMPORTED_PROOF` | Paper3D:425-432 |
| `BH-IIID-EDGE-B12-0004` | `p3:lem:rank-atom-hopf-trace-localization` | `p3:lem:primitive-hopf-cell-normalization` | `PREMISE_OF` | Paper3D:416-419 |
| `BH-IIID-EDGE-B12-0005` | `p3:lem:rank-atom-hopf-trace-localization` | `p3:thm:reeb-universal` | `PREMISE_OF` | Paper3D:481-485 |
| `BH-IIID-EDGE-B12-0006` | `p3:thm:determinant-rank-character` | `p3:thm:reeb-universal` | `IMPORTED_PROOF` | Paper3D:482-488 |
| `BH-IIID-EDGE-B12-0007` | `p3c:thm:generated-dual-depth-hierarchy` | `p3:thm:reeb-universal` | `IMPORTED_PROOF` | Paper3D:484-488 |
| `BH-IIID-EDGE-B12-0008` | `p3:lem:unit-trace-forces-reciprocal-active-fraction` | `p3:thm:eight-mode-harmonic-response` | `PREMISE_OF` | Paper3D:608-614 |
| `BH-IIID-EDGE-B12-0009` | `p3:lem:unit-trace-forces-reciprocal-active-fraction` | `p3d:cor:generated-active-support-inheritance` | `PREMISE_OF` | Paper3D:617-636 |
| `BH-IIID-EDGE-B12-0010` | `p3:cor:derived-infrared-projector` | `p3d:cor:generated-active-support-inheritance` | `IMPORTED_PROOF` | Paper3D:617-636 |
| `BH-IIID-EDGE-B12-0011` | `p3:thm:reeb-universal` | `p3:prop:ordering-versus-step-size` | `PREMISE_OF` | Paper3D:722-729 |
| `BH-IIID-EDGE-B12-0012` | `p3:thm:hopf-decomposition` | `p3:thm:sequential` | `IMPORTED_PROOF` | Paper3D:771-782 |
| `BH-IIID-EDGE-B12-0013` | `p3:thm:reeb-universal` | `p3:thm:sequential` | `PREMISE_OF` | Paper3D:773-799 |
| `BH-IIID-EDGE-B12-0014` | `p3c:thm:generated-dual-depth-hierarchy` | `p3:thm:sequential` | `IMPORTED_PROOF` | Paper3D:734-808 |
| `BH-IIID-EDGE-B12-0015` | `p3b:def:sector-trace-born-state` | `p3:prop:one_parameter_reduction` | `IMPORTED_PROOF` | Paper3D:926-953 |
| `BH-IIID-EDGE-B12-0016` | `p3:prop:one_parameter_reduction` | `p3:lem:reduced-born-reciprocity` | `PREMISE_OF` | Paper3D:1004-1053 |
| `BH-IIID-EDGE-B12-0017` | `p3:def:reciprocal-quotient-coordinate` | `p3:lem:reduced-born-reciprocity` | `PREMISE_OF` | Paper3D:1004-1053 |
| `BH-IIID-EDGE-B12-0018` | `p2a:thm:generated-born-inheritance` | `p3:lem:reduced-born-reciprocity` | `IMPORTED_PROOF` | Paper3D:1005-1034 |
| `BH-IIID-EDGE-B12-0019` | `p3:lem:reduced-born-reciprocity` | `p3d:thm:born-seven-depth-reflection` | `PREMISE_OF` | Paper3D:1081-1091 |
| `BH-IIID-EDGE-B12-0020` | `p3d:thm:born-seven-depth-reflection` | `p3d:cor:born-operational-scale-inversion` | `PREMISE_OF` | Paper3D:1093-1128 |
| `BH-IIID-EDGE-B12-0021` | `p3b:def:sector-trace-born-state` | `p3:lem:spectral-trace-sector-valuation` | `IMPORTED_PROOF` | Paper3D:1186-1196 |
| `BH-IIID-EDGE-B12-0022` | `p3b:lem:equal-born-role-weights` | `p3:lem:spectral-trace-sector-valuation` | `IMPORTED_PROOF` | Paper3D:1197-1204 |
| `BH-IIID-EDGE-B12-0023` | `p3:def:visible-reciprocal-sector-weights` | `p3:lem:spectral-trace-sector-valuation` | `PREMISE_OF` | Paper3D:1172-1218 |
| `BH-IIID-EDGE-B12-0024` | `p3:lem:spectral-trace-sector-valuation` | `p3:def:scalar-response-readout-normalization` | `DEFINITION_DEPENDS` | Paper3D-RunningResponse-v1_159.tex:1237-1256 |
| `BH-IIID-EDGE-B12-0025` | `p3:def:visible-reciprocal-sector-weights` | `p3:thm:geff_from_reciprocity` | `PREMISE_OF` | Paper3D-RunningResponse-v1_159.tex:1306-1332 |
| `BH-IIID-EDGE-B12-0026` | `p3:lem:spectral-trace-sector-valuation` | `p3:thm:geff_from_reciprocity` | `PREMISE_OF` | Paper3D-RunningResponse-v1_159.tex:1306-1332 |
| `BH-IIID-EDGE-B12-0027` | `p3:def:scalar-response-readout-normalization` | `p3:thm:geff_from_reciprocity` | `PREMISE_OF` | Paper3D-RunningResponse-v1_159.tex:1306-1332 |
| `BH-IIID-EDGE-B12-0028` | `p3:def:uv-ir-calibration-pair` | `p3:thm:geff_from_reciprocity` | `CALIBRATION_PREMISE` | Paper3D-RunningResponse-v1_159.tex:1306-1332 |
| `BH-IIID-EDGE-B12-0029` | `p3:thm:geff_from_reciprocity` | `p3d:cor:primitive-unit-quadratic-response` | `PREMISE_OF` | Paper3D-RunningResponse-v1_159.tex:1354-1359 |
| `BH-IIID-EDGE-B12-0030` | `p3d:cor:primitive-unit-quadratic-response` | `p3d:cor:two-scale-response-normalizations` | `PREMISE_OF` | Paper3D-RunningResponse-v1_159.tex:1387-1392 |
| `BH-IIID-EDGE-B12-0031` | `p3:thm:geff_from_reciprocity` | `p3d:cor:born-euler-response-pair` | `PREMISE_OF` | Paper3D-RunningResponse-v1_159.tex:1415-1422 |
| `BH-IIID-EDGE-B12-0032` | `p1b:thm:born-euler-anticommutation` | `p3d:cor:born-euler-response-pair` | `IMPORTED_PROOF` | Paper3D-RunningResponse-v1_159.tex:1415-1422 |
| `BH-IIID-EDGE-B12-0033` | `p3:thm:geff_from_reciprocity` | `p3d:thm:minimal-born-laurent-characterization` | `CLAIM_IDENTIFICATION` | Paper3D-RunningResponse-v1_159.tex:1461-1477 |
| `BH-IIID-EDGE-B12-0034` | `p3d:thm:minimal-born-laurent-characterization` | `p3d:cor:rank-character-laurent-family` | `PREMISE_OF` | Paper3D-RunningResponse-v1_159.tex:1558-1573 |
| `BH-IIID-EDGE-B12-0035` | `p1b:thm:laurent-family` | `p3d:cor:rank-character-laurent-family` | `IMPORTED_PROOF` | Paper3D-RunningResponse-v1_159.tex:1558-1573 |
| `BH-IIID-EDGE-B12-0036` | `p3d:cor:rank-character-laurent-family` | `p3d:thm:v285-calibration-free-hierarchy-dip` | `PREMISE_OF` | Paper3D-RunningResponse-v1_159.tex:1615-1639 |
| `BH-IIID-EDGE-B12-0037` | `p3d:cor:rank-character-laurent-family` | `p3d:cor:born-midpoint-shell-coordinate` | `PREMISE_OF` | Paper3D-RunningResponse-v1_159.tex:1684-1696 |
| `BH-IIID-EDGE-B12-0038` | `p3d:cor:rank-character-laurent-family` | `p3d:thm:canonical-nonnegative-laurent-projection` | `PREMISE_OF` | Paper3D-RunningResponse-v1_159.tex:1756-1776 |
| `BH-IIID-EDGE-B12-0039` | `p1b:thm:laurent-family` | `p3d:thm:canonical-nonnegative-laurent-projection` | `IMPORTED_PROOF` | Paper3D-RunningResponse-v1_159.tex:1756-1776 |
| `BH-IIID-EDGE-B12-0040` | `p3d:thm:canonical-nonnegative-laurent-projection` | `p3d:thm:least-support-n2-dressing` | `PREMISE_OF-POSITIVEPART-ONLY` | Paper3D-RunningResponse-v1_159.tex:1810-1822 |
| `BH-IIID-EDGE-B12-0041` | `p3d:cor:rank-character-laurent-family` | `p3d:thm:least-support-n2-dressing` | `PREMISE_OF` | Paper3D-RunningResponse-v1_159.tex:1810-1822 |
| `BH-IIID-EDGE-B12-0042` | `p3c:prop:v2219-first-actual-carrier` | `p3d:thm:v2219-carrier-four-dressing` | `IMPORTED_PROOF` | Paper3D-RunningResponse-v1_159.tex:1856-1863 |
| `BH-IIID-EDGE-B12-0043` | `p3d:cor:rank-character-laurent-family` | `p3d:thm:v2219-carrier-four-dressing` | `PREMISE_OF-RANK-MIDPOINT` | Paper3D-RunningResponse-v1_159.tex:1856-1863 |
| `BH-IIID-EDGE-B12-0044` | `p3:thm:geff_from_reciprocity` | `p3:cor:fully_derived_one_parameter_trajectory` | `PREMISE_OF` | Paper3D-RunningResponse-v1_159.tex:1935-1961 |
| `BH-IIID-EDGE-B12-0045` | `p3:lem:reduced-born-reciprocity` | `p3:cor:fully_derived_one_parameter_trajectory` | `PREMISE_OF` | Paper3D-RunningResponse-v1_159.tex:1935-1961 |
| `BH-IIID-EDGE-B12-0046` | `p3:thm:geff_from_reciprocity` | `p3:thm:exact-reciprocal-freeze-interface` | `PREMISE_OF` | Paper3D-RunningResponse-v1_159.tex:2023-2026 |
| `BH-IIID-EDGE-B12-0047` | `p3d:thm:born-seven-depth-reflection` | `p3d:thm:v222-born-phase-conjugation` | `PREMISE_OF` | Paper3D-RunningResponse-v1_159.tex:2078-2091 |
| `BH-IIID-EDGE-B12-0048` | `p3c:thm:v222-rank-character-unitary-companion` | `p3d:thm:v222-born-phase-conjugation` | `IMPORTED_PROOF` | Paper3D-RunningResponse-v1_159.tex:2078-2091 |
| `BH-IIID-EDGE-B12-0049` | `p3d:thm:born-seven-depth-reflection` | `p3d:thm:v222-primitive-phase-twist` | `PREMISE_OF` | Paper3D-RunningResponse-v1_159.tex:2130-2149 |
| `BH-IIID-EDGE-B12-0050` | `p3:thm:geff_from_reciprocity` | `p3:thm:riccati` | `PREMISE_OF` | Paper3D-RunningResponse-v1_159.tex:2329-2336 |
| `BH-IIID-EDGE-B12-0051` | `p1b:thm:laurent-family` | `p3:thm:riccati` | `IMPORTED_PROOF` | Paper3D-RunningResponse-v1_159.tex:2329-2336 |
| `BH-IIID-EDGE-B12-0052` | `p3:thm:geff_from_reciprocity` | `p3:prop:n_closed` | `PREMISE_OF` | Paper3D-RunningResponse-v1_159.tex:2355-2360 |
| `BH-IIID-EDGE-B12-0053` | `p1b:thm:laurent-family` | `p3:prop:n_closed` | `IMPORTED_PROOF` | Paper3D-RunningResponse-v1_159.tex:2355-2360 |
| `BH-IIID-EDGE-B12-0054` | `p3:prop:n_closed` | `p3:def:active-reduced-window` | `PREMISE_OF` | Paper3D-RunningResponse-v1_159.tex:2373-2379 |
| `BH-IIID-EDGE-B12-0055` | `p1b:thm:laurent-family` | `p3:def:active-reduced-window` | `IMPORTED_PROOF` | Paper3D-RunningResponse-v1_159.tex:2373-2379 |
| `BH-IIID-EDGE-B12-0056` | `p3:def:active-reduced-window` | `p3:thm:exact-calibrated-secant-range` | `PREMISE_OF` | Paper3D-RunningResponse-v1_159.tex:2404-2412 |
| `BH-IIID-EDGE-B12-0057` | `p1b:thm:laurent-family` | `p3:thm:exact-calibrated-secant-range` | `IMPORTED_PROOF` | Paper3D-RunningResponse-v1_159.tex:2404-2412 |
| `BH-IIID-EDGE-B12-0058` | `p1b:prop:trace-coordinate` | `p3:def:neutral-visibility-readout` | `IMPORTED_CONSTRUCTOR` | Paper3D-RunningResponse-v1_159.tex:2414-2439 |
| `BH-IIID-EDGE-B12-0059` | `p3c:cor:corealized-protected-visibility-family` | `p3:def:neutral-visibility-readout` | `IMPORTED_OCCURRENCE` | Paper3D-RunningResponse-v1_159.tex:2414-2439 |
| `BH-IIID-EDGE-B12-0060` | `p3:def:neutral-visibility-readout` | `p3:thm:basis-neutral-entropy-lift` | `PREMISE_OF` | Paper3D-RunningResponse-v1_159.tex:2479-2500 |
| `BH-IIID-EDGE-B12-0061` | `p3:thm:exact-calibrated-secant-range` | `p3:thm:basis-neutral-entropy-lift` | `PREMISE_OF` | Paper3D-RunningResponse-v1_159.tex:2479-2500 |
| `BH-IIID-EDGE-B12-0062` | `p3c:cor:corealized-protected-visibility-family` | `p3:thm:basis-neutral-entropy-lift` | `IMPORTED_OWNER` | Paper3D-RunningResponse-v1_159.tex:2479-2500 |
| `BH-IIID-EDGE-0001` | `p3d:thm:v2211-excess-character-certificate` | `p3d:thm:v173-fixed-depth-laurent-excess-jet` | `PREMISE_OF` | Paper3D-RunningResponse-v1_159.tex:2593-2632 |
| `BH-IIID-EDGE-0002` | `BH-IIID-A-0010` | `p3d:thm:v173-fixed-depth-laurent-excess-jet` | `REQUIRES` | Paper3D-RunningResponse-v1_159.tex:2593-2632 |
| `BH-IIID-EDGE-0003` | `BH-IIID-A-0011` | `p3d:thm:v173-fixed-depth-laurent-excess-jet` | `SCOPE_GUARD` | Paper3D-RunningResponse-v1_159.tex:2593-2632 |
| `BH-IIID-EDGE-0004` | `p3d:thm:v2211-excess-character-certificate` | `p3d:prop:v2211-excess-jet-counterfamily` | `DEFINITIONAL_CONTEXT` | Paper3D-RunningResponse-v1_159.tex:2655-2661 |
| `BH-IIID-EDGE-0005` | `p3d:thm:v2211-excess-character-certificate` | `p3d:thm:v2216-exjet-global-obstruction` | `DEFINITIONAL_CONTEXT` | Paper3D-RunningResponse-v1_159.tex:2797-2809 |
| `BH-IIID-EDGE-0006` | `p3:thm:exact-calibrated-secant-range` | `p3d:thm:v2216-exjet-global-obstruction` | `PREMISE_OF` | Paper3D-RunningResponse-v1_159.tex:2797-2809 |
| `BH-IIID-EDGE-0007` | `p3d:thm:v2216-exjet-global-obstruction` | `p3d:cor:v2216-raw-euler-nongluing` | `PREMISE_OF` | Paper3D-RunningResponse-v1_159.tex:2819-2823 |
| `BH-IIID-EDGE-0008` | `p1b:thm:v226-dual-coefficients` | `p3d:prop:v226-response-coefficients` | `IMPORTED_PROOF` | Paper3D-RunningResponse-v1_159.tex:2840-2844 |
| `BH-IIID-EDGE-0009` | `p1b:cor:v226-source-jets` | `p3d:prop:v226-response-coefficients` | `IMPORTED_PROOF` | Paper3D-RunningResponse-v1_159.tex:2840-2844 |
| `BH-IIID-EDGE-0010` | `p1b:cor:v227-response-jets` | `p3d:cor:v227-running-frequency` | `IMPORTED_PROOF` | Paper3D-RunningResponse-v1_159.tex:2864-2867 |
| `BH-IIID-EDGE-0011` | `p3:prop:n_closed` | `p3d:thm:v2216-positive-born-provider` | `PREMISE_OF` | Paper3D-RunningResponse-v1_159.tex:2933-2969 |
| `BH-IIID-EDGE-0012` | `p3d:thm:v2216-positive-born-provider` | `p3d:cor:v2216-born-positive-approximation` | `PREMISE_OF` | Paper3D-RunningResponse-v1_159.tex:2989-2997 |
| `BH-IIID-EDGE-0013` | `p3:prop:n_closed` | `p3d:thm:v2216-finite-born-second-jet` | `PREMISE_OF` | Paper3D-RunningResponse-v1_159.tex:3054-3076 |
| `BH-IIID-EDGE-0014` | `p3d:thm:v2216-finite-born-second-jet` | `p3d:prop:v2216-finite-born-limits` | `PREMISE_OF` | Paper3D-RunningResponse-v1_159.tex:3100-3121 |
| `BH-IIID-EDGE-0015` | `p3d:thm:v2216-exjet-global-obstruction` | `p3d:cor:v2216-second-jet-transgression` | `PREMISE_OF` | Paper3D-RunningResponse-v1_159.tex:3154-3161 |
| `BH-IIID-EDGE-0016` | `p3d:prop:v2216-finite-born-limits` | `p3d:cor:v2216-second-jet-transgression` | `PREMISE_OF` | Paper3D-RunningResponse-v1_159.tex:3154-3161 |
| `BH-IIID-EDGE-0017` | `p3d:thm:v2216-finite-born-second-jet` | `p3d:def:v2218-finite-orbit-value` | `DEFINITIONAL_CONTEXT` | Paper3D-RunningResponse-v1_159.tex:3179-3197 |
| `BH-IIID-EDGE-0018` | `p3d:def:v2218-finite-orbit-value` | `p3d:prop:v2218-finite-orbit-contacts` | `PREMISE_OF` | Paper3D-RunningResponse-v1_159.tex:3227-3241 |
| `BH-IIID-EDGE-0019` | `p3d:thm:v2216-finite-born-second-jet` | `p3d:prop:v2218-diagonal-cancellation` | `PREMISE_OF` | Paper3D-RunningResponse-v1_159.tex:3265-3276 |
| `BH-IIID-EDGE-0020` | `p3d:def:v2218-finite-orbit-value` | `p3d:def:v2218-fixed-momentum-candidate` | `DEFINITIONAL_CONTEXT` | Paper3D-RunningResponse-v1_159.tex:3284-3316 |
| `BH-IIID-EDGE-0021` | `BH-IIID-A-0013` | `p3d:thm:v2218-fixed-candidate-endpoints` | `SCOPE_GUARD` | Paper3D-RunningResponse-v1_159.tex:3367-3395 |
| `BH-IIID-EDGE-0022` | `p3d:def:v2218-fixed-momentum-candidate` | `p3d:thm:v2218-fixed-candidate-endpoints` | `PREMISE_OF` | Paper3D-RunningResponse-v1_159.tex:3367-3395 |
| `BH-IIID-EDGE-0023` | `p3d:prop:v2218-finite-orbit-contacts` | `p3d:thm:v2218-fixed-candidate-endpoints` | `PREMISE_OF` | Paper3D-RunningResponse-v1_159.tex:3367-3395 |
| `BH-IIID-EDGE-0024` | `p3d:def:v2218-fixed-momentum-candidate` | `p3d:prop:v2218-finite-value-junction` | `PREMISE_OF` | Paper3D-RunningResponse-v1_159.tex:3427-3436 |
| `BH-IIID-EDGE-0025` | `p3d:cor:rank-character-laurent-family` | `p3d:prop:v2218-finite-value-junction` | `PREMISE_OF-POSITIVEPART_ONLY` | Paper3D-RunningResponse-v1_159.tex:3427-3436 |
| `BH-IIID-EDGE-0026` | `p3c:prop:v2219-first-actual-carrier` | `p3d:cor:v286-protected-grade-four-incidence-test` | `IMPORTED_PROOF` | Paper3D-RunningResponse-v1_159.tex:3598-3608 |
| `BH-IIID-EDGE-0027` | `p3b:thm:v286-finite-heat-incidence-gram` | `p3d:cor:v286-protected-grade-four-incidence-test` | `IMPORTED_PROOF` | Paper3D-RunningResponse-v1_159.tex:3598-3608 |
| `BH-IIID-EDGE-0028` | `p3b:prop:v286-heat-incidence-contact-obstruction` | `p3d:cor:v286-protected-grade-four-incidence-test` | `IMPORTED_PROOF` | Paper3D-RunningResponse-v1_159.tex:3598-3608 |
| `BH-IIID-EDGE-0029` | `p2a:def:v229-action-incidence-certificate` | `p3d:cor:v286-protected-grade-four-incidence-test` | `IMPORTED_PROOF` | Paper3D-RunningResponse-v1_159.tex:3598-3608 |
| `BH-IIID-EDGE-0030` | `BH-IIIB-A-0009` | `p3d:cor:v286-protected-grade-four-incidence-test` | `REQUIRES` | Paper3D-RunningResponse-v1_159.tex:3598-3608 |
| `BH-IIID-EDGE-0031` | `p3b:thm:v319-petersen-moment-six` | `p3d:prop:v319-petersen-no-running` | `IMPORTED_PROOF` | Paper3D-RunningResponse-v1_159.tex:3630-3637 |
| `BH-IIID-EDGE-0032` | `p1b:thm:v229-coupled-homothety` | `p3d:prop:v229-static-radius-test` | `IMPORTED_PROOF` | Paper3D-RunningResponse-v1_159.tex:3661-3664 |
| `BH-IIID-EDGE-0033` | `BH-IIID-A-0012` | `p3d:thm:v2216-finite-born-second-jet` | `NORMALIZATION_CHOICE` | Paper3D-RunningResponse-v1_159.tex:3054-3076 |
| `BH-IIID-EDGE-0034` | `BH-IIID-A-0003` | `p3d:thm:v2216-exjet-global-obstruction` | `SCOPE_GUARD` | Paper3D-RunningResponse-v1_159.tex:2797-2809 |
| `BH-IIID-EDGE-0035` | `BH-IIID-A-0013` | `p3d:prop:v2218-finite-value-junction` | `SCOPE_GUARD` | Paper3D-RunningResponse-v1_159.tex:3427-3436 |

## E1 proof replay register

| Proof replay ID | Claim | Proof lines | Result |
|---|---|---|---|
| `E1-IIID-B1-001` | `p3:lem:rank-atom-hopf-trace-localization` | 375–387 | REPRODUCED_WITH_DECLARED_SCOPE |
| `E1-IIID-B1-002` | `p3:lem:primitive-hopf-cell-normalization` | 412–435 | REPRODUCED_WITH_DECLARED_SCOPE |
| `E1-IIID-B1-003` | `p3:thm:reeb-universal` | 481–492 | REPRODUCED_WITH_DECLARED_SCOPE |
| `E1-IIID-B1-004` | `p3:lem:unit-trace-forces-reciprocal-active-fraction` | 550–587 | REPRODUCED_WITH_DECLARED_SCOPE |
| `E1-IIID-B1-005` | `p3:thm:eight-mode-harmonic-response` | 608–615 | REPRODUCED_WITH_DECLARED_SCOPE |
| `E1-IIID-B1-006` | `p3d:cor:generated-active-support-inheritance` | 617–640 | REPRODUCED_WITH_DECLARED_SCOPE |
| `E1-IIID-B1-007` | `p3d:cor:unit-boundary-normal-form` | 683–694 | REPRODUCED_WITH_DECLARED_SCOPE |
| `E1-IIID-B1-008` | `p3:prop:ordering-versus-step-size` | 722–729 | REPRODUCED_WITH_DECLARED_SCOPE |
| `E1-IIID-B1-009` | `p3:thm:sequential` | 771–808 | REPRODUCED_WITH_DECLARED_SCOPE |
| `E1-IIID-B1-010` | `p3:prop:one_parameter_reduction` | 923–964 | REPRODUCED_WITH_DECLARED_SCOPE |
| `E1-IIID-B1-011` | `p3:lem:reduced-born-reciprocity` | 1029–1054 | REPRODUCED_WITH_DECLARED_SCOPE |
| `E1-IIID-B1-012` | `p3d:thm:born-seven-depth-reflection` | 1081–1091 | REPRODUCED_WITH_DECLARED_SCOPE |
| `E1-IIID-B1-013` | `p3d:cor:born-operational-scale-inversion` | 1119–1127 | REPRODUCED_WITH_DECLARED_SCOPE |
| `E1-IIID-B1-014` | `p3:lem:spectral-trace-sector-valuation` | 1186–1219 | REPRODUCED_WITH_DECLARED_SCOPE |
| `E1-IIID-B2-001` | `p3:thm:geff_from_reciprocity` | 1306–1332 | VERIFIED-CONDITIONAL |
| `E1-IIID-B2-002` | `p3d:cor:primitive-unit-quadratic-response` | 1354–1359 | VERIFIED-CONDITIONAL |
| `E1-IIID-B2-003` | `p3d:cor:two-scale-response-normalizations` | 1387–1392 | VERIFIED-CONDITIONAL |
| `E1-IIID-B2-004` | `p3d:cor:born-euler-response-pair` | 1415–1422 | VERIFIED-CONDITIONAL |
| `E1-IIID-B2-005` | `p3d:thm:minimal-born-laurent-characterization` | 1461–1477 | VERIFIED |
| `E1-IIID-B2-006` | `p3d:cor:rank-character-laurent-family` | 1558–1573 | VERIFIED-CONDITIONAL |
| `E1-IIID-B2-007` | `p3d:thm:v285-calibration-free-hierarchy-dip` | 1615–1639 | VERIFIED-CONDITIONAL |
| `E1-IIID-B2-008` | `p3d:cor:born-midpoint-shell-coordinate` | 1684–1696 | VERIFIED-CONDITIONAL |
| `E1-IIID-B2-009` | `p3d:thm:canonical-nonnegative-laurent-projection` | 1756–1776 | UNRESOLVED |
| `E1-IIID-B2-010` | `p3d:thm:least-support-n2-dressing` | 1810–1822 | VERIFIED-CONDITIONAL |
| `E1-IIID-B2-011` | `p3d:thm:v2219-carrier-four-dressing` | 1856–1863 | UNRESOLVED |
| `E1-IIID-B2-012` | `p3:cor:fully_derived_one_parameter_trajectory` | 1935–1961 | VERIFIED-CONDITIONAL |
| `E1-IIID-B2-013` | `p3:thm:exact-reciprocal-freeze-interface` | 2023–2026 | VERIFIED-CONDITIONAL |
| `E1-IIID-B2-014` | `p3d:thm:v222-born-phase-conjugation` | 2078–2091 | VERIFIED-CONDITIONAL |
| `E1-IIID-B2-015` | `p3d:thm:v222-primitive-phase-twist` | 2130–2149 | VERIFIED-CONDITIONAL |
| `E1-IIID-B2-016` | `p3d:prop:v223-curvature-clock` | 2202–2206 | VERIFIED-CONDITIONAL |
| `E1-IIID-B2-017` | `p3:thm:riccati` | 2329–2336 | VERIFIED-CONDITIONAL |
| `E1-IIID-B2-018` | `p3:prop:n_closed` | 2355–2360 | VERIFIED-CONDITIONAL |
| `E1-IIID-B2-019` | `p3:def:active-reduced-window` | 2373–2379 | VERIFIED-CONDITIONAL |
| `E1-IIID-B2-020` | `p3:thm:exact-calibrated-secant-range` | 2404–2412 | VERIFIED-CONDITIONAL |
| `E1-IIID-B2-021` | `p3:thm:basis-neutral-entropy-lift` | 2479–2500 | VERIFIED-CONDITIONAL |
| `E1-IIID-B3-001` | `p3d:thm:v2211-excess-character-certificate` | 2578–2589 | VERIFIED-CONDITIONAL |
| `E1-IIID-B3-002` | `p3d:thm:v173-fixed-depth-laurent-excess-jet` | 2624–2632 | VERIFIED-CONDITIONAL |
| `E1-IIID-B3-003` | `p3d:prop:v2211-excess-jet-counterfamily` | 2655–2661 | VERIFIED |
| `E1-IIID-B3-004` | `p3d:thm:v2216-complete-action-jets` | 2724–2733 | VERIFIED |
| `E1-IIID-B3-005` | `p3d:thm:v2216-exjet-global-obstruction` | 2797–2809 | VERIFIED |
| `E1-IIID-B3-006` | `p3d:cor:v2216-raw-euler-nongluing` | 2819–2823 | VERIFIED-CONDITIONAL |
| `E1-IIID-B3-007` | `p3d:prop:v226-response-coefficients` | 2840–2844 | VERIFIED-CONDITIONAL |
| `E1-IIID-B3-008` | `p3d:cor:v227-running-frequency` | 2864–2867 | VERIFIED-CONDITIONAL |
| `E1-IIID-B3-009` | `p3d:thm:v2216-positive-born-provider` | 2933–2969 | VERIFIED |
| `E1-IIID-B3-010` | `p3d:cor:v2216-born-positive-approximation` | 2989–2997 | VERIFIED |
| `E1-IIID-B3-011` | `p3d:thm:v2216-finite-born-second-jet` | 3054–3076 | VERIFIED |
| `E1-IIID-B3-012` | `p3d:prop:v2216-finite-born-limits` | 3100–3121 | VERIFIED |
| `E1-IIID-B3-013` | `p3d:cor:v2216-second-jet-transgression` | 3154–3161 | VERIFIED-CONDITIONAL |
| `E1-IIID-B3-014` | `p3d:prop:v2218-finite-orbit-contacts` | 3227–3241 | VERIFIED |
| `E1-IIID-B3-015` | `p3d:prop:v2218-diagonal-cancellation` | 3265–3276 | VERIFIED |
| `E1-IIID-B3-016` | `p3d:thm:v2218-fixed-candidate-endpoints` | 3367–3395 | VERIFIED-CONDITIONAL |
| `E1-IIID-B3-017` | `p3d:prop:v2218-finite-value-junction` | 3427–3436 | VERIFIED-CONDITIONAL |
| `E1-IIID-B3-018` | `p3d:cor:v286-protected-grade-four-incidence-test` | 3597–3608 | VERIFIED-CONDITIONAL |
| `E1-IIID-B3-019` | `p3d:prop:v319-petersen-no-running` | 3630–3637 | VERIFIED-CONDITIONAL |
| `E1-IIID-B3-020` | `p3d:prop:v229-static-radius-test` | 3661–3664 | VERIFIED-CONDITIONAL |

## Independent checks (verbatim outcomes from check ledgers)

### `Paper3D-ExactChecks-v1_1.json` — 10 recorded source controls

- `E3-HOPF-C2`: 4*pi**2
- `E3-MULT-CHAR`: diagonalize arbitrary multiplicity basis; residue trace becomes r independent copies
- `E3-TRACE-DENSITY`: exact matrix-unit basis test for all 64 independent observables in End_R(R^8), at each tested rank; nontrivial orthogonal conjugates
- `E4-STATE-NONLINEAR`: support density is not additive; theorem explicitly does not claim otherwise
- `E3-CLOCK-DEPTH`: 
- `E3-SCHEME-SIGN`: 
- `E3-BORN-REFLECTION`: log coordinate bijection and exact exponential identities; alpha>1
- `E3-ROLE-TRACE`: independent diagonal trace on unequal 5/15-dimensional matrices followed by Born-unmarked label scalarizer
- `E4-SCOPE-TESTS`: [{'test': 'scheme below positive threshold', 'witness': 'sigma = critical-1', 'outcome': 'dual ratio increases; theorem trichotomy explicitly permits it'}, {'test': 'alpha=1 in reflection proof', 'witness': 'log_alpha=0', 'outcome': 'all depths same response; unique midpoint requires alpha>1 as explicitly assumed'}, {'test': 'moving product leaf', 'witness': 'a=exp(t), b=exp(2t), ab variable', 'outcome': 'one-coordinate fixed-product claim inapplicable; RED excludes it'}, {'test': 'unmarked rank-three projector', 'witness': 'Pi3(u) with u not specified', 'outcome': 'particular P not selected; generated orbit only, as theorem states'}, {'test': 'non-Born-invariant label scalarizer', 'witness': 'lambda(e_x)=1/3, lambda(e_p)=2/3', 'outcome': 'fails inherited Born-unmarked owner premise; not a counterexample'}, {'test': 'semigroup tau versus depth q', 'witness': 'q_sp(1)=7(1-exp(-1)) != 1', 'outcome': 'upstream III-C deptharg issue; III-D uses explicit q coordinate, no automatic promotion'}]
- `E3-HARMONIC-REM`: 
### `Paper3D-Batch02ExactChecks-v1_1.json` — 15 recorded source controls

- `E3-IIID-B2-ROOT-CAL`: UV/IR rank-two linear system and full kappa>0 gauge cancellation
- `E3-IIID-B2-LAUR-UNIQUE`: Coefficient comparison in Laurent basis with explicit constant-no-EH condition
- `E3-IIID-B2-EULER`: Affine and quadratic identities: constant B retained
- `E3-IIID-B2-DIP`: Unique minimum and m^2+v^2=1, Born-exchanged endpoint slopes
- `E3-IIID-B2-TRACE-JUNC`: Distributional Hessian valid for two-piece junction F=C on r<C, Hact on r>C; NOT valid for globally constant hat-H=C
- `E3-IIID-B2-DRESS`: D3 selects j=2 while actual carrier rule selects j=4; separate predicates do not conflict
- `E3-IIID-B2-PHASE`: Completed phase conjugation and primitive twist directly verified with integer-depth phase quotient
- `E3-IIID-B2-CAP`: Direct mp 190-digit endpoint ratio and positive nonzero cap errors
- `E3-IIID-B2-SECANT`: High precision independent logarithmic secant and strict convexity domain sampling
- `E3-IIID-B2-ENTROPY`: Multiplicity-one-plus-seven state entropy and derivative; endpoint τ=∞
- `E4-IIID-B2-JUNC-LITERAL`: 
- `E4-IIID-B2-QSIG`: 
- `E4-IIID-B2-ROLE`: 
- `E4-IIID-B2-ENTROPY`: 
- `E4-IIID-B2-REG`: 
### `Paper3D-Batch03ExactChecks-v1_1.json` — 31/31 recorded passes

- `E3-IIID-B3-EXCESS-ODE` **E3**: actual local frozen excess W(r)=rE'-wE; EA=0 and EB=wC
- `E3-IIID-B3-EXCESS-JET` **E3**: two same diagonal-value germs yield different local susceptibilities
- `E3-IIID-B3-LOCAL-JET-BOUND` **E3**: positive branch bounded strictly below 2/(U+C)
- `E3-IIID-B3-LOCAL-JET-END` **E3**: terminal χ(C+δ)/δ→2/[C(U+C)]
- `E3-IIID-B3-EXJET-GLOBAL` **E3**: Egl integral strictly 0<Egl<Delta; Wglob=w(Delta-Egl)>0 for R>C, with terminal E(C)=0
- `E3-IIID-B3-ACTION-CHAIN` **E3**: full second derivative includes A_rr,2A_rb b', A_bb(b')², A_b b''
- `E3-IIID-B3-DIAG-TWOJET` **E3**: diagonal a'-p, p'-k, a''-k equations independently checked
- `E3-IIID-B3-MEASURE-MASS` **E3**: inversion density integrates to 1 (mass=1.0)
- `E3-IIID-B3-MEASURE-POS` **E3**: density strictly positive on both sides of s=b
- `E3-IIID-B3-MEASURE-ATOMFREE` **E3**: zero/zero at x=a removable
- `E3-IIID-B3-MEASURE-RESOLVENT` **E3**: five quadrature x values reproduce F_B from positive atom-free density within 3e-24 relative
- `E3-IIID-B3-MEASURE-TERMINAL` **E3**: F_B(C²)=1/2 and weighted inverse mass 1/(2 C²)
- `E3-IIID-B3-MEASURE-INFINMOM` **E3**: density tail ~ log(1+b/a)/[s log²(s/a)]; first moment diverges
- `E3-IIID-B3-SCHUR-MIN` **E3**: explicit stationary shift reduces quadratic form to χ(R)H²/2 including Q_C=0
- `E3-IIID-B3-FINITE-SLOPE` **E3**: 5-cell positive harmonic-node discretization preserves total mass and χ'(C) exactly
- `E3-IIID-B3-FINITE-PHI-NONNEG` **E3**: finite 2×2 spectral trace phi≥0, zero at y=0 across s
- `E3-IIID-B3-FINITE-REFLECTION` **E3**: exact Phi(-a,y)=y/8 from Ψ(x)+Ψ(-x)=x²
- `E3-IIID-B3-PHI-FIRST-JET` **E3**: Phi_y(s,0)=(Psi'(s)-Psi'(a))/(8(s-a)), including removable s=a
- `E3-IIID-B3-PHI-SECOND-JET` **E3**: Phi_yy(s,0) checked by independent spectral derivative vs divided-difference expression
- `E3-IIID-B3-PHI-COINCIDENCE` **E3**: eigenvalue-coincidence limit Phi_yy(a,0)=fourth derivative of Psi(a)/48
- `E3-IIID-B3-FINITE-THIRD-JET` **E3**: finite frozen second and third curvature jets independently differentiated
- `E3-IIID-B3-CANDIDATE-CUBIC` **E3**: finite candidate terminal cubic coefficient Q/[H² C (U+C)] confirmed at three decreasing positive increments
- `E3-IIID-B3-DRESS-JUMP` **E3**: finite differenced jump 0.1049020311 vs exact 0.1049013585
- `E3-IIID-B3-GRADE4-GRAM` **E3**: positive Schur complement iff B outside interior span, zero on B=C
- `E3-IIID-B3-STATIC-OBSTRUCTION` **E3**: R=R0(1+(R/Rs)^2) is a nonzero quadratic, cannot hold on interval
- `E4-IIID-B3-E4-LOCAL-GLOBAL` **E4**: positive frozen EXCHAR not same global action: endpoint zero forces global ODE trivial; no contradiction with local germ
- `E4-IIID-B3-E4-NOT-ACTION` **E4**: finite source/Schur realization is mathematical unless field action, metric-source incidence, density and physical norm separately shown
- `E4-IIID-B3-E4-NEUTRAL-SOURCE` **E4**: native source 8-channel real trace ≠ automatically physical ordinary finite-Hilbert trace; no type promotion
- `E4-IIID-B3-E4-GRADE4` **E4**: positive P4 or Gram positive before elimination does not imply nonzero actual metric Hessian; B4 may vanish or lie in C span
- `E4-IIID-B3-E4-UV-RESTRICTION` **E4**: upper finite-value estimate applies only on bands with pair spectral lower bound, not global slow-roll Hessian
- `E4-IIID-B3-E4-REG-ROLE` **E4**: homothety static-radius contradiction does not apply FLRW or auxiliary round factor

### Additional manual source-separated controls

- `E3-IIID-B3-TOMOGRAPHY-DUAL` E3 **PASS**: Using Tr(I)=15, Tr(Bi)=0, Tr(BiBj)=1 if i=j and -1/136 otherwise, Tr(Ei Dj)=[1+136 Tr(BiBj)]/137=delta_ij, hence derivative reconstruction in the common native algebra.
- `E3-IIID-B3-ENERGY-SAMPLES` E3 **PASS**: At k-th source derivative, common-denominator degree ≤(k+1)(m1+m2); Hermitian reality pairs every upper-half-plane zero with its lower-half-plane conjugate. More than half the degree distinct upper-plane zeros forces identically zero numerator.
- `E3-IIID-B3-TRANS-INTEGRAL` E3 **PASS**: F(R)=R-C+integral_C^R (R-t)K(t)dt satisfies F(C)=0, F'(C)=1 and F''(R)=K(R); difference of two primitives affine and vanishes by two endpoint conditions.
- `E3-IIID-B3-RG-DISCONNECT` E3 **PASS**: For a fixed finite matrix M, ∂_{log μ} eig(M)=0 absent an actually supplied μ-dependent insertion. The referenced III-B theorem supplies M2 and M4 isotropy and first sextic anisotropy on the 10-axis orbit, not a running coupling.
- `E3-IIID-B3-FROZEN-GLOBAL-SIGN` E3 **PASS**: For R>C, strict convexity of log cosh gives n_R>0 and χ'_7(R)>0; the frozen logarithmic germ gives f_R'''(R)=-3χ_7(R)/R<0. No single C³ function with Hessian χ_7 matches all these third jets.
- `E3-IIID-B3-DIAGONAL-TANGENT` E3 **PASS**: F_b(0)=D_vF_b(0)=0 identically; at b=r the Hessian is K_loc(b) ∇log(r/b)⊗∇log(r/b)=K_loc [[1,-1],[-1,1]], whose diagonal pullback is zero.
- `E3-IIID-B3-UV-TRACE-BOUND` E3 **PASS**: On λ_min(M+J)≥m0, 2(1-δ)≤Ψ''≤2. The trace Hessian of an off-diagonal J with Tr(J²)=2y bounds the complete value between (1-δ)βy/4 and βy/4; this is a value bound only.

## Cross-paper exact consumed clauses

- `p1b:thm:laurent-family` at `Paper1C-TechnicalMaterial-v1_58.tex:20624-20675`: scope-matched Laurent/secant theorem independently replayed.
- `p1b:thm:born-euler-anticommutation` at `Paper1C-TechnicalMaterial-v1_58.tex:20698-20741`: Euler pair verified.
- `p3c:prop:v2219-first-actual-carrier` at `Paper3C-ProtectedHierarchy-v1_179.tex:354-372`: grade 4 actual proved upstream; role-incidence remains separate.
- `p3c:thm:v222-rank-character-unitary-companion` at `Paper3C-ProtectedHierarchy-v1_179.tex:4739-4795`: character period/winding as mathematical interpolation, not physical phase law.
- `p3c:cor:corealized-protected-visibility-family` at `Paper3C-ProtectedHierarchy-v1_179.tex:3326-3355`: NEUT7 is generated on co-realized parent; no new occurrence tag.
- `p1b:prop:trace-coordinate` at `Paper1B-M8Geometry-v1_131.tex:6080-6102`: 1+7 common-rate semigroup mathematical owner.
- `p3e:eq:laur17-Q` at `Paper3G-TechnicalMaterial-v1_47.tex:4938-4944`: Q_sigma fixed there on PQTI only; not imported in III-D coefficient clause.
- `p3f:thm:v263-laurent-coefficient-character` at `Paper3F-CompleteDynamics-v1_256.tex:14857-14907`: full coefficient character derived later on its own owner; cannot silently retroactively count as III-D premise.
- `p1b:thm:v226-dual-coefficients` at `Paper1B-M8Geometry-v1_131.tex:22044-22074`: 137-effect inverse: source-matched E1 and independent simplex biorthogonality E3.
- `p1b:cor:v226-source-jets` at `Paper1B-M8Geometry-v1_131.tex:22076-22103`: common native frame derivative and covariant transport, physical matrix input separate.
- `p1b:cor:v227-response-jets` at `Paper1B-M8Geometry-v1_131.tex:22190-22215`: energy sample count: fixed-source Hermitian rational parent, not running curvature extrapolation.
- `p3b:thm:v286-finite-heat-incidence-gram` at `Paper3B-SpectralAction-v1_181.tex:3743-3823`: positive finite Gram-Schur proof only with complete actual licensed B4 and stationary interior.
- `p3b:prop:v286-heat-incidence-contact-obstruction` at `Paper3B-SpectralAction-v1_181.tex:3825-3858`: nonlinear second contact can cancel positive finite Gram.
- `p3b:thm:v319-petersen-moment-six` at `Paper3B-SpectralAction-v1_181.tex:5875-5903`: uniform ten-axis moments second/quartic isotropic, first sextic H6.
- `p1b:thm:v229-coupled-homothety` at `Paper1B-M8Geometry-v1_131.tex:24075-24094`: a_R=a0/G; static curvature identification is an additional condition.
- `p2a:def:v229-action-incidence-certificate` at `Paper2A-GeometricConstitution-v3_215.tex:11451+`: typed physical B4 insertion necessary, not supplied by a nonzero carrier.

## Constituted versus not-derived boundaries

- `BH-IIID-BND-001` lines 105–260: **Constituted:** III-C active orbit and terminal P0 on ND_sp, G0-occurring Hurwitz branch. **Not inferred:** arbitrary scale-dependence, arbitrary support P, FLAG chronology.
- `BH-IIID-BND-002` lines 116–136: **Constituted:** δ_sigma=δ0+sigma_fin; III-C anchor under same-operator 2O owner selects REG0 only there. **Not inferred:** uniform scheme-free origin; dimensionful hierarchy reference.
- `BH-IIID-BND-003` lines 843–1220: **Constituted:** III-B T_sec and Born unmarked λ_B; III-D RED excludes channel-rich responses. **Not inferred:** full independent sector dynamics or β function, dimensional phase Dirac geometry.
- `BH-IIID-BND-004` lines 1056–1128: **Constituted:** s(q)/U=α^-q and C/U=α^-7 assumed; μ(q)/μ_U=α^-q/4 requires matched owner. **Not inferred:** absolute curvature radius or cutoff k without matching.
- `BH-IIID-BND-005` lines 1237–1776: **Constituted:** normalized role trace and RED+UV+IR plus explicit owner-typed rank placement. **Not inferred:** full spacetime action normalization, coefficient dressing law or off-shell continuation.
- `BH-IIID-BND-006` lines 1778–1900: **Constituted:** j4 actual grade from III-C, role selector explicit. **Not inferred:** Q_sigma coefficient base or physical action incidence from carrier criterion alone.
- `BH-IIID-BND-007` lines 2051–2237: **Constituted:** completed character and its phase return; algebraic cap errors conditional on anchor. **Not inferred:** phase insertion into action or cap freeze/metric dynamics.
- `BH-IIID-BND-008` lines 2245–2501: **Constituted:** RED+UV+IR two-root g, NEUT7 scalar plus seven mixed state. **Not inferred:** evolution/beta law, secant=physical entropy index, physical time-shell matching.
- `BH-IIID-BND-009` lines 2502–2684: **Constituted:** exact Ward defect test and necessary/sufficient EXJET/EXCHAR certificates. **Not inferred:** a physical source with W=0 from secant alone, or global EXJET on terminal-normalized action.
- `BH-IIID-BND-010` lines 2684–3161: **Constituted:** exact chain rule, residual tests, analytic mathematical providers and source Gram comparison. **Not inferred:** native heat-action origin, arbitrary field metric second contact, physical fRR or action equality from matched finite jets.
- `BH-IIID-BND-011` lines 3179–3454: **Constituted:** defined source section and its mathematical complete jets/UV bound. **Not inferred:** physical source-section selection, native heat-action identification, unique profile, smooth dressed action.
- `BH-IIID-BND-012` lines 3552–3674: **Constituted:** geometric grade 4 availability and mathematical finite positive Gram test; static comparison polynomial. **Not inferred:** nonzero actual B4/fRR from carrier alone, RG flow from Petersen data, FLRW/static identification without hypothesis.

## Proof-chain limits and integrity

The typed edges are source-matched premises, not automatic proof of a physical mechanism. Citation-only/candidate links do not imply graph ancestry. The issue impact index records verified consumers separately from unconfirmed possible propagation. No new physical finite-incidence claim is asserted from this audit. Source and upstream audits were not edited or reopened. This file is the single current Paper III-D cumulative audit; per-batch records are evidence retained in the integrated DAG layer, not competing audit versions.

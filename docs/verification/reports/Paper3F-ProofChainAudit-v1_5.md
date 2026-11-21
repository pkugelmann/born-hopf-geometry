# Paper Paper3F current-source normalization integration — 18 November 2026

**Current paper:** `Paper3F-CompleteDynamics-v1_269.tex` (SHA-256 `11e4f62493ff4e01d519607cbcd32bb463d1187b117eb7f4300bfadc0679e154`).  
**Framework:** `Paper00-PapersMinimal-v3_036.zip`; **scope:** TARGETED SOURCE INTEGRATION AND BOUNDED MATH CHECKS, NOT A FULL NEW PAPER AUDIT.  
**Source claims:** `p3f:prop:v3036-newton-exchange-invariance; p3f:prop:v3036-gapped-schur-pole; p3f:rem:v3036-newton-owner-status`.  
**Disposition:** Bounded exact quadratic exchange identity and regular gapped-Schur lemma; physical Newton action/source identification remains open.  
**Evidence:** `Paper00-PlanckCurvatureConsistency-v1_5.md` and `Paper00-PlanckCurvatureConsistencyChecks-v1_4.py` (91/91 scoped checks, independently rerun).  
**Ownership:** The earliest unresolved source-native physical source/metric bridge remains `p3f:prop:v2211-newton-owner-matching`; no new axioms, no independent issue duplicate, no physical closure promotion. Historical issue status and prior proofs are preserved verbatim below.

---

## Historical audits and prior scoped updates (unchanged content)

# Source migration and repair-integration addendum — Paper3F-ProofChainAudit-v1_3.md

**Integration release:** `Paper00-PapersMinimal-v3_007.zip`, 14 November 2026.
**Current paper source:** `Paper3F-CompleteDynamics-v1_263.tex`.
**Status:** `SOURCE_INTEGRATED; GLOBAL_SOURCE_REAUDIT_PENDING`. An inherited historical audit is not a correctness certificate for the newer current manuscript.
**Evidence policy:** Local algebraic proofs and scoped tests do not discharge physical source/observable interfaces or automatically alter the canonical proof DAG.

---

## Historical source-bound audit: Paper3F-ProofChainAudit-v1_2.md
# Paper3F — v2.372 source repair addendum (13 November 2026)

**Successor:** `Paper3F-ProofChainAudit-v1_2.md`.  
**Current source:** `Paper3F-CompleteDynamics-v1_257.tex`.  
**Current SHA-256:** `e2c80646af8af5827c1c0df9484ba2c38585906f0e64649fa528d42c952ae440`.  
**Historical audit:** `Paper3F-ProofChainAudit-v1_1.md`.  
**Source repair scope:** 3 distinct issue(s); 5 textual corrections.  
**Disposition:** `SOURCE_REPAIRED_WITH_SCOPED_CHECKS; FORMAL_REAUDIT_PENDING` for only the listed IDs. Other issues and all original evidence statuses unchanged.

| Issue ID | New source line(s) | Repaired issue |
|---|---|---|
| `BH-IIIF-G-0002` | 8278, 8292 | The linear aR curvature action changes the full symplectic current; only constant b is invisible, while Hessian blindness is a different property. |
| `BH-IIIF-G-0005` | 13225, 13250 | Schur edge has positive smallest nonzero singular value only with aligned full-column-rank couplings on one complement; row rank alone fails. |
| `BH-IIIF-G-0003` | 9854 | The curvature-to-U equality explicitly inherits Paper III-E’s CELL_{K→U} hypothesis. |

The historical report below refers to the previous source version and explicitly marks those same issue IDs as `OPEN` **as of that old version**. Those specific historical labels are superseded only as source-edit dispositions by the addendum above; the original audit text is retained to prevent loss of evidence or false global certification. Other issues are unchanged. Recheck the updated source theorem and its proof/use dependencies before promoting an issue to closed in the canonical DAG.

---

## Historical predecessor audit (unchanged text; former source version)

# Born–Hopf Geometry — Paper III-F Rigorous Proof-Chain Audit
**Artifact:** `Paper3F-ProofChainAudit-v1_1.md`  |  **Framework:** `v2_370`  |  **Protocol:** `Paper00-RigorousVerificationDAGWorkProtocol-v2_4`  |  **Date:** 2026-11-11
**Current authoritative source:** `Paper3F-CompleteDynamics-v1_256.tex`  |  **SHA256:** `47d43b2d08b2245ade810eae64a9e1cc827398f60899af0afed7cb2398358a77`  |  **lines:** 1–23,747
**Verdict:** FULLY_AUDITED_WITH_OPEN_GAPS for Paper III-F, not for the whole framework. All source items were reviewed; four printed claims have localized incorrect or unguarded steps; one further claim has missing proof evidence. Valid but conditional claims and source-reproduced calculations are not promoted into physical existence or full independent certifications.

## Coverage and evidence tiers
- Named results **442/442**; proof environments **364/364**, including four standalone proof blocks in the final region; formal remarks **66/66**; material unnamed equation clusters **144**.
- Statuses: **169 VERIFIED**, **149 VERIFIED-CONDITIONAL**, **102 REPRODUCED** (further independent certification required), **18 FORMALIZED**, **4 INCONSISTENT**. One additional open proof-evidence issue does not force an incorrect-claim label.
- Reviewed explicit `\ref`/`\eqref` sources: **843** occurrences, resolved uniquely in frozen current corpus; unknown/unresolved **0**.
- **188** unique source-scoped specialized conditions; **269** typed reviewed edges, **217** source-supported proof-traversable edges; all other typed edges nonpromoting, plus candidate/citation-only links.
- All nine batch ledgers preserve E1 source statements and proofs, independent E3 tests, and applicable E4 adversarial/domain controls. A passing script is an evidence certificate only for its tested calculation, not blanket proof or physical realization.

## Complete first-origin open issue register
### BH-IIIF-G-0001: MISSING_EVIDENCE — MODERATE — OPEN
**Exact source:** `p3f:cor:v176-first-class-constraint-propagation`; `Paper3F-CompleteDynamics-v1_256.tex:6191-6218`. **Earliest step:** Their bulk Poisson algebra closes with the usual field-dependent structure functions
**Finding and proof obligation:** Supply explicit source-matched bracket/constraint closure proof (or checked imported ADM theorem) on regular same-owner scalar-tensor–Yang–Mills phase space; identify any further local differentiability/constraint conditions. Not a demand for a global Cauchy flow.
**Why:** Central first-class and dynamical constraint-preservation conclusion lacks independently replayable displayed Poisson-bracket computation or explicit controlling imported certificate in this source region.
**Conditions:** consumed BH-IIIF-A-0042, BH-IIIF-A-0046; open none confirmed.
**Direct upstream source-supported paths:** p3f:thm:v176-local-bosonic-euler-noether → p3f:thm:v176-adm-constraint-packet → p3f:cor:v176-first-class-constraint-propagation.
**Verified defective downstream paths:** none. **Other papers proven defective:** none.
**Possible but unconfirmed effects:** Global reduced phase-space conclusion within same corollary ; Any downstream claim consuming first-class propagation, to be reviewed for exact proof-use.
**Scope-limited independent/bypass routes:** none asserted.
**Unresolved action (NO SOURCE EDIT PERFORMED):** Exact bulk smeared bracket computation/independent published theorem with all regular scalar-tensor and gauge couplings matched, plus origin and no-boundary scope. Do not invent new framework lemmas.

### BH-IIIF-G-0002: INCORRECT_STEP — MODERATE — OPEN
**Exact source:** `p3f:prop:vacuum-shift-symplectic-scope`; `Paper3F-CompleteDynamics-v1_256.tex:8277-8284`. **Earliest step:** Equality of Hessians or of the common off-shell symplectic current therefore cannot select κ in the preceding proposition.
**Finding and proof obligation:** Correct/distinguish curvature Hessian from full metric covariant off-shell symplectic current. The aR affine direction changes the Einstein-Hilbert presymplectic current. Retain b-only invisibility, and separately retain valid coefficient-family connection argument for κ=0.
**Why:** The full metric EH term has nonzero kinetic presymplectic form, unlike a purely constant shift. Therefore off-shell symplectic data can distinguish the slope parameter, contrary to the source assertion.
**Conditions:** consumed BH-IIIF-A-0058, BH-IIIF-A-0055; open none confirmed.
**Direct upstream source-supported paths:** p3f:thm:born-coefficient-family-first-response → p3f:prop:complete-born-action-defect → p3f:prop:vacuum-shift-symplectic-scope.
**Verified defective downstream paths:** none. **Other papers proven defective:** none.
**Possible but unconfirmed effects:** Any later proposition which relies specifically on full off-shell symplectic-current blindness of the affine aR coefficient; no such exact proof-use path certified in this batch..
**Scope-limited independent/bypass routes:** p3f:thm:born-coefficient-family-first-response → p3f:prop:complete-born-action-defect → p3f:cor:constructor-born-discharge-bare.
**Adversarial certificate:** `{'metric': 'g=diag(-1,e^{2q(t)},e^{-2q(t)},1), smooth Lorentz on a local finite chart', 'curvature': 'sqrt(-g)=1, R=2 (qdot)^2, checked from full Christoffel/Ricci', 'action_shift': 'Delta L=sqrt(-g)(aR+b)=2a(qdot)^2+b', 'presymplectic': 'omega^t=4a(delta1 q delta2 qdot-delta2 q delta1 qdot), nonzero e.g. delta1 q=1, delta2 q=t; b contributes no presymplectic kinetic form', 'domain_check': 'Smooth, nondegenerate Lorentz metric and arbitrary local off-shell variations. Compactly supported time/space profile gives a nonzero pointwise current on the interior. No physical realization theorem is needed for this general metric action claim.'}`.
**Unresolved action (NO SOURCE EDIT PERFORMED):** Adjust the statement or restrict “symplectic current” to some separately defined projected curvature-only object; full metric current counterexample otherwise persists.

### BH-IIIF-G-0003: MISSING_CONDITION — MINOR — OPEN
**Exact source:** `p3:thm:local-fR-field-equation`; `Paper3F-CompleteDynamics-v1_256.tex:9848`. **Earliest step:** U=Lambda_EH^2=(3/pi) K_p
**Finding and proof obligation:** Keep the Paper III-E condition CELL_{K→U} attached to the U=(3/π)Kp comparison. It is not derived solely from Kp=6/Rmom² and U=Lambda_EH². The same theorem correctly includes that condition at line 9929.
**Why:** The numerically normalized 3D/4D curvature relation has an additional origin-certified action/geometry port; the field-equation variation does not need it.
**Conditions:** consumed p3e:eq:v2211-momentum-eh-port; open p3e:eq:v2211-momentum-eh-port (conditional port, no evidence of unconditional discharge).
**Direct upstream source-supported paths:** p3e:eq:v2211-momentum-eh-port → p3:thm:local-fR-field-equation.
**Verified defective downstream paths:** none. **Other papers proven defective:** none.
**Possible but unconfirmed effects:** Any numeric momentum curvature / 4D EH comparison relying on line 9848 rather than on the guarded statement at 9929; not independently located as a proof-use..
**Scope-limited independent/bypass routes:** p3f:thm:general-local-fR-variation with normalized action ACT_MRESP, not requiring CELL_KtoU for the Euler equation.
**Unresolved action (NO SOURCE EDIT PERFORMED):** Clarify the earlier sentence to carry CELL_{K→U} or explicitly refer to the later restriction. No paper change authorized.

### BH-IIIF-G-0004: MISSING_CONDITION — MODERATE — OPEN
**Exact source:** `p3:cor:no-independent-lr-gauge-coefficient`; `Paper3F-CompleteDynamics-v1_256.tex:11166-11171`. **Earliest step:** Inside (GRED_7)+(CAL_GRED(kappa)), 1/g_L^2=1/g_R^2=kappa f_2/48.
**Finding and proof obligation:** For the absolute dimensionless expression κ f₂/48, also require r_fib Λcut=1 (BH-IIIF-A-0016). Without it theorem 201 gives κ r_fib² f₂ Λcut²/48. The base CAL_GRED by itself explicitly excludes automatic saturation.
**Why:** Without saturation the absolute gauge coefficient changes by (r_fibΛcut)²; an unguarded numeric comparison is false in an admissible calibration branch while equality g_L=g_R survives.
**Conditions:** consumed BH-IIIF-A-0011, BH-IIIF-A-0012, BH-IIIF-A-0016; open BH-IIIF-A-0016 (separately optional).
**Direct upstream source-supported paths:** p3:thm:born-spherical-spectral-action-reduction → p3:cor:no-independent-lr-gauge-coefficient.
**Verified defective downstream paths:** none. **Other papers proven defective:** none.
**Possible but unconfirmed effects:** p3:cor:born-spectral-action-closure-status repeats the shorthand and must inherit the saturation guard; numerical remote couplings unverified..
**Scope-limited independent/bypass routes:** p3:prop:round-fibre-left-right-equality: geometric g_L=g_R independently of saturation ; p3:thm:born-spherical-spectral-action-reduction: κ r_fib² C_EH without saturation.
**Unresolved action (NO SOURCE EDIT PERFORMED):** State CELL_GRED_SAT explicitly (or state it is included in the specialized absolute-reduction branch) in corollary; preserve general formula and no physical U1 claim.

### BH-IIIF-G-0005: INVALID_GENERAL_BOUND / MISSING_RANK_ALIGNMENT — MODERATE — OPEN
**Exact source:** `p3f:prop:v1118-feshbach-propagation-not-genesis`; `Paper3F-CompleteDynamics-v1_256.tex:13215-13233, decisive lines 13225-13229`. **Earliest step:** If Delta != 0 and A_L,A_R are full rank then sigma_min(A_L U A_R^dagger)>=sigma_min(A_L)sigma_min(A_R)/|Delta|>0.
**Finding and proof obligation:** Paired complement U unitary and Delta !=0, A_L and A_R only full rank. Establish additional compatible subspace alignment/invertibility of product, or restrict theorem to an actual square-invertible couplings domain supported by source. As written full rank does not guarantee that bound. No new repair theorem added.
**Why:** The Schur reduction can be rank deficient despite full-rank individual rectangular couplings, so nonzero transported mass/gap does not follow in the stated domain.
**Conditions:** consumed BH-IIIF-A-0115, BH-IIIF-A-0117; open Actual mutual row-space transversality of A_L U and A_R, or suitable square two-sided invertibility, not asserted by printed full-rank premise..
**Direct upstream source-supported paths:** none independently verified.
**Verified defective downstream paths:** none. **Other papers proven defective:** none.
**Possible but unconfirmed effects:** Any downstream claim that deduces automatic nonzero Feshbach gap solely from rectangular full rank; no material use found in this batch that requires the failed inequality..
**Scope-limited independent/bypass routes:** p3f:thm:v1118-finite-source-operator-gap uses directly Phi_T²>=m_T²I and D_A²>=0, independent of failed full-rank product inequality. ; p3f:cor:v1118-balanced-schur-return uses exact Schur rescaling, not positive singular-value lower bound..
**Exact finite counterexample:** `{'Delta': 1, 'U': 'I3', 'A_L': [[1, 0, 0], [0, 1, 0]], 'A_R': [[0, 1, 0], [0, 0, 1]], 'A_L_rank': 2, 'A_R_rank': 2, 'A_L_shape': [2, 3], 'A_R_shape': [2, 3], 'T_Fesh': [[0, 0], [-1, 0]], 'sigma_min_AL': 1, 'sigma_min_AR': 1, 'sigma_min_T': 0, 'claimed_lower_bound': 1}`.
**Unresolved action (NO SOURCE EDIT PERFORMED):** Require a source-supported stronger product-rank / alignment hypothesis or verify that the actual declared couplings are square/invertible. Do not silently amend the paper in this audit.

## Batch-by-batch audit census
| Batch | Current source lines | Results | Proofs | Remarks | New issues |
|---:|---|---:|---:|---:|---:|
| 1 | 1–2202 | 36 | 22 | 4 | 0 |
| 2 | 2203–4225 | 33 | 24 | 7 | 0 |
| 3 | 4226–6569 | 42 | 28 | 8 | 1 |
| 4 | 6570–9070 | 50 | 42 | 13 | 1 |
| 5 | 9071–11272 | 44 | 38 | 7 | 2 |
| 6 | 11273–14514 | 74 | 46 | 13 | 1 |
| 7 | 14515–17237 | 54 | 51 | 4 | 0 |
| 8 | 17238–20000 | 54 | 54 | 0 | 0 |
| 9 | 20001–23747 | 55 | 59 | 10 | 0 |

## Full result-by-result disposition ledger
Legend: VERIFIED = checked at stated mathematical scope; VERIFIED-CONDITIONAL = valid under printed antecedents; REPRODUCED = E1 proof source-replayed but incomplete independent certification; FORMALIZED = a definition/axiom-boundary, not a claim of physical occurrence; INCONSISTENT = localized printed proof/normalization error. Exact claims/proofs in the corresponding machine-readable ledger.
| ID | Result source label | Source lines | Disposition |
|---|---|---|---|
| `BH-IIIF-C-0001` | `p3:def:lat-pol-csa-gred-hypotheses` | 206–532 | FORMALIZED |
| `BH-IIIF-C-0002` | `p3f:thm:minimal-configuration-tangent-vdom` | 534–543 | REPRODUCED |
| `BH-IIIF-C-0003` | `p3f:thm:joint-same-datum-relation-closure` | 558–586 | REPRODUCED |
| `BH-IIIF-C-0004` | `p3:def:local_doubled_patch` | 674–720 | FORMALIZED |
| `BH-IIIF-C-0005` | `p3:lem:no-metric-reciprocal-duality` | 722–746 | VERIFIED |
| `BH-IIIF-C-0006` | `p3:lem:cotangent-lift-uniqueness` | 766–786 | VERIFIED |
| `BH-IIIF-C-0007` | `p3:thm:local_reciprocal_atlas` | 806–898 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0008` | `p3:cor:homogeneous-cotangent-inverse-scaling` | 960–988 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0009` | `p3:def:sharp-scalar-resolution-frontier` | 1004–1037 | FORMALIZED |
| `BH-IIIF-C-0010` | `p3:thm:exact-spectral-resolution-staircase` | 1039–1096 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0011` | `p3f:cor:sharp-frontier-discharges-generated-boundary` | 1129–1162 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0012` | `p3f:cor:sharp-frontier-generates-position-history` | 1180–1218 | REPRODUCED |
| `BH-IIIF-C-0013` | `p3:cor:spectral-resolution-thresholds` | 1234–1249 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0014` | `p3f:cor:v259-derived-plateau-finite-band-activation` | 1265–1310 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0015` | `p3f:thm:spectral-frontier-event-process` | 1326–1395 | REPRODUCED |
| `BH-IIIF-C-0016` | `p3f:cor:frontier-transverse-shell-symbol` | 1413–1438 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0017` | `p3f:cor:frontier-transverse-area-density` | 1440–1472 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0018` | `p3f:cor:v259-affine-hopf-area-channel` | 1474–1490 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0019` | `p3f:cor:v191-frontier-efold-spacing` | 1533–1562 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0020` | `p3f:cor:v191-comparison-band-capture` | 1570–1600 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0021` | `p3f:thm:v260-history-tagged-shell-stack` | 1603–1620 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0022` | `p3f:cor:v260-boundary-increment-capacity` | 1638–1666 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0023` | `p3f:thm:v260-operation-activation-hierarchy` | 1668–1697 | REPRODUCED |
| `BH-IIIF-C-0024` | `p3f:cor:v260-frontier-event-density` | 1711–1732 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0025` | `p3f:cor:v260-coexact-shell-availability` | 1734–1748 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0026` | `p3f:thm:v261-casimir-hopf-frontier` | 1752–1786 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0027` | `p3f:cor:v261-first-protected-transverse-onset` | 1800–1819 | REPRODUCED |
| `BH-IIIF-C-0028` | `p3f:cor:v261-scalar-vector-frontier-delay` | 1829–1854 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0029` | `p3f:cor:v2180-scalar-frontier-type-firewall` | 1857–1875 | REPRODUCED |
| `BH-IIIF-C-0030` | `p3f:cor:v261-heat-sharp-functional-relation` | 1886–1908 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0031` | `p3f:cor:v261-current-shell-rank-obstruction` | 1910–1936 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0032` | `p3:def:local_kunneth_born` | 1943–1983 | FORMALIZED |
| `BH-IIIF-C-0033` | `p3:thm:local_kunneth_connection` | 2005–2033 | VERIFIED |
| `BH-IIIF-C-0034` | `p3:def:macrolocal_sector` | 2075–2086 | FORMALIZED |
| `BH-IIIF-C-0035` | `p3f:thm:qloc-fourier-criterion` | 2088–2117 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0036` | `p3:prop:qloc-sufficient-criterion` | 2133–2170 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0037` | `p3f:thm:common-heat-specializes-kinetic-trace` | 2218–2239 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0038` | `p3f:cor:profile-invariant-joint-heat-descendants` | 2277–2288 | REPRODUCED |
| `BH-IIIF-C-0039` | `p3f:thm:v2140-background-gauge-response-complex` | 2314–2375 | REPRODUCED |
| `BH-IIIF-C-0040` | `p3f:cor:v2140-ghost-not-particle` | 2398–2405 | REPRODUCED |
| `BH-IIIF-C-0041` | `p3f:thm:v181-natural-relative-scalar-selector` | 2424–2438 | VERIFIED |
| `BH-IIIF-C-0042` | `p3f:cor:v181-degree-two-relative-selector-spectrum` | 2448–2461 | REPRODUCED |
| `BH-IIIF-C-0043` | `p3f:thm:v180-exact-finite-quartic-scalar-action` | 2463–2498 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0044` | `p3f:prop:v243-rooted-native-quartic-test` | 2511–2542 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0045` | `p3f:thm:v245-rooted-quartic-global-minima` | 2560–2580 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0046` | `p3f:prop:v244-rooted-phase-schur-order` | 2633–2667 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0047` | `p3f:cor:v180-scalar-clock-noether-mass-defect` | 2711–2727 | REPRODUCED |
| `BH-IIIF-C-0048` | `p3f:thm:v180-incidence-harmonic-resolution` | 2729–2746 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0049` | `p3f:cor:v180-hurwitz-return-polar-invariance` | 2748–2765 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0050` | `p3f:cor:complete-frontier-mode-density` | 2767–2786 | VERIFIED |
| `BH-IIIF-C-0051` | `p3f:thm:v189-ward-schur-k16-tt` | 2798–2811 | REPRODUCED |
| `BH-IIIF-C-0052` | `p3f:thm:v1148-finite-metric-constructor` | 2845–2882 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0053` | `p3f:cor:v1148-metric-haar-coefficients` | 2985–3002 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0054` | `p3f:cor:v1145-finite-quantum-source-schur` | 3081–3118 | REPRODUCED |
| `BH-IIIF-C-0055` | `p3f:cor:complete-reduction-reuse` | 3179–3188 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0056` | `p3f:thm:tt-dirac-vertex-contact` | 3231–3271 | REPRODUCED |
| `BH-IIIF-C-0057` | `p3f:cor:level-one-quadrupole-incidence` | 3317–3336 | REPRODUCED |
| `BH-IIIF-C-0058` | `p3f:cor:kneser-spin-five-mirror-metric-vertex` | 3354–3394 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0059` | `p3f:v2171:thm:retention` | 3484–3503 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0060` | `p3f:v2171:cor:sourcejets` | 3527–3543 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0061` | `p3f:v2171:thm:quartic` | 3552–3569 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0062` | `p3f:v2171:thm:boundarypair` | 3593–3603 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0063` | `p3f:v2171:thm:baryonstationary` | 3636–3656 | REPRODUCED |
| `BH-IIIF-C-0064` | `p3f:thm:v164-same-action-profile-invariance` | 3719–3741 | VERIFIED |
| `BH-IIIF-C-0065` | `p3f:thm:v236-same-action-response-descent` | 3745–3769 | VERIFIED |
| `BH-IIIF-C-0066` | `p3f:thm:v169-complete-gravity-action` | 3812–3830 | REPRODUCED |
| `BH-IIIF-C-0067` | `p3f:thm:v169-explicit-free-dirac-source` | 3893–3915 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0068` | `p3f:thm:v169-flrw-lapse-and-phase-action` | 3969–3990 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0069` | `p3f:thm:v169-finite-source-work` | 4050–4084 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0070` | `p3:thm:completed-carrier-dynamical-asymmetry` | 4230–4255 | REPRODUCED |
| `BH-IIIF-C-0071` | `p3:thm:locality_selection` | 4282–4297 | REPRODUCED |
| `BH-IIIF-C-0072` | `p3:def:analytic-localizer` | 4317–4332 | FORMALIZED |
| `BH-IIIF-C-0073` | `p3f:lem:diagonal-eh-full-variation` | 4334–4359 | VERIFIED |
| `BH-IIIF-C-0074` | `p3:thm:local_spectral_asymptotics` | 4367–4417 | REPRODUCED |
| `BH-IIIF-C-0075` | `p3f:cor:local-asymptotics-lorentzian-interpretation` | 4441–4461 | REPRODUCED |
| `BH-IIIF-C-0076` | `p3f:cor:stationary-quadratic-action-derived-later` | 4463–4481 | REPRODUCED |
| `BH-IIIF-C-0077` | `p3f:thm:joint-connection-uninserted-trace-closure` | 4483–4521 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0078` | `p3f:def:v174-native-yang-mills-phase-space-domain` | 4553–4585 | FORMALIZED |
| `BH-IIIF-C-0079` | `p3f:lem:v174-yang-mills-complex-connection-real-form` | 4587–4662 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0080` | `p3f:thm:v174-generated-joint-gauge-phase-space-action` | 4677–4810 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0081` | `p3f:cor:v174-yang-mills-gauge-reduction-wick-discharge` | 4872–4883 | REPRODUCED |
| `BH-IIIF-C-0082` | `p3f:thm:joint-gauge-principal-symbol-inheritance` | 4905–4948 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0083` | `p3f:thm:v175-generated-joint-einstein-action` | 4976–5056 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0084` | `p3f:cor:v267-joint-eh-newton-readout` | 5091–5127 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0085` | `p3f:prop:v2211-newton-owner-matching` | 5134–5164 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0086` | `p3f:thm:v175-native-local-scalar-action` | 5225–5295 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0087` | `p3f:cor:generated-action-owner-dependency` | 5337–5350 | REPRODUCED |
| `BH-IIIF-C-0088` | `p3f:cor:joint-owner-coefficient-noninsertion` | 5352–5362 | REPRODUCED |
| `BH-IIIF-C-0089` | `p3f:def:v176-local-bosonic-noether-domain` | 5386–5415 | FORMALIZED |
| `BH-IIIF-C-0090` | `p3f:thm:v166-native-local-action-invariance` | 5417–5449 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0091` | `p3f:thm:v176-local-bosonic-euler-noether` | 5490–5567 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0092` | `p3f:thm:v179-normalized-scalar-hessian` | 5611–5638 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0093` | `p3f:cor:v177-source-coordinate-polar-invariance` | 5650–5670 | VERIFIED |
| `BH-IIIF-C-0094` | `p3f:thm:v244-stationary-physical-hessian-propagation` | 5689–5737 | VERIFIED |
| `BH-IIIF-C-0095` | `p3f:cor:v244-scalar-harmonic-propagation` | 5754–5774 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0096` | `p3f:cor:v244-transverse-gauge-propagation` | 5776–5806 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0097` | `p3f:thm:v199-rgas-kinetic-connection` | 5819–5835 | VERIFIED |
| `BH-IIIF-C-0098` | `p3f:cor:v199-rgas-spectral-frame` | 5846–5857 | VERIFIED |
| `BH-IIIF-C-0099` | `p3f:cor:v179-noether-normalized-response` | 5880–5905 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0100` | `p3f:cor:v111-gauge-gram-no-stationarity` | 5919–5940 | VERIFIED |
| `BH-IIIF-C-0101` | `p3f:prop:v179-radial-einstein-response` | 5971–5996 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0102` | `p3f:cor:v176-coupled-gauge-scalar-moment-map` | 6043–6078 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0103` | `p3f:thm:v176-adm-constraint-packet` | 6080–6168 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0104` | `p3f:cor:v176-first-class-constraint-propagation` | 6191–6218 | REPRODUCED |
| `BH-IIIF-C-0105` | `p3f:cor:v176-noether-ward-derivative-tower` | 6220–6244 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0106` | `p3f:cor:v176-restricted-broken-weyl-trace` | 6246–6261 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0107` | `p3f:def:common-holomorphic-finite-jet-owner` | 6287–6300 | FORMALIZED |
| `BH-IIIF-C-0108` | `p3f:thm:finite-local-bosonic-clock-real-form` | 6302–6314 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0109` | `p3:thm:common-position-spectral-origin` | 6341–6451 | REPRODUCED |
| `BH-IIIF-C-0110` | `p3f:thm:v177-local-clocked-fermion-jet` | 6477–6520 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0111` | `p3f:cor:v1122-root-generated-fermion-member-handoff` | 6541–6558 | REPRODUCED |
| `BH-IIIF-C-0112` | `p3f:prop:v246-bilinear-parent-jets` | 6572–6601 | VERIFIED |
| `BH-IIIF-C-0113` | `p3f:cor:v246-canonical-member-handoff` | 6609–6630 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0114` | `p3f:prop:v221-relative-chiral-comparison-frame` | 6640–6664 | VERIFIED |
| `BH-IIIF-C-0115` | `p3f:thm:v173-stationary-solution-family` | 6687–6728 | REPRODUCED |
| `BH-IIIF-C-0116` | `p3f:cor:v257-classical-family-provider` | 6741–6758 | REPRODUCED |
| `BH-IIIF-C-0117` | `p3f:cor:v173-local-stationary-family-host` | 6767–6783 | REPRODUCED |
| `BH-IIIF-C-0118` | `p3f:cor:act-cl-discharges-act-eh` | 6785–6802 | REPRODUCED |
| `BH-IIIF-C-0119` | `p3f:def:v2211-certified-response-domain` | 6813–6835 | FORMALIZED |
| `BH-IIIF-C-0120` | `p3f:cor:generated-action-response-variation` | 6837–6877 | REPRODUCED |
| `BH-IIIF-C-0121` | `p3f:thm:born-coefficient-family-first-response` | 6898–6954 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0122` | `p3:cor:common-action-metric-backreaction` | 7036–7086 | REPRODUCED |
| `BH-IIIF-C-0123` | `p3f:def:v2105-vacuum-excitation-source-split` | 7106–7129 | FORMALIZED |
| `BH-IIIF-C-0124` | `p3f:def:v2105-qroot` | 7131–7155 | FORMALIZED |
| `BH-IIIF-C-0125` | `p3f:thm:general-local-fR-variation` | 7170–7225 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0126` | `p3f:thm:term-ren-zero-order-redundancy` | 7253–7277 | VERIFIED |
| `BH-IIIF-C-0127` | `p3f:prop:complete-action-legendre-potential` | 7290–7312 | VERIFIED |
| `BH-IIIF-C-0128` | `p3f:cor:v2187-normalized-born-potential-scope` | 7334–7366 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0129` | `p3f:prop:v2218-candidate-ir-vacuum` | 7408–7445 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0130` | `p3f:cor:v2218-fixed-visibility-canonical-rate` | 7550–7579 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0131` | `p3f:prop:v2219-carrier4-legendre` | 7601–7614 | REPRODUCED |
| `BH-IIIF-C-0132` | `p3f:thm:v2219-coherent-uv-scalaron` | 7623–7650 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0133` | `p3f:prop:v2219-closed-uv-trace` | 7659–7685 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0134` | `p3f:prop:v2219-scalar-particle-vertex` | 7694–7719 | VERIFIED |
| `BH-IIIF-C-0135` | `p3f:thm:v223-cap-parent` | 7739–7765 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0136` | `p3f:cor:v223-cap-metric` | 7790–7806 | VERIFIED |
| `BH-IIIF-C-0137` | `p3f:prop:v223-cap-legendre` | 7819–7835 | REPRODUCED |
| `BH-IIIF-C-0138` | `p3f:thm:v288-cap-vacuum-root-stability` | 7860–7898 | REPRODUCED |
| `BH-IIIF-C-0139` | `p3f:thm:v223-collar-error` | 7965–8033 | REPRODUCED |
| `BH-IIIF-C-0140` | `p3f:prop:v223-collar-determinant` | 8072–8087 | VERIFIED |
| `BH-IIIF-C-0141` | `p3f:thm:bare-born-potential-criterion` | 8135–8186 | VERIFIED |
| `BH-IIIF-C-0142` | `p3f:prop:complete-born-action-defect` | 8208–8259 | VERIFIED |
| `BH-IIIF-C-0143` | `p3f:prop:vacuum-shift-symplectic-scope` | 8275–8287 | INCONSISTENT |
| `BH-IIIF-C-0144` | `p3f:cor:constructor-born-discharge-bare` | 8299–8318 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0145` | `p3f:def:v1164-curvature-response-types` | 8358–8377 | FORMALIZED |
| `BH-IIIF-C-0146` | `p3f:thm:v1164-exceptional-curvature-susceptibility` | 8379–8403 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0147` | `p3f:prop:v1164-heat-hessian-no-insertion` | 8415–8435 | VERIFIED |
| `BH-IIIF-C-0148` | `p3f:prop:v1164-dirac-a4-a6-firewall` | 8446–8486 | REPRODUCED |
| `BH-IIIF-C-0149` | `p3f:prop:v1164-terminal-jet-addition-nogo` | 8501–8527 | VERIFIED |
| `BH-IIIF-C-0150` | `p3f:thm:v1164-scalaron-port-matching` | 8536–8575 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0151` | `p3f:prop:v1164-scalar-overlap-condition` | 8586–8607 | REPRODUCED |
| `BH-IIIF-C-0152` | `p3f:prop:v1165-raw-euler-port` | 8636–8662 | REPRODUCED |
| `BH-IIIF-C-0153` | `p3f:thm:v1165-positive-no-free-force` | 8671–8699 | VERIFIED |
| `BH-IIIF-C-0154` | `p3f:prop:v1165-scalar-dirac-heat-mismatch` | 8710–8734 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0155` | `p3f:prop:v1165-analytic-k16-obstruction` | 8736–8752 | VERIFIED |
| `BH-IIIF-C-0156` | `p3f:prop:v1166-neutral-photon-mixing` | 8791–8814 | VERIFIED |
| `BH-IIIF-C-0157` | `p3f:thm:v118-conformal-trace` | 8847–8862 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0158` | `p3f:prop:v118-hyperbolic-mass-gram` | 8885–8907 | VERIFIED |
| `BH-IIIF-C-0159` | `p3f:prop:v118-dirichlet-scalar-ghy` | 8920–8941 | VERIFIED |
| `BH-IIIF-C-0160` | `p3f:prop:v118-localizer-aware-hessian` | 8953–8986 | VERIFIED |
| `BH-IIIF-C-0161` | `p3f:prop:v118-ward-and-low-mode` | 8995–9021 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0162` | `p3f:prop:v229-cap-vs-coherent-uv-hessian` | 9073–9100 | VERIFIED |
| `BH-IIIF-C-0163` | `p3f:cor:v229-actual-curvature-schur-test` | 9112–9127 | VERIFIED |
| `BH-IIIF-C-0164` | `p3f:thm:v2188-bare-vacuum-trace` | 9167–9202 | VERIFIED |
| `BH-IIIF-C-0165` | `p3f:cor:v2188-bare-vacuum-born-scope` | 9216–9228 | VERIFIED |
| `BH-IIIF-C-0166` | `p3f:cor:laur17-terminal-ren-representative` | 9252–9312 | REPRODUCED |
| `BH-IIIF-C-0167` | `p3f:cor:v2118-native-cyclic-ren0-firewall` | 9331–9357 | REPRODUCED |
| `BH-IIIF-C-0168` | `p3f:cor:transported-k16-k48-action-junction` | 9369–9381 | REPRODUCED |
| `BH-IIIF-C-0169` | `p3f:thm:v266-gp-exact-k16-junction-condition` | 9383–9405 | REPRODUCED |
| `BH-IIIF-C-0170` | `p3f:thm:term-ren-multiplicative-action-quotient` | 9417–9454 | VERIFIED |
| `BH-IIIF-C-0171` | `p3f:cor:pqti-same-action-invariance` | 9473–9493 | VERIFIED |
| `BH-IIIF-C-0172` | `p3f:cor:term-ren-terminal-vacuum` | 9507–9524 | VERIFIED |
| `BH-IIIF-C-0173` | `p3f:cor:normalized-terminal-vacuum-data` | 9542–9555 | VERIFIED |
| `BH-IIIF-C-0174` | `p3f:thm:trace-linearized-scalaron-mass` | 9564–9611 | VERIFIED |
| `BH-IIIF-C-0175` | `p3f:cor:derived-minimal-response-scalaron` | 9634–9656 | REPRODUCED |
| `BH-IIIF-C-0176` | `p3f:thm:v199-rgas-conformal-hessian` | 9668–9690 | VERIFIED |
| `BH-IIIF-C-0177` | `p3f:cor:v199-rgas-scalaron-factor` | 9700–9716 | VERIFIED |
| `BH-IIIF-C-0178` | `p3f:def:nonlinear-response-realization-atlas` | 9734–9799 | FORMALIZED |
| `BH-IIIF-C-0179` | `p3:thm:local-fR-field-equation` | 9801–9939 | INCONSISTENT |
| `BH-IIIF-C-0180` | `p3:cor:born-carrier-gauge-gravity-split` | 9955–9974 | REPRODUCED |
| `BH-IIIF-C-0181` | `p3f:thm:canonical-local-gred-pullback` | 10018–10041 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0182` | `p3f:thm:unique-born-invariant-gred-connection` | 10067–10120 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0183` | `p3f:cor:v181-full-born-holonomy` | 10158–10167 | VERIFIED |
| `BH-IIIF-C-0184` | `p3f:cor:protected-projector-midpoint-ancestry` | 10177–10202 | VERIFIED |
| `BH-IIIF-C-0185` | `p3f:thm:generated-fibre-spin-joint-operator` | 10219–10333 | REPRODUCED |
| `BH-IIIF-C-0186` | `p3f:prop:m8td-explicit-nonconstant-zero` | 10413–10432 | VERIFIED |
| `BH-IIIF-C-0187` | `p3f:prop:native-source-dipole-normalization` | 10458–10485 | VERIFIED |
| `BH-IIIF-C-0188` | `p3f:thm:native-shifted-signed-root` | 10537–10555 | REPRODUCED |
| `BH-IIIF-C-0189` | `p3f:thm:native-shift-displacement` | 10587–10618 | REPRODUCED |
| `BH-IIIF-C-0190` | `p3f:thm:v2183-native-weak-carrier-class` | 10660–10704 | REPRODUCED |
| `BH-IIIF-C-0191` | `p3f:cor:v259-native-su2-discharge` | 10726–10737 | REPRODUCED |
| `BH-IIIF-C-0192` | `p3f:cor:v259-minimal-born-protection` | 10755–10766 | REPRODUCED |
| `BH-IIIF-C-0193` | `p3f:cor:v2183-native-weak-morse-dirac` | 10777–10809 | REPRODUCED |
| `BH-IIIF-C-0194` | `p3f:cor:v2183-native-weak-barrier-energy` | 10821–10837 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0195` | `p3f:cor:v2183-native-weak-lorentzian-instability` | 10850–10871 | VERIFIED |
| `BH-IIIF-C-0196` | `p3:def:normalized-born-product-metric` | 10934–10962 | FORMALIZED |
| `BH-IIIF-C-0197` | `p3:def:gred-connection-generator-normalization` | 10964–11019 | FORMALIZED |
| `BH-IIIF-C-0198` | `p3:lem:minimal-scalar-trace-multiplicity` | 11030–11043 | REPRODUCED |
| `BH-IIIF-C-0199` | `p3:lem:totally-geodesic-born-odd-fibers` | 11053–11059 | VERIFIED |
| `BH-IIIF-C-0200` | `p3:prop:round-fibre-left-right-equality` | 11075–11088 | VERIFIED |
| `BH-IIIF-C-0201` | `p3:thm:born-spherical-spectral-action-reduction` | 11096–11144 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0202` | `p3:cor:no-independent-lr-gauge-coefficient` | 11166–11177 | INCONSISTENT |
| `BH-IIIF-C-0203` | `p3:cor:born-spectral-action-closure-status` | 11179–11192 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0204` | `p3f:cor:euclidean-quasi-locality` | 11204–11214 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0205` | `p3:cor:d3_derived` | 11229–11246 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0206` | `p3f:prop:v2109-hilbert-lapse-source` | 11313–11326 | VERIFIED |
| `BH-IIIF-C-0207` | `p3f:thm:v2109-poisson-source-projection` | 11332–11351 | VERIFIED |
| `BH-IIIF-C-0208` | `p3f:thm:v2109-moving-source-schur` | 11365–11389 | VERIFIED |
| `BH-IIIF-C-0209` | `p3f:thm:v2109-mixed-scalaron-decoupling` | 11403–11419 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0210` | `p3f:prop:v2167-complete-neutral-return` | 11446–11471 | VERIFIED |
| `BH-IIIF-C-0211` | `p3f:cor:v2167-charged-source-return` | 11480–11500 | VERIFIED |
| `BH-IIIF-C-0212` | `p3f:prop:v2167-causal-inherited-return` | 11518–11531 | VERIFIED |
| `BH-IIIF-C-0213` | `p3f:cor:v2167-family-equivariant-retention` | 11542–11556 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0214` | `p3f:thm:v2168-left-return-test` | 11616–11637 | VERIFIED |
| `BH-IIIF-C-0215` | `p3f:thm:v2168-hierarchy-source-return` | 11684–11714 | VERIFIED |
| `BH-IIIF-C-0216` | `p3f:thm:v267-two-scalar-return-defect` | 11830–11852 | VERIFIED |
| `BH-IIIF-C-0217` | `p3f:cor:v267-anchored-heat-action-test` | 11859–11875 | VERIFIED |
| `BH-IIIF-C-0218` | `p3f:prop:v267-exact-heat-jet-normalization` | 11883–11903 | VERIFIED |
| `BH-IIIF-C-0219` | `p3f:cor:v2191-action-corner-inverse` | 11929–11958 | VERIFIED |
| `BH-IIIF-C-0220` | `p3f:prop:v239-same-action-electron-pencil` | 11981–12002 | VERIFIED |
| `BH-IIIF-C-0221` | `p3f:prop:v240-action-source-gram-test` | 12019–12055 | VERIFIED |
| `BH-IIIF-C-0222` | `p3f:prop:v245-electron-actual-block-defect` | 12079–12112 | VERIFIED |
| `BH-IIIF-C-0223` | `p3f:prop:v2168-source-arrow-certificate` | 12148–12159 | VERIFIED |
| `BH-IIIF-C-0224` | `p3f:thm:v2168-free-clock-poles` | 12191–12214 | VERIFIED |
| `BH-IIIF-C-0225` | `p3f:cor:v2168-free-clifford-dispersion` | 12236–12253 | VERIFIED |
| `BH-IIIF-C-0226` | `p3f:thm:v2168-kinetic-congruence` | 12278–12298 | VERIFIED |
| `BH-IIIF-C-0227` | `p3f:prop:v2168-component-band-retention` | 12357–12377 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0228` | `p3f:prop:v224-native-tensor` | 12471–12487 | VERIFIED |
| `BH-IIIF-C-0229` | `p3f:thm:v224-stress-transport` | 12504–12529 | VERIFIED |
| `BH-IIIF-C-0230` | `p3f:prop:v224-normalization-transport` | 12569–12588 | VERIFIED |
| `BH-IIIF-C-0231` | `p3f:thm:v224-reference-cap-parent` | 12602–12644 | VERIFIED |
| `BH-IIIF-C-0232` | `p3f:prop:v224-collar-finite-transport` | 12689–12705 | VERIFIED |
| `BH-IIIF-C-0233` | `p3f:prop:v224-companion-descendant` | 12734–12760 | VERIFIED |
| `BH-IIIF-C-0234` | `p3f:cor:v228-derived-electron-pair` | 12954–12972 | VERIFIED |
| `BH-IIIF-C-0235` | `p3f:thm:v187-born-connection-parent-restriction` | 12992–13008 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0236` | `p3f:thm:v187-boundary-germ-schur-quotient` | 13010–13026 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0237` | `p3f:thm:v183-generated-boundary-owner` | 13047–13078 | REPRODUCED |
| `BH-IIIF-C-0238` | `p3f:def:v1113-q5-complement-transport-gate` | 13091–13111 | FORMALIZED |
| `BH-IIIF-C-0239` | `p3f:prop:v1113-q5-feshbach-specialization` | 13113–13133 | VERIFIED |
| `BH-IIIF-C-0240` | `p3f:thm:v1118-finite-source-operator-gap` | 13188–13208 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0241` | `p3f:prop:v1118-feshbach-propagation-not-genesis` | 13215–13233 | INCONSISTENT |
| `BH-IIIF-C-0242` | `p3f:cor:v1118-balanced-schur-return` | 13235–13246 | VERIFIED |
| `BH-IIIF-C-0243` | `p3f:prop:v1119-left-family-return` | 13264–13281 | VERIFIED |
| `BH-IIIF-C-0244` | `p3f:cor:v1119-orientation-visibility` | 13283–13291 | VERIFIED |
| `BH-IIIF-C-0245` | `p3f:cor:v1120-positive-return-target` | 13318–13329 | VERIFIED |
| `BH-IIIF-C-0246` | `p3f:cor:v1124-n7jet-closure` | 13335–13351 | REPRODUCED |
| `BH-IIIF-C-0247` | `p3f:thm:v1125-qroot-typing-no-go` | 13358–13373 | REPRODUCED |
| `BH-IIIF-C-0248` | `p3f:thm:v1128-qroot-neutral-constructor-closure` | 13388–13418 | REPRODUCED |
| `BH-IIIF-C-0249` | `p3f:thm:v1125-terminal-scalaron-schur-decoupling` | 13433–13465 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0250` | `p3f:prop:v245-terminal-legendre-schur-slope` | 13479–13501 | VERIFIED |
| `BH-IIIF-C-0251` | `p3f:prop:v1131-action-before-terminal-readout` | 13527–13541 | REPRODUCED |
| `BH-IIIF-C-0252` | `p3f:cor:v1132-charged-preterminal-member-handoff` | 13569–13587 | REPRODUCED |
| `BH-IIIF-C-0253` | `p3f:cor:v1132-charged-action-chronology` | 13596–13603 | REPRODUCED |
| `BH-IIIF-C-0254` | `p3f:cor:v1133-direct-mass-source-handoff` | 13611–13624 | REPRODUCED |
| `BH-IIIF-C-0255` | `p3f:thm:v1134-successor-cell-cayley` | 13641–13668 | VERIFIED |
| `BH-IIIF-C-0256` | `p3f:cor:v1134-hyperbolic-flow` | 13670–13684 | VERIFIED |
| `BH-IIIF-C-0257` | `p3f:thm:v1135-nested-stationary-boundary-descent` | 13703–13723 | VERIFIED |
| `BH-IIIF-C-0258` | `p3f:cor:v1135-internal-particle-response` | 13750–13766 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0259` | `p3f:cor:v1135-history-variation-internal-response` | 13768–13778 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0260` | `p3f:cor:v1136-fixed-datum-support` | 13785–13802 | VERIFIED |
| `BH-IIIF-C-0261` | `p3f:cor:v1136-direct-cell-no-efficiency` | 13815–13827 | REPRODUCED |
| `BH-IIIF-C-0262` | `p3f:thm:v1137-charge-preserving-schur` | 13834–13859 | VERIFIED |
| `BH-IIIF-C-0263` | `p3f:cor:v1137-charge-preserving-history-variation` | 13875–13889 | VERIFIED |
| `BH-IIIF-C-0264` | `p3f:cor:v1137-bl2-dirac-branch-no-go` | 13891–13908 | REPRODUCED |
| `BH-IIIF-C-0265` | `p3f:cor:v1139-bl2-boundary-pair-block` | 13915–13933 | REPRODUCED |
| `BH-IIIF-C-0266` | `p3f:cor:v1139-bl2-fixed-owner-transport` | 13935–13947 | REPRODUCED |
| `BH-IIIF-C-0267` | `p3f:cor:v1141-k48-fixed-owner-specialization` | 13954–13971 | REPRODUCED |
| `BH-IIIF-C-0268` | `p3f:def:v1141-k48-h-response-jet` | 13973–13989 | FORMALIZED |
| `BH-IIIF-C-0269` | `p3f:thm:v1142-k48-h-t5-schur-zero` | 14009–14040 | VERIFIED |
| `BH-IIIF-C-0270` | `p3f:cor:v1142-k48-quarter-no-schur-shift` | 14042–14054 | VERIFIED |
| `BH-IIIF-C-0271` | `p3f:thm:v1144-causal-dynamic-schur` | 14070–14100 | VERIFIED |
| `BH-IIIF-C-0272` | `p3f:cor:v1144-collisionless-source-schur` | 14102–14151 | REPRODUCED |
| `BH-IIIF-C-0273` | `p3f:cor:v1144-kinetic-limits` | 14153–14176 | VERIFIED |
| `BH-IIIF-C-0274` | `p3f:cor:v2202-improved-trace-handoff` | 14244–14260 | VERIFIED |
| `BH-IIIF-C-0275` | `p3f:cor:v2202-mass-map-selector` | 14279–14291 | VERIFIED |
| `BH-IIIF-C-0276` | `p3f:thm:v2202-hyperbolic-target` | 14304–14337 | VERIFIED |
| `BH-IIIF-C-0277` | `p3f:thm:v2202-free-band-selection` | 14357–14380 | VERIFIED |
| `BH-IIIF-C-0278` | `p3f:cor:v2202-terminal-diagnostics` | 14398–14425 | VERIFIED |
| `BH-IIIF-C-0279` | `p3f:thm:v2211-terminal-radial-obstruction` | 14444–14483 | VERIFIED |
| `BH-IIIF-C-0280` | `p3f:thm:v1140-finite-pole-source-transport` | 14524–14569 | VERIFIED |
| `BH-IIIF-C-0281` | `p3f:cor:schur-positive-gap-weight` | 14592–14610 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0282` | `p3f:cor:v1140-pole-transport-composition` | 14625–14630 | VERIFIED |
| `BH-IIIF-C-0283` | `p3f:thm:v199-second-schur-jet` | 14663–14681 | VERIFIED |
| `BH-IIIF-C-0284` | `p3f:cor:v199-moving-critical-eigenvalue` | 14694–14704 | VERIFIED |
| `BH-IIIF-C-0285` | `p3f:thm:v202-boundary-higher-vertices` | 14752–14769 | VERIFIED |
| `BH-IIIF-C-0286` | `p3f:cor:v202-critical-source-vertices` | 14779–14796 | VERIFIED |
| `BH-IIIF-C-0287` | `p3f:thm:v202-all-order-schur-residual` | 14807–14831 | VERIFIED |
| `BH-IIIF-C-0288` | `p3f:thm:v263-laurent-coefficient-character` | 14857–14892 | VERIFIED |
| `BH-IIIF-C-0289` | `p3f:thm:v263-dressed-born-legendre-descent` | 14910–14966 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0290` | `p3f:cor:v263-g24-dressing-placement-discharge` | 14990–15011 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0291` | `p3f:thm:v167-source-conditioned-boundary-schur` | 15018–15051 | VERIFIED |
| `BH-IIIF-C-0292` | `p3f:cor:regular-dual-boundary-restriction` | 15070–15082 | VERIFIED |
| `BH-IIIF-C-0293` | `p3f:cor:v167-boundary-third-variation` | 15097–15114 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0294` | `p3f:thm:v176-explicit-source-jet-schur` | 15116–15154 | VERIFIED |
| `BH-IIIF-C-0295` | `p3f:thm:v167-ward-schur-descent` | 15190–15210 | VERIFIED |
| `BH-IIIF-C-0296` | `p3f:thm:v167-terminal-schur-order` | 15232–15272 | VERIFIED |
| `BH-IIIF-C-0297` | `p3f:cor:v167-terminal-load-owner-firewall` | 15291–15308 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0298` | `p3f:prop:v2203-workport-ward` | 15340–15355 | VERIFIED |
| `BH-IIIF-C-0299` | `p3f:prop:v2203-workport-symmetry-onset` | 15422–15440 | VERIFIED |
| `BH-IIIF-C-0300` | `p3f:thm:v2203-complete-boundary-work` | 15454–15480 | VERIFIED |
| `BH-IIIF-C-0301` | `p3f:prop:v2203-two-work-ports` | 15551–15578 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0302` | `p3f:cor:v2203-workport-pressure-bounds` | 15598–15611 | VERIFIED |
| `BH-IIIF-C-0303` | `p3f:prop:v2203-euler-heat-third-jet` | 15658–15692 | VERIFIED |
| `BH-IIIF-C-0304` | `p3f:prop:v2203-anchored-work` | 15729–15750 | VERIFIED |
| `BH-IIIF-C-0305` | `p3f:prop:v2203-source-normalized-remainder` | 15769–15791 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0306` | `p3f:thm:v2203-euler-incidence` | 15828–15858 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0307` | `p3f:prop:v2203-euler-scalar-work` | 15880–15902 | VERIFIED |
| `BH-IIIF-C-0308` | `p3f:prop:v2203-conformal-completion` | 15931–15949 | VERIFIED |
| `BH-IIIF-C-0309` | `p3f:thm:v2203-active-boundary-square` | 15984–16020 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0310` | `p3f:thm:v2203-isolated-native-scalar-cold-obstruction` | 16047–16059 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0311` | `p3f:prop:v2203-stationary-envelope` | 16086–16097 | VERIFIED |
| `BH-IIIF-C-0312` | `p3f:prop:v2203-causal-mean-ports` | 16126–16149 | VERIFIED |
| `BH-IIIF-C-0313` | `p3f:prop:v2203-collisionless-memory-cancellation` | 16170–16183 | VERIFIED |
| `BH-IIIF-C-0314` | `p3f:prop:v2203-frozen-dirac-active-kernel` | 16193–16228 | VERIFIED |
| `BH-IIIF-C-0315` | `p3f:cor:v2203-no-second-minimal-mean` | 16247–16258 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0316` | `p3f:thm:v2203-terminal-boundary-budget` | 16278–16306 | VERIFIED |
| `BH-IIIF-C-0317` | `p3f:thm:v2203-local-source-cold-tail` | 16343–16370 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0318` | `p3f:prop:v2203-cold-energy-history` | 16392–16410 | VERIFIED |
| `BH-IIIF-C-0319` | `p3f:prop:v2203-frozen-late-influence` | 16433–16450 | VERIFIED |
| `BH-IIIF-C-0320` | `p3f:thm:v2205-closed-matched-work` | 16502–16532 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0321` | `p3f:cor:v2205-fixed-coefficient-response` | 16548–16587 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0322` | `p3f:prop:v2206-mixed-heat-jet` | 16624–16660 | VERIFIED |
| `BH-IIIF-C-0323` | `p3f:cor:v2206-metric-schur-jet` | 16670–16686 | VERIFIED |
| `BH-IIIF-C-0324` | `p3f:thm:v2206-loaded-static-energy` | 16694–16732 | VERIFIED |
| `BH-IIIF-C-0325` | `p3f:cor:v2206-passive-relaxation-sign` | 16743–16758 | VERIFIED |
| `BH-IIIF-C-0326` | `p3f:prop:v2207-static-temporal-identifiability` | 16800–16830 | VERIFIED |
| `BH-IIIF-C-0327` | `p3f:thm:v2207-quadratic-history-ports` | 16851–16896 | VERIFIED |
| `BH-IIIF-C-0328` | `p3f:thm:v2207-monotone-loading-sign` | 16911–16928 | VERIFIED |
| `BH-IIIF-C-0329` | `p3f:prop:v215-geometric-connection-comparisons` | 16980–17011 | REPRODUCED |
| `BH-IIIF-C-0330` | `p3f:cor:geo-singular-boundary-application` | 17033–17061 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0331` | `p3f:cor:geo-boundary-crossing-tests` | 17070–17094 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0332` | `p3f:prop:v215-cartan-scalar-gauge-restriction` | 17142–17181 | VERIFIED |
| `BH-IIIF-C-0333` | `p3f:cor:v215-cartan-n2-identification` | 17197–17219 | VERIFIED |
| `BH-IIIF-C-0334` | `p3f:prop:complete-source-cauchy-matrix` | 17252–17289 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0335` | `p3f:cor:v2174-scalar-coordinate-bound` | 17333–17346 | VERIFIED |
| `BH-IIIF-C-0336` | `p3f:prop:native-spherical-kinetic-determinant` | 17361–17400 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0337` | `p3f:prop:native-source-curvature-trace` | 17427–17437 | VERIFIED |
| `BH-IIIF-C-0338` | `p3f:thm:native-spherical-local-cauchy` | 17456–17513 | REPRODUCED |
| `BH-IIIF-C-0339` | `p3f:cor:native-spherical-canonical-matching` | 17536–17556 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0340` | `p3f:prop:spherical-quadratic-principal-block` | 17580–17603 | VERIFIED |
| `BH-IIIF-C-0341` | `p3f:lem:v2190-source-orbit-form` | 17639–17667 | VERIFIED |
| `BH-IIIF-C-0342` | `p3f:thm:v2190-joint-characteristic-flow` | 17688–17733 | REPRODUCED |
| `BH-IIIF-C-0343` | `p3f:cor:v2190-local-interacting-graph` | 17768–17783 | REPRODUCED |
| `BH-IIIF-C-0344` | `p3f:cor:v2190-complete-gauge-constraint` | 17794–17810 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0345` | `p3f:prop:v2216-curvature-contacts` | 17852–17876 | VERIFIED |
| `BH-IIIF-C-0346` | `p3f:thm:v2216-causal-ricci-inverse` | 17888–17911 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0347` | `p3f:thm:v2216-physical-hopf-mode` | 17938–17965 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0348` | `p3f:prop:v2216-source-chain-rule` | 17991–18031 | VERIFIED |
| `BH-IIIF-C-0349` | `p3f:prop:v2216-complete-metric-work` | 18048–18068 | VERIFIED |
| `BH-IIIF-C-0350` | `p3f:cor:v2217-source-test-execution` | 18084–18105 | REPRODUCED |
| `BH-IIIF-C-0351` | `p3f:thm:v2216-shared-response` | 18147–18174 | VERIFIED |
| `BH-IIIF-C-0352` | `p3f:thm:v2216-source-response` | 18211–18250 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0353` | `p3f:prop:v2216-source-spectral-moments` | 18266–18292 | VERIFIED |
| `BH-IIIF-C-0354` | `p3f:cor:v2216-source-full-poles` | 18335–18344 | REPRODUCED |
| `BH-IIIF-C-0355` | `p3f:thm:v2216-cold-tail-bv` | 18385–18419 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0356` | `p3f:cor:v2216-cold-tail-finite-errors` | 18432–18443 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0357` | `p3f:cor:v2217-sign-population-tail` | 18454–18469 | VERIFIED |
| `BH-IIIF-C-0358` | `p3f:thm:v2216-coupled-normal-form` | 18505–18537 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0359` | `p3f:thm:v2216-terminal-momentum-budget` | 18560–18583 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0360` | `p3f:thm:v2216-local-terminal-handoff` | 18611–18638 | REPRODUCED |
| `BH-IIIF-C-0361` | `p3f:thm:v2216-corner-energy` | 18667–18687 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0362` | `p3f:thm:v2216-finite-locality` | 18709–18727 | REPRODUCED |
| `BH-IIIF-C-0363` | `p3f:thm:v2216-action-residual-control` | 18756–18788 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0364` | `p3f:prop:v2209-inherited-schur-square` | 18838–18860 | VERIFIED |
| `BH-IIIF-C-0365` | `p3f:cor:v2209-analytic-criticality` | 18873–18881 | REPRODUCED |
| `BH-IIIF-C-0366` | `p3f:thm:v2209-geometric-transfer` | 18892–18930 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0367` | `p3f:prop:v2209-complete-normal-turnover` | 18956–18979 | REPRODUCED |
| `BH-IIIF-C-0368` | `p3f:prop:v2210-lit-support-curvature` | 19031–19051 | VERIFIED |
| `BH-IIIF-C-0369` | `p3f:thm:v2210-lit-transverse-operator` | 19063–19120 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0370` | `p3f:cor:v2210-lit-native-potential-contact` | 19143–19177 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0371` | `p3f:cor:v2210-lit-closed-kinetic-test` | 19199–19222 | REPRODUCED |
| `BH-IIIF-C-0372` | `p3f:cor:v2210-lit-canonical-pump` | 19230–19250 | VERIFIED |
| `BH-IIIF-C-0373` | `p3f:prop:v2210-lit-transfer-energy` | 19260–19276 | REPRODUCED |
| `BH-IIIF-C-0374` | `p3f:thm:v2210-lit-boundary-jets` | 19291–19331 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0375` | `p3f:thm:v286-same-action-grade-four-survival` | 19358–19397 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0376` | `p3f:thm:v287-three-jet-frr-consistency` | 19417–19462 | REPRODUCED |
| `BH-IIIF-C-0377` | `p3f:prop:v2210-lit-gaussian-jets` | 19480–19501 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0378` | `p3f:cor:v2210-lit-overlap-test` | 19512–19529 | REPRODUCED |
| `BH-IIIF-C-0379` | `p3f:prop:v2210-lit-analytic-projection` | 19545–19559 | REPRODUCED |
| `BH-IIIF-C-0380` | `p3f:prop:v2210-lit-causal-support` | 19573–19583 | REPRODUCED |
| `BH-IIIF-C-0381` | `p3f:prop:v2210-lit-static-integrability` | 19594–19611 | REPRODUCED |
| `BH-IIIF-C-0382` | `p3f:prop:v2212-conformal-heat-load` | 19658–19700 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0383` | `p3f:cor:v2212-conformal-shape-contacts` | 19718–19747 | VERIFIED |
| `BH-IIIF-C-0384` | `p3f:prop:v2212-weyl-conformal-weight` | 19759–19773 | REPRODUCED |
| `BH-IIIF-C-0385` | `p3f:prop:v2212-dirac-a6-einstein` | 19784–19812 | REPRODUCED |
| `BH-IIIF-C-0386` | `p3f:thm:v2212-a6-kottler-ports` | 19860–19917 | REPRODUCED |
| `BH-IIIF-C-0387` | `p3f:cor:v2212-scalar-overlap-tidal-ports` | 19972–19984 | VERIFIED |
| `BH-IIIF-C-0388` | `p3f:thm:v226-response-reconstruction` | 20668–20682 | REPRODUCED |
| `BH-IIIF-C-0389` | `p3f:cor:v227-finite-handoff` | 20704–20713 | REPRODUCED |
| `BH-IIIF-C-0390` | `p3f:prop:v246-charged-marked-isospectral-ambiguity` | 20736–20770 | VERIFIED |
| `BH-IIIF-C-0391` | `p3f:prop:v246-electron-spectral-floor-test` | 20799–20812 | VERIFIED |
| `BH-IIIF-C-0392` | `p3f:prop:v246-cap-metric-hessian-defect` | 20826–20857 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0393` | `p3f:prop:v246-singular-scalaron-cancellation` | 20887–20903 | VERIFIED |
| `BH-IIIF-C-0394` | `p3f:prop:v246-causal-hessian-integrability` | 20930–20941 | VERIFIED |
| `BH-IIIF-C-0395` | `p3f:thm:v246-finite-source-influence-parent` | 20961–21007 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0396` | `p3f:cor:v246-finite-mean-source-euler-parent` | 21047–21079 | REPRODUCED |
| `BH-IIIF-C-0397` | `p3f:thm:v247-native-influence-ward` | 21114–21176 | REPRODUCED |
| `BH-IIIF-C-0398` | `p3f:cor:v247-native-causal-cauchy-equivalence` | 21206–21225 | REPRODUCED |
| `BH-IIIF-C-0399` | `p3f:prop:v247-native-causal-continuation` | 21244–21276 | REPRODUCED |
| `BH-IIIF-C-0400` | `p3f:prop:v247-native-curvature-orbit-bounds` | 21297–21325 | VERIFIED |
| `BH-IIIF-C-0401` | `p3f:thm:v248-native-constant-vacua` | 21360–21420 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0402` | `p3f:prop:v248-native-vacuum-masses` | 21442–21468 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0403` | `p3f:cor:v248-bare-all-rank-vacuum` | 21506–21536 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0404` | `p3f:cor:v248-quartic-vacuum-promotion` | 21554–21567 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0405` | `p3f:prop:v249-fixed-current-source-nonimplication` | 21607–21658 | VERIFIED |
| `BH-IIIF-C-0406` | `p3f:prop:v249-fourth-moment-right-overlap` | 21683–21727 | VERIFIED |
| `BH-IIIF-C-0407` | `p3f:thm:v249-native-vacuum-correction-budget` | 21776–21823 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0408` | `p3f:prop:v249-weighted-remainder-budget` | 21842–21885 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0409` | `p3f:thm:v249-evaluated-raw-a6-vacuum` | 21900–21923 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0410` | `p3f:prop:v250-boson-elimination-fermion-jet` | 21978–22015 | REPRODUCED |
| `BH-IIIF-C-0411` | `p3f:prop:v250-native-scalar-variation-scope` | 22031–22049 | REPRODUCED |
| `BH-IIIF-C-0412` | `p3f:prop:v250-zero-scalar-member-fibre` | 22061–22081 | REPRODUCED |
| `BH-IIIF-C-0413` | `p3f:thm:v250-exact-heat-homothety` | 22115–22141 | VERIFIED |
| `BH-IIIF-C-0414` | `p3f:prop:v250-native-product-heat-scale` | 22165–22196 | VERIFIED |
| `BH-IIIF-C-0415` | `p3f:thm:v250-exact-parallel-scalar-heat` | 22207–22254 | VERIFIED |
| `BH-IIIF-C-0416` | `p3f:prop:v251-primitive-canonical-scalar-packet` | 22341–22365 | VERIFIED |
| `BH-IIIF-C-0417` | `p3f:prop:v251-native-scalar-mixed-jets` | 22399–22425 | VERIFIED |
| `BH-IIIF-C-0418` | `p3f:thm:v251-forward-causal-native-packet` | 22472–22526 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0419` | `p3f:prop:v251-forward-source-trace-operator` | 22591–22621 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0420` | `p3f:prop:v251-forward-source-trace-sign` | 22635–22656 | VERIFIED |
| `BH-IIIF-C-0421` | `p3f:thm:v251-forward-higgs-hyperbolic-target` | 22721–22748 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0422` | `p3f:cor:v257-native-force-margin` | 22772–22797 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0423` | `p3f:thm:v251-forward-bare-radial-global-future` | 22846–22872 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0424` | `p3f:cor:v260-canonical-exchange` | 22934–22969 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0425` | `p3f:prop:v260-jordan-flux` | 22983–23015 | REPRODUCED |
| `BH-IIIF-C-0426` | `p3f:cor:v260-conormal-jordan-distinction` | 23042–23056 | REPRODUCED |
| `BH-IIIF-C-0427` | `p3f:thm:v275-joint-positive-action-jets` | 23073–23123 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0428` | `p3f:thm:v289-complete-source-twojet` | 23163–23187 | VERIFIED |
| `BH-IIIF-C-0429` | `p3f:prop:v289-flrw-tensor-obstruction` | 23205–23242 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0430` | `p3f:thm:v319-petersen-mirror-contact` | 23288–23308 | VERIFIED |
| `BH-IIIF-C-0431` | `p3f:cor:v319-petersen-response-owner` | 23317–23328 | REPRODUCED |
| `BH-IIIF-C-0432` | `p3f:prop:v338-no-unique-two-core-mass-map` | 23352–23365 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0433` | `p3f:thm:v346-near-terminal-active-vacuum` | 23396–23414 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0434` | `p3f:cor:v346-active-vacuum-scalaron` | 23438–23453 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0435` | `p3f:prop:v353-projector-transversality` | 23489–23514 | VERIFIED |
| `BH-IIIF-C-0436` | `p3f:thm:v353-interior-parity` | 23529–23547 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0437` | `p3f:prop:v353-chiral-mixed-jet` | 23556–23585 | VERIFIED |
| `BH-IIIF-C-0438` | `p3f:prop:v353-observable-quadratic` | 23612–23633 | VERIFIED |
| `BH-IIIF-C-0439` | `p3f:prop:v358-native-photon-cone-scope` | 23645–23660 | VERIFIED-CONDITIONAL |
| `BH-IIIF-C-0440` | `p3f:prop:v358-photon-heat-hessian` | 23669–23690 | VERIFIED |
| `BH-IIIF-C-0441` | `p3f:cor:v358-photon-gauge-orbit` | 23699–23715 | VERIFIED |
| `BH-IIIF-C-0442` | `p3f:prop:v358-local-photon-cone-test` | 23722–23738 | VERIFIED |

## Canonical assumption condition registry
Every distinct condition appears once at its earliest verified current-source occurrence. Use edges inherit condition IDs; they do not create new GP1–GP3 axioms or assert automatic fulfillment. Conditional physical branches and actual action/occupancy selection are kept distinct from algebraic identities.
| Condition ID | First origin line | Specialized scoped predicate |
|---|---:|---|
| `BH-IIIF-A-0001` | 495 | QLOC: for all N, ∥[q(D²/Λ²)M_aq(D²/Λ²),q(D²/Λ²)M_bq(D²/Λ²)]∥≤C_N∥a∥∞∥b∥∞(1+Λd(E,F))^{−N} for separated E,F, Λ≥Λ₀ on specified local elliptic realization |
| `BH-IIIF-A-0002` | 2088 | For Q=q(D²/Λ²), D self-adjoint wave group finite-speed v>0 and r(s)=q(s²) with Fourier transform of r² integrable with all-orders polynomial tail decay |
| `BH-IIIF-A-0003` | 2133 | L=D²≥0 complete Davies–Gaffney representative and q(z)=∫ e^(−tz)dν(t) for finite complex/real Borel ν |
| `BH-IIIF-A-0004` | 2146 | LAP-MOM: ω=ν*ν finite total variation and ∫s^m d\|ω\|(s)<∞ for every integer m≥0; for fixed target order N, one m with 2m≥N suffices |
| `BH-IIIF-A-0005` | 243 | The physically occurring minimal local action has configuration functor Met(U)×∏Γ_c(E_i), with the compact momentum carrier as a coefficient representation rather than varied local section. VDOMx is its derived tangent, not a new selector. |
| `BH-IIIF-A-0006` | 300 | Optional generic zero-derivative local-action member REN0(Λren) with E^(0)_μν=Λren g_μν for a declared real Λren; not selected by the protected bare scalar coefficient. |
| `BH-IIIF-A-0007` | 308 | Specialized zero-term-free member REN0^0: Λren=0, strictly stronger than the generic REN0(Λren) family; not inferred from one background subtraction. |
| `BH-IIIF-A-0008` | 313 | Exact higher-curvature metric Euler variation E_{≥4}=0 on stated metric/field/boundary domain, a sufficient exact two-derivative Einstein branch. |
| `BH-IIIF-A-0009` | 319 | IR_{2∂}(ε*): higher-curvature Euler variation norm bounded by ε* relative to EH variation on specified field/domain class; distinct approximation branch, NOT equivalent to exact E_{≥4}=0. |
| `BH-IIIF-A-0010` | 382 | SOLHIST^phys_U: a particular actual world history is selected as an on-shell member [q_world]∈M_stat,U([S_L]); stationary family derivation alone does not select this member. |
| `BH-IIIF-A-0011` | 403 | GRED7^phys: for the optional diagonal-fibre reduction, a physical member (g_F,∇^fluc_iso,R_act) compatible with already-derived X7,U^can and ω_B and normalized Einstein coefficient is physically realized/adopted. Not used in premise-minimal JOINT chain. |
| `BH-IIIF-A-0012` | 443 | CAL_GRED: supply basis/convention and metric Γ_AB=κ r_fib² δ_AB plus YM normalization, without assuming the separate optional compact-cell saturation. No physical coefficient fixed without declared calibration. |
| `BH-IIIF-A-0013` | 467 | BULK8: optional Born-equivariant comparison on Y8 with equal reciprocal-pair auxiliary metrics, normalized comparison measures, Born-invariant L8≥0 Laplace-type operator, and standard smooth heat expansion incl. separate fixed-set terms; no physical time/energy moduli. |
| `BH-IIIF-A-0014` | 482 | MATCH_{8→7}: optional supplied result-independent normalized-volume map matching projected eight-dimensional bulk coefficient to physical seven-dimensional Einstein coefficient; not implied by Born exchange or GRED7. |
| `BH-IIIF-A-0015` | 1032 | ID_{F/A}: separately chosen numerical scale equality ΛF=Λcut; sharp scalar spectral frontier theorem does not use this match. |
| `BH-IIIF-A-0016` | 446 | CELL_GRED_SAT: optional compact-fibre cell saturation r_fib Λcut=1, strictly more specific than the GRED generator-metric calibration alone. |
| `BH-IIIF-A-0017` | 2316 | C39 finite Euclidean background gauge domain: compatible windows/constant ranks, real positive physical nonzero block, all exact zero modes and actual quotient measure retained. |
| `BH-IIIF-A-0018` | 2427 | C41 relative SU2×U1 scalar operators are bi-invariant on SU2, translation invariant U1, Born inversion even and order ≤2. |
| `BH-IIIF-A-0019` | 2463 | C43 stationary round metric and canonically normalized real local quartic scalar member restricted to 14D comparison band; not a physical m_p=2 statement. |
| `BH-IIIF-A-0020` | 2513 | C44 physical rooted quartic application requires the actual preterminal source-incidence map and the same unrenormalized rooted quadratic/quartic action word. |
| `BH-IIIF-A-0021` | 2644 | C46 finite rooted phase Gram becomes an action Hessian only when source frame and stationary Qperp interior belong to one actual physically licensed action. |
| `BH-IIIF-A-0022` | 2800 | C51 physical K16 boundary/trace preserves TT subspace and the same-action internal Hessian is invertible on the declared quotient. |
| `BH-IIIF-A-0023` | 2837 | C52 complete licensed finite CAR/actually finite bosonic quantum word has positive fixed-rank kinetic Gram and all consumed metric/field/constraint/interaction/source jets. |
| `BH-IIIF-A-0024` | 3249 | C56 TT contact evaluates on homogeneous isotropic parity-balanced unpolarized FREE source, with excluded vector/spin/axial background bilinears vanishing. |
| `BH-IIIF-A-0025` | 3354 | C58 source calculation requires an occurring marked A5 and the existing upper coupled j=9/2, ell=5 Dirac source block; physical occupation separately owned. |
| `BH-IIIF-A-0026` | 3462 | C59 exact nilpotent finite Grassmann and even complete parent action with regular selected bosonic stationary solution and invertible C on quotient. |
| `BH-IIIF-A-0027` | 3630 | C63 actual consumed classical parent and BL2 are baryon invariant, stationary solution unique/equivariant, and quantum/constraint/charge frame respects baryon action. |
| `BH-IIIF-A-0028` | 3772 | C66 inherited active f(R) Legendre chart chi>0, non-null smooth boundary fixed h and F, and separate native M² physical projection matching as asserted. |
| `BH-IIIF-A-0029` | 3893 | C67 actually generated constant invariant free Dirac mass on compatible spin region with no omitted interactions or endpoint forces; not a full K16 particle packet. |
| `BH-IIIF-A-0030` | 4078 | C69 exact FLRW interpretation of finite averaged energy requires true homogeneous energy, isotropic stress and vanishing spatial flux, certified for a full invariant multiplet/state. |
| `BH-IIIF-A-0031` | 4317 | Compact-support local analytic multiplier equals one near U0 and field variations are compactly supported inside U0. |
| `BH-IIIF-A-0032` | 4367 | Smooth local semiclassical derivative expansion with generated C_IR^der and GRAV-ASYM; no claim of exact trace or unconditional Lorentzian action. |
| `BH-IIIF-A-0033` | 4483 | One ordinary joint trace, no inserted central projector/weight; real parity-even O(4) positive derivative-free quadratic curvature functional. |
| `BH-IIIF-A-0034` | 4553 | Stationary smooth globally hyperbolic clock product with CAUS, positive Qrho, closed/support boundary, and no principal-order deformation. |
| `BH-IIIF-A-0035` | 4587 | Holomorphic Euclidean/Lorentzian connection and gauge first jets under oriented tau=i t, with no extra contour-end term. |
| `BH-IIIF-A-0036` | 4905 | For broader-than-native gauge branch, claim-specific same-variable Lorentz realization preserving generated metric conformal class, field identity and principal coefficient. |
| `BH-IIIF-A-0037` | 4976 | Smooth local four-dimensional spin Dirac owner, Lichnerowicz Laplace convention, common-heat joint carrier, parity-even local heat a2 and interior compact variations. |
| `BH-IIIF-A-0038` | 4976 | Holomorphic lapse/spatial metric/first clock derivatives, oriented zero-shift clock continuation with no untransported boundary term. |
| `BH-IIIF-A-0039` | 5091 | Physical G requires an actual action/metric/source normalization projection whose EH coefficient and all consumed mixed source/stress/boundary jets match, not only raw trace 96. |
| `BH-IIIF-A-0040` | 5178 | Optional constituted smooth non-null boundary with local chirality-projector mixed D_A² self-adjoint conditions, transported boundary and no null/corner/asymptotic extension. |
| `BH-IIIF-A-0041` | 5225 | Hermitian generated odd Φ and native common-heat local a2/a4, nonmetric 1/2 role; holomorphic first jets to continue the Lorentzian scalar action. |
| `BH-IIIF-A-0042` | 5417 | Gauge/diffeomorphism acting on complete local bosonic owner preserves every source, coupling, grading, localizer, boundary, orientation and other mark, with compact support. |
| `BH-IIIF-A-0043` | 5611 | Admitted fixed linear odd scalar source R whose Gram is positive on a claim-complete support; polar normalization and coordinate maps keep its physical image/owner. |
| `BH-IIIF-A-0044` | 5689 | An actual stationary solution, valid gauge/constraint reduction, no gyrokinetic cross term, and time-independent M>0, L>=0 on its real physical block. |
| `BH-IIIF-A-0045` | 5971 | Canonically normalized constant linear odd ray, F=κJ-h²/12>0 and fixed Fref; stationary potential required for Hessian pole and all coupled sectors retained. |
| `BH-IIIF-A-0046` | 6080 | Local Einstein–YM–odd-scalar ADM owner on interior closed/support slice with κJ>0, F(Φ) !=0, and positive graviton branch F>0 where claimed. |
| `BH-IIIF-A-0047` | 6287 | Finite local heat polynomial with nondegenerate holomorphic common metric/clock/field jets and an oriented transported interior/boundary problem; not exact full heat. |
| `BH-IIIF-A-0048` | 6477 | Irreducible complex Lorentz Clifford spinor, admissible positive future clock-normal Hermitizing line, native identity internal pairing with no inserted K_L/K_R. |
| `BH-IIIF-A-0049` | 6541 | A specific Dirac/Yukawa member is independently generated from an occurring root by licensed finite geometric constructor and actually matches the consumed fermion slot. |
| `BH-IIIF-A-0050` | 6574 | Complete local finite bosonic+ordered quadratic odd action A+cF barpsi D(q) psi, cF>0. |
| `BH-IIIF-A-0051` | 6613 | Actual chiral D_LR coefficient has independently generated charge-source incidence and required charged Cert_hier certificate. |
| `BH-IIIF-A-0052` | 6642 | Two isometric port frames with j0*j1=sqrt(24/25)I and explicitly specified left/right assignment within same action. |
| `BH-IIIF-A-0053` | 6693 | Complete local ACTcl action; exact finite target, equalizer, GP2 quotient and declared stationary family sort, without chosen member. |
| `BH-IIIF-A-0054` | 6815 | Actual scalar-action coefficient satisfies Paper3B action/contact normalized root and zero defect; physical chi7 additionally passes Paper3D fixed-depth excess. |
| `BH-IIIF-A-0055` | 6899 | Fixed scheme sigma and connected positive R range of horizontal L_U determinant-dual coefficient line on certified contact action. |
| `BH-IIIF-A-0056` | 7172 | g C2 nondegenerate Lorentz, compactly supported inverse metric variations, f C1 in neighborhood and phi=fprime(R) C2 there; admitted action continuation. |
| `BH-IIIF-A-0057` | 7131 | On an occurring complete-cap fresh root rho0=p0=0, renormalized quantum excitation Hilbert stress has zero expectation. |
| `BH-IIIF-A-0058` | 7336 | Generated undressed bare coefficient first-response constructor and retained fbar(C)=0 on positive separated roots 0<C<U. |
| `BH-IIIF-A-0059` | 7392 | Composed candidate fQ with fixed Q=8 sqrt(alpha), visibility y and finite Psi orbit, physical incidence not independently selected. |
| `BH-IIIF-A-0060` | 7555 | On fixed visibility parent R_tau=C exp(H exp(-tau)), admit active curvature equal to hierarchy readout; tau is not physical time. |
| `BH-IIIF-A-0061` | 7625 | Additional same-parent signed two-sided UV quadratic scalaron action through R_J=0 with coefficient Q/U, distinct from IR chart. |
| `BH-IIIF-A-0062` | 7672 | Separately owned homogeneous s(t) coefficient A(s)>0 in UV action, with its metric variation in the same total stress source. |
| `BH-IIIF-A-0063` | 7748 | Exact conditional cap first-order auxiliary owner, smooth non-null Dirichlet boundary with h and Phi fixed, rest independent of auxiliaries. |
| `BH-IIIF-A-0064` | 7821 | On cap coefficient anchors 2B_U>d=1-B_U/B_I, positive regular Hessian and Phi branch. |
| `BH-IIIF-A-0065` | 7865 | Cap e in (0,1), B_U>2, p e>8, p>1 and B_I<=p for one positive vacuum root. |
| `BH-IIIF-A-0066` | 7967 | Finite Dirichlet-Neumann fixed reference width lambda>0 and fixed metric geometry with matching B_lambda used in both source and gravity. |
| `BH-IIIF-A-0067` | 8074 | Collar extension is integrated as independent Gaussian field with fixed L2 measure and claimed multiplicity m_c. |
| `BH-IIIF-A-0068` | 8380 | Complete same-action quotient physical retarded inverse for eliminated source block and reduced retained metric/scalar response. |
| `BH-IIIF-A-0069` | 8417 | Compact Euclidean joint Dirac heat e^-A is trace class with differentiable A and mixed jets, unlocalized for trace-cyclic second variation. |
| `BH-IIIF-A-0070` | 8448 | Pure ordinary torsion-free Dirac metric a4/a6 heat on conformally flat restricted metric test; full zeta6 common-heat normalization uncalculated. |
| `BH-IIIF-A-0071` | 8538 | Constrained causal physical scalaron chart has fRR(R0)!=0 and a retarded invertible remaining block with compatible source normalization. |
| `BH-IIIF-A-0072` | 8673 | Stationary real Ward/constraint quotient has strictly positive self-adjoint boundedly invertible eliminated Cw block. |
| `BH-IIIF-A-0073` | 8738 | Operator D(s)^2 analytic on compact fixed-domain uniformly analytic trace-class heat patch, with transverse analytic R(s) crossing C2. |
| `BH-IIIF-A-0074` | 8793 | On regular homogeneous isotropic A=0 background, external EM current zero and local common action has no linear photon term for nearby z. |
| `BH-IIIF-A-0075` | 8847 | Source-free four-dimensional native local odd-scalar and metric Euler on shell with metric-independent internal Yang-Mills pairing. |
| `BH-IIIF-A-0076` | 8887 | Trace-orthonormal gauge-stable real odd support of dimension N with F=kJ-r²/12>0; N>=2 for sectional curvature statement. |
| `BH-IIIF-A-0077` | 8922 | Additionally constituted smooth non-null boundary with fixed induced metric and odd scalar for local nonminimal F(Ph)R term. |
| `BH-IIIF-A-0078` | 8955 | Actual localized heat owner L=phi_U and D have all first/mixed second metric/source/coframe jets, with trace-class Duhamel legitimacy. |
| `BH-IIIF-A-0079` | 9004 | Compact selfadjoint midpoint weak Dirac has protected projector P, complement gap g and \|\|QVQ\|\|+\|z\|<g. |
| `BH-IIIF-A-0080` | 9114 | Complete same-action W(R,z) with invertible stationary Hessian Hzz; dynamic scalaron pole additionally uses full kinetic-normalized retarded inverse. |
| `BH-IIIF-A-0081` | 9169 | Bare undressed same-action f_b, 0<C<U, no separate Lambda, source-free constant scalar curvature, action domain [C,U]. |
| `BH-IIIF-A-0082` | 9254 | Euler endpoint P(C7)=C7 with paired TERM and REN in one physical action, raw ZC>0 for normalized end datum; action and source scale jointly. |
| `BH-IIIF-A-0083` | 9383 | Historical rank-two junction uses source-matched identical geometric metric and excludes an independent surface curvature/distributional stress layer; current continuity alone is insufficient. |
| `BH-IIIF-A-0084` | 9566 | Differentiable family of four-dimensional metric trace equations at a constant-background R0,T0 with fixed Lambda; f twice differentiable at R0 and regular d/dε commute with Box; fsecond nonzero only on wave branch. |
| `BH-IIIF-A-0085` | 9670 | Four-dimensional Riemannian constant scalar background with C2 F(R), compact support or boundaryless integration-by-parts, and conformal g=exp(2σ)gbar. |
| `BH-IIIF-A-0086` | 9803 | ACT_MRESP direct or source-certified classical-continuation normalized action on compact interior U0, complete matter source and local MRESPcl regularity. |
| `BH-IIIF-A-0087` | 10020 | Generated Paper III-B ratio diffeomorphism j_x, scalar-diagonal SU2 quotient, and actual III-A reciprocal position chart U. |
| `BH-IIIF-A-0088` | 10078 | Parent-generated basic SU2 midpoint connection ωB=1/2(θx+θp) and exact Born action; full holonomy and fibre-spin images are derived. |
| `BH-IIIF-A-0089` | 10222 | Generated P_B/ω_B and both multiplication-side embeddings into Spin(4), faithful W_L⊕W_R, any nonzero generated finite spectator K; no independent fluctuations. |
| `BH-IIIF-A-0090` | 10415 | Native spatial Cartan insertion u=εq3 with \|ε\|≤1 for uniqueness, nonhomogeneous-gap prerequisite; exact mode exists for all permitted finite ε. |
| `BH-IIIF-A-0091` | 10529 | Native selfadjoint spatial Dirac with simple zero and gap g, bounded perturbation V of size w, and \|e\|+w\|t\|<g/90. |
| `BH-IIIF-A-0092` | 10660 | Generated principal vertical SU2 role with induced inversion-equivariant lift on source spatial sphere and specified M8 relative quotient; not an arbitrary U2 bundle. |
| `BH-IIIF-A-0093` | 10779 | Specified round homogeneous SU2 Yang–Mills pure-gauge A=fΘ branch and physical gauge quotient; no claim for complete matter-coupled Hessian. |
| `BH-IIIF-A-0094` | 10823 | Imported Paper V-A common-heat g2²=2π² matched to same round Yang–Mills group and proper time t=Rτ. |
| `BH-IIIF-A-0095` | 10936 | Optional GRED7 homogeneous physical round-fibre connection member, equal auxiliary vector round metric factors, normalized Haar measure; fibre radius r_fib=Rmom. |
| `BH-IIIF-A-0096` | 10970 | Generator conventions κ and normalized Γ_AB=κr_fib²δ_AB and source YM coefficient convention; κ=1 vs κ=1/4 are distinct basis choices. |
| `BH-IIIF-A-0097` | 11206 | Semiclassical Euclidean local spectral derivative action in U0 with QLOC bound and complete higher-derivative remainder. |
| `BH-IIIF-A-0098` | 11231 | Actually occurring LORdir or source/field-matched CONTcl plus normed IR2∂(ε*) bound on retained higher-variation terms. |
| `BH-IIIF-A-0099` | 11315 | Zero shift c=1, fixed matter fields during metric variation and T covariant source sign, on a regular ADM chart. |
| `BH-IIIF-A-0100` | 11334 | k>0, fixed f(0)=f0 on decaying/finite-energy half-line with Dirichlet inverse and admissible j dual pairings. |
| `BH-IIIF-A-0101` | 11367 | Smooth selfadjoint block family with fixed retained Hilbert spaces, moving complementary stationary section and inverse C; preserve derivative of projector. |
| `BH-IIIF-A-0102` | 11405 | Terminal chi small with \|\|Cchi^-1\|\|=O(chi), uniformly bounded cross-blocks and regular N inverse; background memory may persist. |
| `BH-IIIF-A-0103` | 11448 | One fixed R,L,E owner splitting, shared regular spectral zeta, full source B, resolved coupled return and actual source insertion. |
| `BH-IIIF-A-0104` | 11544 | Inherited full-rank Jm tensor I_G family intertwiner and Gpm tensor I_G positive kinetic action, no independent external frame. |
| `BH-IIIF-A-0105` | 11618 | Complete canonically normalized actual tagged left source and current with all Gram/cross terms, not simply unmarked eigenvalues. |
| `BH-IIIF-A-0106` | 11686 | Actual native hierarchy support/arrow incidence, e-mu/mu-tau orthogonality and e-tau endpoint retained when present. |
| `BH-IIIF-A-0107` | 11832 | Complete charged sectors with true positive inherited multiplicity and rooted first moments; heat certificate requires same complete source. |
| `BH-IIIF-A-0108` | 11885 | Actual 3x3 chiral square block from a single already-licensed local action on exact factorized Euclidean scalar heat branch. |
| `BH-IIIF-A-0109` | 12021 | Tagged left current and right Gram/jet contractions measured in same actual canonical Hessian, with right mixing not suppressed. |
| `BH-IIIF-A-0110` | 12193 | Stationary finite clock with complete free quadratic rest symbol and generated local Lorentz Clifford derivative; no interacting pole conclusion. |
| `BH-IIIF-A-0111` | 12473 | Torsion-free pure-metric Dirac specialization, native internal rank 48, protected scalar weight 1/8 and fixed common heat convention. |
| `BH-IIIF-A-0112` | 12506 | Full metric-plus-matter source variation including stress and contacts, first-order local field redefinition, no missing matter transport. |
| `BH-IIIF-A-0113` | 12604 | Finite reference boundary source with BI>BU>0, ell,Rs>0, HS-unit M, signed stationary parent; action occurrence separate. |
| `BH-IIIF-A-0114` | 13012 | Already generated Born parent and regular nested stationary boundary quotient, no independently chosen configuration/retarded history. |
| `BH-IIIF-A-0115` | 13093 | Optional Q5 complement transport with declared invertible paired block, compatible owners and licensed source-word; not first genesis. |
| `BH-IIIF-A-0116` | 13190 | Source-preserving Euclidean branch with D_A² nonnegative, covariantly constant terminal Phi and Phi_T² >=mT²I. |
| `BH-IIIF-A-0117` | 13217 | Full rank paired rectangular coupling condition actually printed, insufficient for positive sigma_min of A_L U A_R dagger without compatible subspace alignment. |
| `BH-IIIF-A-0118` | 13337 | Terminal N7JET and existing neutral source grammar imported as a conditional certified jet, not new action occurrence. |
| `BH-IIIF-A-0119` | 13360 | Only licensed neutral constructor/source grammar and already established Fock/positive words; no ambient unrestricted rooted selector. |
| `BH-IIIF-A-0120` | 13435 | Same action with invertible regular retained Hessian and smooth terminal Legendre scalaron map, residual neutral mixing kept. |
| `BH-IIIF-A-0121` | 13529 | Upstream Paper V-A mass-labelled charged packet certified and sourced before noninjective action readouts; not independent new mass derivation. |
| `BH-IIIF-A-0122` | 13643 | Source-certified successor-cell stationary boundary, normalized rho in [0,1], G>0 and fixed response owner; transport not source genesis. |
| `BH-IIIF-A-0123` | 13705 | One occurring stationary action with P,B,I owner decomposition and invertible/gauge-fixed Schur blocks, actual physical J_P separately licensed. |
| `BH-IIIF-A-0124` | 13836 | Graded charge operator commuting with complete Hessian and invariant regular eliminated quotient; charge fixed under history variation. |
| `BH-IIIF-A-0125` | 13917 | Distinct physical BL2 pair source with charge ±2 in K16 branch; cannot be silently imported into neutral Dirac branch. |
| `BH-IIIF-A-0126` | 13956 | Homogeneous K48 H scalar and nontrivial two-dimensional C3 T5, unbroken equivariant quadratic Hessian, separate endpoint datum. |
| `BH-IIIF-A-0127` | 14072 | Occurring causal source/field system, retarded-invertible Cdyn(z) with correct dynamical non-Hermitian couplings; no static identification. |
| `BH-IIIF-A-0128` | 14104 | Admitted local Hamiltonian/Vlasov collisionless source with transported occupations, regular retarded source and order-of-limits control. |
| `BH-IIIF-A-0129` | 14246 | Actual matched scalaron packet, same-action complete metric/scalar source without extraneous F term, residual trace and finite local support. |
| `BH-IIIF-A-0130` | 14306 | Admitted gauge-stable n>=1 scalar support, normalized kinetic generator basis and Omega>0; target geometry only, no new physical scalar state. |
| `BH-IIIF-A-0131` | 14446 | Terminal F=1 with only displayed two-derivative potential and explicitly no residual source/quantum/gauge effective corrections; radial obstruction conditional. |
| `BH-IIIF-A-0132` | 14526 | Fixed physical inverse-propagator action on quotient; Hermitian real analytic D, invertible C, 1D kernel S and nonzero derivative a; source on same chart. |
| `BH-IIIF-A-0133` | 14596 | Fixed energy-independent Hamiltonian, positive complementary gap δI≤C-EI≤DI, retained u normalized in same norm. |
| `BH-IIIF-A-0134` | 14649 | Smooth stationary family, fixed quotient and boundary/interior frame, C>0, full Hessian allowed critical; moving simple mode separate. |
| `BH-IIIF-A-0135` | 14737 | Real C4 stationary physical action with invertible interior Hessian on fixed finite quotient; higher vertices use the actual moving source. |
| `BH-IIIF-A-0136` | 14860 | Generated one-dimensional positive PQTI coefficient Qσ>1; depth parameter evaluated as supplied, not assumed to obey physical secant addition. |
| `BH-IIIF-A-0137` | 15020 | Existing actual boundary/trace split and stationarity on gauge quotient; interior invertibility, and full H inverse only where used for first source jet. |
| `BH-IIIF-A-0138` | 15343 | All actual metric/field/source/mark Lie variations, canonical endpoint and source/gravity allocation retained in physical Hilbert work. |
| `BH-IIIF-A-0139` | 15599 | Complete Hermitian lapse/scale work insertions on finite physical Hilbert space, positive trace-one state; separate pressure operator. |
| `BH-IIIF-A-0140` | 15659 | Common C3 trace/Duhamel domain for true Euler/metric varied input and noncommuting heat and localizer contacts. |
| `BH-IIIF-A-0141` | 15772 | Complete bare f(R) on-shell homogeneous source separately conserved, fixed Einstein comparison coefficient and nonzero F. |
| `BH-IIIF-A-0142` | 15829 | An actually realized position Hopf slice with circle submersion and homogeneous curvature coefficient A(t); no momentum-space owner identification. |
| `BH-IIIF-A-0143` | 15933 | Homogeneous coherent matched native scalar/gravity packet Ω=F−\|h\|²/(6M²)>0 with canonical endpoint and its complete two work ports. |
| `BH-IIIF-A-0144` | 16128 | Same normalized initial finite source density and complete unitary generator on two histories, with state, centre, source/metric contacts. |
| `BH-IIIF-A-0145` | 16280 | Licensed affine terminal F=1,P=C and closed FLRW curvature K, comparison source and only genuinely additional separately counted excess. |
| `BH-IIIF-A-0146` | 16345 | Fixed finite CAR source, massive sign operator, integrable a(t)^-1, convergent centre and decaying a ε0′; no automatic state preparation. |
| `BH-IIIF-A-0147` | 16697 | Admitted uniform-clock-lapse static positive Routh source with ν-independent A,j,E0 and complete source interaction; reference state held fixed. |
| `BH-IIIF-A-0148` | 16804 | Covariant diagnostic Z(b,q)(u·∇q)² with strictly stationary u·∇q=0; advected b∝a^-3 only for inference test. |
| `BH-IIIF-A-0149` | 16852 | A physical quotient/source action actually supplies complete finite symmetric kinetic/elastic blocks and no unshown lapse dependence; frozen monotone case adds M,K>0. |
| `BH-IIIF-A-0150` | 17035 | Actual singular interior same-action Hessian with supplied source/trace maps, range constraint and provider-matched analytic rank-change hypotheses. |
| `BH-IIIF-A-0151` | 17144 | Same actual canonical gauge action with Cartan A=fΘ on physical round S3, homogeneous positive Z(φc) and matched Einstein coefficient. |
| `BH-IIIF-A-0152` | 17252 | Finite first-jet licensed gauge/constraint chart with same-units differentiable L_cl(q,v) and Hermitian H(q,v) including central, interaction and moving-frame terms. |
| `BH-IIIF-A-0153` | 17333 | Spherical/homogeneous metric–scalar restriction with F(Phi)>0, smooth coordinate-only/first-jet source and independent lapse variation, retaining constraint and full finite source. |
| `BH-IIIF-A-0154` | 17580 | Constant-coefficient aR²+b Ric²+c Rm² metric action in proper-time spherical reduction on licensed clock real-form chart. |
| `BH-IIIF-A-0155` | 17639 | Fixed positive trace-one finite source state and marked unitary orbit, actual finite constraints/support retained, no all-unitaries-physical inference. |
| `BH-IIIF-A-0156` | 17688 | Complete C³ source–geometry first-jet action with invertible physical velocity Hessian on an actual regular constraint/gauge chart. |
| `BH-IIIF-A-0157` | 17794 | Prelicensed infinitesimal classical cotangent gauge action plus anti-Hermitian source representation, complete action invariant under the same finite Lie algebra. |
| `BH-IIIF-A-0158` | 17888 | Conformal FLRW Ricci inverse with fixed a_i>0 and a_i prime, continuous supplied R, positive bounded regular finite interval, initial data held fixed under variations. |
| `BH-IIIF-A-0159` | 17938 | Actually retained four-dimensional real scalar mass/xi action with allowed support, charge-one Hopf harmonic and transported endpoint and physical clock. |
| `BH-IIIF-A-0160` | 17991 | Actually licensed complete source functional or finite Dirac band on fixed coherent frame; transported fields/state/projectors/normalization and initial preparation included. |
| `BH-IIIF-A-0161` | 18147 | Multiple co-consumed quadratic action constituents share one and the same finite interior z with C_i positive on common physical quotient. |
| `BH-IIIF-A-0162` | 18266 | Finite stationary gapped source with positive trace-one CAR state, integrable bounded scale variation/cold tail and sector-wise preparation. |
| `BH-IIIF-A-0163` | 18505 | Actually selected native metric/scalar plus complete source and gauge/constraint restriction with source work Ward relation, regular p/F branch. |
| `BH-IIIF-A-0164` | 18709 | Smooth finite physical heat/localizer finite-frontier domain with declared Davies–Gaffney/heat propagation and fixed profile; sharp projector not automatically local. |
| `BH-IIIF-A-0165` | 18838 | Positive Schur/interior kinetic comparison on same actual action and physically matched target geometry, scalar support and source/metric constraints. |
| `BH-IIIF-A-0166` | 19031 | Actually retained two-scalar Einstein target and transverse line, geodesic/background and proper source contacts, no unjustified projection of other sectors. |
| `BH-IIIF-A-0167` | 19291 | Complete real C² stationary boundary/interior action on actual regular gauge quotient, proper metric/source marks and moving-domain transport; invertible C where used. |
| `BH-IIIF-A-0168` | 19358 | Actual same-action finite gauge quotient where H=H4+H_rem, H_rem positive semidefinite on all metric–interior tangents and C blocks strictly positive. |
| `BH-IIIF-A-0169` | 19417 | One fixed Z>0, f in C²(I), constant Lambda_ren and identical curvature tangent on FLRW, constant trace, and conformal Hessian evaluations. |
| `BH-IIIF-A-0170` | 19480 | Quantization and measure license one real finite positive interior Gaussian determinant C(m)>0 with all metric/control and measure factors retained. |
| `BH-IIIF-A-0171` | 19594 | Local regular simply connected static domain with trial scalar acceleration and proper gradient closedness; non-spherical curl condition tested. |
| `BH-IIIF-A-0172` | 19658 | Four-dimensional smooth common spin chart with F>0, transported unitary L² pairing, fixed cutoff and differentiable heat/localizer trace domain. |
| `BH-IIIF-A-0173` | 19784 | Unprojected torsion-free ordinary metric Dirac a6 with literature representative, all Euler derivatives before Einstein/Kottler specialization, no finite-band projection shortcut. |
| `BH-IIIF-A-0174` | 19860 | Constant R Kottler metric m>0, r>0 on a smooth local static region, raw sixth-order Euler tensor, no physical source/cold identification. |
| `BH-IIIF-A-0175` | 20736 | The actual source has certified unit current-aligned arrows, fixed left probe and all real/complex source return contacts; scalar heat equality alone does not select right words. |
| `BH-IIIF-A-0176` | 20826 | Two C2 scalar-curvature densities matched at C through first jet, same smoothly transported compact-interior metric tests and a constant-curvature approach. |
| `BH-IIIF-A-0177` | 20961 | Actually supplied finite Hermitian generator with fixed initial positive normalized density; C2 control jets on compact history tube and local nonzero normalized influence logarithm. |
| `BH-IIIF-A-0178` | 21360 | Same native ordinary-trace scalar matrix, positive F, owned V0, full matrix scalar Euler stationarity, source-free constant Einstein chart; rank/spectrum supports restricted only as actually admitted. |
| `BH-IIIF-A-0179` | 21776 | Actually co-consumed, exactly once, complete signed Hilbert and scalar remainder insertions on full native metric/scalar equations, with enough weighted derivative control for budget. |
| `BH-IIIF-A-0180` | 22115 | Actual compact unlocalized Euclidean ordinary-Dirac heat trace, common transported domain and fixed cutoff; admitted unconstrained homothetic variation and no moving projector. |
| `BH-IIIF-A-0181` | 22207 | Actual parallel finite Hermitian internal scalar and graded tensor Dirac with anticommuting geometric gamma and common tensor trace/domain; not a nonparallel rooted midpoint. |
| `BH-IIIF-A-0182` | 22341 | Already selected primitive rooted Ystar identity member, no offset, canonical source/fermion scaling and actual native scalar support with no additional physical Yukawa selection. |
| `BH-IIIF-A-0183` | 22846 | Exact classical degree-at-most-four source-free primitive polynomial packet on positive-F, radial gauge-compatible closed Einstein-frame FLRW with a_i>1/sqrt(2L), H_i>0 and matching constraint. |
| `BH-IIIF-A-0184` | 23163 | Finite real quadratic stationary parents on common fixed source/energy frame with common invertible physical probe matrix Q and positive symmetric T; not inherited by incomplete probes. |
| `BH-IIIF-A-0185` | 23205 | Full four-dimensional compact-interior metric tangent space including TT deformations; equality of scalar FLRW restrictions is not equality of complete tensor Hessians. |
| `BH-IIIF-A-0186` | 23396 | One-sided sourced terminal metric f(R) member with C>0, U>5C, 3C<C2, 0<=n7<=1 and actual fRR>0 on active comparison collar; not the affine terminal physical vacuum. |
| `BH-IIIF-A-0187` | 23489 | Fixed actual orthogonal rank-r boundary projector/involution with stated gamma conjugation domain, source norm and trace; finite cap resolvent is only a comparison until generated. |
| `BH-IIIF-A-0188` | 23722 | Actually selected local homogeneous isotropic parity-even gauge invariant positive ZE,ZB transverse source action; full nonlocal optical cone requires separate principal-symbol certification. |

## Source-first E1 and independent/adversarial evidence location
- All **364** exact source proof environments and all **66** formal remarks: `DAG/AuditLayer/Paper3F-v1_1/SourceCensus.json`.
- All **442** source-printed claim records, statuses, and locally identified evidence gates: `DAG/AuditLayer/Paper3F-v1_1/AuditClaimLedger.json`.
- All nine complete original per-batch source/evidence objects: `DAG/AuditLayer/Paper3F-v1_1/Batches/`; E3/E4 suite summary: `DAG/AuditLayer/Paper3F-v1_1/ProofEvidenceLedger.json`.
- Proof routes and per-target condition inheritance: `DAG/AuditLayer/Paper3F-v1_1/ProofRoutes.json`. Nonpromoting edges and review scope retained in `DAG/AuditLayer/Paper3F-v1_1/TypedDependencyEdges.json`.
- Global query: `DAG/CombinedGraphIndex-v1_104.json` and `Paper00-DAGQuery-v1_104.py`. Issue ledger: `DAG/AuditLayer/Paper3F-v1_1/GapRegistry.json`.

## Qualification of physical claims and affected interfaces
Exact cotangent/spectral/Clifford/finite-action identities do not, by themselves, prove occurrence of an action, boundary state, transverse optical cone, generated particle pole, scalaron phase, or global spacetime. Conditions are not mathematical errors. Rectangular Feshbach propagation has one invalid positive-gap inference, but the source-specific bypass gap propositions are not automatically refuted. Off-shell symplectic-current counterexample does not undo separate coefficient-family κ=0 result. Cross-paper mathematical impact is asserted only for verifiable material proof use; mere similarity and citation are quarantined.

**Source integrity:** Papers and imported material in `Sources-v2_370/` are frozen and unchanged. This report is a completed source audit with five open issues, not a paper revision, physical realization certificate, or a proof of the whole framework.

---

## Current-source issue-specific repair addendum — 18 November 2026 (batch 3)

**Current source:** `Paper3F-CompleteDynamics-v1_268.tex`; **SHA256:** `37f986adbb46e4fed0dd7b98cb4e0ab102572b490d6a2c035d18e2626fab842a`. Original audit history retained above, not erased. This addendum supersedes the named defects only at the corrected theorem-statement scope, never an unconditional global E3/E4/physical statement.

### BH-IIIF-G-0004 — `p3:cor:no-independent-lr-gauge-coefficient`

- **Effective status:** `SOURCE_CLAIM_CORRECTED__PHYSICAL_OWNER_OR_GLOBAL_AUDIT_PENDING`.
- **Exact source:** `Paper3F-CompleteDynamics-v1_268.tex:11344`, SHA above.
- **Original defect:** For the absolute dimensionless expression κ f₂/48, also require r_fib Λcut=1 (BH-IIIF-A-0016). Without it theorem 201 gives κ r_fib² f₂ Λcut²/48. The base CAL_GRED by itself explicitly excludes automatic saturation.
- **Correction:** Corrected absolute gauge coefficient to κ f₂(r_fib Λcut)^2/48; κ f₂/48 needs explicit r_fib Λcut=1. Parity gL=gR retained.
- **Retained owner / limit:** Exact radius/cutoff identity formula now sourced; any physical coupling normalization remains owner-specific.
- **Local evidence:** `Paper00-MathematicalRepairBatch3Verification-v1_1.json` (26 bounded checks overall). No complete replacement proof-chain audit or new global theorem certificate asserted.


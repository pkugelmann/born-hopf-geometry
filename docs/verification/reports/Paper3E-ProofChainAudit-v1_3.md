# Source migration and repair-integration addendum — Paper3E-ProofChainAudit-v1_3.md

**Integration release:** `Paper00-PapersMinimal-v3_007.zip`, 14 November 2026.
**Current paper source:** `Paper3E-GravityAction-v1_197.tex`.
**Status:** `SOURCE_INTEGRATED; GLOBAL_SOURCE_REAUDIT_PENDING`. An inherited historical audit is not a correctness certificate for the newer current manuscript.
**Evidence policy:** Local algebraic proofs and scoped tests do not discharge physical source/observable interfaces or automatically alter the canonical proof DAG.

---

## Historical source-bound audit: Paper3E-ProofChainAudit-v1_2.md
# Repair addendum — Paper3E / 13 November 2026

**Current manuscript:** `Paper3E-GravityAction-v1_191.tex` (SHA-256 `4483fa84b3d5de8113171edbb6177ffdb303bd65d6dd47effacd9d47f9ec896c`)  
**Historical report preserved:** `Paper3E-ProofChainAudit-v1_1.md` verbatim below.  
**Disposition:** Scoped source repairs, not complete independent mathematical re-audit; all prior DAG proof/physical statuses unchanged.  

| Issue | Current source line(s) | Change | Disposition |
|---|---|---|---|
| `BH-IIIE-G-0001` | `Paper3E-GravityAction-v1_191.tex:840`, `Paper3E-GravityAction-v1_191.tex:857` | Separated seven-real-dimensional Clifford response W_7 from complex spin W_spin and corrected J_Delta codomain and V-A consumers. | SOURCE_CORRECTED; REAUDIT PENDING / IMPORTED GATE RETAINED |
| `BH-IIIE-G-0002` | `Paper3E-GravityAction-v1_191.tex:984`, `Paper3E-GravityAction-v1_191.tex:993`, `Paper3E-GravityAction-v1_191.tex:1025` | Retyped CRP4 as unique scheme-depth partial B-connection; no full BxM connection uniqueness without independent M-direction data. | SOURCE_CORRECTED; REAUDIT PENDING / IMPORTED GATE RETAINED |
| `BH-IIIE-G-0003` | `Paper3E-GravityAction-v1_191.tex:1371`, `Paper3E-GravityAction-v1_191.tex:1377`, `Paper3E-GravityAction-v1_191.tex:1733`, `Paper3E-GravityAction-v1_191.tex:1749`, `Paper3E-GravityAction-v1_191.tex:1759`, `Paper3E-GravityAction-v1_191.tex:1776`, `Paper3E-GravityAction-v1_191.tex:1797` | Scoped ordinary heat trace class to finite/compact parents; noncompact localized/relative/volume trace is a distinct readout requiring a trace certificate. | SOURCE_CORRECTED; REAUDIT PENDING / IMPORTED GATE RETAINED |
| `BH-IIIE-G-0004` | `Paper3E-GravityAction-v1_191.tex:4287`, `Paper3E-GravityAction-v1_191.tex:4290` | Carrier-four D_4(C_2)/Q is scheme dependent; 0.825729956674 is the REG0 numeric value, propagated to VI-A/VI-B. | SOURCE_CORRECTED; REAUDIT PENDING / IMPORTED GATE RETAINED |
| `BH-IIIE-G-0005` | `Paper3E-GravityAction-v1_191.tex:4656` | Bare reciprocal midpoint derivative is zero at x=1; at q=7/2 it requires R_s^2=UC, not a generic cap reference. | SOURCE_CORRECTED; REAUDIT PENDING / IMPORTED GATE RETAINED |
| `BH-IIIE-G-0006` | `Paper3E-GravityAction-v1_191.tex:4600`, `Paper3E-GravityAction-v1_191.tex:4679`, `Paper3E-GravityAction-v1_191.tex:4689` | Consistent curvature dimensions for Y,j and h_eff; dimensionless rescaling y=Y/R_s now retains R_s^16 Jacobian. | SOURCE_CORRECTED; REAUDIT PENDING / IMPORTED GATE RETAINED |
| `BH-IIIE-G-0007` | `Paper3E-GravityAction-v1_191.tex:6147` | Replaced nonexistent III-F section reference with exact current proposition and remark labels, separating restricted tests. | SOURCE_CORRECTED; REAUDIT PENDING / IMPORTED GATE RETAINED |

See `Paper00-AuditRepairBatch-v1_3.md` and the 28/28 scoped controls in the current atlas. Source hashes and line numbers appearing in the original text below refer to its **previous source edition**; original OPEN flags are historical and have not been changed or globally promoted.

---

## Historical audit baseline (unaltered original text)

# Paper III-E — Rigorous proof-chain audit (complete source review)

**Source:** `Paper3E-GravityAction-v1_190.tex` (Framework v2.370), SHA-256 `c09e1f6c834e784d593f12827045a22b184671324c5091f2e50b12e076e3119b`.

**Audit protocol:** `Paper00-RigorousVerificationDAGWorkProtocol-v2_4.md`, with E1 source replay, E3 independently calculated algebra/numerical tests, E4 adversarial and counterfamily testing. E0 file integrity is not a proof.

**Classification:** `FULLY_AUDITED_WITH_OPEN_GAPS`. **Complete source coverage:** lines 1–6,449; **115/115** formal claims, **92/92** proof environments, **30/30** formal remarks. **Scope:** paper III-E only, not unconditional framework or physical experiment verification.

**Six batches:** B1 1–1211 (14 claims, 10 proofs, 17 checks); B2 1212–2133 (14, 10, 24); B3 2134–3237 (22, 19, 36); B4 3238–4382 (25, 23, 62); B5 4383–5611 (26, 16, 78); B6 5612–6449 (14, 14, 127). All 344 exact or targeted reproducibility checks across the listed batch suites passed their designed predicates; semantic source gaps remain separately reported.

**Claim dispositions:** FORMALIZED: 12, REPRODUCED: 5, UNRESOLVED: 5, VERIFIED: 15, VERIFIED-CONDITIONAL: 78. Conditional physical-action/whole-action contacts are not upgraded by algebraic reconstruction.

## Seven still-open issues

### BH-IIIE-G-0001 — TYPE_OR_DOMAIN (MODERATE, OPEN)

**First origin:** `p3e:cor:even-external-internal-grading-ancestry` — `Paper3E-GravityAction-v1_190.tex:851-860`.

**Exact obligation:** Type J_Delta and its chirality operator on the exact spin carrier W_L⊕W_R (eight real dimensions), separately from the seven-real-dimensional Clifford block W; source does not supply their identification.

**Preserved:** Parity-preserving spin ancestry remains valid with its correctly typed carrier.

### BH-IIIE-G-0002 — TYPE_OR_DOMAIN (MODERATE, OPEN)

**First origin:** `p3e:thm:crp4-uniqueness` — `Paper3E-GravityAction-v1_190.tex:963-1011`.

**Exact obligation:** Specify independent spacetime M-direction connection on π_M*W* or restrict uniqueness to the scheme–depth B partial connection; unique B fourth-root transport is not a unique full B×M connection.

**Preserved:** CRP4 fourth-root determinant and scheme-depth transport.

### BH-IIIE-G-0003 — TYPE_OR_DOMAIN (MODERATE, OPEN)

**First origin:** `p3e:thm:general-closed-gravitational-readout` — `Paper3E-GravityAction-v1_190.tex:1711-1744; controlling domain Paper3E-GravityAction-v1_190.tex:1335-1377`.

**Exact obligation:** On the noncompact trace-per-volume/relative-trace branch explicitly permitted by the source, distinguish a finite localized/relative trace from the positive unlocalized heat operator itself being in the ordinary Schatten-L1 class. For an L1 conclusion either exhibit a trace-class sector owner or a declared trace-class localizer and change the output sort accordingly; no construction is performed here.

**Preserved:** unresolved noncompact branch; verified compact/finite branch

### BH-IIIE-G-0004 — TYPE_OR_DOMAIN (MODERATE, OPEN)

**First origin:** `p3e:thm:v2219-carrier-four-jets` — `Paper3E-GravityAction-v1_190.tex:4251-4259`.

**Exact obligation:** Determine whether the local numeric equality is meant only on REG0 (ln alpha=4pi^2+1/(6sqrt2)) or uniform on the already defined positive REGσ scheme locus; the same theorem states no explicit REG0 guard.

**Preserved:** unresolved scope qualifier on scheme-dependent numerical claim

### BH-IIIE-G-0005 — MISSING_CONDITION (MINOR, OPEN)

**First origin:** `p3e:thm:v223-cap-source / immediate post-theorem comparison` — `Paper3E-GravityAction-v1_190.tex:4620-4629`.

**Exact obligation:** Identify R_s=sqrt(U C) and q(R)=ln(U/R)/ln alpha before concluding x(q=7/2)=1 and vanishing derivative. Otherwise state the derivative zero at x=1 without hierarchy-depth substitution.

**Preserved:** established missing hierarchy-midpoint guard on ancillary derivative

### BH-IIIE-G-0006 — TYPE_OR_DOMAIN (MODERATE, OPEN)

**First origin:** `p3e:prop:v223-source-volume` — `Paper3E-GravityAction-v1_190.tex:4550-4556,4568-4571,4585-4590,4634-4646`.

**Exact obligation:** Make W_s quadratic/linear/source terms and exp[-W_s/(8h_eff)] dimensionally homogeneous using the declared [R_s]=curvature and stated dimensionless Y, and supply the corresponding density/Jacobian and h_eff type.

**Preserved:** unresolved dimensional coordinate/measure normalization despite verified pure Gaussian algebra

### BH-IIIE-G-0007 — DAG_COVERAGE (MINOR, OPEN)

**First origin:** `p3e:rem:v229-native-selection` — `Paper3E-GravityAction-v1_190.tex:6095-6099`.

**Exact obligation:** Resolve the cited PaperIII-F section label on the authoritative v2.370 source; if intended, verify exact subject-matched cross-reference to source-tested no-go results.

**Preserved:** established missing source reference, unverified intended replacement

## Verification and propagation policy

Inherited canonical conditions and upstream theorem flags are unchanged. Newly explicit Paper III-E conditions are source-local scope predicates, not additional physical axioms. All accepted material imports are traced to exact source-use anchors and remain conditional on their own hypotheses. Citation-only, possible-target, and unresolved-label links are excluded from proof traversal. Mathematical existence, spectral comparison, physical occurrence, actual action/contact selection, and empirical readout are distinct.

## Source-ordered per-batch detailed audit reports


---

# Detailed Batch 1

# Paper III-E — Rigorous verification, batch 01 (of planned source slices)

**Frozen source:** `Paper3E-GravityAction-v1_190.tex`; SHA-256 `c09e1f6c834e784d593f12827045a22b184671324c5091f2e50b12e076e3119b`

**Coverage:** lines 1–1,211; 14/115 formal declarations, 10/92 proofs, 1/30 remarks; 17 exact E3 symbolic checks passed.

**Disposition:** {'VERIFIED': 1, 'FORMALIZED': 3, 'VERIFIED-CONDITIONAL': 7, 'UNRESOLVED': 2, 'REPRODUCED': 1}. These are batch-level verdicts, not a full-paper or upstream-corpus certification.

## Per-claim evidence ledger

| ID | Source line | Claim label | Current verdict |
|:--|--:|:--|:--|
| BH-IIIE-C-0001 | 246 | `p3e:prop:v169-analytic-reconstruction-firewall` | VERIFIED |
| BH-IIIE-C-0002 | 285 | `p3:def:causal-wick-response-hypotheses` | FORMALIZED |
| BH-IIIE-C-0003 | 419 | `p3e:prop:v2211-whole-action-newton-certificate` | VERIFIED-CONDITIONAL |
| BH-IIIE-C-0004 | 486 | `p3e:cor:typed-planck-normalization` | VERIFIED-CONDITIONAL |
| BH-IIIE-C-0005 | 706 | `p3e:thm:uniform-reg-response-bundle` | VERIFIED-CONDITIONAL |
| BH-IIIE-C-0006 | 765 | `p3e:cor:owner-typed-active-spectral-profile` | VERIFIED-CONDITIONAL |
| BH-IIIE-C-0007 | 851 | `p3e:cor:even-external-internal-grading-ancestry` | UNRESOLVED |
| BH-IIIE-C-0008 | 871 | `p3e:prop:c12-scheme-depth-closure-criterion` | VERIFIED-CONDITIONAL |
| BH-IIIE-C-0009 | 938 | `p3e:def:crp4-cross-role-positive-parent` | FORMALIZED |
| BH-IIIE-C-0010 | 963 | `p3e:thm:crp4-uniqueness` | UNRESOLVED |
| BH-IIIE-C-0011 | 1013 | `p3e:cor:crp4-c12-discharge` | VERIFIED-CONDITIONAL |
| BH-IIIE-C-0012 | 1037 | `p3e:cor:v179-response-energy-quarter-character` | VERIFIED-CONDITIONAL |
| BH-IIIE-C-0013 | 1117 | `p3e:prop:conditional-susceptibility-half-weight` | REPRODUCED |
| BH-IIIE-C-0014 | 1168 | `p3e:prop:v236-mresp-decomposition` | FORMALIZED |

## Open source-anchored issues

### BH-IIIE-G-0001 — TYPE_OR_DOMAIN (MODERATE)

**Origin:** `Paper3E-GravityAction-v1_190.tex:851-860` / `p3e:cor:even-external-internal-grading-ancestry`.

In this manuscript W is a seven-real-dimensional trace-free Cl(0,3) block at lines 112,622,629. Imported diagonal-fibre spin transport targets W_L and W_R, a half-spin direct sum of four complex (eight real) dimensions; source gives no graded identification of these non-isomorphic codomains. The standalone map and Gamma_W are therefore not well typed as printed.

**Preserved valid result:** The conditional parity-preserving spin map into W_L direct-sum W_R may be mathematically valid after explicit type naming. This is not a refutation of the Paper III-B spin theorem.

**Verified downstream check:** Paper5A-FiniteMatterGeometry-v3_202.tex:803-826 (p5:cor:chi5-visible-chirality) cites the grading ancestry

**Required certificate:** Define separate W_7 and W_spin=W_L⊕W_R, exact S_x and Gamma_Wspin and J_Delta maps with matching dimensions; replay later uses under those types.

### BH-IIIE-G-0002 — TYPE_OR_DOMAIN (MODERATE)

**Origin:** `Paper3E-GravityAction-v1_190.tex:963-1011` / `p3e:thm:crp4-uniqueness`.

A unique scheme–depth B transport does not determine the spacetime M part of a full connection on pi_M^* W*. The source specifies no M-direction ∇^M for W*, and the antecedent positive-line fourth-root theorem is a B-base statement. Thus the full B×M connection is not uniquely induced without an inherited spacetime connection or a restriction to the relative B-direction connection.

**Preserved valid result:** The unique B-direction positive root, determinant transport, and displayed B-connection are verified; an explicit local choice of full d or a separately existing M-connection would cure the scope issue, but no repair is executed in this audit.

**Verified downstream check:** Paper5D-TechnicalMaterial-v1_47.tex:2440-2476 consumes the CRP4 connection in scheme-depth B role; that B-only route is not blocked

**Required certificate:** Clarify d=d_B versus d_{B×M}; if full, identify source-certified ∇^M on W* and its frame covariance, then verify direct-sum formula.

## Evidence gates and qualified ports

- E1: source replay of all 10 self-contained proof environments in this slice; definitions and no-proof corollary separately scoped.
- E3: 17 exact zero-reduction tests (SymPy), including the 7 integer depth hits; type and physical-owner gates require additional semantic checks.
- E4: tested grading-carrier typing and non-uniqueness of unspecified M-direction connections; discarded out-of-domain counterfamilies.
- No source-proven equivalence between raw joint and scalar Newton constants has been assumed; the constant-z physical matching stays conditional.
- The CELL curvature/EH residual, actual ACD_H/CRP4 port, PQTI tensorial normalization, REG scheme evaluation, and terminal metrics are kept distinct from proved algebraic descendants.
- The current paper’s conditions are not reintroduced as global DAG assumptions until their earliest logical appearance is checked against the existing registry.

## Continuation and archive policy

The next source slice is 1,212–2,133. No archive has been modified in this batch. The final batch will emit the successor global DAG atlas and proof-chain-audits ZIP, with only the newest version of each included component.


---

# Detailed Batch 2

# Paper III-E — rigorous DAG verification, batch 02

**Frozen source:** `Paper3E-GravityAction-v1_190.tex`; SHA-256 `c09e1f6c834e784d593f12827045a22b184671324c5091f2e50b12e076e3119b`.

**Source coverage:** lines **1,212–2,133**, 14/115 formal claims, 10/92 proof environments, 7/30 formal remarks. Cumulative: **28/115 claims, 20/92 proofs, 8/30 remarks** through line 2,133.

**Current verdicts:** {'FORMALIZED': 4, 'VERIFIED': 1, 'VERIFIED-CONDITIONAL': 8, 'UNRESOLVED': 1}. One new issue; the two Batch 1 issues remain open. These classifications apply to exact theorem scopes, not all external physical realizations.

## Exhaustive source-anchored formal-claim ledger

| Claim ID | Line | Source label | Outcome |
|:--|--:|:--|:--|
| BH-IIIE-C-0015 | 1335 | `p3e:def:grav-closed-occurrence` | FORMALIZED |
| BH-IIIE-C-0016 | 1367 | `p3e:def:grav-smooth-expansion-domain` | FORMALIZED |
| BH-IIIE-C-0017 | 1380 | `p3e:thm:born-orbit-eh-identification` | VERIFIED |
| BH-IIIE-C-0018 | 1508 | `p3:def:f2_rescaled` | FORMALIZED |
| BH-IIIE-C-0019 | 1527 | `p3:def:projected-grav-scalar-operator` | FORMALIZED |
| BH-IIIE-C-0020 | 1548 | `p3:lem:scalar-remnant-laplacian` | VERIFIED-CONDITIONAL |
| BH-IIIE-C-0021 | 1586 | `p3e:thm:generated-gravitational-heat-role` | VERIFIED-CONDITIONAL |
| BH-IIIE-C-0022 | 1711 | `p3e:thm:general-closed-gravitational-readout` | UNRESOLVED |
| BH-IIIE-C-0023 | 1747 | `p3e:cor:native-heat-action-constructor` | VERIFIED-CONDITIONAL |
| BH-IIIE-C-0024 | 1775 | `p3:prop:EH_from_a2` | VERIFIED-CONDITIONAL |
| BH-IIIE-C-0025 | 1827 | `p3e:thm:fixed-scalar-and-active-weights` | VERIFIED-CONDITIONAL |
| BH-IIIE-C-0026 | 1929 | `p3:thm:EH-normalization-gauge` | VERIFIED-CONDITIONAL |
| BH-IIIE-C-0027 | 2014 | `p3e:cor:grav-heat-branch` | VERIFIED-CONDITIONAL |
| BH-IIIE-C-0028 | 2068 | `p3e:cor:singleton-heat-profile-fibre` | VERIFIED-CONDITIONAL |

## E1 source replay / E3 independent assessment

- **BH-IIIE-C-0015 (1335) — FORMALIZED:** Defines d_g-sector scalar Laplacian exponential and closing map. Noncompact trace/volume is expressly a different domain, not automatic global L1.
- **BH-IIIE-C-0016 (1367) — FORMALIZED:** Sufficient compact, boundaryless smooth 4d Riemannian domain for local heat asymptotics; not inferred from finite root.
- **BH-IIIE-C-0017 (1380) — VERIFIED:** Independent change-of-variables proof of integral naturality; 1/2+1/2=1 on j_B(g); no off-diagonal or finite matrix trace equality.
- **BH-IIIE-C-0018 (1508) — FORMALIZED:** Direct integral ∫0∞e^-u du=1 yields f2=(4π)^-2; process-relative convention, not gauge or matter moment.
- **BH-IIIE-C-0019 (1527) — FORMALIZED:** Explicit hypothesis class aΔ+E with a>0 and e^-tL 1=1; a generated minimal scalar branch, not generic spinorial Dirac-square.
- **BH-IIIE-C-0020 (1548) — VERIFIED-CONDITIONAL:** Differentiate unital semigroup at t=0: L1=E=0. Constant a absorbed as t_eff=at and Λ_eff²=Λ_g²/a; no claim of rigidity of generic bundle operator.
- **BH-IIIE-C-0021 (1586) — VERIFIED-CONDITIONAL:** Given occurring root and source-stated frozen local scalar role, Δ and P_W determine strongly continuous e^-tΔ and e^-τP_W. Semigroup/generator/domain/functoriality checked; co-realization inherits II-A constructor-origin/GP1 boundary, not all physical process tokens. No generic joint-heat-origin closure of prior BH-IIIB-G-0002 asserted.
- **BH-IIIE-C-0022 (1711) — UNRESOLVED:** Ordinary A_g ∈ L1 and Tr_H A_g are valid on compact smooth or finite scalar carriers. The stated noncompact relative/trace-per-volume alternative does not entail ordinary L1; theorem does not repeat the branch guard.
- **BH-IIIE-C-0023 (1747) — VERIFIED-CONDITIONAL:** On frozen claim-complete native heat-action owner with trace-class/localized readout, composition Δ→heat semigroup→closed scalar trace meets III-A pre-action grammar; no full physical effective-action owner is inferred.
- **BH-IIIE-C-0024 (1775) — VERIFIED-CONDITIONAL:** Independent scalar 4d Seeley–DeWitt a2=R/6 positive; Born 1/2+1/2 gives single copy; ambient τ8(P0)=1/8 yields f2Λ²/48. Only GRAV-ASYM smooth expansion, not finite-m_p heat coefficient.
- **BH-IIIE-C-0025 (1827) — VERIFIED-CONDITIONAL:** Heat a0/a2 terms and ambient τ8(P0)=1/8 match; active-state endpoint eigenvalues I8/8 and P0 imply e^S/8=1 and 1/8. Vanishing terminal Hessian also consumes MRESP visibility u(C)=0; renormalized vacuum not inferred.
- **BH-IIIE-C-0026 (1929) — VERIFIED-CONDITIONAL:** Algebraic if-and-only-if for EH coefficient ONLY: f2Λ²=f2′Λ′²; rescaling profile changes a0 and higher-heat outputs, so no whole-action physical equivalence asserted.
- **BH-IIIE-C-0027 (2014) — VERIFIED-CONDITIONAL:** Exponent integral and algebra give Λg²=96π²U; cell comparison Λg Rmom=24√(3π) remains an actual-owner conditional; raw joint 96U stays separate.
- **BH-IIIE-C-0028 (2068) — VERIFIED-CONDITIONAL:** For attained λ>0 in frozen minimal heat role, F=e^-u, f2=1/(16π²), and unique Λ²=96π²λ; profile invariance is valid only on this fibre and complete generated descendant scopes.

## New open source-anchored finding

### BH-IIIE-G-0003 — TYPE_OR_DOMAIN / MISSING_CONDITION (MODERATE)

**Earliest root:** `Paper3E-GravityAction-v1_190.tex:1711-1744`, `p3e:thm:general-closed-gravitational-readout`; controlling domain `Paper3E-GravityAction-v1_190.tex:1335-1377`.

**Issue:** The theorem asserts the unlocalized positive heat operator is in ordinary trace class `L¹(H_g)` and has an ordinary full carrier trace. The preceding definition explicitly allows noncompact parents only after their own trace-per-volume or relative-trace domain is supplied. Those alternatives do not entail `Tr_H_g(e^{-tΔ})<∞` or `e^{-tΔ}∈L¹(H_g)`.

**Independent in-domain branch test:** On flat `R⁴`, the scalar heat kernel diagonal is `(4πt)^−2`; a trace per unit volume is finite, but the unlocalized ordinary trace is infinite. Compact smooth `S⁴` is the positive control: its heat eigenvalue sum is finite for every `t>0`.

**What survives:** The theorem is verified on finite windows and compact smooth parents. The Einstein–Hilbert `a₂` derivation assumes the compact four-dimensional `(GRAV-ASYM)` parent, so this new finding does not invalidate the scoped EH coefficient or heat-profile law.

**Verified material path:** `p3e:def:grav-closed-occurrence` → `p3e:thm:generated-gravitational-heat-role` → `p3e:thm:general-closed-gravitational-readout` → `p3e:cor:native-heat-action-constructor` (latter requires trace-domain correction for noncompact action). No remote-papers path certified.

**Required certificate:** Declare finite/compact ordinary trace scope, or provide an explicit noncompact localized/relative/volume trace with a correctly typed output claim; do not infer ordinary L¹ from FSRΣ notation. This is not a refutation of the compact statement.

## Already-open and inherited issues

- **BH-IIIE-G-0001 (Batch 1):** seven-real-dimensional Clifford `W` versus half-spin `W_L⊕W_R` grading-carrier type ambiguity; unchanged.
- **BH-IIIE-G-0002 (Batch 1):** unique scheme-depth B transport does not alone choose a full spacetime M connection; unchanged.
- **BH-IIIB-G-0002 (previous III-B audit):** frozen full operator-square heat process/readout origin remains a general upstream obligation. The narrower III-E scalar metric-root construction must not be used to mark the generic issue globally resolved.

## E3 exact checks and spectral positive control

- **24 exact symbolic zero reductions passed**, including `1/2+1/2`, `τ8(P0)=1/8` vs `τ8(I8)=1`, `a₂=R/6`, `Λg²=96π² U`, `Λg Rmom=24√(3π)` under CELL, semigroup/projector matrix identities, and entropy endpoint weights.
- A separate numerical E3 test used the exact unit-round `S⁴` scalar spectrum `λℓ=ℓ(ℓ+3)`, `dℓ=(2ℓ+3)(ℓ+2)(ℓ+1)/6`, yielding the expected small-time heat trace `1/(6t²)+1/(3t)+29/90+O(t)`:

| t | Observed remainder after a₀,a₂ | Expected a₄ |
|--:|--:|--:|
| 0.030 | 0.328166652 | 0.322222222 |
| 0.010 | 0.324187795 | 0.322222222 |
| 0.005 | 0.323203031 | 0.322222222 |
| 0.002 | 0.322614072 | 0.322222222 |

## E4 attacks and scope verdicts

- **Valid:** noncompact heat trace per unit volume is finite without the unlocalized operator being trace class (G-0003).
- **Out-of-domain:** adding `ξR` to the minimal scalar generator violates unit preservation; replacing the Born-diagonal metric pair by unrelated off-diagonal metrics violates the theorem’s embedding hypothesis.
- **Not a contradiction:** optional profiles with the same EH coefficient can have different bare vacuum/high-curvature outputs; the normalization theorem is deliberately EH-only.
- **Not a contradiction:** the exact fixed finite Dirac-square trace is not a four-dimensional continuum heat coefficient. The source recognizes that missing operator/effective-action port explicitly.
- **Inherited, not duplicated:** Paper III-B’s full generic native-heat output-origin gap is preserved pending a licensed constructor certificate.

## Seven remarks and unnamed clauses

- **Line 1489** (p3e:rem:v2211-finite-smooth-action-port): VERIFIED SCOPE FIREWALL: finite physical D_x,p traces are not exact 4d scalar a2 coefficients; actual operator/effective action coefficient port left independent.
- **Line 1891** (p3:rem:corner-trace-convention): VERIFIED ambient rank-one scalar projector trace 1/8 versus full scalar multiplication trace 1.
- **Line 1912** (anonymous optional enlarged-profile normalization): VERIFIED for EH coefficient only; separate normalization of distinct output a0 not inferred.
- **Line 1996** (anonymous separate origins of 6, 2pi and Newton): VERIFIED symbolic identities; measured G and scalar/joint owner matching remain separate.
- **Line 2109** (anonymous additional profile representatives): SCOPE ONLY: optional representatives deferred; no alternative profile selected.
- **Line 2115** (anonymous kinematic carrier density): VERIFIED factor 1/8 unaffected by multiplying a separate sector-density comparison after closure.
- **Line 2124** (anonymous local Born-Liouville phase volume): SCOPE ONLY: CAL_hbar and separate widths/cell needed; no state count inferred here.

## Audit boundaries and next batch

- **No paper edits or new theory.** Source-to-observable boundaries maintained: compact scalar heat coefficient ≠ raw joint coefficient ≠ exact finite momentum trace ≠ physically normalized Newton coupling. Calibration and physical action/export ports remain independent where source says so.
- **Canonical conditions:** reuses `BH-IIIB-A-0007`, `BH-IIIB-A-0008`, and `BH-IIIB-A-0013` rather than duplicating their assumptions. First-occurrence reconciliation for new explicit trace-domain/GRAV-ASYM predicates remains a final atlas-integration task.
- **Baselines:** latest supplied DAG v1.102 and ProofChainAudits v1.20; no archive edited in this batch.
- **Next source range:** lines **2,134–3,100**, beginning with operational Lorentzian signature and causal chain.

**Companion machine-readable evidence:** `Paper3E-RigorousVerificationBatch02-v1_2.json`, including all per-claim import candidates, boundary records, E3 tests, and E4 negative evidence.**


---

# Detailed Batch 3

# Paper III-E — Rigorous verification, batch 03 (causal/spectral/dilation segment)

**Frozen source:** `Paper3E-GravityAction-v1_190.tex`; SHA-256 `c09e1f6c834e784d593f12827045a22b184671324c5091f2e50b12e076e3119b`.
**Corpus:** `Paper00-PapersMinimal-v2_370` (unchanged); **protocol:** `Paper00-RigorousVerificationDAGWorkProtocol-v2_4.md`.

**Coverage:** lines **2,134–3,237**; **22/115** source formal claims, **19/92** proof environments, **6/30** formal remarks; **36/36** independent exact symbolic controls passed. The batch includes the complete dilation proof and complete conformal-cutoff theorem, rather than ending mid-theorem at line 3,100.

**Verdicts (this batch):** **3 VERIFIED**, **17 VERIFIED-CONDITIONAL**, **2 FORMALIZED**. No new source-supported mathematical issue was established; the previously recorded Paper III-E findings G-0001, G-0002 and G-0003 remain open and distinct. The noncompact branch of G-0003 is inherited by the readout scope in lines 2,835–2,868 but is not counted again.

## Complete source-bound claim ledger

| ID | Lines | Claim label | Verdict | Independent/core qualification |
|:--|:--|:--|:--|:--|
| BH-IIIE-C-0029 | 2157–2190 | `p3:thm:lorentzian-signature` | VERIFIED-CONDITIONAL | Solve Q=Aτ²+B|ξ|² vanishing on |ξ|=cτ: A=-Bc², B>0. The existence of every tangent sphere direction… |
| BH-IIIE-C-0030 | 2214–2269 | `p3e:thm:clock-hopf-null-ray-geometry` | VERIFIED-CONDITIONAL | Independent 2x2 Lorentz Gram calculation and quotient period cT=2πR, all exact. |
| BH-IIIE-C-0031 | 2294–2323 | `p3e:cor:null-coframe-frobenius-boundary` | VERIFIED-CONDITIONAL | Independent dual basis Gram computation and exterior-product two-term check: (±c dt∧dη+η∧dη)/2≠0; on… |
| BH-IIIE-C-0032 | 2336–2361 | `p3e:thm:positive-null-generator-components` | VERIFIED-CONDITIONAL | Independent boundary/strict-cone substitution E=c||p||+δ verifies nonnegative components and… |
| BH-IIIE-C-0033 | 2373–2390 | `p3e:def:lf-ray-geometry-package` | FORMALIZED | Type census checks N± tangent, ℓ± cotangent, γ families, p± generator germs; no cross-owner promotion. |
| BH-IIIE-C-0034 | 2392–2438 | `p3:cor:chiral-projective-null-directions` | VERIFIED-CONDITIONAL | Direct Pauli determinant and right Weyl contragredient group-automorphism computation. |
| BH-IIIE-C-0035 | 2470–2488 | `p3e:cor:projective-primal-dual-null-ray` | VERIFIED-CONDITIONAL | Independent support pairing qn(vn)=c−c=0; unique spatial unit n fixes a dual support ray. |
| BH-IIIE-C-0036 | 2490–2518 | `p3:cor:causal-scalar-principal-part` | VERIFIED-CONDITIONAL | Independent Hamilton equations, symplectic Jacobian det=1, coefficient rescaling b→ab, and Legendre… |
| BH-IIIE-C-0037 | 2549–2606 | `p3:thm:minimal-local-scalar-cone-order` | VERIFIED-CONDITIONAL | Direct principal symbol differentiation and characteristic ratio |ξ|/τ=√(b/a); independent polar… |
| BH-IIIE-C-0038 | 2643–2656 | `p3e:thm:primitive-scalar-support-ancestry` | VERIFIED-CONDITIONAL | The unique irreducible trivial real representation is the tensor-unit R; second distinguishable copy… |
| BH-IIIE-C-0039 | 2672–2700 | `p3e:thm:metric-principal-descendant-saturation` | VERIFIED-CONDITIONAL | Independent algebra comparing quadratic zero sets: proportionality forces b/a=c_op², whereas an… |
| BH-IIIE-C-0040 | 2721–2764 | `p3:def:paper-iv-finite-field-input` | FORMALIZED | Type check scalar Laplacian nonnegative, A1=0; domain separates full smooth-parent differential… |
| BH-IIIE-C-0041 | 2766–2791 | `p3:thm:p3-p4-lorentzian-chain-closure` | VERIFIED-CONDITIONAL | Independent mode substitution and exact mass shell E²=c²(ℏ²λ)+μ²c⁴. |
| BH-IIIE-C-0042 | 2815–2823 | `p3:cor:closed-lorentzian-dilation-constraint` | VERIFIED-CONDITIONAL | Independent determinant density/Jacobian square confirms no causal-field Hamiltonian used in the… |
| BH-IIIE-C-0043 | 2835–2855 | `p3:cor:wick-from-gp-constitution` | VERIFIED-CONDITIONAL | Independent distinction: a single number Tr e^(−tΔ) cannot determine a two-point correlation kernel;… |
| BH-IIIE-C-0044 | 2900–2928 | `p3:prop:spectral-gap-mass-upgrade` | VERIFIED-CONDITIONAL | Direct monotonicity of ℏ²c²λ+μ²c⁴ in λ, with positive λmin; λ=0 remains lower if included, so… |
| BH-IIIE-C-0045 | 2973–3006 | `p3e:thm:compact-haar-born-balance` | VERIFIED | Independent uniqueness of Haar and product pushforward theorem; symbolic S³ volume density… |
| BH-IIIE-C-0046 | 3023–3030 | `p3e:cor:haar-effective-balance-firewall` | VERIFIED | Independent smooth conformal rescaling g_p=c^(1/2) β_*g_x changes 4d effective volume ratio to c… |
| BH-IIIE-C-0047 | 3040–3054 | `p3e:cor:born-diagonal-effective-density-balance` | VERIFIED-CONDITIONAL | For any diffeo β, determinant density transformation gives β*dμ_β*g=dμ_g; conformal 4d off-diagonal… |
| BH-IIIE-C-0048 | 3081–3126 | `p3:thm:dilation_identity` | VERIFIED-CONDITIONAL | Independent exact determinant and positive-square calculation; explicitly test nonunit J and J=1… |
| BH-IIIE-C-0049 | 3187–3199 | `p3:cor:dilation_linear` | VERIFIED-CONDITIONAL | Independent exact symbolic substitution. The relation is linear in μx and μp with temporal scales… |
| BH-IIIE-C-0050 | 3216–3224 | `p3:thm:conformal-compactification-cutoff` | VERIFIED | Independent simple Lie algebra → compact u(N) obstruction (kernel all or injective; injective… |

## E1 replay, E3 independent checks and E4 adversarial outcomes

### 1. Exact GP1 cone and metric conformal signature, lines 2,134–2,212
The upstream Paper III-A `p3:thm:gp1-speed-calibration` at lines 2,368–2,440 bounds each generated velocity by the clock–Hopf constant, and `p3:cor:gp1-round-causal-envelope` at 2,443–2,474 uses actually licensed round isometry conjugations to attain every tangent sphere direction. The convex envelope is therefore **exactly** the full ball, not merely a ball-shaped upper bound. Paper I-C, under the Paper I-B label `p1b:prop:local-coframe`, establishes coframe/cone uniqueness. Independent check: an O(3)-invariant quadratic form `A τ²+B|ξ|²` zero on `|ξ|=cτ` forces `A=−Bc²`, up to nonzero scalar sign. Conditional only on the established `(CAUS)`/`CAL_t` domain; no field equation or measured light propagation assumed.

### 2. Clock–Hopf ray, Frobenius and chiral null directions, lines 2,214–2,489
The oriented II-D principal-to-metric normalization and III-A contragredient action make `N±=(c⁻¹∂t ± eH)/√2` well typed. Independent Gram and dual-coframe calculations verify `g(N±,N±)=0`, `g(N+,N−)=−1`, `ℓα(Nβ)=δαβ`, and `g⁻¹(ℓ±,ℓ±)=0`. A full quotient orbit turn is `s=√2 cT=√2 2πR`; neither null helix closes on the elapsed universal cover. The nonzero contact component `η∧dη` certifies the Frobenius obstruction, but the clock–Hopf 2D orbit cylinder admits local `x±` coordinates.

In the positive polar `E≥c||p||`, `|p_H|≤||p||` establishes both `p±≥0`. The upstream II-E spinor theorem supplies the left C² map and the **conjugate-dual**, not ordinary left, right action. Direct Pauli determinant and a nontrivial complex SL(2,C) right-Weyl composition test pass. This is projective local geometry, not a finite-QCD operator or a chosen physical ray; Paper VII-B explicitly consumes it only as the LF-A geometry package.

### 3. Local scalar order, undeformed principal and energy threshold, lines 2,490–2,947
An O(3)-invariant **scalar** first-order principal form has no spatial generator; the least spatially propagating scalar principal order is two. The PDE principal symbol `aω²−b|k|²` has Hamilton base speed squared `b/a`. The separately normalized positive Hamiltonian `H=(a π²+b|∇φ|²)/2` has speed squared **`ab`**, because its symbol is in a different coefficient convention; the symplectic rescaling `φ′=φ/√a, π′=√a π` reconciles the two. No inconsistent factor was found. The same-owner undeformed branch freezes the relative temporal/spatial quadratic owner, and then the characteristic front saturates `c_op`; other media may remain strictly slower.

A separately constituted neutral real tensor-unit support does **not** determine speed; II-A independently requires principal ancestry and smooth hyperbolic finite propagation. In the conservative smooth-parent free-law domain, formal selfadjointness kills real time drift, the nonnegative rest term is an explicit stability condition, and substitution on each finite eigenblock gives `E²=ℏ² c_field² λ+μ² c_field⁴`. The threshold claims concern a selected positive-gap block; the zero mode is not silently removed from every scalar spectrum.

### 4. Euclidean heat reconstruction scope, lines 2,835–2,898
The scalar heat trace is valid on the finite or compact ordinary-trace owner. A scalar trace is **not** a Euclidean quantum two-point kernel, and no automatic `(WICK_2cyc)`, `(WICK_same)`, finite reflection-positive reconstruction, or interacting infinite-volume continuation is inferred. The noncompact ordinary-L¹ issue from Batch 2 (`BH-IIIE-G-0003`) is inherited without duplication. Paper IV finite kernel reconstructions are later, conditional consumer results, not independent premises for the III-E Lorentzian sign.

### 5. Haar, Born-diagonal metric density and cubic Jacobian, lines 2,958–3,203
Haar uniqueness independently proves that a compact group isomorphism pushes normalized Haar to normalized Haar. The Born factor exchange preserves the compact product but **does not** constrain arbitrary separately chosen effective density factors. In four dimensions the III-G off-diagonal witness `g_p^(c)=c^(1/2) β_*g_x` has volume-density ratio `c`, despite unchanged compact Haar measures. On the **generated diagonal**, however, `β*dμ_{β_*g}=dμ_g` is an exact diffeomorphism identity. With `J_B` the absolute coordinate Jacobian, the two diagonal Lorentzian sector determinants give **`λ_x³ λ_t = J_B² λ_p³ λ_E`**, which reduces to the historical Jacobian-free formula only for `J_B=1`. The `μ_x=λ_x³, μ_p=λ_p³` form is linear in the two volume variables with the temporal/Jacobian coefficients held fixed.

### 6. Conformal compactification and finite unitary no-go, lines 3,206–3,237
The smooth compactification `(S³×S¹_conf)/Z₂` and its Einstein static universal cover `S³×R` are standard. Independently, a nontrivial continuous finite-dimensional unitary representation of connected noncompact simple `SO_0(2,4)` would give an injective Lie-algebra map into compact `u(N)`, which is impossible; `P U(g) P` generally violates the group product law by the omitted cross-band term `P U(g1)(I−P)U(g2)P`. Nonunitary finite algebraic conformal representations are expressly not excluded.

**Independent machine algebra:** 36 exact checks (36 zero residuals) in `Paper3E-Batch03-IndependentChecks-v1_1.json`, with reproducible script `Paper3E-Batch03-IndependentChecks-v1_1.py`. These are supplemented by theorem-level independent arguments, not represented as physical process certificates.

## E4 attack register

- **E4-IIIE-B03-001 — REJECTED-AFTER-IMPORT:** A GP1 speed bound alone might bound only an axis, not the full sphere. **Disposition:** III-A exact convex-envelope corollary consumes actual O(3) tangent isotropy and Hopf-orbit conjugates, establishes all sharp boundary directions.
- **E4-IIIE-B03-002 — PASSED-CONTROL:** Check contragredient inverse-action sign, geodesic/nonperiodic cover, and finite common quotient period. **Disposition:** Source transports oriented pair (eta0,xi0) natively; independently calculated N± periods agree, and cover clock displacement prevents closure.
- **E4-IIIE-B03-003 — FAILED-COUNTEREXAMPLE-CONFIRMS-OBSTRUCTION:** Try to find global functions x± with dx±=ell± on R×S3 despite contact curvature. **Disposition:** dell±=±deta/√2 nonzero; eta∧deta nonzero contact 3-form, and each ell wedge dell nonzero.
- **E4-IIIE-B03-004 — REJECTED-BY-SCOPE:** An O(3)-invariant first-order scalar symbol might already produce spatial fronts. **Disposition:** Scalar O(3) invariant linear symbol proportional to omega; base Hamilton projection has zero spatial component. Matrix/Dirac first-order operators are different target sort.
- **E4-IIIE-B03-005 — INVALID-OUT-OF-DOMAIN:** Take second-order scalar principal form omega²−v²|k|² with 0<v<c_op. **Disposition:** Admissible for cone-faithful medium branch, but changes temporal/spatial relative principal owner and violates explicit undeformed same-owner hypothesis.
- **E4-IIIE-B03-006 — INVALID-OUT-OF-DOMAIN:** Add stationary damping gamma partial_t, which changes dispersion. **Disposition:** Formal selfadjointness on invariant product measure is explicit and excludes any real nonzero time-drift coefficient.
- **E4-IIIE-B03-007 — SCOPE-QUALIFIER-NO-REFUTATION:** Include constant Laplace zero mode, below first nonzero eigenvalue. **Disposition:** Proposition concerns positive imported lambda_min on selected gapped block, not full spectrum bottom when zero mode retained.
- **E4-IIIE-B03-008 — VALID POSITIVE FIREWALL WITNESS:** Scale g_p=c^(1/2) beta_*g_x (c!=1) and seek Haar invariance with effective balance violation. **Disposition:** Volume density scales by c in four dimensions while normalized compact Haar remains invariant. No attack on Born-diagonal claim.
- **E4-IIIE-B03-009 — REJECTED-AS-SOURCE-ALREADY-QUALIFIED:** Use nonunit Jacobian and independent effective metrics to invalidate Jacobian-free formula. **Disposition:** Source retains J_B² explicitly and requires g_p=beta_*g_x; independent metrics are excluded.
- **E4-IIIE-B03-010 — INHERITED ISSUE BH-IIIE-G-0003:** Extend ordinary heat trace unqualified to noncompact parent. **Disposition:** Compact proof controls actual readout; general noncompact theorem already recorded unresolved in Batch 2. No duplicate issue introduction.
- **E4-IIIE-B03-011 — INVALID-OUT-OF-DOMAIN:** Use finite 2x2 Weyl representation of SL(2,C) to contradict finite conformal no-go. **Disposition:** Finite Weyl boosts and conformal representations are nonunitary; no-go concerns nontrivial exact finite-dimensional unitary action of connected noncompact simple group.
- **E4-IIIE-B03-012 — INVALID-AUTOMATIC-PROMOTION:** Identify derived null geometry automatically with a physical QCD light-front source or hadron alignment. **Disposition:** Source explicitly excludes physical operator/state/limit and Paper7B uses separate LF-A to LF-D typed packages.

## Scope and imported ancestry

The source-boundary review records four typed separation certificates (`BND-IIIE-B03-001` through `004`): operational cone/ray token, scalar principal/field occurrence, Haar/effective-density owner, and smooth conformal/finite-carrier representation. They are stored in the machine ledger. Source-verified imports were bounded to Paper III-A cone and polar, Paper I-C coframe, Paper II-D Hopf normalization, Paper II-E Weyl chiral ray, Paper II-A support/principal inheritance, and Paper III-G two technical-appendix interfaces; these peer papers have **not** been independently audited here.

**Material downstream uses confirmed (without full remote audit):** `p3:thm:lorentzian-signature` → Paper IV-A `p4:thm:three-map-bridge` at 1409–1417; `p3:thm:p3-p4-lorentzian-chain-closure` → Paper IV-B `p4:thm:finite-one-particle-dispersion` at 1957–1968; `p3e:def:lf-ray-geometry-package` → Paper VII-B `p11:def:hadronic-distribution-package` at 2390–2404. The last retains independent operator, state and limit ports. No new issue propagation from Batch 3 was established.

## Open findings and continuation

- **BH-IIIE-G-0001 (moderate):** Clifford `W_7` versus spin-grading `W_L⊕W_R` type declaration, from Batch 1; no new source contradiction here.
- **BH-IIIE-G-0002 (moderate):** CRP4 scheme–depth B connection does not by itself uniquely fix the full B×M connection, from Batch 1; no new effect established here.
- **BH-IIIE-G-0003 (moderate):** noncompact relative/volume trace does not entail ordinary unlocalized heat operator trace class, from Batch 2; restricted finite/compact heat readout remains valid and is used in this batch.

**Cumulative:** lines **1–3,237**, **50/115 formal claims**, **39/92 proofs**, **14/30 remarks**. This is **PARTIALLY AUDITED**, with 3 currently open Paper III-E findings. The total claim count includes definitions and all named proposition/theorem/corollary results. **No new gap/assumption nodes are inserted into the canonical global atlas in this intermediate batch**, avoiding duplicate first-occurrence conditions. Final merging and schema/ZIP verification remain deferred until every Paper III-E source claim has been examined.

**Next batch:** lines **3,238 onward** through the maximal complete hierarchy-response proof unit that can be finished without ending inside a theorem; target about **4,300** (adjust to proof boundary). The supplied DAG Atlas v1.102, ProofChainAudits v1.20 and papers corpus v2.370 remain unchanged.


---

# Detailed Batch 4

# Paper III-E — Rigorous verification and typed-DAG audit, batch 04

**Frozen target:** `Paper3E-GravityAction-v1_190.tex` (SHA-256 `c09e1f6c834e784d593f12827045a22b184671324c5091f2e50b12e076e3119b`), from `Paper00-PapersMinimal-v2_370(1).zip`. **Audit protocol:** `Paper00-RigorousVerificationDAGWorkProtocol-v2_4.md`. **Authoritative current-source lines:** **3,238–4,382** of 6,449; the slice ends before the next capped-scalaron section. No parent paper or previously supplied archive was edited.

**Batch census:** 25 named formal declarations (3 VERIFIED; 19 VERIFIED-CONDITIONAL; 2 FORMALIZED; 1 UNRESOLVED), 23 replayed proof environments, 2 formal remarks. **E3:** 62/62 exact and high-precision controls pass; **E4:** 15 paper-theorem challenges plus 2 explicit in-domain REG-family mutation controls. Independent algebraic checks do not substitute for empirical or action-occurrence certificates.

**Single new open finding:** `BH-IIIE-G-0004` (moderate; scheme-dependent rank-four midpoint *decimal*). `BH-IIIE-G-0001`–`G-0003` remain open; no new defects are attributed to their unchanged proof paths. This is **PARTIALLY AUDITED** across the full paper; terminal DAG/archive integration is deferred.

## 1. Complete source-bound claim ledger

| Claim ID | Source lines | Source label or source title | Verdict | E3 and scope assessment |
|:---|:---|:---|:---|:---|
| BH-IIIE-C-0051 | 3252–3281 | `p3:def:normalized-reduced-shell-length` | FORMALIZED | Eigenvalue/trace normalization and endpoint exact checks in E3-B04. |
| BH-IIIE-C-0052 | 3283–3304 | `p3e:thm:entropy-effective-count-uniqueness` | VERIFIED | Independent semigroup-character argument plus octet/pure-state exact controls; no physical entropy process inferred. |
| BH-IIIE-C-0053 | 3323–3359 | `p3:thm:index-locking` | VERIFIED-CONDITIONAL | Independent spectrum normalization, Shannon-like entropy, derivative and both endpoint checks. |
| BH-IIIE-C-0054 | 3399–3423 | `p3:rem:index-locking-status` | VERIFIED-CONDITIONAL | Independent two-family signature-injectivity check on frozen support/scale/role; pointwise support rank degeneracy at C does not erase running family identity. |
| BH-IIIE-C-0055 | 3439–3464 | `p3e:def:primitive-quadratic-trace-inheritance` | FORMALIZED | Dimensionless residual has U χ / Z_C vs 16√ασ; positive Z_C necessary to define hatγ. |
| BH-IIIE-C-0056 | 3466–3510 | `p3e:thm:pqti-quadratic-normalization` | VERIFIED-CONDITIONAL | Independent coefficients 8×2×√ασ=16√ασ, ratio law, and scheme-rescaling covariance tested exactly. |
| BH-IIIE-C-0057 | 3580–3600 | `p3:def:reduced-curvature-transport-factor` | VERIFIED-CONDITIONAL | Cancel κ symbolically and verify g(C)=g(U)=1 and (C+U)R g=R²+CU. |
| BH-IIIE-C-0058 | 3609–3657 | `p3e:thm:regular-two-scale-terminal-reconstruction` | VERIFIED-CONDITIONAL | Independent solution of the second-order terminal value problem plus exact Euler identity and endpoint value. |
| BH-IIIE-C-0059 | 3684–3716 | `p3e:cor:two-scale-affine-junction-family` | VERIFIED-CONDITIONAL | Check affine kernel, sharp-regular slope and absence of change in Hessian. |
| BH-IIIE-C-0060 | 3728–3754 | `p3e:thm:canonical-covariant-hessian-pullback` | VERIFIED-CONDITIONAL | Independent general 2×2 quadratic form pullback, matrix Hessian, positive semidefiniteness, and semigroup exact control. |
| BH-IIIE-C-0061 | 3773–3802 | `p3e:thm:response-homothety` | VERIFIED-CONDITIONAL | Independent nonconstant dimensionless h=x² example and scale-invariant first derivative check. |
| BH-IIIE-C-0062 | 3812–3831 | `p3e:cor:uv-susceptibility-homothety` | VERIFIED-CONDITIONAL | Independent scaling check and alternative positive γ family; no numerical γ identified. |
| BH-IIIE-C-0063 | 3845–3870 | `p3:lem:curvature-transport-character` | VERIFIED-CONDITIONAL | Exact two-root scale substitution and midpoint square-root identity. |
| BH-IIIE-C-0064 | 3891–3911 | `p3e:thm:general-hessian-reconstruction` | VERIFIED | Independent polynomial h example with terminal value/slope and exact second derivative. |
| BH-IIIE-C-0065 | 3921–3942 | `p3e:cor:terminal-data-minimality` | VERIFIED | Independent rank test of endpoint map and Hessian-invisible affine shifts. |
| BH-IIIE-C-0066 | 3958–3979 | `p3e:thm:v2217-uv-ir-moment-nonuniqueness` | VERIFIED-CONDITIONAL | Independent polynomial χ moment integrals, weighted-mean bound, and endpoint-jet-preserving perturbation with both moments zero. |
| BH-IIIE-C-0067 | 4001–4016 | `p3:lem:protected-hessian-transport` | VERIFIED-CONDITIONAL | Independent U endpoint h(U)=γ/U and C endpoint h(C)=0; no additional scaling character arises within declared sorts. |
| BH-IIIE-C-0068 | 4033–4063 | `p3e:thm:complete-minimal-smooth-response-family` | VERIFIED-CONDITIONAL | Independent positivity/limits of factors and generic terminal reconstruction exact controls. |
| BH-IIIE-C-0069 | 4076–4123 | `p3e:cor:mresp-composite-witness-transport` | VERIFIED-CONDITIONAL | Independent uniqueness of C² output and source verification of the II-A Orig/RootReal conditional theorem; origin is a premise, not inferred from mere written formula. |
| BH-IIIE-C-0070 | 4144–4153 | `p3:lem:terminal-protected-slope` | VERIFIED-CONDITIONAL | Independent terminal derivative calculation; does not use a first-variation semigroup. |
| BH-IIIE-C-0071 | 4166–4173 | `p3:lem:terminal-hamiltonian-lagrangian-sign` | VERIFIED-CONDITIONAL | Direct endpoint subtraction independent of Hamiltonian interpretation. |
| BH-IIIE-C-0072 | 4183–4217 | `p3:thm:master-lagrangian` | VERIFIED-CONDITIONAL | Independent endpoint jet and convexity checks as a specialization of the general Cauchy theorem. |
| BH-IIIE-C-0073 | 4251–4271 | `p3e:thm:v2219-carrier-four-jets` | UNRESOLVED | Independent n4(q) derivative, tanh algebra and q↔R Jacobian; high precision agrees with REG0; valid REG positive σ=±1 changes D4(C2)/Q. |
| BH-IIIE-C-0074 | 4284–4303 | `p3e:prop:v288-cap-laurent-nonidentification` | VERIFIED-CONDITIONAL | Independent Hessian-limit incompatibility and analytic-regularity comparison. |
| BH-IIIE-C-0075 | 4319–4352 | `p3e:thm:v287-s3-acceleration-hessian` | VERIFIED-CONDITIONAL | Independent nonlinear cubic f(R) exact acceleration differentiation plus arbitrary first-jet boundary exemplar. |

**Claim/proof traceability:** every nondefinition entry has its adjacent proof span recorded independently in the JSON ledger; both definitions are recorded as FORMALIZED. The two remarks (lines 3,880 and 4,372) were checked as scope boundaries, not counted as proof theorems. Each claim links by actual ID to the relevant independent checks, with source assumptions and type qualifications in the machine ledger.

## 2. E1 source replay + E3 independent verification

### Entropy-effective state and protected action coefficients (lines 3,238–3,573)
The normalized active state has the source spectrum `1/(1+7u)` and `u/(1+7u)` with sevenfold degeneracy, for `u=ln(R/C)/ln(U/C) ∈ [0,1]`. Thus

```math
S(u)=\ln(1+7u)-\frac{7u}{1+7u}\ln u,\qquad \frac{dS}{du}=-\frac{7\ln u}{(1+7u)^2}.
```

The continuous entropy-sufficient multiplicative count on finite tensor products, with the pure and uniform-octet calibrations, is uniquely `N=e^S`. The independent E3 checks verify trace, spectrum, endpoint entropies (0 and `ln 8`), and the derivative; direct reasoning supplies the continuity/Cauchy-character argument. The count is a theorem in its declared finite-state domain, not a physical particle count.

The generated action uses separate matching classes: static `P0` has protected coefficient `1/8`, whereas the active seven-branch composite gets running nonlinear weight `e^S/8`. This use of the Paper II-A canonical signature theorem remains conditional on the *complete frozen support/scale/role signature* and occurring MRESPmin composite; it is not inferred from the support rank at the pure endpoint.

The PQTI certificate is an **actual same-action second-jet equality**, not a consequence of merely writing down an abstract square root. If that separately evaluated residual vanishes, the raw seed carries `sqrt(alpha_sigma)/8` and multiplying the entire action by eight yields `Q''=2` and `chi_UV=16 sqrt(alpha_sigma)/Lambda_EH^2`. Algebraic factor 16 and scheme covariance check independently. Neither the existence of a realized PQTI port nor an empirical value of gamma is certified by those equalities.

### Two-root response, terminal ODE, affine shifts and Hessian transport (lines 3,574–3,888)
The bare two-root response simplifies to `g(R)=(R^2+CU)/[(C+U)R]` (auxiliary kappa cancels) and satisfies `g(C)=g(U)=1`. With constant bare Hessian `h=2/(C+U)`, the terminal data `f(C)=0`, `f'(C)=1` give

```math
f_{\mathrm{reg}}(R)=(R-C)+\frac{(R-C)^2}{U+C},\qquad Rf_{\mathrm{reg}}^\prime-f_{\mathrm{reg}}=\frac{R^2+CU}{U+C}.
```

Changing the remaining affine member `kappa (R−C)` does not change the Hessian, but does shift the Euler/Legendre potential by `kappa C`. The source term “regular C1 member” is safe when read as a specified **junction-slope matching choice**; it cannot mean all other bare `[C,U]` members fail to be C1, because they too are C2 there. This distinction was tested adversarially and recorded as a wording scope guard, not a separate source failure.

For a covariant Hessian tensor under the minimal pullback `A_tau=e^{−tau/2} I`, `A_tau^* H A_tau=e^{−tau}H`; cross-term and semigroup tests pass. Scale homothety of a dimensionless response `f=U fhat(R/U)` forces `h=U^{−1} hhat` and, with fixed active weight, `chi_UV=gamma_sigma/U`. The amplitude `gamma_sigma` is **not numerically fixed by homothety**; the actual PQTI port remains an independent conditional route. The generated-owner scale is `U=Lambda_EH^2`, `C/U=alpha_sigma^{−7}` on the stated stage, with the Born midpoint a curvature scale rather than an automatic geometric radius.

### General Hessian reconstruction, UV/IR moments and occurring response (lines 3,889–4,232)
For a continuous specified Hessian `h`, double integration with two terminal jets determines a unique C2 `f`; the homogeneous kernel is exactly `span{1,R−C}`. A single independent scalar endpoint condition cannot remove both affine freedoms. The endpoint moments are the integral increments of `f'` and `R f'−f`, respectively, with integrands `chi` and `R chi`. A compactly supported C∞ second-derivative perturbation with vanishing zeroth and first moments gives distinct smooth interior profiles with identical endpoint germs. Both moment cancellations and endpoint cancellations pass independent checks.

The minimal curvature-Hessian response `h=(gamma/U) (e^{S(u)}/8) u` is nonnegative, zero at the protected endpoint and positive on the interior. Source-member terminal conditions on the total `f=R+C_sp`, namely `f(C)=0`, `f'(C)=1`, impose `C_sp(C)=−C`, `C_sp'(C)=0`. These are typed *source terminal data*, not a terminal-vacuum principle or a proof of a propagating scalar.

The conditional rooted-output witness theorem uses the Paper II-A generated-image theorem **only if** the frozen tuple is jointly occurring and a licensed finite word has the specified response-graph sort. Constructing a mathematical `C2` graph alone is not a Lorentzian metric/action realization. That physical promotion is expressly excluded in E1 and the E4 scope test.

### Rank-four Laurent freeze and capped/FLRW separation (lines 4,233–4,382)
Paper III-D’s actual-grade-four positive Laurent index `n_4^+` is zero below `C_4`; its first active derivative boundary occurs at `C_4`. At `C_2=√(U C_4)` the rank-four and seven-level indices are smooth. The source’s third-derivative jump evaluates to

```math
[f_{RRR}]_{C_4}=\frac{(U-C_4)\ln Q}{4C_4(U+C_4)\ln\alpha_\sigma}\,\chi_7(C_4)>0.
```

Independent differentiation of `ln cosh` and the `q↔R` Jacobian confirm this expression, and a midpoint regularity challenge is rejected. The symbolic discontinuity and its *location* therefore survive independently of the disputed decimal at `C_2`. The exact `D_4(C_2)/Q` value, however, varies with the positive REG scheme; see G-0004 below.

The capped gravity density and positive-part Laurent comparator are not equal on the same curvature chart: the latter has a Hessian tending to zero at `C_7`, while the cited capped analytic response, on the condition `2BU>d`, has Hessian bounded below by `2BU−d>0`. Affine modifications do not fix a Hessian mismatch. This is a **same-chart nonidentification**, not a prohibition on all cross-owner correspondences.

For the k=+1 round closed-three-sphere homogeneous metric jet, the unreduced local Lagrangian `L_f=2 pi^2 Z N a^3 f(R)` has

```math
\frac{\partial^2L_f}{\partial\ddot a^2}=\frac{72\pi^2 Za}{N^3}f_{RR}(R).
```

The `R`-versus-acceleration derivative, second derivative, and boundary first-jet invariance tests pass. This **does not** count the physical propagating scalar modes; Hamiltonian constraints or physical solution space are not included. The final formal remark keeps older rank-two/K16-kink comparisons historical, not active source results.

## 3. New issue certificate — BH-IIIE-G-0004

| Field | Source-verified value |
|:---|:---|
| Issue class / severity | `TYPE_OR_DOMAIN` with numerical-readout scope; **moderate**, OPEN |
| Earliest located source | `Paper3E-GravityAction-v1_190.tex:4251–4259`, `p3e:thm:v2219-carrier-four-jets` |
| Source assertion | `D_4(C_2)/Q=0.825729956674...`, with no explicit `REG_0` qualifier in the theorem as printed |
| Verified positive control | `ln alpha_0=4pi^2+1/(6sqrt2)` gives **0.8257299566743899173773...** |
| In-domain variation | `sigma_fin=+1` gives **0.8261002425941142257374...**; the ratio is not scheme-invariant |
| Target of finding | **Only** the unqualified decimal’s domain; not the exact positive-part index, `C_2` midpoint, `C_4` freeze or third-jet jump |
| Required adjudication | Establish an already licensed source `REG_0` guard for this numeric claim, or show the claim was explicitly intended scheme-relative; no new mechanism or changed numerical definition is authorized |
| Remote effects | A downstream use of this *particular number* could inherit the qualification; no verified downstream material path currently located |

The exact scheme-parametric expression checked is

```math
\frac{D_4(C_2)}{Q}=\exp\!\left[\ln Q\left(\frac{\ln\cosh(2\ln\alpha_\sigma)}{2\ln\alpha_\sigma}-1\right)\right],\qquad Q=8\sqrt{\alpha_\sigma}.
```

Changing sigma is an **in-domain** counterexample to the uniform-decimal interpretation, not a counterexample to the source’s conditional algebraic rank-four result. The evidence identifiers are `E3-IIIE-B04-057`, `E4-IIIE-B04-058`, `E4-IIIE-B04-059` and `E4-IIIE-B04-011`. The issue remains open for precise published-scope adjudication; this audit did not edit the paper.

## 4. Adversarial E4 challenge register

| ID | Matched challenge | Verdict | Reason / boundary |
|:---|:---|:---|:---|
| E4-IIIE-B04-001 | Could N(ρ)=exp(k S(ρ)) with k≠1 obey every premise? | REJECTED | Octet condition forces 8^k=8, k=1; without entropy sufficiency/multiplicativity alternative counts are explicitly enlarged roles. |
| E4-IIIE-B04-002 | Treat III-D secant-matched entropy state as active MRESP state. | INVALID-TYPE-MERGE | III-C generates ρτ from same visibility process; u=log(R/C)/log(U/C) inversion is independent of III-D n_sec. |
| E4-IIIE-B04-003 | At u=0, σact has rank one, same as P0; does that invalidate type separation? | REJECTED-BY-FAMILY-SIGNATURE | Signature uses frozen role and scale dependence of complete constituent, not pointwise support rank at one endpoint. Same-image of generated term signatures is a conditional input. |
| E4-IIIE-B04-004 | Mutate γ to g≠16sqrt(ασ) while keeping MRESP homothety. | VALID MRESP-ONLY CONTROL, INVALID PQTI COUNTEREXAMPLE | Shows PQTI is an additional evaluated actual-action certificate; mutated g fails its coefficient residual. No unconditional coefficient selection claimed. |
| E4-IIIE-B04-005 | Add affine κ(R−C) to constant Hessian and demand same Euler potential. | REJECTED-BY-EXPLICIT-TERMINAL-SLOPE | Violates fixed Z_C=1; the next corollary explicitly keeps this affine family. |
| E4-IIIE-B04-006 | Use a nonlinear amplitude A with nonzero D²A to produce extra Hessian term. | OUT-OF-DOMAIN | Theorem requires linear generated amplitude A:W→W and Hessian at origin; nonlinear A changes type/grammar. |
| E4-IIIE-B04-007 | Choose χ(U)=U^(-2) and expect homothety. | REJECTED | Violates exact λ^-1 Hessian scaling when visibility factors are dimensionless and nonzero on interior. |
| E4-IIIE-B04-008 | One nonlocal scalar boundary condition could fix both affine coefficients nonlinearly. | OUT-OF-DOMAIN | Statement explicitly concerns continuous linear scalar conditions; rank ≤1 for one linear functional. |
| E4-IIIE-B04-009 | Perturb by smooth interior u, preserve both endpoint moments but change interior curvature. | VALID POSITIVE WITNESS (SUPPORTS THEOREM) | u and u′ vanish on collars, giving ∫u″=0, ∫R u″=0; small \|epsilon\| preserves χ>0 on support. |
| E4-IIIE-B04-010 | Infer a real physical metric action from the mathematical graph alone. | REJECTED-BY-SORT | Source requires jointly occurring input tuple and an explicitly frozen output sort RespGraph; Lorentzian action is a different sort. |
| E4-IIIE-B04-011 | Vary REGσ within I+ and test printed scheme-independent midpoint decimal. | VALID SOURCE-DOMAIN CHALLENGE — BH-IIIE-G-0004 | REG0 yields 0.825729956674389917; σ=+1 yields 0.826100242594114226. Exact symbol formula survives; number needs REG0 guard. |
| E4-IIIE-B04-012 | Seek a third-derivative kink at Born midpoint C2. | REJECTED | C2>C4>C7, both n4 and n7 raw Laurent indices smooth in neighborhood of C2; kink arises at positive-part boundary C4. |
| E4-IIIE-B04-013 | Add affine term and multiply comparator by finite nonzero scalar to match cap at C7. | REJECTED | Comparator second derivative tends to zero, cap lower bound remains >0; affines cannot change second derivatives. |
| E4-IIIE-B04-014 | Interpret nonzero unreduced acceleration Hessian as automatic propagating scalar mode. | INVALID-PHYSICAL-PROMOTION | No Hamiltonian constraints or physical scalaron sector provided by this jet calculation; source expressly disclaims it. |
| E4-IIIE-B04-015 | Interpret “regular C1 member” as a claim other κ have no C1 regularity within [C,U]. | WORDING-SCOPE BOUNDARY | All κ members are C2 on bare interval. “Regular” must refer to the source-matched terminal junction slope; not used to infer intrinsic loss of C1. |

Two additional numerical mutant schemes (`sigma_fin=−1,+1`) were evaluated within the declared REG positive family; both changed the numeric midpoint ratio. All 62 E3 scalar/symbolic controls pass. Adversarial challenges rejected by the theorem’s explicit domain do not generate new issue nodes.

## 5. Constructor/condition and typed-import boundaries

**BND-IIIE-B04-001** — Paper3E lines 3244-3437. `[CONST] MRESPmin typed co-realized family` → `[GEN] III-C visibility/normalized state` → `[DER] entropy count unique by sufficiency/multiplicativity` → `[ID] map to nonlinear action under matching signature`. E/U of entropy coupling derived; physical occurrence and terms require jointly occurring MRESP.

**BND-IIIE-B04-002** — Paper3E lines 3439-3573. `[CONST] separate actual-action PQTI compare` → `[DER] positive tensor-square half character` → `[CAL] octet scalar trace whole-action normalization` → `[ID] γ/ZC fixed only after PQTI residual zero`. No action appearance inferred from an abstract positive tensor square; separate physical comparison required.

**BND-IIIE-B04-003** — Paper3E lines 4233-4304 and III-D lines 1479-1556, 1835-1870. `[CONST] rank-character n_j^L(α) for positive REGσ` → `[GEN] first carrier grade P4` → `[DER] n4 positive-part freeze at C4` → `[CAL] printed D4(C2)/Q decimal matches REG0 only`. Exact scheme-parametric freeze is valid; decimal scope pending REG0 anchor.

**BND-IIIE-B04-004** — Paper3E lines 4076-4142, II-A lines 2219-2300. `[FROZEN] joint input tuple, schema and output sort before evaluation` → `[GEN] finite integration word to C2 graph` → `[DER] independent unique graph and non-obstructed conditional realization` → `[REAL] no automatic Lorentzian action realization`. Rooted generated-image theorem applies only on the declared origin-certified joint input domain.

**BND-IIIE-B04-005** — Paper3E lines 4284-4369, III-F lines 7819-7856. `[CONST] cap f_c action on its independent source/boundary ports` → `[DER] analytic positive cap fRR bound` → `[HOST] separate rank4 Laurent comparator` → `[DER] Hessian mismatch on shared curvature chart` → `[REAL] local FLRW acceleration jet not physical extra scalar mode`. Common-parent reductions and owner substitutions not automatically identified; same chart only.

**Material imports replayed at their exact interface (not full peer-paper re-audits):**

- `PaperIII-C / p3c:cor:corealized-protected-visibility-family` (Paper3C 3326-3363): full normalized ρτ and entropy postprocessor under occurring active composite.
- `PaperII-A / p2:cor:canonical-constituent-identification` (Paper2A 2738-2771): injective equal-image frozen signature allows unique 2-term identification.
- `PaperII-A / p2a:thm:rooted-generated-image-corealization` (Paper2A 2219-2300): conditional generated image co-realization after licensed Orig word.
- `PaperIII-D / p3d:cor:rank-character-laurent-family` (Paper3D 1479-1573): n_j positive/full secants and C_j positions.
- `PaperIII-D / p3d:thm:v2219-carrier-four-dressing` (Paper3D 1835-1870): first actual carrier-grade j=4 instead of optional least-support j=2.
- `PaperIII-F / p3f:prop:v223-cap-legendre` (Paper3F 7819-7856): independent uniform cap Hessian lower bound under 2BU>d.
- `PaperIII-B / p3b:thm:generated-action-response-owner` (Paper3E 1142-1162; Paper3B located): generated U=Λ_EH² identity-stage section.

The JSON ledger separately records verified typed `IMPORTED_PROOF` and `ISSUE_AT` edges with source locators and guard predicates. It does **not** invent global assumption IDs or reintroduce G0/GP1–GP3 and already recorded canonical conditions as new nodes. Any assumptions newly encountered in this batch must be reconciled against the global registry at the final merge.

## 6. Other open findings, scope firewall and release status

- **BH-IIIE-G-0001 (moderate, Batch 1):** Clifford `W` 7-real block vs the spin grading carrier `W_L⊕W_R`; overloaded map codomain/`Gamma_W` needs typed declaration. This batch does not modify that theorem.
- **BH-IIIE-G-0002 (moderate, Batch 1):** unique positive CRP4 connection along scheme-depth base `B` does not uniquely determine a full bundle connection on `B×M`; the established B-transport stays valid.
- **BH-IIIE-G-0003 (moderate, Batch 2):** relative/noncompact trace-per-volume need not make the unlocalized heat operator ordinary trace class. Compact finite/smooth heat-port proofs remain intact.
- **BH-IIIE-G-0004 (moderate, this batch):** numerical scheme guard at rank-four midpoint; exact Laurent positive-part geometry and C4 jump independently verified.

**Active scope firewalls:**

- Metric f(R) action physically occurring is not derived from smooth response-graph reconstruction.
- PQTI amplitude equality is evaluated action-port comparison, not tensor-square type alone.
- Affine Hessian kernel does not fix full zero-order response/Legendre potential without terminal data.
- Rank-four positive Laurent comparator is not the capped gravity working density.
- FLRW acceleration jet Hessian alone is not propagating scalaron certificate.
- Section 4372 old rank-two K16 kink is explicitly comparison-only/superseded.
- Source-regime scheme-zero midpoint number must not be treated as σ-independent prediction.

**Cumulative coverage after Batch 4:** **75/115** named claims, **62/92** proof environments, **16/30** formal remarks, source through **line 4,382**, four open findings. Not-yet-reviewed source starts at line **4,383**, with capped scalaron and further physical-action ports. Current overall status: `PARTIALLY_AUDITED` (correctness of unreviewed downstream source is not inferred).

**Archive retention:** `Paper00-DAGAtlas-v1_102(1).zip`, `Paper00-ProofChainAudits-v1_20(1).zip` and source `Paper00-PapersMinimal-v2_370(1).zip` are **unchanged**. The final batch will merge the complete target audit, deduplicate canonical conditions and issues, run schema/archive validation, and package only latest component versions in the DAG and audit ZIP successors. This batch releases intermediate markdown/JSON/reproducible controls only.

**Reproducibility and limitations:** `Paper3E-RigorousVerificationBatch04-v1_1.json` gives every named declaration’s exact source/proof span, verdict, independent evidence IDs, scoped imported uses, 15 theorem-level E4 challenges, one complete new gap certificate, and five boundary adjudications. `Paper3E-Batch04-IndependentChecks-v1_1.json` gives 62 exact/precision E3 controls plus 2 scheme-mutation checks; companion `.py` scripts regenerate the deterministic checks. Tests establish identities on declared mathematical domains, not experimental validation or actual physical occurrence. No archive was released or claimed to have passed final global DAG verification.


---

# Detailed Batch 5

# Paper III-E — Rigorous verification and typed-DAG audit, Batch 05

**Authoritative frozen source:** `Paper3E-GravityAction-v1_190.tex`, SHA-256 `c09e1f6c834e784d593f12827045a22b184671324c5091f2e50b12e076e3119b`, under `Paper00-PapersMinimal-v2_370(1).zip`.
**Audit protocol:** `Paper00-RigorousVerificationDAGWorkProtocol-v2_4.md` and inherited non-reopening guard from `Paper00-ProofChainAuditProtocol-v1_1.md`.
**Newly examined source:** **lines 4,383–5,611 inclusive** of 6,449, completing the capped scalaron and boundary-source constructor section at a major source boundary.
**No paper or master ZIP was edited.**

**Batch census:** **26** formal declarations (4 `VERIFIED`, 16 `VERIFIED-CONDITIONAL`, 4 `REPRODUCED` import/owner packets, 1 `FORMALIZED`, 1 `UNRESOLVED` dimensional clause); **16** direct proof environments replayed; **7** formal remarks reviewed; **6** mathematically material unnamed assertions separately classified. **E3:** **78/78** deterministic exact or high-precision independent controls passed. **E4:** **18** theorem- and scope-level challenges, plus **2** targeted mutation/dimension tests. New gap certificates: `BH-IIIE-G-0005` (minor) and `BH-IIIE-G-0006` (moderate). Earlier `G-0001`–`G-0004` persist unchanged. The numeric algebra in G-0006 is verified; its source dimensional sort is unresolved.

**Cumulative:** **101/115** formal declarations, **78/92** proof environments, **23/30** formal remarks audited, through line 5,611; **6** currently open target-paper findings. Remaining lines **5,612–6,449**. Overall target status remains `PARTIALLY_AUDITED` pending final source slice and global DAG merge.

## 1. Complete formal-claim ledger

| ID | Source lines | Current-source claim | Status | Independent evidence and scope |
|---|---:|---|---|---|
| BH-IIIE-C-0076 | 4398–4420 | `p3e:thm:general-scalaron-decoupling` — General metric-(mathfrak f) scalaron decoupling criterion | `VERIFIED` | Direct limit in independent smooth f(R) test. |
| BH-IIIE-C-0077 | 4427–4472 | `p3:thm:scalar-threshold` — Scalaron decoupling for the complete minimal response family | `VERIFIED-CONDITIONAL` | Independent entropy endpoint weights and algebraic Hessian/mass limits verified; III-F trace equation checked at its precise constant-curvature scope. |
| BH-IIIE-C-0078 | 4489–4498 | `p3e:cor:source-endpoint-not-vacuum` — The source endpoint is not a terminal vacuum | `VERIFIED` | Exact endpoint substitution; independently compare III-F sourced trace theorem. |
| BH-IIIE-C-0079 | 4504–4529 | `p3:cor:scalar-threshold-handoff` — Owner-typed Paper-III terminal handoff | `VERIFIED-CONDITIONAL` | Direct substitution, monotone q_tau=7(1-e^-tau), exact six finite inversions. |
| BH-IIIE-C-0080 | 4550–4574 | `p3e:def:v223-cap-data` — Normalized cap data and ports | `FORMALIZED` | Independent half-angle rationalization and B=BI*(1-c²t²). |
| BH-IIIE-C-0081 | 4576–4608 | `p3e:thm:v223-cap-source` — Normalized source response and reciprocal transport | `VERIFIED-CONDITIONAL` | Exact tensor determinant/trace, source Hessian and nontrivial exact metric-transport/Jacobian checks pass. |
| BH-IIIE-C-0082 | 4634–4651 | `p3e:prop:v223-source-volume` — Finite source volume and multiplicity | `UNRESOLVED` | Exact determinant and Gaussian normalization algebra passes; dimension-exponent adversary finds W quadratic and linear terms of incompatible types with dimensionless Y. |
| BH-IIIE-C-0083 | 4667–4701 | `p3e:thm:v223-exact-cap-reduction` — Exact capped action on a stated constructor domain | `VERIFIED-CONDITIONAL` | Independent flux minimization, complete source stationarity and 1/8-to-1/4 boundary normalization verify the stated finite reduction. |
| BH-IIIE-C-0084 | 4720–4731 | `p3e:prop:v223-port-incidence` — Common-interior incidence distinguishes the cap | `VERIFIED` | Direct symbolic minimization under all three incidence patterns and exact Hessian difference. |
| BH-IIIE-C-0085 | 4795–4815 | `p3e:prop:v224-source-moments` — Three-moment source test | `VERIFIED` | Independent 4x4 matrix inversion, nonisotropic PSD test and isotropic reference positive control. |
| BH-IIIE-C-0086 | 4831–4847 | `p3e:prop:v224-common-multiplicity` — Common Einstein/source multiplicity | `VERIFIED-CONDITIONAL` | Independent analytic small-r expansion and source/EH derivatives at zero. |
| BH-IIIE-C-0087 | 4858–4869 | `p3e:cor:v224-reference-source-status` — Exact source law with remaining physical inputs | `REPRODUCED` | Exact algebraic cap B and incidence controls corroborate the claimed equality; underlying full boundary reference-field proof not independently re-established here. |
| BH-IIIE-C-0088 | 4892–4916 | `p3e:thm:v164-generated-gravitational-heat-orbit` — Generated gravitational heat orbit | `VERIFIED-CONDITIONAL` | Independent rescaling of effective heat generator and coefficient; scalar heat moment integral checked. |
| BH-IIIE-C-0089 | 4918–4929 | `p3e:cor:v164-newton-fixes-profile-orbit` — Newton normalization fixes the orbit | `VERIFIED-CONDITIONAL` | Independent exact factor 6(4π)²=96π². |
| BH-IIIE-C-0090 | 4932–4957 | `p3e:cor:v174-yang-mills-action-derived-later` — Derived-later local Yang--Mills action and phase space | `REPRODUCED` | Source-matched III-F theorem located and its scope inspected, not a second independent E3 audit of the full phase-space result. |
| BH-IIIE-C-0091 | 4959–4989 | `p3e:cor:v175-einstein-scalar-actions-derived-later` — Derived-later joint-Dirac Einstein and native odd-scalar actions | `REPRODUCED` | Exact raw normalization U_J^raw=96U and κ_J=12U checked against III-F source, but full spinor action variation is not independently reproved. |
| BH-IIIE-C-0092 | 4995–5020 | `p3e:cor:v176-local-bosonic-noether-constraint-derived-later` — Derived-later local bosonic Noether and constraint packet | `REPRODUCED` | Exact source theorem and canonical-momentum formulas located; no E3 reconstruction of full constrained Hamiltonian completed. |
| BH-IIIE-C-0093 | 5048–5077 | `p3e:thm:v188-two-depth-structures` — Two independent depth structures | `VERIFIED-CONDITIONAL` | Independent SL(2,3) commutator order 8, SL(2,5) perfect order 120, quaternion Q8 commutator ±1. |
| BH-IIIE-C-0094 | 5122–5145 | `p3e:prop:v1107-raw-not-physical-euler` — The raw Laurent secant cannot be the terminal metric Euler response | `VERIFIED-CONDITIONAL` | Independent exact Euler derivative/primitive and endpoint Hessian nonidentity. |
| BH-IIIE-C-0095 | 5185–5229 | `p3e:prop:v2218-raw-heat-log-port` — Exact logarithmic raw-heat value and inverse-Euler test | `VERIFIED-CONDITIONAL` | Independent exact first/second derivatives, reconstructed log-Euler response and terminal jets. |
| BH-IIIE-C-0096 | 5257–5308 | `p3e:thm:v2218-factorized-heat-clock` — Complete contact residual and forced heat-clock trajectory | `VERIFIED-CONDITIONAL` | Exact ODE/contact differentiation, t(q) substitution, c0,c2 and offset ratios. |
| BH-IIIE-C-0097 | 5333–5356 | `p3e:cor:v2218-distinct-heat-visibility-clocks` — Fixed cutoff and distinct-clock tests | `VERIFIED-CONDITIONAL` | Exact terminal t0 alpha^7/8 limit and quotient c0/c2=6/t, coefficient derivative. |
| BH-IIIE-C-0098 | 5482–5518 | `p3e:thm:laur17-projected-terminal-freeze` — Terminal endpoint evaluation, no-second-EH firewall, and scalaron status | `VERIFIED-CONDITIONAL` | Independent affine Euler intercept invariant and zero Hessian; III-F terminal source theorem inspected. |
| BH-IIIE-C-0099 | 5531–5561 | `p3:thm:active-window-matching-rule` — Six finite scalar hierarchy hits and one asymptotic endpoint | `VERIFIED-CONDITIONAL` | Six exact finite t_j inversions plus terminal limit. |
| BH-IIIE-C-0100 | 5573–5592 | `p3:prop:uv-limit-active-density` — Ultraviolet and terminal limits | `VERIFIED-CONDITIONAL` | Independent entropy visibility endpoint Hessian and smooth qτ limits. |
| BH-IIIE-C-0101 | 5594–5607 | `p3:cor:frozen-constant-term-readout` — Terminal frozen nonlinear magnitude readout | `VERIFIED-CONDITIONAL` | Exact endpoint algebra independent of any terminal vacuum. |

**Proof count:** 16 direct adjacent `\begin{proof}`/`\end{proof}` environments; all have exact spans in `Paper3E-RigorousVerificationBatch05-v1_1.json`. The four derived-later owner packets are marked `REPRODUCED`, not `VERIFIED`, because their III-F source statements and key coefficients were examined but complete joint-Dirac/Hamiltonian independent proofs were *not* performed in this target-paper audit. They cannot be promoted solely by citation.

**Remarks (7):** lines 4531–4537 preserve six finite smooth level hits plus asymptote; 4744–4759 preserve conditional native cap selection; 4763–4780 reject inference from mere phase Gram trace cancellation; 5157–5166 separate raw Laurent and physical Euler sorts; 5366–5396 restrict heat-clock equation to comparator; 5422–5454 keep generated character/owner genealogy separate from actualization; 5520–5529 distinguish optional smooth MRESP from active Laurent owner. All seven have direct scope dispositions in the JSON ledger.

**Material unnamed statements (6):** `(i)` reciprocal midpoint `q=7/2` derivative (unresolved G-0005), `(ii)` M8 rank-4 determinant root, `(iii)` amplitude `e^{-τ/2}` versus response `e^{-τ}`, `(iv)` K16 continuity from positive common susceptibility, `(v)` multiplicative continuous character `D(s)=Q^s`, `(vi)` affine terminal Euler intercept and formal Einstein root. They remain explicitly tracked even though they are not named theorem environments.

## 2. Independent mathematical verification (E1 source replay, E3 exact evidence)

### A. Source-normalized scalaron criterion (4,388–4,529)

For `f ∈ C²((C,U]) ∩ C¹([C,U])`, if `f''>0`, `f''→0⁺` and `f'−Rf''→L>0`, the algebraic mass `m_s²=(f'−Rf'')/(3f'')` tends to positive infinity. As an independent control, `f(R)=(R−C)+(R−C)³/6` has `f''=R−C`, `f'(C)=1` and the required divergent ratio. On the smooth `MRESP_min` response the Hessian `h=(γσ/U)w_nl(u)u` is positive for `0<u≤1` and tends to zero at `u=0`; independent entropy-state limiting values are `w_nl(0)=1/8`, `w_nl(1)=1`. The physically measured mass requires an existing full trace-equation background; imported III-F 9564–9611 makes that restriction explicit. On the source pair `(F_C,Z_C)=(0,1)`, the unsourced vacuum residual is `C≠0`. Thus no automatic terminal vacuum is claimed or proved.

### B. Capped positive tensor, complete source word and Gaussian (4,550–4,780)

With `G=√(1+x²)`, `t=x/(1+G)` and `c²=1−B_U/B_I`, direct rationalization gives `t²=(G−1)/(G+1)` and the exact identity `B=B_I(1−c²t²)=B_U+2Δ/(1+G)`. For `v=ct`, both symmetric two-channel ports `M_±=I±vX` are positive, with determinant `1−v²`. Their tensor `T_s=M_+⊗M_-` satisfies **`det T_s=b⁴` and `Tr T_s⁻¹=4/b²`**. Direct completion of the full 4×4 source matrix gives `Y_*=-T_s⁻¹j`, `W_*=-Tr(jᵀT_s⁻¹j)`, and the scalar variation Hessian `−(I_4⊗T_s⁻¹)/4`. With `ρ=R_s/2`, `W_*/8=−σ²/(8B²)`.

An independent non-scalar exact matrix example confirms `AᵀT_r A=T_s`, transported `j_r=A^{-T}j_s`, unchanged source return, and the four-column Jacobian rule. For 16 Gaussian entries, `det(I_4⊗T_s)=b¹⁶`, hence the metric volume is `b⁸`. Completing the square yields the supplied `(8πℏ_eff)^8` prefactor and cancellation of the `b` determinant. The algebra survives arbitrary positive spectators provided their entire multiplicity and reference normalization are retained. *This pure algebra is distinct from the source's contradictory dimensional-coordinate phrase; see G-0006.*

For the conjugate-flux cap, independently minimizing `(a²+G⁻¹b²)/2` at `a+b=2√Δ R` gives `2Δ R²/(1+G)`, hence the declared `B(R)R²`. The sourced term supplies `−σ²/B²`; the specified first-order parent supplies GHY term `f_c'K/4` alongside interior `f_c/8`. All three source-incidence patterns have been checked: independent interiors produce `B_I(1-v²)r²`, symmetric shared interior `B_I r²`, and antisymmetric shared interior `B_I(1-v²)r²`. Equal dimensions and common co-consumption do not determine native incidence. The physical source/normal operator and measure are explicitly prerequisites rather than proved native selections.

**Ancillary midpoint defect (G-0005):** The bare reciprocal coordinate response `4ρ²/[b(x)b(1/x)]` is stationary at `x=1`, but not at an arbitrary hierarchy-labelled depth `q=7/2` unless `x(q=7/2)=1`, equivalently `R_s=√(UC)` for `R=U α^{-q}`, `C=U α^{-7}`. The theorem's cap data have only `R_s>0`. High-precision E4 positive and negative controls provide a direct bounded counterexample to the unguarded **comparison sentence**, not to the transported-source theorem.

### C. Source moments, independent multiplicities and native-status firewall (4,786–4,885)

With commuting involutions `A=X⊗I` and `B=I⊗X`, exact multiplication gives

```
T(u)^(-1) = [I + u(B-A) - u²AB] / (1-u²)².
Tr(j†T(u)^(-1)j) = [a0 + u a1 - u² a2]/(1-u²)².
```

The three fixed-frame source moments are necessary and sufficient for a constant inverse-square scalar return on an *open interval*. For moving source/frame only the complete functional identity remains; no stronger fixed-moment criterion has been transferred. With `R_s²=P_0 C_7`, `B(0)=B_I` and `B'(0)=0`, the normalized small-curvature comparison is `r−(m/M_E)C_7+O(r²)`. In particular, `m=M_E` is a genuine matching premise; `m=96` is not established as a native species count. I-B/III-F reference Poisson source is rechecked at exact interface, not independently reconstructed across those peer manuscripts.

### D. Scalar profile orbit, local owner imports, and exceptional groups (4,889–5,116)

`F_a(u)=exp(-au)` at scale `Λ` depends only on `a/Λ²`: `Λ_eff²=Λ²/a`. Under `(a,Λ)→(ρa,√ρ Λ)` the entire same-action expression and its variation remain unchanged. The smooth scalar `a₂` moment is `1/[a(4π)²]`; Einstein coefficient is `Λ_eff²/[6(4π)²]`, so the numeric factor **`96π²`** checks exactly. This fixes an *orbit*, not an absolute heat rate or a generic joint-Dirac physical Newton coefficient.

III-F's local Yang–Mills, joint Einstein–scalar, and Noether/ADM corollaries are **imported-with-scope**, not promoted to global nonlinear `f(R)` action theorems. The checked import includes `κ_J=12U`, `U_J^raw=96U`; its physical coupling remains a distinct matched-action port. Independent finite matrix enumeration verifies `SL(2,3)` order 24 with derived subgroup order 8, `SL(2,5)` perfect order 120, and `[Q_8,Q_8]={±1}`. These support the exceptional group-derived chain independently of the Clifford rank hierarchy: they are different sorts, not one group-derived particle decay clock.

### E. Laurent inverse-Euler firewall and fixed finite trace (5,120–5,254)

The raw lower-Laurent secant `(R²+UC)/(U+C)` uniquely gives `f_raw=(R−C)+(R−C)²/(U+C)` under normalized terminal jets, with `f_raw''=2/(U+C)>0`. The source compares it to the distinct `EXJET7` local-Hessian route with `f_{RR}(C)=0`; arbitrary affine kernels cannot remove this second-derivative difference. No contradiction is implied between a raw scalar *value* and a physical metric *response* from a different action port.

For finite seed `Z_H`, `A_p=15/2−q_H` and `R_H=U α^{-q_H}` give `A_p=1/2+log(R_H/C)/L`, independent of the interpolation profile. A positive direct value promotion has **negative** Hessian `−γ/(LR²)`. A positive affine *Euler* port instead yields `f_log=R−C+λ[R/C−1−log(R/C)]` with `f_log''=λ/R²>0`; this one does not vanish at the terminal endpoint. Both are expressly proposed tests, not arbitrary exclusions of all physical finite-action reductions.

### F. Forced heat-clock comparator, terminal quotient and hierarchy (5,255–5,611)

The controlled smooth tensor product has local coefficients `c0=(8−q)/[(4π)²t²]`, `c2=(8−q)/[6(4π)²t]`. The complete source/contact residual is

```
η_H = [L − 1/(8−q) − d(log t)/dq] dq.
```

Independent ODE integration verifies the unique root-normalized zero-residual trajectory `t(q)=t0(8−q)α^q/8`. Substitution verifies `U_H(q)/U_H(0)=α^(−q)`, `c0(q)/c0(0)=8 α^(−2q)/(8−q)` and normalized `c0/c2` ratio `8 α^(−q)/(8−q)`. At fixed `t` the residual does not vanish identically; a positive affine time correspondence with `τ` fails because `t(τ)→t0 α⁷/8` is finite. **No physical operator clock is selected** by that comparator ODE; the paper expressly retains that obligation.

For the terminal rank-seven owner, the imported Legendre–Euler equation at `R=C_7` implies the affine-kernel-invariant intercept `−C_7`. The retained slope-one representative `f_term(R)=R−C_7` has exactly zero Hessian and is not a second Einstein term. The source separates this quotient from an independent full physical history or vacuum. Finally `q_sp(τ)=7(1-e^(−τ))` reaches **six** integer levels at finite `τ_j=−ln(1−j/7)` and level **seven** only asymptotically. This is not a seven-projector chronology. The source endpoint `C_sp(C)=−C` also follows by exact subtraction under `(F_C,Z_C)=(0,1)`.

## 3. All new issue certificates

### BH-IIIE-G-0005 — unguarded hierarchy midpoint in the reciprocal bare source

- **Class/severity:** `MISSING_CONDITION / TYPE_OR_DOMAIN`, **MINOR**, `OPEN`; comparison statement, not a theorem refutation.
- **Exact origin:** `Paper3E-GravityAction-v1_190.tex:4620–4629`, immediately after `p3e:thm:v223-cap-source`.
- **Printed assertion:** bare reciprocal return has vanishing logarithmic `q` derivative at `q=7/2`.
- **E3 positive control:** `R_s=√(UC)` implies `x=1` at the Born midpoint; symmetry `b(x)b(1/x)` forces zero derivative.
- **E4 in-domain witness:** set `U=10`, `C=1`, `α=(U/C)^(1/7)`, `B_I=3`, `B_U=1`, `R_s=2`. The cap definition permits this `R_s`. Then `x(q=7/2)=√10/2`, and `d_q log([b(x)b(1/x)]⁻¹)` is **`−0.0561883538303380274544346…`**, not zero.
- **Required condition:** the additional existing geometric-mean specialization `R_s²=UC` (with `q(R)=log(U/R)/log α`), or scope the derivative claim to `x=1` rather than `q=7/2`.
- **Downstream supported impact:** local midpoint stationarity assertion alone. No verified path to the classical cap or the source-transport equality: those are independent and remain correct. Physical midpoint source selection unproved; no neighboring paper declared affected.
- **Provenance:** conditional source family in cap definition (free `R_s`), exact reciprocal tensor word, independent mutation and positive control `E4M-IIIE-B05-001`.

### BH-IIIE-G-0006 — Gaussian units and source-coordinate normalization

- **Class/severity:** `TYPE_OR_DOMAIN / NORMALIZATION_OR_READOUT`, **MODERATE**, `OPEN` as dimensional-typing scope, not counterexample to Gaussian math.
- **Exact origin:** dimension table `:4550–4556`, source coordinate/section `:4568–4571`, source `ρ=R_s/2` `:4585–4590`, Gaussian proposition `:4634–4646`.
- **E1/E3:** positive symmetric 16-variable real Gaussian gives the printed determinant/normalization cancellation. This part **passes**.
- **Type conflict:** with `[R_s]=[ρ]=curvature`, dimensionless `T_s` and the proposition's advertised *dimensionless* `Y`, the quadratic term `Tr(YᵀT_sY)` has dimension 1 while `Tr(j_sᵀY)` has dimension curvature and the stationary return has dimension curvature². The exponential and measure cannot all be dimensionally typed without an additional convention.
- **Remaining evidence obligation:** specify curvature-valued `Y`, `[ℏ_eff]=curvature²`, and a dimensional volume, **or** explicitly rescale `y=Y/R_s`, `ℏbar=ℏ_eff/R_s²` with the complete measure and any `R_s` Jacobian. The audit does not choose a physical native measure.
- **Verified bypass:** the exact algebraic finite Gaussian formula is correct on an abstract real vector space with consistent units; the purely *classical* cap reduction and its stationary source term do not use a quantum integration measure.
- **Scoped impact:** the interpretation of the Gaussian proposition and conditional quantum-integrated clause in `p3e:thm:v223-exact-cap-reduction`, potentially downstream native measure comparison if used; no direct established failure of Newton normalization or background gravitation was found.
- **Provenance:** dimensional mutation `E4M-IIIE-B05-002`, matrix-volume exact checks, and the source text's current unit table.

## 4. Adversarial challenge ledger (E4)

| Evidence | Attempted attack or boundary mutation | Disposition | Certificate |
|---|---|---|---|
| E4-IIIE-B05-001 | Scalaron divergence from Hessian alone as a realized vacuum mass | INVALID-PHYSICAL-PROMOTION | Trace linearization needs an actual constant-curvature background; source explicitly conditions it. |
| E4-IIIE-B05-002 | Source endpoint F_C=0,Z_C=1 solves unsourced terminal trace equation | REJECTED | C Z_C-2F_C=C>0, so there is no such vacuum. |
| E4-IIIE-B05-003 | Use an alternate x with |c t|>=1 to disprove positive T | OUT-OF-DOMAIN | BI>BU>0 gives 0<c<1 and |t|<1. |
| E4-IIIE-B05-004 | Change reciprocal source coordinates but leave incoming section rho I fixed | VALID NEGATIVE CONTROL | A metric isometry preserves the whole action only when the linear source and Jacobian are transported; source says so. |
| E4-IIIE-B05-005 | Claim bare reciprocal source derivative vanishes at q=7/2 for arbitrary R_s | VALID G-0005 | With U=10,C=1,BI=3,BU=1,R_s=2 derivative is -0.05618835...; at R_s=sqrt(UC) it vanishes. |
| E4-IIIE-B05-006 | Demand source quadratic, linear and stationary terms retain curvature units with dimensionless Y | VALID G-0006 | Printed curvature types make W quadratic term dimensionless and linear term curvature; consistent rescaling not specified. |
| E4-IIIE-B05-007 | Add arbitrary background integration weight to geometric Gaussian measure | VALID CONDITION CONTROL | Actual effective action then gains h_eff[8ln b - ln(m(R)/m(0))]; no unconditional native measure selected. |
| E4-IIIE-B05-008 | Tensor a spectator and divide source return by spectator rank without compensating rho | REJECTED | Source normalization requires rho_n=R_s/(2sqrt(n)); tensor multiplicity is not freely discarded. |
| E4-IIIE-B05-009 | Change to symmetric shared interior and assume same B coefficient | REJECTED | Shared symmetric incidence gives BI r² instead of B r²; explicit actual incidence required. |
| E4-IIIE-B05-010 | Infer native species count m=96 from algebraic three-moment target | REJECTED | Target norm is not actual species count or evaluated native source. |
| E4-IIIE-B05-011 | Interpret heat-rate scale orbit as a unique a or SI cutoff | REJECTED | Effective scale Lambda²/a invariant; no representative selected by orbit. |
| E4-IIIE-B05-012 | Identify Clifford q depth with finite group derived depth | REJECTED-BY-TYPE | Rank/codimension filtration and derived subgroup series have different targets. |
| E4-IIIE-B05-013 | Repair raw Laurent Hessian mismatch with an affine Einstein term | REJECTED | Affine terms have zero second derivative; 2/(U+C) remains nonzero. |
| E4-IIIE-B05-014 | Promote positive raw logarithmic finite heat value directly to convex f | REJECTED | Positive γ second derivative is -γ/(LR²), strictly negative. |
| E4-IIIE-B05-015 | At fixed t make hierarchy contact residual vanish identically | REJECTED | L-1/(8-q) depends on q. |
| E4-IIIE-B05-016 | Identify visibility τ with heat proper time t via positive affine law | REJECTED | Forced t(τ) has finite limit, positive affine t(τ) diverges. |
| E4-IIIE-B05-017 | Claim physical heat-clock selection solely because zero-residual ODE has a solution | INVALID-PHYSICAL-PROMOTION | Source calls equation a factorized comparison target, requiring operator and density origin. |
| E4-IIIE-B05-018 | Treat endpoint scalaron quotient as second EH term or seven finite projector events | REJECTED | Terminal term fixed R-C7 with zero Hessian; six finite smooth crossings only and FLAG separate. |

A valid challenge to a *stronger-than-printed physical claim* is not a refutation of the actual conditional theorem. Both issue mutants are independently retained as source-typing/scope certificates, not used to lower the unrelated tensor, group or semigroup proofs.

## 5. Exact cross-paper uses — source-matched, scope-guarded

| Current imported label | Checked upstream source anchor | III-E use line | Required typed scope |
|---|---|---:|---|
| `p3f:thm:trace-linearized-scalaron-mass` | Paper3F-CompleteDynamics-v1_256.tex:9565 | Paper3E:4427 | constant-curvature trace-linearity and scalaron mass conditional physical meaning |
| `p1b:thm:v223-positive-source-transport` | Paper1B-M8Geometry-v1_131.tex:19281 | Paper3E:4594 | whole source-word isometry and source/jacobian transport |
| `p1b:thm:v223-extension-flux` | Paper1B-M8Geometry-v1_131.tex:19230 | Paper3E:4674 | positive normal square-root extension and conjugate-flux minimization |
| `p3f:thm:v223-cap-parent` | Paper3F-CompleteDynamics-v1_256.tex:7740 | Paper3E:4706 | complete scalar-curvature parent including GHY canonical boundary |
| `p1b:thm:v224-poisson-defect` | Paper1B-M8Geometry-v1_131.tex:19354 | Paper3E:4871 | reference normal Poisson source |
| `p3f:thm:v224-reference-cap-parent` | Paper3F-CompleteDynamics-v1_256.tex:12603 | Paper3E:4872 | reference cap parent and positive Dirichlet normalization |
| `p3b:thm:v164-generated-heat-profile` | Paper3B-SpectralAction-v1_181.tex:3238 | Paper3E:4894 | premise-minimal scalar exponential heat generator |
| `p3f:thm:v174-generated-joint-gauge-phase-space-action` | Paper3F-CompleteDynamics-v1_256.tex:4678 | Paper3E:4936 | local pure-gauge stationary product action and constraint packet |
| `p3f:thm:v175-generated-joint-einstein-action` | Paper3F-CompleteDynamics-v1_256.tex:4977 | Paper3E:4962 | local joint Dirac Einstein coefficient |
| `p3f:thm:v175-native-local-scalar-action` | Paper3F-CompleteDynamics-v1_256.tex:5226 | Paper3E:4964 | native odd-scalar local action |
| `p3f:thm:v176-adm-constraint-packet` | Paper3F-CompleteDynamics-v1_256.tex:6081 | Paper3E:4995 | local ADM constraint and scalar canonical-momentum packet |
| `p3c:thm:v2218-born-heat-depth` | Paper3C-ProtectedHierarchy-v1_179.tex:5914 | Paper3E:5188 | finite seed depth and physical operator comparison scope |
| `p3f:cor:laur17-terminal-ren-representative` | Paper3F-CompleteDynamics-v1_256.tex:9253 | Paper3E:5462 | same-action terminal Euler intercept and one-jet affine quotient |
| `p3e:thm:uniform-reg-response-bundle` | Paper3E-GravityAction-v1_190.tex:707 | Paper3E:5533 | uniform positive REG smooth spectral scale hierarchy |

No incoming citation was promoted to a proof-use edge without checking the exact target and source domain. The above **14** links are material ancestry for these target statements only; their `IMPORTED_PROOF` edges, AND guards and source-use locators are in the batch ledger. This does not certify peer-paper derivations globally. In particular the imported joint-Dirac/noether package is **REPRODUCED** pending an independent full theorem proof, not opportunistically upgraded to `VERIFIED`.

## 6. Boundary adjudications, canonical assumptions and inherited issues

Seven detailed `BND-IIIE-B05-*` records are in the machine ledger, separating physical constitution, source generation, normal response and selected action. Key blocked promotions: scalaron Hessian → vacuum solution; mathematical cap source → native gravitational source; isometry → selected input section; scalar heat-rate orbit → physical Newton/joint-Dirac coefficient; zero-contact comparator → derived physical proper-time trajectory; group-derived subgroup clock → Clifford hierarchy; terminal Einstein representative → observed cosmological history.

New condition candidates are *not* given duplicate `BH-A` identifiers in this intermediate report: `R_s²=UC` for the q-midpoint comparison and a homogeneous `Y,ℏ_eff`/measure convention. Their earliest established occurrences and equivalence to any existing canonical assumptions must be reconciled against the **global** AssumptionRegistry at final merge. Conditions already proved earlier (G0/GP1–GP3, `H_1`, `m_p=1`, calibrated REG/CRP4, smooth corealization) are inherited, not reopened.

**Inherited open issues unchanged:**

- `BH-IIIE-G-0001`, moderate: grading carrier `W` 7-real block versus `W_L⊕W_R` spin grading map (Batch 1).
- `BH-IIIE-G-0002`, moderate: CRP4 unique base `B`-direction transport versus unlicensed uniqueness of a full `B×M` connection (Batch 1).
- `BH-IIIE-G-0003`, moderate: noncompact relative heat trace not necessarily ordinary trace-class global heat operator (Batch 2).
- `BH-IIIE-G-0004`, moderate: rank-four numerical midpoint value is verified only on `REG_0`, not arbitrary positive REG member (Batch 4).

**Cumulative status:** `PARTIALLY_AUDITED_WITH_6_OPEN_FINDINGS`. Current confidence is claim-specific E1/E3/E4 evidence, not whole-framework physical action validation. No original source paper, prior audit archive, or DAG archive is changed.

## 7. Next batch and release boundary

**Next range:** lines **5,612–6,449** (final Paper III-E source slice). Its initial section is gravity export and actual physical action obligations, followed by Petersen, scale independence, conormal cap, boundary-Schur source, whole-action matching and quantum-reduced Newton response.

**Final-batch tasks:** finish all **115/115** named claim dispositions, **92/92** proof environments and **30/30** formal remarks; adjudicate all 6 findings with any final new findings; reconcile canonical conditions once; merge the typed E1/E3/E4 layer into the **full original** DAG Atlas; validate the core and new audit layer; preserve histories and provenance; write and read back `Paper00-DAGAtlas-v1_103.zip` and `Paper00-ProofChainAudits-v1_21.zip` with **only the latest versions of each component**. The source corpus and supplied ZIPs remain unchanged until that verified final release. A genuine open condition is recorded, not silently patched or erased.

**Reproducibility:** `Paper3E-RigorousVerificationBatch05-v1_1.json` records the 26 claim spans, 16 proof spans, 7 remarks, six unnamed mathematical assertions, 18 challenges, two complete gap certificates, seven boundary audits and 14 typed imported-proof uses. `Paper3E-Batch05-IndependentChecks-v1_1.py` regenerates 78 independent controls and two issue-mutant witnesses in its `.json`. All artifacts are source-identity checked by SHA-256.


---

# Detailed Batch 6

# Paper III-E — Rigorous verification, Batch 06 (final source slice)

**Frozen source:** `Paper3E-GravityAction-v1_190.tex` (`c09e1f6c834e784d593f12827045a22b184671324c5091f2e50b12e076e3119b`); framework v2.370.
**Lines audited:** 5612–6449; 14/14 declarations and proof environments, 7/7 remarks; 127/127 independent controls passed.
**Batch verdicts:** VERIFIED=3, VERIFIED-CONDITIONAL=11. **New issue:** `BH-IIIE-G-0007` (reference locator only).

## 1. Every formal statement and source-replayed proof

| Claim ID | Source lines | Source label | Evidence-backed status |
|---|---:|---|---|
| BH-IIIE-C-0102 | 5809–5830 | `p3e:cor:v2216-local-global-response-scope` | VERIFIED-CONDITIONAL |
| BH-IIIE-C-0103 | 5872–5886 | `p3e:prop:v319-petersen-gravity-firewall` | VERIFIED-CONDITIONAL |
| BH-IIIE-C-0104 | 5912–5930 | `p3e:thm:v346-cell-scale-independence` | VERIFIED-CONDITIONAL |
| BH-IIIE-C-0105 | 5967–5992 | `p3e:thm:v229-conormal-cap` | VERIFIED-CONDITIONAL |
| BH-IIIE-C-0106 | 6005–6017 | `p3e:cor:v229-rooted-amplitude` | VERIFIED-CONDITIONAL |
| BH-IIIE-C-0107 | 6037–6054 | `p3e:prop:v229-source-counterfamily` | VERIFIED-CONDITIONAL |
| BH-IIIE-C-0108 | 6075–6082 | `p3e:prop:v229-complete-cap-injective` | VERIFIED |
| BH-IIIE-C-0109 | 6106–6146 | `p3e:prop:v289-cap-source-ward` | VERIFIED-CONDITIONAL |
| BH-IIIE-C-0110 | 6209–6237 | `p3e:thm:v353-positive-schur` | VERIFIED-CONDITIONAL |
| BH-IIIE-C-0111 | 6248–6267 | `p3e:prop:v353-schur-jet` | VERIFIED-CONDITIONAL |
| BH-IIIE-C-0112 | 6275–6294 | `p3e:prop:v353-schur-orientation` | VERIFIED |
| BH-IIIE-C-0113 | 6320–6334 | `p3e:prop:v356-whole-action-jet-criterion` | VERIFIED |
| BH-IIIE-C-0114 | 6369–6393 | `p3e:prop:v358-finite-reduction-covariance` | VERIFIED-CONDITIONAL |
| BH-IIIE-C-0115 | 6404–6429 | `p3e:cor:v358-gaussian-newton-measure` | VERIFIED-CONDITIONAL |

### BH-IIIE-C-0102: Local source certification and global response have distinct scope
- **Source/label:** `p3e:cor:v2216-local-global-response-scope`, lines 5809–5830; proof 5831–5847.
- **E1 replay:** Two integrations fix the affine freedom from f(C)=0,f’(C)=1. Differentiating R f’−f gives R f’’ and hence P=C+∫_C^R t D2(t)χ7(t)dt. The claim does not identify the raw Laurent Euler excess with this metric Euler function. Source III-D provides a distinct non-gluing certificate.
- **E3:** 6 targeted exact/numerical controls, see machine-readable independent ledger. Controls of this sort do not alone establish physical occurrence.
- **Typed scope:** Actual EXJET7 is local; global coefficient requires owned smooth second-jet transport, endpoint/source/boundary and physical normalization.
- **Exact imported prerequisites checked:** `p3d:thm:v2216-exjet-global-obstruction`, `p3d:cor:v2216-raw-euler-nongluing`, `p3d:prop:v2216-finite-born-limits`, `p3d:thm:v2216-complete-action-jets`

### BH-IIIE-C-0103: No automatic metric, Newton, or curvature correction
- **Source/label:** `p3e:prop:v319-petersen-gravity-firewall`, lines 5872–5886; proof 5887–5894.
- **E1 replay:** Existing 15-dimensional edge representations on each marked quaternionic factor yield 225=120+105 in symmetric/antisymmetric exchange eigenspaces. Availability of this auxiliary tensor does not alter the uninserted metric/operator/physical action.
- **E3:** 2 targeted exact/numerical controls, see machine-readable independent ledger. Controls of this sort do not alone establish physical occurrence.
- **Typed scope:** The conclusion is about non-insertion, not a no-go for an independently derived sourced finite anisotropy.
- **Exact imported prerequisites checked:** `p1b:thm:petersen-factor-exchange`

### BH-IIIE-C-0104: Exact scale residual and an independent cutoff counterfamily
- **Source/label:** `p3e:thm:v346-cell-scale-independence`, lines 5912–5930; proof 5931–5942.
- **E1 replay:** From U=Λg²/(96π²), Kp=6/Rmom² and ρH=3/π, U/(ρHKp)=(Λg Rmom)²/(24√(3π))². Changing Λg→sΛg at fixed pre-port momentum data shifts the residual by 2log(s).
- **E3:** 3 targeted exact/numerical controls, see machine-readable independent ledger. Controls of this sort do not alone establish physical occurrence.
- **Typed scope:** This mathematical counterfamily is pre-port only, not an actual licensed physical cutoff variation.
- **Exact imported prerequisites checked:** No additional indispensable remote theorem beyond the stated action/definition and source hypotheses.

### BH-IIIE-C-0105: Full conormal flux realization and absolute weight
- **Source/label:** `p3e:thm:v229-conormal-cap`, lines 5967–5992; proof 5993–6003.
- **E1 replay:** For common positive K0 and GK0, constrained p0+p1=j stationary equations yield p0=j/(1+G),p1=Gj/(1+G) and positive minimum 〈j,K0^-1 j〉/[2(1+G)]. The transported source covariance commuting with UR makes the all-column norm b²γN²R²d0. Matching 2Δ requires b²γN²d0=4Δ.
- **E3:** 8 targeted exact/numerical controls, see machine-readable independent ledger. Controls of this sort do not alone establish physical occurrence.
- **Typed scope:** Inherited Paper I-B operator-domain positivity, full homothety and source-column covariance; physical b, normal operator and density remain unselected.
- **Exact imported prerequisites checked:** `p1b:prop:v229-affine-conormal`, `p1b:thm:v229-coupled-homothety`

### BH-IIIE-C-0106: Evaluated amplitude target for the rooted block
- **Source/label:** `p3e:cor:v229-rooted-amplitude`, lines 6005–6017; proof 6018–6024.
- **E1 replay:** The singlet spectral weights of the rooted positive 2x2 A block give 〈KD〉=Q_D. Paper I-B exact conormal theorem makes d0=Q_D/μ². Substitution of γN=μ/Rs into the preceding cap-amplitude target yields b_req²=4Δ Rs²/Q_D.
- **E3:** 9 targeted exact/numerical controls, see machine-readable independent ledger. Controls of this sort do not alone establish physical occurrence.
- **Typed scope:** Only on the frozen constant two-partner block with the same source, normal-bag and shared operator domain; b_req is a comparison target.
- **Exact imported prerequisites checked:** `p1b:thm:v229-conormal-response`, `p3e:thm:v229-conormal-cap`

### BH-IIIE-C-0107: Geometric anchors alone do not select the source
- **Source/label:** `p3e:prop:v229-source-counterfamily`, lines 6037–6054; proof 6055–6069.
- **E1 replay:** h is nonnegative and reciprocal; its polynomial factor has double zeros at x²=C/U and U/C. The remaining factor vanishes at x=1 and at 0,∞. The inequality [2/(1+G)]h/t² ≤ 2(1+G)(G²−2)²/G⁸≤4 gives Bε<BI for 0<ε<1/4. Nonzero h away from anchors changes B.
- **E3:** 24 targeted exact/numerical controls, see machine-readable independent ledger. Controls of this sort do not alone establish physical occurrence.
- **Typed scope:** The deformed current is a mathematically admissible comparison; physical occurrence is expressly not claimed.
- **Exact imported prerequisites checked:** `p3e:thm:v229-conormal-cap`

### BH-IIIE-C-0108: The retained inverse-square source cannot hide a coefficient mismatch
- **Source/label:** `p3e:prop:v229-complete-cap-injective`, lines 6075–6082; proof 6083–6085.
- **E1 replay:** Differentiation yields d_B[R²B−σ²/B²]=R²+2σ²/B³>0 for B>0. Hence a common complete density at fixed R and σ forces the same B.
- **E3:** 5 targeted exact/numerical controls, see machine-readable independent ledger. Controls of this sort do not alone establish physical occurrence.
- **Typed scope:** Pointwise fixed R and fixed source σ; not a statement about retuning the source or boundary.
- **Exact imported prerequisites checked:** No additional indispensable remote theorem beyond the stated action/definition and source hypotheses.

### BH-IIIE-C-0109: One-anchor differential certificate for the complete inverse-square source
- **Source/label:** `p3e:prop:v289-cap-source-ward`, lines 6106–6146; proof 6147–6161.
- **E1 replay:** The derivative of T^-1 is −T^-1 T’ T^-1, so s’=2〈j’,T^-1j〉−〈T^-1j,T’T^-1j〉. Multiplying by B² gives exact differential (B²s)’; connectedness plus one reference fixes σ². For the 4x4 port full-column trace T_s^-1=4/b² yields B²s=(BI Rs)².
- **E3:** 14 targeted exact/numerical controls, see machine-readable independent ledger. Controls of this sort do not alone establish physical occurrence.
- **Typed scope:** Valid for positive C1 B,T and C1 j on a connected interval with a reference. No physical native operator/current determination from Ward algebra.
- **Exact imported prerequisites checked:** `p3e:thm:v223-cap-source`

### BH-IIIE-C-0110: Positive two-channel Schur characterization
- **Source/label:** `p3e:thm:v353-positive-schur`, lines 6209–6237; proof 6238–6246.
- **E1 replay:** The block inverse top compression equals S_+^-1, and with J=(Rs/√2)P+ the trace is −Rs² Tr_{E+}S_+^-2/16. Rank2 S+=bI gives −Rs²/(8b²). For A=D=I, bI iff CC†=u²I, yielding unitary polar factor for u≠0.
- **E3:** 25 targeted exact/numerical controls, see machine-readable independent ledger. Controls of this sort do not alone establish physical occurrence.
- **Typed scope:** Positive Hermitian 2+2 comparison source and normalized frame; does not prove the actual Dirac DtN map equals this finite model.
- **Exact imported prerequisites checked:** `p3e:def:v223-cap-data`

### BH-IIIE-C-0111: Exact first curvature-jet target
- **Source/label:** `p3e:prop:v353-schur-jet`, lines 6248–6267; proof 6268–6273.
- **E1 replay:** Two derivatives of S=A−CD^-1C† at C(0)=0 give S’(0)=A’(0), S’’(0)=A’’(0)−2C’(0)C’(0)†. From t=R/(2Rs)+O(R³), b’’(0)=−c²/(2Rs²).
- **E3:** 2 targeted exact/numerical controls, see machine-readable independent ledger. Controls of this sort do not alone establish physical occurrence.
- **Typed scope:** Requires C² regularity through reference R=0 and the specifically justified normalization at R=0; native equality is a test.
- **Exact imported prerequisites checked:** `p3e:thm:v353-positive-schur`

### BH-IIIE-C-0112: Scalar-source non-identifiability
- **Source/label:** `p3e:prop:v353-schur-orientation`, lines 6275–6294; proof 6295–6300.
- **E1 replay:** For K_U off-diagonal uU, Schur block bI gives common scalar trace but mixed inverse block −uU/b retains U orientation. Separate Sε diagonal positive examples have identical Tr Sε^-2=2/b² while not proportional to the identity.
- **E3:** 9 targeted exact/numerical controls, see machine-readable independent ledger. Controls of this sort do not alone establish physical occurrence.
- **Typed scope:** A scalar return alone cannot identify current orientation, full response or same-source coupling.
- **Exact imported prerequisites checked:** `p3e:thm:v353-positive-schur`

### BH-IIIE-C-0113: Equivalent first-jet and action matching
- **Source/label:** `p3e:prop:v356-whole-action-jet-criterion`, lines 6320–6334; proof 6335–6344.
- **E1 replay:** On a connected open regular source chart, zero differential of S_phys−zS_J implies constant difference, and the converse follows by differentiation. The x,y example matches the EH x coefficient at z=1/96 but differs in source y curvature.
- **E3:** 1 targeted exact/numerical controls, see machine-readable independent ledger. Controls of this sort do not alone establish physical occurrence.
- **Typed scope:** One constant z and all retained variations on one connected chart; physical projection itself not generated.
- **Exact imported prerequisites checked:** `p3e:prop:v2211-whole-action-newton-certificate`

### BH-IIIE-C-0114: Exact finite reduction covariance test
- **Source/label:** `p3e:prop:v358-finite-reduction-covariance`, lines 6369–6393; proof 6394–6402.
- **E1 replay:** Differentiation under positive finite integration gives z〈S_u〉_z and Hessian z〈S_uv〉−z² Cov_z(S_u,S_v)/hbar. Differentiating the normalized expectation with respect to z gives −Cov_z(S_u,S)/hbar and the oriented integral from 1 to z.
- **E3:** 11 targeted exact/numerical controls, see machine-readable independent ledger. Controls of this sort do not alone establish physical occurrence.
- **Typed scope:** Source-independent internal measure and legal interchange; if external source-dependent density is present it contributes additional terms.
- **Exact imported prerequisites checked:** No additional indispensable remote theorem beyond the stated action/definition and source hypotheses.

### BH-IIIE-C-0115: Gaussian determinant and measure criterion
- **Source/label:** `p3e:cor:v358-gaussian-newton-measure`, lines 6404–6429; proof 6430–6435.
- **E1 replay:** Complete the Gaussian square with source-dependent positive K and common density rho(x)dy: Γ_z=z S_red+(hbar/2)ln detK−hbar ln rho+(m hbar/2)ln z + constant. Therefore dΓ_z−z dΓ_1=hbar(1−z)d ln(sqrt(detK)/rho). K=e^{x²},rho=1 yields zero first derivative but nonzero Hessian at 0.
- **E3:** 7 targeted exact/numerical controls, see machine-readable independent ledger. Controls of this sort do not alone establish physical occurrence.
- **Typed scope:** Gaussian-specific source-dependent measure, identical for all z; extra measure requirement is not a Born–Hopf physical measure selection.
- **Exact imported prerequisites checked:** `p3e:prop:v358-finite-reduction-covariance`

## 2. Formal remarks

| Lines | Remark | Disposition |
|---|---|---|
| 5896–5905 | A possible sixfold angular diagnostic, not a gravitational source | FORMALIZED-SCOPE |
| 5943–5953 | Physical owner status | FORMALIZED-SCOPE |
| 6087–6100 | What the conormal theorem establishes | SOURCE_REFERENCE_UNRESOLVED |
| 6162–6169 | Scope of the one-anchor test | FORMALIZED-SCOPE |
| 6302–6313 | Native-source firewall and dependence | FORMALIZED-SCOPE |
| 6346–6355 | Separate physical matching obligation | FORMALIZED-SCOPE |
| 6437–6446 | Physical projection remains an independent gate | FORMALIZED-SCOPE |

## 3. Source-local G-0007 certificate

- **ID:** BH-IIIE-G-0007; `DAG_COVERAGE / MISSING_EVIDENCE`; MINOR; OPEN.
- **Origin:** `Paper3E-GravityAction-v1_190.tex:6095–6099`, `p3e:rem:v229-native-selection`.
- **Exact failure:** `p3f:sec:v229-action-tests` is not defined in any `.tex` source of the authoritative `Paper00-PapersMinimal-v2_370` archive. An apparently related section `p3f:sec:v229-cap-uv-hessian` occurs at Paper III-F:9071, but cannot be substituted without checking intent and coverage.
- **E3/E4:** complete reference-label census; no proof step in the conormal flux theorem requires the dangling locator.
- **Impact:** navigability and source-matched downstream-reference certificate only; no established mathematical refutation or physical prediction effect.
- **Resolution requirement:** locate current intended Paper III-F section/results and replace/migrate the reference in an explicitly separate source-editing task. The audit leaves source unchanged.

## 4. E4 adversarial challenges

| ID | Attack | Disposition |
|---|---|---|
| E4-IIIE-B06-001 | Infer a global physical metric from local EXJET7 Hessian alone | REJECTED-BY-SOURCE |
| E4-IIIE-B06-002 | Read Petersen auxiliary 120-dimensional exchange eigenspace as a new 120-element 2I action | OUT-OF-DOMAIN |
| E4-IIIE-B06-003 | Vary cutoff s at fixed momentum and falsely claim true physical history | INVALID-PHYSICAL-PROMOTION |
| E4-IIIE-B06-004 | Assert conormal b=1 follows from unit incoming singlet | REJECTED |
| E4-IIIE-B06-005 | Retain only one conormal source column | OUT-OF-DOMAIN |
| E4-IIIE-B06-006 | Conclude finite reciprocal midpoint and endpoints determine unique source profile | VALID-COUNTERFAMILY |
| E4-IIIE-B06-007 | Use a variable physical sigma to evade injection at fixed sigma | OUT-OF-DOMAIN |
| E4-IIIE-B06-008 | One reference s and Ward only at one point imply s=σ²/B² globally | VALID-REJECTION |
| E4-IIIE-B06-009 | Scalar Schur inverse-square return determines unitary channel orientation | VALID-NONIDENTIFIABILITY |
| E4-IIIE-B06-010 | Treat C(0)=0 as sufficient to fix A(0),D(0) and Schur first jets | OUT-OF-DOMAIN |
| E4-IIIE-B06-011 | Gravity-only EH coefficient matching proves all-direction physical action equality | VALID-COUNTEREXAMPLE |
| E4-IIIE-B06-012 | Assume quantum first-jet scaling follows from classical action factor at fixed hbar | VALID-OBSTRUCTION |
| E4-IIIE-B06-013 | Treat nonexistent PaperIII-F cap-test section label as verified proof import | VALID-SOURCE-LOCATOR |
| E4-IIIE-B06-014 | Assume Gaussian first source derivative at one point ensures all jets match | VALID-HESSIAN-COUNTEREXAMPLE |
| E4-IIIE-B06-015 | Demand any continuous U(R) has an operator curvature derivative | OUT-OF-CLAIM |

## 5. Qualified downstream and upstream dependencies

- Papers III-D and I-B imports were checked only where directly used by Paper III-E. Imported source proof hypotheses retain their own domain, normal operator and density conditions.
- Earlier G-0005 is in a general cap family. This final source section explicitly restricts the conormal member to `R_s=√(UC)`; this provides a domain-specific valid route, not a retroactive unconditional proof of the earlier claim.
- Earlier G-0006 dimensional Gaussian coordinate/measure issue remains unresolved. The last finite quantum theorem independently demonstrates what additional measure information is required for a physical Newton projection.
- The raw `U_J^raw=96U` and the pre-port cell ratio do not supply a common-owner physical Newton action or observed gravitational normalization.

## 6. Audit/verification boundary

- All fourteen formal proofs were source-replayed. Independent evidence uses exact calculus, positive matrix/spectral reconstruction, counterfamilies, finite Gibbs differentiation, determinant tests and a complete cross-reference census.
- Code and JSON companion files preserve every control and result. E1, E3 and E4 are separate evidence roles conducted by one executor, not a claim of simultaneous independent-agent work.
- The complete six-batch source census and the seven issue certificates will be integrated in the versioned Atlas audit layer. The proof-chain audit ZIP contains one finished Paper3E audit file, not every intermediate batch.


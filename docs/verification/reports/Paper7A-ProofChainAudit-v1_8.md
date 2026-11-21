# Paper7A — current-source bounded verification annex, 2026-11-18

This is the latest full audit report, with the original historical audit text preserved verbatim below. Current source matches v3.031; older `OPEN` entries retain historical meaning. For the **effective current disposition**, see `Paper00-QCDReverificationBatch1-v1_1.md` and crosswalk v1.3 in the DAG. This is not a full new-paper E3/E4 audit.

**Reviewed roots:** 8 · **Local corrections verified:** 6 · **Owner-gated:** 2.

| Issue | Current source line | Effective source disposition |
|---|---:|---|
| `BH-G-000134` | 314 | Source conditional, owner unresolved |
| `BH-G-000135` | 449 | Scoped local correction verified |
| `BH-G-000136` | 1220 | Scoped local correction verified |
| `BH-G-000137` | 1220 | Scoped local correction verified |
| `BH-G-000138` | 1338 | Source conditional, owner unresolved |
| `BH-G-000139` | 1562 | Scoped local correction verified |
| `BH-G-000140` | 1721 | Scoped local correction verified |
| `BH-G-000141` | 1721 | Scoped local correction verified |

---

## Preserved historical source-era audit (original text below)

# Source migration and repair-integration addendum — Paper7A-ProofChainAudit-v1_7.md

**Integration release:** `Paper00-PapersMinimal-v3_007.zip`, 14 November 2026.
**Current paper source:** `Paper7A-QCDKernel-v1_172.tex`.
**Status:** `SOURCE_INTEGRATED; GLOBAL_SOURCE_REAUDIT_PENDING`. An inherited historical audit is not a correctness certificate for the newer current manuscript.
**Evidence policy:** Local algebraic proofs and scoped tests do not discharge physical source/observable interfaces or automatically alter the canonical proof DAG.

---

## Historical source-bound audit: Paper7A-ProofChainAudit-v1_6.md
# Repair addendum — Paper7A, 13 November 2026

**Current source:** `Paper7A-QCDKernel-v1_166.tex` (SHA-256 `dcbc2551f9fc08eebeedc41c83a3c2a0f0a9b5144e4471218bb3307d1e73afb6`)  
**Inherited audit:** `Paper7A-ProofChainAudit-v1_5.md`; the complete text follows, unedited as historical evidence.  
**Disposition:** SOURCE-REPAIR EVENT, not independent full re-audit; no theorem/physical status promotion.  

| Distinct source-audit issue | Current TeX location(s) | Repair/scope | Remaining status |
|---|---|---|---|
| `BH-G-000134` | `Paper7A-QCDKernel-v1_166.tex:304`, `Paper7A-QCDKernel-v1_166.tex:676` | Retired fermion SVD source replaced by current charged-preterminal parent contraction and certified hierarchy-arrow interface. | SOURCE_REPAIRED; IMPORTED/PHYSICAL CONDITION OPEN |
| `BH-G-000135` | `Paper7A-QCDKernel-v1_166.tex:452`, `Paper7A-QCDKernel-v1_166.tex:460`, `Paper7A-QCDKernel-v1_166.tex:986` | A2 roots decomposed in sl3(C); su3 is the eight-real-dimensional compact form, not all End0(C). | SOURCE_REPAIRED; REAUDIT PENDING |
| `BH-G-000136` | `Paper7A-QCDKernel-v1_166.tex:1210`, `Paper7A-QCDKernel-v1_166.tex:1228` | Scalar curvature shell is required to be a nonzero orthogonal projection before its Rayleigh infimum is defined. | SOURCE_REPAIRED; REAUDIT PENDING |
| `BH-G-000137` | `Paper7A-QCDKernel-v1_166.tex:1210`, `Paper7A-QCDKernel-v1_166.tex:1217`, `Paper7A-QCDKernel-v1_166.tex:1225`, `Paper7A-QCDKernel-v1_166.tex:1228` | Rayleigh-gap loss is separated from actual compressed heat-kernel loss unless the shell reduces H. | SOURCE_REPAIRED; REAUDIT PENDING |
| `BH-G-000138` | `Paper7A-QCDKernel-v1_166.tex:1339`, `Paper7A-QCDKernel-v1_166.tex:1344` | Diagonal/global color singlet is distinguished from vertexwise Gauss-invariant physical QCD block. | SOURCE_REPAIRED; IMPORTED/PHYSICAL CONDITION OPEN |
| `BH-G-000139` | `Paper7A-QCDKernel-v1_166.tex:1568` | Finite exponential-transfer source-derivative sign corrected; log responses carry Duhamel ordering and contact jets. | SOURCE_REPAIRED; REAUDIT PENDING |
| `BH-G-000140` | `Paper7A-QCDKernel-v1_166.tex:1688`, `Paper7A-QCDKernel-v1_166.tex:1708` | Static susceptibility includes the source-Hessian contact term and a spectral sum on the excited subspace. | SOURCE_REPAIRED; REAUDIT PENDING |
| `BH-G-000141` | `Paper7A-QCDKernel-v1_166.tex:1688` | Spectral susceptibility sum explicitly requires a simple isolated finite ground state and positive gap. | SOURCE_REPAIRED; IMPORTED/PHYSICAL CONDITION OPEN |

See `Paper00-AuditRepairBatch-v1_2.md` and the 24/24 scoped math controls in the active DAG atlas for checks and counterexamples. Historical source-hash and line locations below apply **only** to the previous paper version. Do not reinterpret their original `OPEN`, `REFUTED`, or `VERIFIED` labels as new-version global adjudications.

---

## Historical audit baseline (unaltered text)

# Paper VII-A — Rigorous Verification DAG Proof-Chain Audit, Batches 1–5

**Current final state:** `FULLY_AUDITED_WITH_OPEN_GAPS`; **314 of 314 formal statements** and **nine material unnamed derivations**, source-anchored through line **8831**. Earlier batch notes below are retained as historical checkpoints, not the final disposition. Only claims with appropriate independent evidence are marked `VERIFIED` or `VERIFIED-CONDITIONAL`; the others are explicitly not certified. **No source edits or new theory.**

**Source freeze:** `Paper7A-QCDKernel-v1_165.tex` — SHA256 `11233c2be618f189ec69edef36bc7a78122d90f13d28cc2f7c39b5b94076788a`; identical in `Paper00-PapersMinimal-v2_371` and `Paper00-DAGAtlas-v1_115/Sources-v2_371`. **Protocol:** `Paper00-RigorousVerificationDAGWorkProtocol-v2_4`. **Current cumulative lines:** 1–8831, with original Batch 1 evidence retained unchanged.

## Batch 1 statement dispositions (original source lines 1–1876)

| Status | Formal statements | Interpretation |
|---|---:|---|
| `VERIFIED` | 12 | E1 plus independent exact/theorem E3 on actual mathematical claim |
| `VERIFIED-CONDITIONAL` | 12 | E1 and independent check of conditional conclusion, retaining printed antecedent |
| `REPRODUCED` | 11 | Source proof rechecked, but independent central certificate/import not established |
| `FORMALIZED` | 16 | Definition, scoped rule, or remark read and typed |
| `INCONSISTENT` | 6 | A precise source-level problem recorded under one or more issue IDs |

**Batch 1 scope at that point:** The following Batch 1 statement ledger retains its original 57-item counts; Batch 2 dispositions appear below. At the Batch 1–2 boundary, 198 formal blocks remained unaudited; 134 remain at the current Batch 3 boundary. Paper VII-B/C consumers and earlier papers are consulted only to verify specific imported scope or forward links, not audited independently. The disconnected source-prefix/complete physical occurrence distinction is intentionally preserved. No physical mass, strong infrared scale, string tension, or hadron spectrum is certified by this batch.

## Independent finite certificates

1. **Hurwitz shell graph.** Independently construct the 24 quaternion units `{±1, ±i, ±j, ±k} ∪ { (±1±i±j±k)/2 }`, connect points at scalar product `1/2`; exact SymPy eigenvalues `8:1, 4:4, 0:9, -2:8, -4:2`, degree 8 and 96 edges. The band dimensions sum to 24, and `9×8=72`.
2. **Cube link and spinor remainder.** The 8 local cube directions have vanishing first and third moments and second moment `(8/3)I_3`; order-three Taylor bound `8*(3/(8ℓ))*(ℓ³/6)=ℓ²/2` matches source at lines 1048–1086. Fixed ℓ/R=π/3 remains non-asymptotic.
3. **Finite Schur scalar source.** Independent random 5×5 Hermitian block check yields full Schur eigenvector residual `<3e-15` and exact source-derivative agreement `<2e-15`; symbolic spectral order proves `δ/(δ+s) ≤ w ≤ D/(D+s)` under `0<δI≤C−EI≤DI`.
4. **Dirac Schur determinant and scalar insertion.** Independent random 4×4 Hermitian K confirms the complex block determinant and mass derivative trace identities (floating-point error at numerical precision).
5. **Adversarial controls.** Noncommuting spectral shell projection, 1×1 positive source transfer, 2×2 nonlinear-source contact, 3×3 degenerate ground, and global-versus-local color Gauss countercontrols are explicit and respect the printed mathematical domain of the tested unqualified claim.

## All distinct Batch 1 issues

### BH-G-000134 — `CROSS_PAPER_CONFLICT` (moderate)

**First origin:** `p10:eq:qrg-quark-mass-operator-needed`, `Paper7A-QCDKernel-v1_165.tex:298-307`. **Layer:** `SOURCE-AS-PRINTED`. **Lifecycle:** `OPEN`.

**Finding and evidence:** Current P5A v3.202 lines 5247-5316 explicitly closes FERMION_PRETERMINAL_PARENT_CONTRACTION and retires FERMION_SAME_ACTION_SVD_ASSEMBLY; current P5B v5.192 lines 315-329 says no SVD assembly interface remains. P7A lines 301 and 710-718 call it live.

**Exact remaining obligation:** Replace historical retired SVD assembly prerequisite with current V-A v397 source and certified hierarchy-arrow input; keep G16 RG for execution.

**Scope/impact:** Terminology/dependency incompatibility; does not refute the upstream charged source realization. Cross-paper impacts remain candidate-only: Paper7B quantitative quark-source consumers.

### BH-G-000135 — `TYPE_OR_DOMAIN` (moderate)

**First origin:** `p10:prop:d4-a2-reading-of-qcd-color-support`, `Paper7A-QCDKernel-v1_165.tex:450-462`. **Layer:** `SOURCE-AS-PRINTED`. **Lifecycle:** `OPEN`.

**Finding and evidence:** Root matrices E_12 are in sl_3(C) but not in su(3); End_0(C) has complex dimension 8 (real dimension 16), whereas su(3) has real dimension 8. Current P5A v3.202 lines 1445-1490 explicitly constructs su(3) as an 8-real-dimensional compact form by complexification.

**Exact remaining obligation:** Type the displayed root-space decomposition in sl_3(C) (complexification), and distinguish its compact su(3) real form; propagate same distinction to line 979.

**Scope/impact:** The 8-dimensional adjoint counting and SU(3) gauge closure survive after correcting types. No certified remote impact.

### BH-G-000136 — `MISSING_CONDITION` (minor)

**First origin:** `p10:thm:primitive-scalar-shell-coefficient-fixed`, `Paper7A-QCDKernel-v1_165.tex:1210-1215`. **Layer:** `SOURCE-AS-PRINTED`. **Lifecycle:** `OPEN`.

**Finding and evidence:** For valid spectral projector P_sh=0 (empty spectral band) the infimum is over the empty set, so no finite excitation energy exists; paper does not print P_sh!=0.

**Exact remaining obligation:** Require a nonzero scalar spectral projector (a nonempty unit-vector domain) before declaring gamma_sh exists as a finite number.

**Scope/impact:** Does not affect a certified nonempty scalar shell. No certified remote impact.

### BH-G-000137 — `MISSING_CONDITION` (moderate)

**First origin:** `p10:thm:primitive-scalar-shell-coefficient-fixed`, `Paper7A-QCDKernel-v1_165.tex:1217-1224`. **Layer:** `INTERPRETED`. **Lifecycle:** `OPEN`.

**Finding and evidence:** Exact 2x2 countertest: H=diag(0,4), P=(1/2)[[1,1],[1,1]], gamma=2, exp(-gamma) = exp(-2), whereas ||P exp(-H) P|| on Ran P=(1+exp(-4))/2; these differ and P is the spectral projector of a Hermitian curvature-test matrix I-P.

**Exact remaining obligation:** Either identify epsilon_sh as an auxiliary Rayleigh-gap diagnostic or prove [P_sh,H_L]=0 (or appropriate semigroup invariance/controlled error) for actual restricted-transfer contraction.

**Scope/impact:** Nominal epsilon=1-exp(-t gamma) remains a valid definition; it is not automatically an actual transfer amplitude. No certified remote impact.

### BH-G-000138 — `TYPE_OR_DOMAIN` (major)

**First origin:** `p10:def:finite-colour-singlet-projector`, `Paper7A-QCDKernel-v1_165.tex:1335-1340`. **Layer:** `SOURCE-AS-PRINTED`. **Lifecycle:** `OPEN`.

**Finding and evidence:** Current P7A theorem p10:thm:v350-local-gauss-projector lines 8368-8395 explicitly proves Ran P_Gauss subset Ran P_sing and gives bilocal qbar(x) q(y) as global singlet but local non-singlet; hence early global projector alone cannot establish physical gauge-invariant block.

**Exact remaining obligation:** Carry the source-defined distinction between diagonal/global color singlet and actual vertexwise local Gauss-invariant physical link/matter states; require declared P_Gauss/invariant truncation for physical label.

**Scope/impact:** Exact Haar average and global triality claims remain correct; physical Gauss projection conditional. Cross-paper impacts remain candidate-only: Paper7B hadronic physical-sector claims, Paper7C continuum native gauge invariance.

### BH-G-000139 — `NORMALIZATION_OR_READOUT` (major)

**First origin:** `p10:def:native-qcd-generating-functional`, `Paper7A-QCDKernel-v1_165.tex:1564-1579`. **Layer:** `SOURCE-AS-PRINTED`. **Lifecycle:** `OPEN`.

**Finding and evidence:** In-domain 1x1 positive transfer K[J]=exp(-J), W=-J, O=-d log K=+1, yet displayed one-point rule gives dW=-1. For K=e^{-tH[J]}, -d log K=t dH/dJ, not dH/dJ unless t is normalized/absorbed.

**Exact remaining obligation:** Reconcile derivative sign and transfer-time/source normalization between -d log K, O_A=dH/dJ and W=log Tr K; retain nonlinear/noncommuting source jets.

**Scope/impact:** Current later p10:thm:v350-dynamical-source-hessian provides consistent W derivatives but does not change the earlier incompatible displayed sign convention. Cross-paper impacts remain candidate-only: Paper7B current/cumulant readouts, Paper7C source insertion limits.

### BH-G-000140 — `NORMALIZATION_OR_READOUT` (major)

**First origin:** `p10:eq:finite-susceptibility-readout`, `Paper7A-QCDKernel-v1_165.tex:1707-1718`. **Layer:** `SOURCE-AS-PRINTED`. **Lifecycle:** `OPEN`.

**Finding and evidence:** Exact H(j)=[[2j^2,-j],[-j,3]]: at j=0 spectral sum is 2/3, while -E_0''(0)=-10/3; difference -4 is the contact H_jj. Later p10:thm:v350-dynamical-source-hessian explicitly includes -beta Tr rho H_ab.

**Exact remaining obligation:** Specify a linear source Hamiltonian with zero source-contact Hessian (or include the H_AB contact term) and the exact ground-energy derivative sign; use the later complete Hessian on general source packets.

**Scope/impact:** The spectral sum is correct for gapped nondegenerate ground and linear perturbative couplings; not for generic declared complete sources. Cross-paper impacts remain candidate-only: Paper7B susceptibility readouts.

### BH-G-000141 — `MISSING_CONDITION` (moderate)

**First origin:** `p10:eq:finite-susceptibility-readout`, `Paper7A-QCDKernel-v1_165.tex:1687-1718`. **Layer:** `SOURCE-AS-PRINTED`. **Lifecycle:** `OPEN`.

**Finding and evidence:** Admissible finite H(0)=diag(0,0,3), perturbation -j(|0><1|+|1><0|) has E_ground(j)=-|j|, no twice differentiable ground energy at j=0 and M_1=0 makes denominator undefined when residue nonzero.

**Exact remaining obligation:** For the printed nondegenerate spectral denominator and ground-energy Hessian, require a simple isolated ground eigenvalue with positive gap to relevant states, or supply a separately defined degenerate-state response.

**Scope/impact:** Finite Schur resolvent identities remain valid without this physical-vacuum uniqueness assumption. Cross-paper impacts remain candidate-only: Paper7B zero-gap susceptibility comparisons.

## Statement-level coverage ledger

| # | Current source start–end | Exact label | Status | Evidence-bound disposition |
|---:|---:|---|---|---|
| 001 | 185–198 | `p10:def:fixed-mp-large-mx` | `FORMALIZED` | m_p fixed by source constitution; m_x is comparison-side scope. |
| 002 | 213–216 | `p10:thm:no-mp-flow-paper-x` | `REPRODUCED` | No-backflow statement replays typed carrier and distinct reciprocal comparison; not an independent global proof. |
| 003 | 228–242 | `p10:cor:v2180-mx-unfolding-no-quark-constructor` | `REPRODUCED` | Transport of existing constructor does not establish new extensive CAR or shift; conditional source-owner restriction. |
| 004 | 318–321 | `p10:def:paper-vi-numerical-import-convention` | `FORMALIZED` | Historical coupling and split coordinates explicitly retained as comparison-only. |
| 005 | 323–336 | `p10:rem:geometric-defect-versus-strong-seed` | `FORMALIZED` | Geometric count and coupling source are distinct typed data. |
| 006 | 338–341 | `p10:rem:paper-vi-quark-split-versus-p8-spurions` | `FORMALIZED` | Split coefficients do not constitute a microscopic mass operator. |
| 007 | 363–366 | `p10:def:logical-status-classes` | `FORMALIZED` | Source-defined logical-status legend; no physical computation asserted. |
| 008 | 368–371 | `p10:thm:inherited-qcd-interface` | `REPRODUCED` | Import boundary matches current charged preterminal V-A source and conditional G16 threshold; stale SVD name challenged separately. |
| 009 | 383–400 | `p10:thm:geometric-qcd-spine` | `VERIFIED-CONDITIONAL` | End(C)=C I + End0(C) gives 1+8 and delta; V-A generated trimer occurrence is a prior condition. |
| 010 | 405–426 | `p10:cor:exceptional-shell-ancestry-of-qcd-delta` | `VERIFIED-CONDITIONAL` | E3 9*8=72=rank(E6)*h(E6)=6*12; III-G imported determinant status remains typed. |
| 011 | 437–465 | `p10:prop:d4-a2-reading-of-qcd-color-support` | `INCONSISTENT` | Root decomposition displayed for compact real su(3), although complex root spaces inhabit sl3(C); BH-G-000135. |
| 012 | 474–497 | `p10:thm:momentum-s3-harmonic-basis` | `VERIFIED` | E3 SU(2) Peter-Weyl scalar Laplace spectrum, (ell+1)^2 multiplicity and closed sum of squares. |
| 013 | 504–514 | `p10:thm:connected-flow-finite-shell-no-go` | `VERIFIED` | E3 continuous image of connected group in finite discrete Sym(F) is a singleton. |
| 014 | 522–553 | `p10:cor:harmonic-null-action-shell-boundary` | `VERIFIED-CONDITIONAL` | E3 round-isometry commutation with full Laplacian eigenspaces and integral U(1) character weights; requires declared intertwiner for shell. |
| 015 | 566–574 | `p10:cor:v203-exact-geometric-sampling` | `REPRODUCED` | Exact sampling uses II-C and I-A specific carrier isometries; source-matched imports located, no assertion that shell sampling is automatically null-equivariant. |
| 016 | 604–637 | `p10:thm:external-theorem-bank-import-map` | `FORMALIZED` | Permission rule for theorem-bank imports; application requires each external theorem hypothesis, not supplied as physical coefficient. |
| 017 | 643–646 | `p10:thm:qcd-readout-chronology` | `FORMALIZED` | Readout chronology is a constitutive provenance constraint, not an empirical prediction. |
| 018 | 651–654 | `p10:thm:finite-qcd-operator-layer-inherited` | `REPRODUCED` | Pure glue finite operator sort distinguished from physical running mass and scale; projective physical Gauss caveat BH-G-000138. |
| 019 | 692–700 | `p10:thm:v164-no-independent-qmass-constructor` | `REPRODUCED` | Actual rooted preterminal source is from P5A v397 on hierarchy-origin certified packet; G16 RG remains needed. |
| 020 | 710–720 | `p10:cor:v164-g34-transitive-status` | `INCONSISTENT` | SVD_ASSEMBLY named as live requirement although current V-A/V-B source retires it; BH-G-000134. |
| 021 | 812–815 | `p10:def:qcd-compiler-endpoint` | `FORMALIZED` | Finite compilation endpoint defined by input completeness, not physical realization. |
| 022 | 817–826 | `p10:def:finite-qcd-compilation-datum` | `FORMALIZED` | Finite typed QCD data tuple and pure glue deletion branch. |
| 023 | 828–846 | `p10:def:compiled-finite-strong-matrices` | `FORMALIZED` | For supplied self-adjoint H the shifted exponential is positive, eigenvalue 1 on ground space. |
| 024 | 848–851 | `p10:thm:finite-qcd-matrix-compiler` | `VERIFIED-CONDITIONAL` | E3 all operations are deterministic finite linear algebra on fully supplied matrices; no physical input generated by this observation. |
| 025 | 883–901 | `p10:def:hurwitz-shell-transfer-complex` | `FORMALIZED` | Hurwitz 24-cell finite cell/transfer complex is a momentum-side definition. |
| 026 | 903–927 | `p10:thm:hurwitz-shell-adjacency-spectrum` | `VERIFIED` | E3 exact 24x24 quaternion adjacency characteristic spectrum: 8(1),4(4),0(9),-2(8),-4(2); Laplacian and 9x8 counts follow. |
| 027 | 932–948 | `p10:lem:hurwitz-cube-link-second-moment` | `VERIFIED` | E3 all eight cube signs give first moment 0 and second moment (8/3)I; checked independently from 24 quaternion units. |
| 028 | 953–990 | `p10:thm:hurwitz-trimer-color-carrier` | `INCONSISTENT` | Local cube split and V-A trimer import replay; literal End0(C_q) ≅ su(3) is wrong as typed; shares BH-G-000135. |
| 029 | 1005–1036 | `p10:cor:paper6-split-carrier-realization` | `VERIFIED-CONDITIONAL` | E3 8=2+3+3 local support identity; 16=7+9 and kappas properly left upstream. |
| 030 | 1048–1073 | `p10:thm:hurwitz-shell-dirac-compression` | `VERIFIED-CONDITIONAL` | E3 covariant Taylor: first moment cancels, second moment gives Dirac principal symbol, odd cubic moment cancels; cubic remainder coefficient ell_H^2/2 verified. |
| 031 | 1088–1108 | `p10:thm:hurwitz-shell-qcd-transfer-compiler` | `VERIFIED-CONDITIONAL` | Gauge covariance follows cancellation of endpoint transforms; self-adjoint finite H is explicit premise, not derived from face positivity. |
| 032 | 1118–1121 | `p10:cor:no-primitive-position-lattice-input` | `FORMALIZED` | Source constitution declares shell primary; position lattice and scale-setting are comparison conventions, not a mathematical nonexistence theorem. |
| 033 | 1131–1134 | `p10:def:finite-strong-generated-algebra` | `FORMALIZED` | Unital finite generated *-algebra and commutant defined. |
| 034 | 1136–1139 | `p10:lem:primitive-exact-block-shell-connectivity` | `VERIFIED-CONDITIONAL` | Connected-component projectors commute with generators preserving each component; requires actual complete set of component-preserving generators. |
| 035 | 1144–1147 | `p10:lem:shell-graph-matrix-units` | `REPRODUCED` | Path matrix units conditional on availability of individually reversible edge transports and endpoint isolation/projectors; input must be checked in actual compiled generator set. |
| 036 | 1152–1155 | `p10:lem:local-color-fock-matrix-units` | `VERIFIED` | E3 finite-dimensional Burnside criterion unital complex algebra has scalar commutant iff full End when *-closed. |
| 037 | 1160–1163 | `p10:lem:gauge-singlet-rank-one-closure` | `VERIFIED` | E3 restriction of Burnside to a fixed invariant singlet block; positivity/invariance not inferred. |
| 038 | 1168–1181 | `p10:thm:finite-strong-algebra-centralizer` | `VERIFIED` | E3 finite-dimensional C*-algebra Wedderburn and commutant decomposition. |
| 039 | 1186–1189 | `p10:cor:no-hidden-dynamical-bypass-projector` | `VERIFIED` | E3 nontrivial projections in finite commutant exactly give reducing subspaces. |
| 040 | 1194–1203 | `p10:thm:quadratic-strong-seed-normalization` | `VERIFIED` | E3 g=sqrt(4 pi alpha) tautology; independently variable transfer matrix elements show no amplitude determination. |
| 041 | 1208–1222 | `p10:thm:primitive-scalar-shell-coefficient-fixed` | `INCONSISTENT` | Rayleigh infimum lacks nonzero-shell condition and is not the actual projected transfer contraction when [P,H]!=0; BH-G-000136/137. |
| 042 | 1284–1311 | `p10:thm:v2211-finite-occupation-assembly` | `VERIFIED-CONDITIONAL` | E3 truncated bosonic commutator I-(N+1)\|N><N\|, finite orthogonal compression and complete three-term derivative; physical capacity is an inherited condition. |
| 043 | 1322–1341 | `p10:def:finite-colour-singlet-projector` | `INCONSISTENT` | Global color Haar projector is mathematically exact, but source labels its image full physical QCD; local Gauss is stricter; BH-G-000138. |
| 044 | 1343–1364 | `p10:thm:finite-colour-singlet-basis-transcript` | `VERIFIED-CONDITIONAL` | E3 Haar orthogonal projection, exterior/symmetric character determinants and necessary Z3 triality. Global singlet count correct; not local Gauss. |
| 045 | 1395–1434 | `p10:thm:finite-qcd-sparse-entry-factorization` | `VERIFIED-CONDITIONAL` | Polynomial normal-ordered finite monomials factor as shell/color/spin/Fock terms on explicitly limited polynomial branch. |
| 046 | 1459–1473 | `p10:def:finite-source-operator-dictionary` | `FORMALIZED` | Finite dictionary source list given, with physical/gauge interpretation conditional on projector and actual source packet. |
| 047 | 1497–1517 | `p10:thm:v264-twist-two-current-stress-owner` | `REPRODUCED` | n1 current identity is algebraic; n2 stress source owner under same-action metric variation, trace/improvement claims require exactly matched variation. |
| 048 | 1522–1525 | `p10:rem:v264-lfrep-stronger-than-twist-two-owner` | `FORMALIZED` | Finite light-front R3 realization is stronger than normalized current/stress insertions. |
| 049 | 1536–1540 | `p10:thm:no-independent-source-normalization` | `VERIFIED-CONDITIONAL` | Derivative of fixed normalized source coupling fixes operator; dynamical residues depend on H eigenvectors. |
| 050 | 1546–1581 | `p10:def:native-qcd-generating-functional` | `INCONSISTENT` | The declared operator -d log K and one-point connected derivative +dW have opposite sign (also missing t normalization); BH-G-000139. |
| 051 | 1583–1603 | `p10:def:complete-finite-qcd-source-transfer-datum` | `FORMALIZED` | Complete source-transfer tuple is a supplied input definition, not a physical completion claim. |
| 052 | 1605–1616 | `p10:thm:master-finite-nonperturbative-qcd-closure` | `REPRODUCED` | Deterministic finite closure only on supplied full source/action/state packet; no numerical physical claim from construction alone. |
| 053 | 1624–1637 | `p10:thm:source-interface-universality` | `REPRODUCED` | Three finite extraction routes are a conditional scoped enumeration; no scattering/resonance realization without separate limit. |
| 054 | 1647–1665 | `p10:cor:finite-qcd-parent-readouts` | `REPRODUCED` | Finite Born effect and current transition weights are valid for compatible given state/effect; not a real hadron occurrence theorem. |
| 055 | 1764–1786 | `p10:thm:complete-schur-scalar-source` | `VERIFIED` | E3 independent Hermitian Schur calculation for eigenvector, Z, Oeff and E derivative; random fixed-block control matches to machine precision. |
| 056 | 1809–1826 | `p10:cor:schur-positive-gap-weight` | `VERIFIED` | E3 spectral-order inequality (1/D)R <= R² <= (1/delta)R proves stated reciprocal pole-weight bounds. |
| 057 | 1841–1856 | `p10:cor:complete-dirac-schur-source` | `VERIFIED` | E3 independent complex Hermitian K test of det Schur and scalar trace derivative; ~1e-14 relative error. |
| U001 | 1684–1758 | `p10:subsec:spectral-readout-theorem` | `INCONSISTENT` | Exact Schur resolvent and residues valid. Static susceptibility omits nonlinear source contact term and nondegenerate positive ground-gap domain; BH-G-000140/141. |

## Source/constructor and dependency guards

**Fixed upstream:** m_p=1; compact S³ momentum carrier; actualized Hurwitz/trimer role with upstream constitution; finite color SU(3) algebra; Paper-IV occupation/capacity when bosons present. These are inherited checkpoints, not new unproved axioms introduced in Paper VII-A.

**Active conditional imports:** actual rooted charged hierarchy-arrow packet and V-A v397 preterminal source member; G16 scheme/RG execution transport; native common-heat matching datum; genuinely supplied local Gauss representation; stable physical state, source/transfer and any claimed pole/continuum limit. The outdated historical SVD alias is a distinct source-compatibility issue, not a reopened upstream occurrence gap.

**Physical versus algebraic:** Global SU(3) singlet Haar projection and its character dimension are verified algebraic; exact local vertexwise Gauss invariance is stronger. Schur residues of finite self-adjoint Hamiltonians are real/orthogonal; resonance widths require the stated external continuous-channel limit. Discrepant spectral-susceptibility/source conventions do not invalidate the correctly checked Schur equalities.

**Impact guard:** Only source-use-witnessed edges may be promoted into the final typed DAG. Candidate remote consumers in VII-B/C are not automatically audited or marked refuted. All issue IDs, negative controls, original source locators and no-new-theory scope are retained for final graph integration.

## Batch 1 handoff (completed)

Batch 2 proceeded from `p10:thm:source-interface-handoff` at line 1878 through the end of the geometry-first D22 source Hessian material at line 3937 (section boundary line 3944). The final batch will generate exactly the next Atlas ZIP (after v1_115) and next ProofChainAudits ZIP (after v1_32), containing only the latest applicable individual audit versions.

**Working evidence files** (to be integrated at final release): `Paper7A-AuditState-Batch1-v1_1.json`, `check_batch1.py`, and `batch1_independent_checks.json` under the current audit work directory.

---

## Batch 2 — null flow, Petersen, gauge/heat, four-dimensional overlap and source certificates

**Frozen source:** `Paper7A-QCDKernel-v1_165.tex:1878–3943`; SHA256 remains `11233c2be618f189ec69edef36bc7a78122d90f13d28cc2f7c39b5b94076788a`. Formal statements **P7A-058 through P7A-116**. Two substantive unnamed derivations D21/D22 indexed as **P7A-U002/U003**. The next source statement begins at line **3962**; line 3944 introduces the next section.

### Cumulative coverage and evidence-qualified dispositions

| Disposition | Batch 1 | Batch 2 | Cumulative |
|---|---:|---:|---:|
| `VERIFIED` | 12 | 16 | 28 |
| `VERIFIED-CONDITIONAL` | 12 | 13 | 25 |
| `REPRODUCED` | 11 | 13 | 24 |
| `FORMALIZED` | 16 | 17 | 33 |
| `INCONSISTENT` | 6 | 0 | 6 |
| **Formal statements** | **57** | **59** | **116 / 314** |

**Evidential rule:** `REPRODUCED` means source derivation rechecked but not enough independent certificate for the complete exact claim; `FORMALIZED` preserves a definition, interface or conditional boundary. `VERIFIED-CONDITIONAL` proves the displayed result on its printed conditions **without** claiming these physical antecedents hold. An issue may remain attached to a `FORMALIZED` record without rendering the entire mathematical object inconsistent.

### Independent Batch 2 certificates

1. **Finite mirror–spin operator and leakage.** Explicit eigenanalysis of a 24×24 candidate yields the exact five eigenvalue families and moments. An independent Hermitian block compression gives `|| iota†K²iota − Keff² − B†B ||=3.05×10⁻¹⁵` in double precision; `B†B` is positive semidefinite. Neither check identifies a physical meson block.
2. **SU(3) face heat inverse and quartic.** Independent Peter–Weyl character sums for all `(p,q)` up to 24 give `h(t_iso)=1/(2π²)`, `t_iso=5.75329584663306`, `h_prime=-0.02761434536217`, `k4=-0.0003095675460803`. Strict monotonicity follows from the Casimir variance; the representation tail is not a physical scale fit.
3. **Native heat positive bounds.** Independently evaluate `a=0.5632936301944446`, `b=1.4367063698055553`, and for `N=96`, `eps_96=6.349176217526962×10⁻⁷⁶`, strictly below the printed `6.35×10⁻⁷⁶`. These are finite face-presentations bounds; no full four-dimensional cell count or asymptotic area law follows.
4. **Three-face Haar interaction and independent D22 table.** Direct double-epsilon contraction reproduces the polarized determinant identity to `1.34×10⁻¹⁵`. A separate SU(3) Weyl-torus quadrature (96×96 torus grid, Schur/Jacobi–Trudi character recurrence) reproduces all five quoted `Z_3(t)` and `k(t)` values to the reported numerical precision. Gauge zero modes give 8-dimensional Hessian null space, relative-source rank 16, conditional on the exact source presentation.
5. **Overlap and source jets.** A fresh Hermitian-sign involution obeys the Ginsparg–Wilson polynomial with residual `2.84×10⁻¹⁵` and integer finite index on a balanced spin carrier. Separate positive-weight discrete source differentiation confirms the full conditional Hessian `A_ab=<S_ab>−Cov(S_a,S_b)`; noncommuting 2×2 source matrices confirm first/second Duhamel Ward response. This does not prove a nonzero physical index sector or matching with a continuum clutching class.
6. **Exact adversarial boundaries.** The positive `U(1)` weight `1−0.4 cos(2θ)` has negative second Fourier coefficient `−0.2`, demonstrating why central face positivity is not enough for positive transfer. The `SU(3)` center-flux `N`-face construction has Hilbert–Schmidt energy `8π²/(3N)`, showing that center holonomy alone gives no extensive area lower bound. These examples support the paper's own restricted claims, not new refutations.

### New distinct Batch 2 issue — one minor unresolved notation scope

#### BH-G-000142 — `TYPE_OR_DOMAIN` (minor)

**Earliest origin:** `p10:def:finite-null-representation-certificate`, `Paper7A-QCDKernel-v1_165.tex:2118-2122`. **Source-as-printed.** **Lifecycle:** `OPEN`, issue status `unresolved`.

**Problem:** Exact search of current P7A finds P_L^+ only at 2119, while its R2/R3 clauses name P_phys,L^+ at 2068–2075 and P_F,L^+ at 2103–2108. Current VII-B lines 2549–2562 and VII-D lines 2539–2542 explicitly introduce the shorthand only after consuming R3.

**Exact obligation:** Bind P_L^+ in Paper VII-A R4 to P_{\mathrm{phys},L}^+ or to the common P_{F,L}^+=P_{\mathrm{phys},L}^+ specifically after R3 is assumed; state whether R4 is meant independently of R3.

**Impact and bounded scope:** R4 uses a plus-momentum shorthand with no local definition in VII-A even though the same definition distinguishes P_F,L^+ from P_phys,L^+ until R3 holds. This is a scoped certificate notational ambiguity, not a counterexample to LFRep. This is not a proof that local Gauss compatibility or R3 is false; later documents supply a consistent conditional alias, so no cross-paper material edge is promoted. The full six-clause LFRep still remains unproved on the generic physical QCD carrier.

### Prior issues retained, without duplication

The eight source-level Batch 1 issues **BH-G-000134 through BH-G-000141** remain in the cumulative issue register; see their complete certificates above. In this batch the global-versus-local singlet physical interpretation (BH-G-000138) is consumed at the purported physical Floquet/singlet level, and the source-derivative/sign and contact-term issues (BH-G-000139–140) remain attached to the earlier generic source-readout formulas. The correctly derived complete same-action blocked Hessian at lines 3574–3615 is independently confirmed but does not retroactively change those earlier printed formulas. No inherited assumption, issue or proof is silently renamed or discharged.

### Batch 2 formal statement ledger

| # | Lines | Exact source label | Verdict | Evidence / boundary |
|---:|---:|---|---|---|
| U001 | 1684–1758 | `p10:subsec:spectral-readout-theorem` | `INCONSISTENT` | Exact Schur resolvent and residues valid. Static susceptibility omits nonlinear source contact term and nondegenerate positive ground-gap domain; BH-G-000140/141. |
| 058 | 1878–1902 | `p10:thm:source-interface-handoff` | `REPRODUCED` | Finite package yields deterministic readouts given the actual action, physical projector, source and state. Carries earlier global-versus-local Gauss issue BH-G-000138 and source-derivative issues BH-G-000139/140. |
| 059 | 1916–1971 | `p10:thm:v252-derived-null-generator-identity` | `VERIFIED-CONDITIONAL` | E3 commuting finite self-adjoint generators and equivariant equal-time seed imply the stated time/Hopf covariance on retained test functions; the chosen unitary generator is explicit, not a new physical field-intertwiner. |
| 060 | 1997–2013 | `p10:cor:v252-null-generator-conservation` | `VERIFIED-CONDITIONAL` | E3 differentiation of the constructed unitary and joint spectral positive-polar bound; no species conservation inferred. |
| 061 | 2023–2153 | `p10:def:finite-null-representation-certificate` | `FORMALIZED` | Six-clause LFRep certificate; R3 physical/Fock identity and R4–R6 remain explicit. The R4 short name P_L^+ is not locally bound; BH-G-000142 records a minor traceability ambiguity. |
| 062 | 2155–2173 | `p10:thm:v133-internal-total-null-conservation` | `REPRODUCED` | Source-matched reuse of the earlier constructed null unitary, with same-carrier R1/R2 guards and R3–R6 retained. |
| 063 | 2184–2202 | `p10:thm:finite-null-representation-status` | `FORMALIZED` | Status theorem expressly leaves native seed, Fock, Gauss, color path, sampling/refinement certificates open; no standalone finite LFRep assertion. |
| 064 | 2218–2221 | `p10:cor:v264-lfrep-optional-finite-readout-scope` | `REPRODUCED` | Owner split isolates source current/stress normalization from optional exact finite Fock simplex; imported V-A source/III-E clock conditions are not newly proved. |
| 065 | 2226–2231 | `p10:prop:executable-native-qcd-protocol` | `FORMALIZED` | Six-row execution record is a reproducibility and no-backflow rule, not a new physical prediction. |
| 066 | 2272–2284 | `p10:def:v323-petersen-strong-contrast` | `FORMALIZED` | Five orthogonal 3D cores and rank-three mirror projectors typed as abstract 15D Petersen role, not QCD quarks/links. |
| 067 | 2286–2299 | `p10:thm:v323-first-coherent-mirror-source` | `REPRODUCED` | Direct 2-core block characteristic polynomial agrees with VII-D p13:prop:v323-petersen-charpolys; its independent full ten-axis coordinate E3 was not rerun; conditional contrast bound follows. |
| 068 | 2311–2319 | `p10:cor:v323-incoherent-evolution` | `VERIFIED-CONDITIONAL` | E3 block-diagonal commutation preserves incoherence under U(t); no assertion that actual strong H commutes with all P_m. |
| 069 | 2326–2344 | `p10:def:v323-action-incidence-test` | `FORMALIZED` | Physical incidence map, isometry, leakage/reducing condition and source insertions are explicit tests, not QCD compiler outputs. |
| 070 | 2346–2358 | `p10:prop:v323-center-firewall` | `VERIFIED` | E3 gcd(2,3)=1 gives trivial Z2-to-Z3 homomorphism. Equal incidence valency supplies no SU3 gauge map. |
| 071 | 2374–2392 | `p10:thm:v327-compression-leakage-pythagoras` | `VERIFIED` | E3 independent random Hermitian K and isometric compression: iota†K²iota=Keff²+B†B to 3.1e-15; self-adjoint invariant implies reducing. |
| 072 | 2403–2424 | `p10:def:v327-conditional-pair-spin-block` | `FORMALIZED` | Optional Wmn⊗C4 candidate has unsupplied physical embedding, flavor owner and coefficients; does not identify its dimension with Hurwitz 24 vertices. |
| 073 | 2426–2455 | `p10:thm:v327-conditional-mirror-spin-spectrum` | `VERIFIED-CONDITIONAL` | E3 direct diagonalization of 24×24 abstract operator matches 8+2+2+6+6 eigenmultiplicities, trace and second moment; physical spectrum explicitly not derived. |
| 074 | 2468–2480 | `p10:prop:v327-spinblind-no-go` | `VERIFIED-CONDITIONAL` | E3 U and Q spin-blind; Q=Dmn² is block diagonal, so core-block-incoherent states persist under only-Q evolution. |
| 075 | 2533–2559 | `p10:def:admissible-color-connection` | `FORMALIZED` | Finite color connection and Hermitian physics-generator convention stated. Heat sections later use anti-Hermitian Lie coordinate X; conversion is a convention guard. |
| 076 | 2561–2572 | `p10:thm:color-connection-kinetic-uniqueness` | `REPRODUCED` | Invariant bilinear form uniqueness for simple su3, with upstream traceless-color constructor; 3D triplet dimension alone does not force SU3. |
| 077 | 2577–2602 | `p10:cor:v174-local-color-phase-space-hamiltonian` | `REPRODUCED` | Imported Paper3F v174 regular local Yang–Mills symplectic/Gauss phase-space theorem applies only on stationary product parity-even pure gauge branch; not a finite Haar regulator. |
| 078 | 2606–2638 | `p10:thm:v245-free-gluon-octet-clock-lock` | `VERIFIED-CONDITIONAL` | E3 linear YM curvature gives eight uncoupled color copies; coexact round S3 spectrum n≥2 and primitive clock imported from Paper3A; free periodicity only. |
| 079 | 2657–2673 | `p10:prop:strong-coupling-normalization` | `REPRODUCED` | Native alpha_s=pi/2 and g_s=sqrt(2)pi import common-heat V-C source; comparison alpha_s(mu) needs owned RG transport. |
| 080 | 2681–2694 | `p10:def:strong-cp-term-separation` | `FORMALIZED` | Theta zero is declared native CP member, not a consequence of CP-even kinetic uniqueness; later V-C determinant orientation is separate import. |
| 081 | 2701–2722 | `p10:def:finite-strong-hamiltonian` | `FORMALIZED` | Parametric finite strong H and exp[-t(H-E0)] defined; actual coupling at execution scale, mass and action representative remain supplied. |
| 082 | 2725–2771 | `p10:thm:v247-singlet-floquet-qcd` | `VERIFIED-CONDITIONAL` | E3 U_free(T)=I implies V_I periodic and exact Dyson one-turn unitary; global Haar reduction is unitary if both blocks gauge invariant. Local Gauss physical scope inherits BH-G-000138. |
| 083 | 2785–2792 | `p10:thm:finite-strong-hamiltonian-closed` | `REPRODUCED` | Parametric pure-glue/full-QCD family exists on supplied admissible action and source choices; representative-independent continuum is not claimed. |
| 084 | 2801–2808 | `p10:cor:whole-family-quark-mass-transport` | `REPRODUCED` | Paper II-A whole-family evaluation on typed mass coefficient port; no G0 physical member or G16 evaluation produced by this construction. |
| 085 | 2814–2823 | `p10:cor:v163-g34-disposition` | `FORMALIZED` | G34 historical scope retyped as quark-mass family already generated and physical member/RG needed for numerical selection. |
| 086 | 2830–2845 | `p10:thm:canonical-haar-heat-representative` | `VERIFIED-CONDITIONAL` | E3 Haar uniqueness on SU3^E and bi-invariant symmetric strongly local diffusion Casimir generator on each simple SU3 group; nonlocal jumps excluded explicitly. |
| 087 | 2847–2860 | `p10:rem:three-distinct-heat-parameters` | `FORMALIZED` | Spectral heat, group face heat and Euclidean transfer times are distinct types; no numeric equality inferred. |
| 088 | 2862–2873 | `p10:rem:v2159-electric-heat-scope` | `FORMALIZED` | Holonomy–flux cotangent quantization implies electric Laplacian conditionally; no magnetic nonlinear face law selected. |
| 089 | 2876–2921 | `p10:thm:v185-heat-hessian-inversion` | `VERIFIED` | E3 independent SU3 character-sum evaluation h(t), hprime<0 and endpoint limits; strict variance yields inverse on positive axis. |
| 090 | 2943–2977 | `p10:cor:v185-common-heat-face-stiffness` | `VERIFIED-CONDITIONAL` | E3 kappa=w/(g3²A²) exact under stated curvature/quadrature convention; independent SU3 root t_iso=5.75329584663306 and quartic checks. |
| 091 | 2996–3005 | `p10:prop:multiface-heat-blocking` | `VERIFIED` | E3 nonzero SU3 triple epsilon contraction and absence of one-variable modes under Haar elimination refute one-face product closure generically. |
| 092 | 3020–3026 | `p10:cor:multiface-effective-action-target` | `REPRODUCED` | Degree-two heat semigroup exact but three-face blocking generates joint terms; refinement targets multiface effective action. |
| 093 | 3033–3052 | `p10:prop:v2158-heat-subdivision-area-nogo` | `VERIFIED` | E3 product exp(-2sum t_i/3)=exp(-2t/3); subdivision count cannot manufacture uniform physical area exponent. |
| 094 | 3060–3066 | `p10:prop:finite-action-universality-status` | `VERIFIED` | E3 curvature-fourth-order action deformation preserves Hessian and changes finite density; fixed-UV QFT4_E import remains conditional on its actual action/phase. |
| 095 | 3068–3090 | `p10:cor:v2159-same-hessian-nonheat-family` | `VERIFIED` | E3 q(e^X)=O(\|\|X\|\|²) so s_H+lambda q² retains first/second identity jets but changes positive density for lambda>0. |
| 096 | 3103–3111 | `p10:prop:v2211-central-transfer-positive-type` | `VERIFIED` | E3 Peter–Weyl convolution eigenvalue a_R/d_R criterion; strictly positive U1 counterweight 1-0.4cos2theta has negative Fourier coefficient -0.2. |
| 097 | 3128–3135 | `p10:cor:v186-g33-finite-continuum-split` | `REPRODUCED` | Retirement of independent G33 follows current VII-C v2.83 fixed-UV QFT4_E; G33-COMP remains representative-equivalence claim-scoped. |
| 098 | 3137–3153 | `p10:prop:v152-unstable-fixed-rank-topology-firewall` | `REPRODUCED` | Imported Paper1B unstable rank-two M8 sector not independently reproved; correct stable-trivialization warning for fixed-rank bundles. |
| 099 | 3164–3178 | `p10:rem:m8-batch-qcd-inputs` | `FORMALIZED` | Paired finite algebra does not construct QCD action or LFRep; earlier historical G33 shorthand must be interpreted under newer G33-COMP scope. |
| 100 | 3183–3193 | `p10:rem:typed-mode-refinement` | `FORMALIZED` | Comparison harmonic/occupation refinement is not a new momentum carrier or automatic physical mode occupation. |
| 101 | 3210–3219 | `p10:thm:v199-quartic-heat-vertex` | `VERIFIED` | E3 independent SU3 rep sums agree quartic coefficient k4=-0.000309567546080; original Paper1C character contraction supplies proof. |
| 102 | 3240–3264 | `p10:thm:v199-haar-interaction-compiler` | `VERIFIED-CONDITIONAL` | E3 invariant Haar projector on each interior edge plus SU3 epsilon 3-face polynomial; finite positive heat time ensures summable character expansion; no continuum limit. |
| 103 | 3307–3332 | `p10:thm:v202-native-heat-bounds` | `VERIFIED` | E3 exact rational comparisons and independent SU3 sum yield a=0.5632936302,b=1.4367063698 and eps96=6.349176e-76<6.35e-76; analytic face tails imported from Paper1C. |
| 104 | 3376–3397 | `p10:prop:center-fractionalization-no-area` | `VERIFIED` | E3 N commuting SU3 faces: center holonomy omega I while sum integrated HS curvature squares=8pi²/(3N). No area-extensive floor from center alone. |
| 105 | 3399–3406 | `p10:prop:finite-exact-chiral-index-zero` | `VERIFIED` | E3 balanced finite odd chiral block has equal rank on domain/codomain; index zero by rank-nullity. |
| 106 | 3421–3474 | `p10:thm:v190-generated-4d-gw-regulator` | `VERIFIED-CONDITIONAL` | E3 independent finite random Hermitian sign involution satisfies exact GW identity and integer trace index. Native 4D Hurwitz/transfer incidence imports Paper1C proof; gap condition mandatory. |
| 107 | 3489–3511 | `p10:def:v190-native-clutching-target` | `FORMALIZED` | Native clutching target pi3(SU3)=Z and candidate diag(q,1); full overlap/clutching matching explicitly not asserted. |
| 108 | 3513–3523 | `p10:cor:v190-g20-finite-regulator-generated` | `REPRODUCED` | Follows gapped GW identity and bounded finite functional calculus; nonzero physical topological sector probabilities are not derived here. |
| 109 | 3526–3536 | `p10:rem:v190-scalar-spin-g20-firewall` | `FORMALIZED` | Scalar temporal spin sign is not an additional gauge-curvature dimension; index independence restricted to same closed index family. |
| 110 | 3538–3554 | `p10:def:v186-g20-layer-split` | `FORMALIZED` | Active G20 layer split names native index/finite neighborhoods and unresolved continuum clutching comparison; imported later positive-sector theorem not reaudited in this batch. |
| 111 | 3574–3603 | `p10:thm:v2210-lit-blocked-source-jets` | `VERIFIED` | E3 discrete positive-weight source check confirms A_a=<S_a>, A_ab=<S_ab>-Cov(S_a,S_b) and nonlinear chart Hessian; mean-source contacts retained. |
| 112 | 3625–3641 | `p10:prop:v2210-lit-multiface-polymer-domain` | `VERIFIED-CONDITIONAL` | Kotecky–Preiss criterion applied on assumed exact polymer activities with uniform holomorphic bound; actual source polymer representation/bounds not supplied by theorem. |
| 113 | 3659–3692 | `p10:thm:v2210-lit-ward-defect` | `VERIFIED` | E3 noncommuting 2×2 finite Hermitian source check Duhamel first and second Ward derivatives; Kubo–Mori covariance operator norm bounds. |
| 114 | 3711–3729 | `p10:cor:v2210-lit-axial-functional-test` | `VERIFIED-CONDITIONAL` | E3 chain rule of same functional yields derivative kernel identity K=-D_S Sigma and mismatch norm; axial physical pole not inferred. |
| 115 | 3747–3767 | `p10:prop:v2210-lit-observable-step-scaling` | `VERIFIED` | E3 composition u(s mu(u)) and scheme chain rule on same local injective scale branch; no RG function generated. |
| 116 | 3786–3807 | `p10:thm:v2210-lit-sector-cumulants` | `VERIFIED` | E3 finite cumulant differentiation; symmetric ±1 yields kappa4=-2, sparse symmetric ±1 yields epsilon-3epsilon²>0 for 0<epsilon<1/3. |
| U002 | 3851–3887 | `p10:sec:v2201-derived-d21` | `VERIFIED-CONDITIONAL` | E3 independent epsilon tensor polynomial and independent character-selection orders; source correctly restricts to valence-three SU3 heat block. |
| U003 | 3891–3937 | `p10:sec:v2201-derived-d22` | `VERIFIED-CONDITIONAL` | E3 independently evaluate Weyl-torus quadrature with Schur-character recurrence on grid 96×96: reproduces all five reported Z3,k table pairs and rank16 relative-source Hessian. |

### Proof ancestry, conditions and forward-impact guard

**LFRep:** the elapsed null-flow generator is a sound *same-carrier* construction **when** the R1 Hopf-equivariant seed and R2 strongly commuting pair exist. Its finite species/Fock equality (R3), local Gauss and zero-mode compatibility (R4), color-path intertwiner (R5) and native-momentum carrier comparison (R6) remain separate; the fact that an R1/R2 unitary exists does not supply those bridges.

**Petersen:** the geometric mirror spectrum lives in the 15-dimensional oriented-edge role of an occurring 2I. Mapping it into the actual gauge-singlet QCD source sector requires an explicit 15D map, reducing/leakage certificate, source projectors and residues. The 24-dimensional spin-tensor block is optional and must not be equated to the 24 Hurwitz vertices or a meson prediction.

**Heat/QCD:** the common-heat coupling boundary is inherited; the face heat time becomes unique only after *the exact face presentation, positive face stiffness, Casimir metric and strongly local heat representative* are fixed. The finite action family is not unique from its Hessian. Higher multiface interactions and claim-scoped universality/refinement/transfer regularity are not inferred from Haar integrability alone.

**Index and Ward:** the generated gapped overlap algebra is a finite regulator identity and does not itself establish the native charge probabilities, physical topological susceptibility or overlap/clutching comparison. Correct blocked and Hamiltonian source Hessians include covariance/contact terms and nonlinear chart jets. Paper VII-C imports are current scope checks only, not an audit of Paper VII-C.

**Import source matches:** Paper I-C `p1b:prop:heat-block` and `p1b:thm:overlap`, Paper III-F `p3f:thm:v174-generated-joint-gauge-phase-space-action`, Paper VII-D `p13:prop:v323-petersen-charpolys`, Paper V-C `p7v2:cor:v259-native-strong-cp` and Paper VII-C QFT4_E conditional branch are found in the supplied current corpus. Paper 1C houses the canonical technical theorem labels historically prefixed `p1b:`; label resolution does not license a broader new result.

### Next batch and artifact policy

**Next source boundary:** `Paper7A-QCDKernel-v1_165.tex:3944`, beginning the strong-clock, mass-gap, confinement and area-law section; the first formal statement starts at **line 3962**. **Remaining coverage:** **198 of 314** formal statements, including technical appendices. Continue under the same source hash and preserve issue IDs BH-G-000134–000142.

**Archive release deferred to final batch as requested.** At final completion, produce `Paper00-DAGAtlas-v1_116.zip` and `Paper00-ProofChainAudits-v1_33.zip` only after integrating the whole Paper VII-A audit, validating the combined global graph and filtering obsolete per-paper and batch versions; keep source/paper archive unchanged. No interim ZIP is represented as complete.

**Machine-readable cumulative audit state:** `audit7a_work/Paper7A-AuditState-Batch2-v1_2.json`; exact check scripts `check_batch2.py`, `check_d22.py`, output certificates `batch2_independent_checks.json`, `batch2_d22_weyl_check.json`, plus retained Batch 1 state/evidence. These evidence artifacts must be integrated into the final DAG audit layer, not used to promote legacy graph statuses en masse.

---

## Batch 3 — strong clock, free color thresholds, face Hodge, gap/flux, and conditional Wilson area law

**Frozen source:** `Paper7A-QCDKernel-v1_165.tex:3944–4946`; 64 formal source statements **P7A-117 to P7A-180**. The first formal entry starts at line 3962 and the final covered theorem ends at 4943; the next formal theorem begins at line **4960** in the chiral sector. SHA256 source freeze remains `11233c2be618f189ec69edef36bc7a78122d90f13d28cc2f7c39b5b94076788a`. The review was performed against the full v2.371 current TeX and exact imported statements from Paper VII-C. Earlier batch handoff paragraphs above are historical and superseded by this batch boundary.

### Cumulative audit status

| Status | Batch 1 | Batch 2 | Batch 3 | Cumulative |
|---|---:|---:|---:|---:|
| `VERIFIED` | 12 | 16 | 17 | 45 |
| `VERIFIED-CONDITIONAL` | 12 | 13 | 22 | 47 |
| `REPRODUCED` | 11 | 13 | 12 | 36 |
| `FORMALIZED` | 16 | 17 | 7 | 40 |
| `INCONSISTENT` | 6 | 0 | 0 | 6 |
| `UNRESOLVED` | 0 | 0 | 6 | 6 |
| **Formal total** | **57** | **59** | **64** | **180 / 314** |

**Interpretation:** A status of `VERIFIED` requires claim-matched E1 and an independent E3 at the printed scope; `VERIFIED-CONDITIONAL` does **not** discharge the physical antecedent. The six `UNRESOLVED` Batch 3 statements inherit two distinct question-level issues. The earlier six `INCONSISTENT` statements have not been reclassified or silently repaired. There are now **11 distinct issue objects** (nine retained plus two new), not six independent new errors.

### Independent mathematical checks and negative controls

1. **Exact face Hodge reconstruction (E3).** Independently enumerate 24 vertices from permutations of `(±1,±1,0,0)`, 96 edges, 96 triangles, and 24 octahedral facets. Form oriented `∂₂:ℝ⁹⁶→ℝ⁹⁶` and `∂₃:ℝ²⁴→ℝ⁹⁶`; `∂₂∂₃=0` holds entrywise. An independent exact SymPy characteristic-polynomial factorization of the integer matrix `Δ₂=∂₂ᵀ∂₂+∂₃∂₃ᵀ`, corroborated by diagonalization, gives `1⁽⁶⁾, 2⁽¹⁶⁾, ((9−√17)/2)⁽⁹⁾, 4⁽¹⁶⁾, 5⁽¹⁶⁾, ((9+√17)/2)⁽⁹⁾, 8⁽¹³⁾, 9⁽¹⁾, 10⁽⁸⁾, 12⁽²⁾`; trace **480**, smallest eigenvalue **1**. Ranks `rank ∂₂=73`, `rank ∂₃=23` support `H¹=H²=0`. This certifies the geometric Hodge result **without** supplying an action of that projector on the physical Fock/gauge Hilbert space.

2. **Mixed and sharp strong-clock diagnostics (E3).** Direct evaluation of the printed coordinate ledger gives `Q₀ᵈⁱᵃᵍ=0.3158981634270445 GeV`, `Q₁ᵈⁱᵃᵍ=0.5510277102128739 GeV`, `τ(√2 E₃₆)=−0.03006265800311203`, `τ(√6 E₃₆)=0.9557796849125015`, sharp `τ_c=3.137749428724092`, and sharp comparison `μ_QCD=0.2843536969782847 GeV`. Lower derivative bound `23/(6π)=1.2201878970>0` verifies uniqueness for both levels on the printed interval; these are **not** native QCD measurements.

3. **SU(3) heat trace and branch recursion (E3).** At the already source-defined face heat time `t_H=5.75329584663306`, independent Casimir character sums give charged norm `u=0.02158988060835081`, nontrivial neutral norm `v=0.00017867469176957`, charged-sector trace tails `q₊=q₋=0.196823465343065`, and neutral nontrivial tail `q₀*=0.011441639034184`. A conservative analytic bound on all omitted `p+q≥24` terms is `<1.6×10⁻²⁰²`. At `z=1.1`, the square-face charged polynomial evaluates to `Φ₅=0.4318926829152<0.45`; the natural neutral-only scalar test evaluates to `0.0009890098942<0.002` (the neutral recursion itself is **not explicitly displayed** in that theorem and therefore its full meaning is not independently certified). These finite tests do not prove a complete connected-polymer inequality.

4. **Native Hurwitz triangle/ribbon four-inequality certificate (E3).** On the *explicit equal-heat comparison branch*, independent evaluation gives `(𝒩_s,𝒩_t,ℬ_s,ℬ_t)=(0.0007891572042, 0.0013821231739, 0.1960993512565, 0.4052908673230)`, strictly below `(0.001,0.002,0.20,0.41)`. This verifies the finite local supersolution, not equality of physical spatial/temporal heat times nor APBI.

5. **Flux and inequality adversarial controls (E4).** For center holonomy `ωI` distributed over `N` commuting SU(3) faces, direct traceless diagonal construction yields `∑_f‖F_f‖²_HS=8π²/(3N)`; hence center support alone does not enforce area extensivity. A separate 2×2 positive `H=diag(0,1)` and a rank-one nonreducing projection `P` has Rayleigh infimum `κ=1/2` on its range, but `λ_min(H−κP)=−0.30901699`: a **global** form bound would be false. The audited source explicitly qualifies the shell bound as *restricted to that shell*, so this challenge is **rejected as a refutation**; the genuine unresolved question is the typed face-to-state map.

6. **Import/domain guards (E1).** Paper VII-C v2.195 source lines 3846–3971 distinguishes finite Gibbs state, QFT4 state/convergence, OS static-sector reflection, ordered Wilson limits and APBI as an independently conditional extensive nonlinear same-owner presentation. Paper VII-A source lines 2996–3058 already proves that blocking generates multiface terms and heat-semigroup subdivision cannot manufacture a new extensive area exponent. Positive asymptotic fundamental tension is rightly restricted to pure-glue or otherwise certified unscreened static-source sectors. No QFT4, APBI, mass-operator transport, or local Gauss bridge is silently discharged.

### New issue certificates (no theory repair performed)

#### BH-G-000143 — `TYPE_OR_DOMAIN` (moderate, **unresolved**)

**Earliest origin:** `p10:thm:primitive-scalar-shell-coefficient-fixed` at `Paper7A-QCDKernel-v1_165.tex:1208-1215 (first occurrence), 4375-4377, 4407-4417 (confirmation)`; current source layer `SOURCE-AS-PRINTED`, lifecycle `OPEN`.

**Finding.** Delta_2,H acts on cellular face two-cochains, whereas H_L is the full finite quantum/gauge/Fock Hilbert space. The expression P_sh,L H_L and its gap Rayleigh test are not well-typed solely from the geometric projector definition. This does not refute the 96×96 Hodge spectrum, spectral projection, or a conditional restricted Rayleigh inequality.

**Exact verification obligation.** Identify a licensed operator representation/lift of the 96-dimensional face-Hodge projector 1_I(Delta_2,H) on the compiled physical Hilbert space H_L for each L, with compatible domains and a nonzero shell range; then state its interaction with H_L (invariant or explicitly restricted Rayleigh).

**Evidence and attack.** Exact source search finds P_sh,L defined by face Delta_2,H at 4377 and 4393 and applied to H_L at 1214 and 4411, while H_L is the full generated algebra carrier at 1133 and may include Fock operators. No face-to-H_L lift or second quantization is specified in the inspected current Paper7A source. E3 24-cell Hodge spectrum reconstructed separately; E4 2×2 example demonstrates that even with a typed P the inequality H−E0≥kP is valid only on P-range absent reducing hypothesis, a qualification the current statement explicitly retains.

**Downstream bounded impact.** p10:thm:primitive-scalar-shell-coefficient-fixed → p10:lem:scalar-shell-transfer-domination → p10:thm:uniform-scalar-shell-transfer-gap. Remote effects remain possible only where source proof use has been checked; no separate remote paper has been audited.

**Resolution requirement.** Provide source evidence for the typed Hodge-to-state projection/intertwiner and retained physical shell carrier, or explicitly treat the Rayleigh as a conditional target until that map is available; do not infer it from equal notation.

#### BH-G-000144 — `LOGICAL_GAP` (major, **unresolved**)

**Earliest origin:** `p10:thm:v2155-triality-branch-core-majorant` at `Paper7A-QCDKernel-v1_165.tex:4662-4695, especially 4685-4695`; current source layer `SOURCE-AS-PRINTED`, lifecycle `OPEN`.

**Finding.** The scalar heat bounds u,v, q±, q0* and local supersolutions are independently correct. But the short proof does not supply a checkable full graph-to-rooted-tree majorization and normalized measure/linked-cluster estimate for the stated all-genus, all-representation Wilson claim. Therefore the positive area exponent and the APBI/APBC consequences cannot be certified solely by the local numeric checks.

**Exact verification obligation.** Prove that the explicit neutral/charged monotone recursion and heat trace-tail/corridor bounds control every connected SU(3) Peter–Weyl surface contribution, including cycles, handles, neutral vacuum decorations, tensor-contraction multiplicities and normalization of the full finite Wilson expectation, with a perimeter-only constant uniform in surface area and APBI levels.

**Evidence and attack.** E3 direct SU3 Peter–Weyl sums: u=0.02158988060835, v=0.00017867469177, q±=0.19682346534 (<0.197), q0*=0.01144163903 (<0.012), Phi5=0.43189268292 (<0.45); two-type 4 inequalities exact. The manuscript states but does not derive an injective/equivalence-class cycle-cut assignment or vacuum denominator bound. E4 checked distinction of local recursion convergence versus full normalized all-genus Wilson expectation; no in-domain counterexample produced.

**Downstream bounded impact.** p10:thm:v2155-triality-branch-core-majorant → p10:cor:v2155-apbc-string-tension-reduction; p10:thm:v2155-triality-branch-core-majorant → p10:thm:v2158-finite-type-triality-branch-core → p10:cor:v2158-apbi-string-tension-reduction. Remote effects remain possible only where source proof use has been checked; no separate remote paper has been audited.

**Resolution requirement.** Source-match a full finite normalized Wilson polymer expansion and a uniform tree/cycle-cut counting bound with precise local type map and face-time decay. Provide independently reproducible finite test controls or theorem citations proving the all-connected-graph step; no new framework claim is to be introduced by the auditor.

### Previously identified issues retained and inheritance

The prior issues remain **BH-G-000134** retired SVD assembly import; **000135** real/complex Lie algebra root-space typing; **000136** nonzero shell range; **000137** shell diagnostic versus actual one-step contraction; **000138** global singlet vs local Gauss; **000139** generating functional source sign/normalization; **000140** nonlinear source-Hessian contact terms; **000141** ground spectral gap/regularity; and **000142** `P_L⁺` LFRep shorthand. Their complete first-origin certificates remain in the preceding cumulative sections and original JSON state. In this batch BH-G-000138 is inherited by the stated global color-singlet and free-state readouts; it does not invalidate the Haar projector itself. BH-G-000143 originates at the already-audited Batch 1 shell formula, but is **newly discovered** from the explicit Hodge domain in this batch; its earliest origin is retroactively recorded without creating a duplicate condition.

### Batch 3 formal statement ledger

| # | Lines | Exact source label | Verdict | E1/E3/E4 and scope |
|---:|---:|---|---|---|
| 117 | 3962–3970 | `p10:def:strong-inverse-clock` | `FORMALIZED` | Perturbative inverse clock is a declared fixed-flavor comparison observable, not the native physical strong energy. |
| 118 | 3972–3980 | `p10:thm:born-hopf-asymptotic-freedom` | `VERIFIED-CONDITIONAL` | E3 direct SU(3) CA=3 and TF=1/2 one-loop coefficient check; running requires fixed nf/perturbative physical matching. |
| 119 | 3985–3988 | `p10:lem:strong-running-import-chain` | `REPRODUCED` | Exact imported color/heat boundary versus threshold physical mass owner; does not discharge mass/RG scale map. |
| 120 | 3993–3996 | `p10:lem:e36-alternating-adjoint-block` | `VERIFIED-CONDITIONAL` | Finite binary-octahedral quotient and SU3 C⊗C*=1⊕8 decomposition; E36 clock zero explicitly excluded. |
| 121 | 4001–4011 | `p10:cor:v188-alternating-defect-provenance` | `REPRODUCED` | 2O/[2O,2O]=C2 and sign character replayed; defect provenance inherited from upstream M8, not re-proved here. |
| 122 | 4013–4016 | `p10:lem:color-singlet-running-no-double-counting` | `VERIFIED` | Orthogonal singlet/adjoint projectors on C⊗C* multiply to zero; independent scalar/projector check. |
| 123 | 4021–4024 | `p10:lem:native-shell-vs-ward-current-determinant` | `REPRODUCED` | Separate source deformation and Ward-current observable maps; no asserted equality of the two determinants. |
| 124 | 4029–4056 | `p10:def:legacy-mixed-clock-diagnostic` | `FORMALIZED` | Legacy coordinate ledger isolated; explicit mass numbers do not become physical Mq eigenvalues. |
| 125 | 4058–4068 | `p10:thm:native-strong-shell-transport-e36-wall` | `VERIFIED-CONDITIONAL` | E3 independent logarithmic derivative and Brent roots at 0.3158981634270 and 0.5510277102129; conditional coordinates. |
| 126 | 4080–4094 | `p10:thm:derived-perturbative-strong-handoff` | `VERIFIED-CONDITIONAL` | E3 separate sharp nf=5,4,3 threshold integration yields 0.2843536969782847 GeV on printed comparison branch. |
| 127 | 4099–4102 | `p10:thm:heavy-quark-threshold-decoupling` | `REPRODUCED` | Usual perturbative matching usable only once actual mass operator, decoupling domain and renormalization scheme supplied; no independent heavy threshold realization. |
| 128 | 4107–4110 | `p10:thm:handoff-scale-scheme-separation` | `REPRODUCED` | Readout/scaling types kept distinct and old E36 identification withdrawn; no equality asserted. |
| 129 | 4115–4118 | `p10:prop:dimensional-transmutation-readout` | `VERIFIED-CONDITIONAL` | RG ODE separation determines scheme-dependent integration constant for specified beta, thresholds and seed. |
| 130 | 4123–4126 | `p10:thm:native-nonperturbative-scale-ratio` | `VERIFIED` | Independent dimensional rescaling argument shows 24/15 and finite counts cannot set absolute energy amplitude. |
| 131 | 4131–4134 | `p10:cor:exact-minimal-scalar-shell-moments` | `VERIFIED` | Finite Hodge eigenvalues/moments independent of any dimensional Hamiltonian multiplier; E3 reconstructed spectrum below. |
| 132 | 4139–4142 | `p10:thm:positive-native-nonperturbative-scale-floor` | `VERIFIED-CONDITIONAL` | Finite Rayleigh positivity iff positive restricted excitation infimum, on nonempty correctly typed invariant subspace. |
| 133 | 4147–4150 | `p10:cor:single-shell-origin-scale-gap-confinement` | `REPRODUCED` | Scale, spectral gap and flux-area readouts are separate maps; no equality or common coefficient inferred. |
| 134 | 4160–4163 | `p10:thm:desert-shell-infrared-cascade-block` | `VERIFIED` | Explicit K_epsilon eigenvalues 1,1−epsilon on unchanged carrier; no implied positive uniform excitation gap. |
| 135 | 4166–4173 | `p10:thm:exact-finite-singlet-projector` | `VERIFIED` | E3 independent compact Haar projection proof; only global SU3 invariants, not full local Gauss physical space (BH-G-000138)., issues 138 |
| 136 | 4176–4179 | `p10:cor:nonzero-triality-no-asymptotic-ray` | `VERIFIED-CONDITIONAL` | Center-character average annihilates r≠0 on global singlet readout; local Gauss interpretation inherits BH-G-000138., issues 138 |
| 137 | 4184–4190 | `p10:thm:kinematic-color-confinement` | `VERIFIED` | Haar projection onto invariants, including zero-triality adjoint with no trivial summand; purely kinematic scope. |
| 138 | 4201–4212 | `p10:cor:v245-isolated-gluon-no-singlet-ray` | `VERIFIED-CONDITIONAL` | One adjoint gluon has no global SU3-invariant ray; conditional identification with actual local physical state requires Gauss check., issues 138 |
| 139 | 4214–4231 | `p10:cor:v245-free-two-gluon-singlet-threshold` | `VERIFIED-CONDITIONAL` | 8⊗8 includes singlet, Bose-symmetric delta_ab and two free n=2 modes give 4Eper on specified free quadratic branch; not glueball mass. |
| 140 | 4233–4236 | `p10:thm:center-triality-superselection` | `VERIFIED` | Center characters multiply in tensor products; zero triality necessary (not sufficient) for singlet. |
| 141 | 4241–4244 | `p10:cor:integer-baryon-number` | `VERIFIED` | Mod-3 quark-minus-antiquark center character implies integer B for color-singlet quark composites. |
| 142 | 4249–4252 | `p10:thm:integer-hadronic-electric-charge` | `VERIFIED-CONDITIONAL` | Quark charges all congruent −1/3 modulo Z, antiquarks +1/3; integer triality implies integer total charge on standard assignments. |
| 143 | 4257–4260 | `p10:thm:vector-flavor-charge-conservation` | `VERIFIED-CONDITIONAL` | Vector phase symmetry gives [H,Qf]=0 if same-action H is vectorlike/diagonal in preserved flavors. |
| 144 | 4265–4268 | `p10:thm:pure-glue-center-obstruction-screening` | `VERIFIED` | Adjoint has trivial Z3 character, hence cannot screen a lone nonzero-triality source with gluons only. |
| 145 | 4276–4294 | `p10:def:v2187-wilson-sector-scope` | `FORMALIZED` | Physical Wilson/area sector explicit: unscreened pure-glue for positive fundamental tension, excludes universal full-QCD tension. |
| 146 | 4299–4302 | `p10:thm:polyakov-center-criterion` | `VERIFIED-CONDITIONAL` | E3 center transformation forces <L>=0 in invariant thermal measure; only forward symmetry implication established. |
| 147 | 4307–4315 | `p10:thm:finite-spectral-discreteness` | `VERIFIED` | Finite self-adjoint spectrum and ordered E1−E0 gap including ground multiplicity; no continuum conclusion. |
| 148 | 4320–4323 | `p10:thm:reflection-positive-transfer-representative` | `VERIFIED` | Direct spectral calculus of exp[−t(H−E0)] gives strictly positive self-adjoint contraction norm one. |
| 149 | 4328–4331 | `p10:thm:finite-heat-kernel-gap` | `REPRODUCED` | Reducing-projector and finite Wedderburn provenance inherited from earlier proved generated *-algebra; graph connectivity alone insufficient. |
| 150 | 4336–4339 | `p10:cor:finite-pure-glue-pf-gap-derived` | `VERIFIED-CONDITIONAL` | Classical finite cone Perron–Frobenius applies only under positivity-improving cone action; mere positive semidefiniteness is weaker. |
| 151 | 4344–4354 | `p10:thm:finite-plaquette-hodge-curvature-hessian` | `VERIFIED` | E3 fresh reconstruction of 24 vertices,96 edges,96 faces,24 cells, ∂²=0 and full 96×96 face-Hodge spectrum. |
| 152 | 4359–4370 | `p10:thm:bilinear-curvature-heat-time` | `VERIFIED-CONDITIONAL` | E3 spectrum Δ2,H≥I and generalized PSD Rayleigh stiffness; physical QYM form must be supplied nonnegative. |
| 153 | 4375–4378 | `p10:thm:scalar-shell-primitive-curvature-norm` | `FORMALIZED` | Geometric face-projector spectral definition valid on C²(K_H); action on H_L is separate unresolved typed bridge BH-G-000143., issues 143 |
| 154 | 4383–4386 | `p10:thm:finite-flat-connection-vacuum-support` | `VERIFIED` | Independent rank computation gives H1=H2=0 on 24-cell S3 cellular complex; only linearized gauge statement. |
| 155 | 4391–4394 | `p10:lem:scalar-shell-dirichlet-kernel` | `VERIFIED` | Spectral projector unique for specified interval in face-Hodge carrier; not physical H_L projector by itself. |
| 156 | 4399–4402 | `p10:thm:scalar-shell-support-saturation` | `VERIFIED` | Finite face Hodge spectral projectors resolve identity; proper scalar shell is not all of face space. |
| 157 | 4407–4415 | `p10:lem:scalar-shell-transfer-domination` | `UNRESOLVED` | Rayleigh quotient and restricted inequality valid if P_sh acts nontrivially on H_L; source only defines P_sh on face cochains; BH-G-000143., issues 143 |
| 158 | 4420–4427 | `p10:thm:uniform-scalar-shell-transfer-gap` | `UNRESOLVED` | Uniform inf-of-Rayleigh equivalence is algebraic but L-family shell projections lack a typed lift to physical H_L; BH-G-000143., issues 143 |
| 159 | 4432–4435 | `p10:thm:pure-ym-gap-not-full-qcd-chiral-gap` | `VERIFIED-CONDITIONAL` | Pure-glue gap does not imply gap on different chiral full-QCD state/limit; Goldstone scenario conditional. |
| 160 | 4440–4443 | `p10:thm:strong-coupling-area-law-import` | `REPRODUCED` | External convergent cluster expansion area-law result conditional on its actual expansion hypotheses; no native derivation from counts. |
| 161 | 4448–4451 | `p10:thm:separated-color-readout-wilson-connector` | `VERIFIED-CONDITIONAL` | Parallel transporter needed to contract two uncontracted separated gauge-charged endpoints; no claim for products of already-local singlets. |
| 162 | 4456–4459 | `p10:lem:nonzero-center-flux-nonflat-face` | `VERIFIED-CONDITIONAL` | Contractible spanning complex with flat connection forces trivial loop holonomy; global topology restriction is essential. |
| 163 | 4464–4467 | `p10:lem:flux-face-scalar-shell-activation` | `VERIFIED` | P_I F≠0 exactly says Hodge band activated; no amplitude bound inferred. |
| 164 | 4472–4481 | `p10:thm:scalar-shell-contraction-nonzero-nality` | `FORMALIZED` | Exact Rayleigh definition on designated nonempty flux-vector domain; positivity remains physical quadratic-form condition. |
| 165 | 4486–4499 | `p10:thm:hurwitz-reciprocal-area-string-tension` | `REPRODUCED` | Chain embedding, metric area and position Wilson holonomy owner; no live monolithic PAIRxp or positive tension implication. |
| 166 | 4509–4512 | `p10:lem:flux-sector-form-lower-bound` | `VERIFIED-CONDITIONAL` | Rayleigh form inequality by flux kappa on nonempty specified domain; strict positivity not inferred. |
| 167 | 4517–4524 | `p10:thm:hurwitz-static-potential-floor` | `VERIFIED-CONDITIONAL` | E3 direct chain of inequalities gives E≥κ*cA*A under explicitly assumed full-domain coercivity and extent. |
| 168 | 4529–4532 | `p10:cor:no-strong-coupling-assumption-native-confinement` | `REPRODUCED` | Center support and global singlets alone do not prove a nonlinear area tension; explicit qualifications retained. |
| 169 | 4537–4540 | `p10:thm:mass-gap-confinement-closure-map` | `FORMALIZED` | Finite map and continuum handoff as targets; no uniform gap/tension certified by finite structure. |
| 170 | 4550–4564 | `p10:thm:v164-generated-finite-vacuum` | `VERIFIED` | E3 direct finite spectral Gibbs beta→∞ gives P0/rank P0; PF simplicity only on improving transfer cone. |
| 171 | 4566–4578 | `p10:thm:v164-physical-transfer-gap` | `VERIFIED-CONDITIONAL` | Physical spectral gap −log(qL)/aL on positive duration and positive eigenvalue; uniform limit and OS/cyclicity separate. |
| 172 | 4580–4599 | `p10:thm:v164-position-area-factorization` | `VERIFIED-CONDITIONAL` | E3 independent commuting SU3 center flux distributed over N faces has 8π²/(3N) energy, no area coercivity; map is inherited. |
| 173 | 4601–4620 | `p10:thm:v164-ordered-wilson-limits` | `REPRODUCED` | Exact fixed-Wilson QFT4 and OS spectral static-sector import matched to Paper7C v2.195; state/reflection conditions remain required. |
| 174 | 4622–4673 | `p10:thm:v2155-triality-branch-core-majorant` | `UNRESOLVED` | E3 all local heat/triality numeric constants and polynomial checks pass, but claimed full normalized polymer/handle-to-tree bound is not independently certified; BH-G-000144., issues 144 |
| 175 | 4699–4742 | `p10:thm:v2158-finite-type-triality-branch-core` | `UNRESOLVED` | Finite-type monotone supersolution implication on rooted trees algebraically holds; extension to all connected polymers and Wilson expectation inherits BH-G-000144., issues 144 |
| 176 | 4758–4832 | `p10:cor:v2158-hurwitz-two-type-triality` | `VERIFIED-CONDITIONAL` | E3 native triangle/ribbon equal-heat four numerical supersolution margins reproduced; does not prove physical equal heat or APBI. |
| 177 | 4842–4864 | `p10:cor:v2158-apbi-string-tension-reduction` | `UNRESOLVED` | Physical area conversion A≤A+ Acell valid under APBI, but full connected surface inequality inherits missing independent proof step BH-G-000144., issues 144 |
| 178 | 4872–4898 | `p10:cor:v2155-apbc-string-tension-reduction` | `UNRESOLVED` | Square APBC specialization and physical-area conversion algebraically correct, but source-level full surface majorant obligation BH-G-000144 remains., issues 144 |
| 179 | 4907–4922 | `p10:rem:v2155-apbc-firewall` | `FORMALIZED` | APBI same-owner nonlinear action presentation remains explicit open physical bridge; does not treat a chart or one-face subdivision as proof. |
| 180 | 4924–4943 | `p10:thm:v165-native-gap-continuum-boundary` | `REPRODUCED` | Imported native Paper5B carrier support theorem is separate from optional QCD continuum-gap branch; physical transfer scaling and QFT4/OS are conditional. |

### Exact dependency/condition guard and next boundary

The seven batch-specific condition uses are **not** newly introduced foundational axioms. For final global graph integration, resolve aliases against the existing assumption register and connect each claim by one explicit `SCOPE_GUARD`/`IMPORTED_PROOF` use edge only when actually consumed:

| Typed condition / earliest known owner | Claim consumers | Status |
|---|---|---|
| fixed\_nf\_perturbative\_branch; Paper7A 3962; earlier G16 RG source to trace in final DAG | P7A-117, P7A-118, P7A-126 | CONDITIONAL |
| physical\_quark\_mass\_and\_RG\_scale\_map; Paper5A/5B/5C owner; already inherited in P7A batch 1 | P7A-119, P7A-127, P7A-129 | OPEN_PHYSICAL_INTERFACE |
| local\_Gauss\_vs\_global\_Haar\_readout; Paper7A 1322 / BH-G-000138 | P7A-135, P7A-136, P7A-138, P7A-139 | OPEN_PHYSICAL_INTERFACE |
| typed\_nonempty\_Hodge\_shell\_on\_quantum\_carrier; Paper7A 1208 / BH-G-000136 + BH-G-000143 | P7A-157, P7A-158 | UNRESOLVED |
| positive\_coercive\_unscreened\_flux\_and\_extent; Paper7A 4276; 4472; 4517 | P7A-164, P7A-166, P7A-167 | CONDITIONAL |
| QFT4\_OS\_static\_sector\_and\_physical\_step; Paper7C v2.195 bounded state/reflection results | P7A-171, P7A-173, P7A-177, P7A-178 | CONDITIONAL |
| same\_owner\_APBI\_and\_branch\_supersolution; Paper7A 4622, 4842; Paper7C 3939–3989 | P7A-174, P7A-175, P7A-176, P7A-177, P7A-178 | CONDITIONAL |

**Next source boundary:** the chiral, CP and topological source-response section begins at line 4947; first formal statement is **P7A-181 at line 4960**. **Remaining:** 134 formal statements out of 314, plus any relevant unnamed proof steps/technical appendices through source line 8831. Preserve all 11 issues, with no bulk status promotion and no unproved global closure.

**ZIP release remains deferred until the last batch at the user’s instruction.** The final audited integration targets `Paper00-DAGAtlas-v1_116.zip` and `Paper00-ProofChainAudits-v1_33.zip`, each containing only the latest applicable versions; the papers source ZIP is not modified. The direct machine state is `audit7a_work/Paper7A-AuditState-Batch3-v1_3.json`, with E3/E4 exact reproducibility scripts and results `check_batch3_geometry.py`, `batch3_geometry_check.json`, `check_batch3_numerics.py`, `batch3_independent_checks.json`. No interim archive is claimed to be a completed audit.


---

## BATCH 4 — Chiral, CP and topological source response (CUMULATIVE v1.4)

**Audit mandate.** The frozen, authoritative target remains `Paper7A-QCDKernel-v1_165.tex`, SHA-256 `11233c2be618f189ec69edef36bc7a78122d90f13d28cc2f7c39b5b94076788a`, framework `Paper00-PapersMinimal-v2_371`, under `Paper00-RigorousVerificationDAGWorkProtocol-v2_4.md` and the supplied proof-chain audit protocol. This report is *not* an amended theorem or theory-development release. The 11 earlier issues and their earliest sources persist unchanged; only the two new, independently localized items below are added.

**Contiguous source scope.** `Paper7A-QCDKernel-v1_165.tex:4947–6272` (67 formal statements, IDs **P7A-181…247**, first formal start 4960 and last proof ends 6269). Additionally audit three materially consumed unnamed steps P7A-U004…U006 at 5191–5199, 5331–5343 and 5447–5465. The current work is incomplete for the rest of the single designated paper: **247/314 formal statements** are source-bound, **67** remain. Earlier dispositions stay in the previous cumulative report sections.

### E3 independent checks and exact/conditional boundaries

**E3-B04-CAYLEY — Massive scalar overlap reduction, P7A-192–194.** On a fresh random 12-dimensional pair of Hermitian involutions `Γ₅` and `ε_H`, set `V=Γ₅ε_H`, `D_ov=(I+V)/a_R`, `R=(I−V)/2`, `D_m=D_ov+mR`, and `D_c=D_ov R^{-1}` on `ran R`. This does not use the manuscript's proof implementation. Checked unitary/Γ₅ Hermiticity, the exact source derivative `∂_mD_m=R`, the Cayley factorization `D_m=R(D_c+m)`, the resolvent insertion, anti-Hermiticity of `D_c`, and the trace equality: all residuals at or below about `3.1×10⁻¹⁴`. A separate diagonal test with two `V=+1` and two `V=−1` phases verifies vanishing scalar insertion on `ker R` and physical zero at `V=−1`. The exact pair kernel `2m/(m²+λ²)` is thus algebraically correct. This does **not** certify an interacting massless thermodynamic spectral density or a physical subtraction scheme.

**E3-B04-MOMENTS — Variational and spectral source certificates, P7A-196–199.** The source-bound Paper4B stationary certificate at lines 908–955 has the same typed `H(h)=H−hO`, normalization `N`, convexity and constrained dual as this batch. Fifty independent Hermitian 7×7 random models with a unique zero-source ground and a centered Hermitian scalar operator verify the spectral Cauchy–Schwarz bound `χ_L(0) ≥ 2M₀²/(N M₁)` and sourced-ground variational source lower bound. Their smallest recorded margins are positive (`0.0131995961` for susceptibility; `1.2045173655` for the sample source certificate). Thirty positive spectral-measure models independently verify the shrinking-window kernel inequality with minimum margin `0.2261873984`. This supports exact finite inequalities; it does not prove the nonzero quadratic-scale moment bound or convergent pressure for the actual QCD sequence.

**E3-B04-CAR-DENSITY — Spatial orbit/Dirac counting, P7A-206–209.** Current Paper5A lines 1021–1041 give the physical quark factorization with 36 left + 36 right components, rather than an automatically doubled conjugate sector; current Paper2C lines 3453–3499 give `D_m=(m+1)(m+2)(2m+3)/6`. Coupling `S=1/2` to `j=n/2` produces eigenvalues `(n+3/2)/R` with rank `(n+1)(n+2)` and `−(n+1/2)/R` with rank `n(n+1)`. Independently summing every `m=0,…,19` gives exactly `2D_m` for one rank-two spin component. The quark rank 72 yields `72D_m` and the prescribed comparison limit `12Λ_F³/π²`. A check at `m=1000` has relative finite-`m` asymptotic error `0.004506503`, consistent with the expected O(1/m) approach. No physical extensive sea/pressure inference is taken from those counts.

**E3-B04-TOPO — CP Fourier response, P7A-233–239.** Independently choose the positive symmetric five-sector distribution `(p_{−2},p_{−1},p_0,p_1,p_2)=(0.05,0.19,0.52,0.19,0.05)`. Its variance is exactly `0.78`; at volume `V=7` the finite source curvature is `0.1114285714…`, reproduced by a symmetric finite difference to `2.3×10⁻¹⁰`. The CP cosine expansion residual is below `1.2×10⁻¹⁶`. General weights require a positive normalized `θ=0` transfer measure; an adversarial signed-sector algebra can yield negative formal curvature but is not an in-domain counterexample to the declared positive measure. The `θ` variable is correctly kept **auxiliary** unless a physical CP-odd sector-character action is separately generated.

**Further exact proof replay.** The finite unique-vacuum SU(3)×SU(3) character theorem, Schur reduction `D_χ=d_χI₈`, scalar and topological covariance identities, index/zero-mode logical distinctions, root-SU2 Hopf classification and Peano/Taylor `C²` versus `C⁴` CP-even remainders are verified at their stated logical scopes. Current Paper7A does not assert a numerical `Σ`, `F_π`, `B₀`, `L_i`, pure-YM `χ_t`, or a native physical strong `θ` parameter from finite counts.

### E4 challenge and new issue certificates

The two issues are **source-bound interface/matching defects**, not failures of the verified finite matrix identities. Each is recorded at its earliest identified material step, linked to the later consumers, and qualified against the framework's existing conditions. Alternative routes and downstream paper effects are not auto-promoted.


#### BH-G-000145 — MISSING_CONDITION (moderate; OPEN)

**Earliest origin:** `p10:thm:conditional-goldstone-package` at `Paper7A-QCDKernel-v1_165.tex:4977–4987, especially 4983/4986`.

**Source step:** “then the standard Goldstone theorem gives eight non-singlet Goldstone modes”.

**Finding.** The 8-dimensional coset count and the finite unique-vacuum obstruction are correct. Nonzero ordered source slope plus group stabilizer alone does not certify eight massless particle poles without the local-QFT and current/spectral conditions consumed by Goldstone’s theorem. Paper7C lists OS/local reconstruction as a separate conditional bridge.

**Exact unresolved check.** To infer eight physical massless Goldstone excitations (not just eight broken Lie algebra directions) from an ordered nonzero condensate with SU(3)_V stabilizer, verify that the limiting branch satisfies an applicable local/positive relativistic QFT Goldstone theorem: conserved local nonsinglet axial currents, field/locality and regularity, suitable vacuum/cluster and spectral hypotheses, with required source-limit transport.

**Adversarial and import evidence.** Paper7A statement line 4983 consumes standard Goldstone theorem but prints only source/condensate order and SU3_V stabilizer. Paper7C v2.195 lines 2527–2587 describes local OS/Wightman reconstruction with additional QFT/reflection/cluster/regularity hypotheses. Neither the current Paper7A finite source algebra nor Paper7A 4983 separately discharges that theorem domain. No in-domain counterexample asserted.

**Verified bounded impacts:** p10:thm:conditional-goldstone-package → p10:thm:goldstone-tangent-axial-saturation, p10:thm:conditional-goldstone-package → p10:thm:gmor-chiral-bridge → p10:thm:native-chiral-coset-action.

**Further, unconfirmed consumers:** Paper7B pion/axial readouts only on actually consumed Goldstone limiting branch; Paper7C local field/QFT4_E/OS export is a potential condition discharge, not automatically inherited by Paper7A.

**Resolution requirement (do not develop theory during audit).** Source-match a certified local/current/spectrum Goldstone domain (e.g. actual matching Paper7C local QFT branch with chiral current and controlled limit), or explicitly qualify the massless-mode conclusion by those hypotheses. Do not add a new dynamics/condensate proof.

**Scope protection.** Not a refutation of Goldstone theorem or QCD chiral physics, and does not assert that continuum locality fails. Eight group generators remain correctly counted.


#### BH-G-000146 — NORMALIZATION_OR_READOUT (moderate; OPEN)

**Earliest origin:** `p10:thm:native-chiral-eft-hierarchy` at `Paper7A-QCDKernel-v1_165.tex:6027–6032 (first), 6035–6040 (explicit projection)`.

**Source step:** “Coefficients at each order are Taylor/source-cumulant coefficients of the same generating functional”.

**Finding.** The chiral p²/p⁴ hierarchy and the fact that the couplings can in principle be computed from QCD correlation functions are sound. But the full connected functional generally contains nonlocal Goldstone poles and chiral loops; projecting it directly onto local p⁴ invariants does not uniquely isolate renormalized L_i without matching/subtractions. Paper7B independently states scheme-dependent L_i^r and chiral-loop terms.

**Exact unresolved check.** Identify the defined renormalized chiral matching functional for L1…L10,H1,H2, including separation of connected Goldstone exchange/loop terms from local 1PI action coefficients, subtraction scale and local operator-basis convention, before claiming that bare connected functional O(p4) basis projection uniquely returns these couplings.

**Adversarial and import evidence.** Algebraic E4: W(p)=A/(p²+M²)+L p⁴ has p⁴ Taylor coefficient A/M⁶+L, not the local L. At M→0 the connected Goldstone term becomes nonanalytic. Paper7B v1.150 lines 1294–1303 requires matching of amplitudes in a chosen renormalization scheme; lines 1959–1979 explicitly retain one-loop chiral logarithms and L_i^r counterterms. Thus direct projection without subtraction/matching is underdetermined.

**Verified bounded impacts:** p10:thm:native-chiral-eft-hierarchy → p10:cor:nlo-chiral-constants-native-targets, p10:cor:nlo-chiral-constants-native-targets → p10:thm:pseudoscalar-source-matrix-export.

**Further, unconfirmed consumers:** Paper7B L1..L10 hadronic amplitudes wherever matched low-energy constants consumed; Paper7B explicitly requires renormalized scheme.

**Resolution requirement (do not develop theory during audit).** Locate a source-verified matching prescription that extracts local renormalized 1PI/chiral EFT coefficients from the same connected QCD generating functional with Goldstone loop/exchange subtraction and scale, or treat direct connected projection as an unresolved readout step; do not fit new coefficients.

**Scope protection.** Not a claim L_i are impossible to derive, nor a refutation of the native current/correlator definitions. This audits only the Paper7A projection statement and Paper7B dependency text.


### Retained issue ancestry and explicit conditional branches

No earlier issue has been closed or superseded: **BH-G-000134…BH-G-000144** remain as documented in Batches 1–3. In particular, the finite Goldstone source functional inherits **BH-G-000139** where the old `Z` sign/normalization is consumed, but the standalone overlap/Cayley algebra and the stationary finite energy variational inequality do **not** thereby fail. **BH-G-000140/141** are not propagated to the linear-source, unique-ground proof routes that explicitly satisfy their stated restrictions. The physical global/local Gauss issue **BH-G-000138** is not applied to the new unprojected orbital-field embeddings, which correctly distinguish them from physical singlet reduction. The two new issues have one unique origin apiece, with no claim of disproof of ordinary Goldstone physics or standard renormalized ChPT matching.

The following branches remain **genuine conditions** rather than newly alleged contradictions: the actual nonzero action-weighted condensate; uniqueness/full convergence of the matched pressure; the local OS/Wightman/current Goldstone domain; physical color/source/sea/clock matching of the extensive quark carrier; renormalized local chiral effective matching scheme; positive and nondegenerate θ=0 sector weights; admissible GW regulator/index family; a licensed physical θ action; and the pure-Yang–Mills large-N_c susceptibility/correlator bridge. A finite determinant and a geometric homotopy class are not promoted to these physical limit observables by nomenclature.

### Batch 4 statement-level source ledger

| # | Statement source lines | Canonical source label | Disposition | E1/E3/E4 check and exact scope |
|---:|---:|---|---|---|

| 181 | 4960–4964 | `p10:prop:minimal-scalar-singlet-order-parameter` | `VERIFIED` | SU(3)_L×SU(3)_R bifundamental and identity stabilizer SU(3)_V verified by direct matrix action; source order parameter is not an established condensate. |
| 182 | 4969–4972 | `p10:thm:vector-flavor-vacuum-preservation` | `VERIFIED` | Direct one-dimensional-character proof: connected semisimple SU(3)×SU(3) has no nontrivial character, so a unique invariant ground ray cannot spontaneously break it. |
| 183 | 4977–4984 | `p10:thm:conditional-goldstone-package` | `UNRESOLVED` | 8=8+8−8 broken-generator count correct after stated SSB stabilizer; massless excitations require a local/positive QFT current-and-spectrum Goldstone theorem domain not discharged by condensate limit alone (BH-G-000145).; inherited/issues BH-G-000145,BH-G-000139 |
| 184 | 4989–4992 | `p10:thm:axial-singlet-goldstone-exclusion` | `VERIFIED-CONDITIONAL` | Anomalous U(1)_A is not exact when anomaly survives; excludes singlet from 8 Goldstone count. Physical anomaly existence remains scoped. |
| 185 | 4997–5000 | `p10:thm:no-residual-goldstone-current-renormalization` | `VERIFIED` | Ward current/charge normalization is algebraically distinct from normalized one-Goldstone F_pi residue; no count-only F_pi inference. |
| 186 | 5005–5013 | `p10:lem:finite-color-singlet-axial-matrix-element` | `FORMALIZED` | Lorentz covariant axial matrix-element definition on a supplied normalized one-pion state; finite approximants only on licensed correlator branch. |
| 187 | 5018–5021 | `p10:thm:goldstone-tangent-axial-saturation` | `VERIFIED-CONDITIONAL` | Spectral insertion gives squared axial vacuum-to-Goldstone residue under local/current-state normalization and a Goldstone pole; existence branch inherits BH-G-000145.; inherited/issues BH-G-000145,BH-G-000139 |
| 188 | 5026–5033 | `p10:thm:gmor-chiral-bridge` | `REPRODUCED` | Standard PCAC/GMOR identity imported with analytic chiral/ordered-limit conditions, and B0=Sigma/F_pi². Printed O(mq²) depends on explicitly stated analyticity rather than uncontrolled chiral logs. |
| 189 | 5038–5041 | `p10:lem:primitive-source-response-duality` | `VERIFIED` | Inverse of an invertible finite Hessian unique on the specified tangent block; not scalar numerical prediction. |
| 190 | 5046–5053 | `p10:lem:inverse-defect-scalar-spurion-selector` | `VERIFIED` | Adjoint octet SU(3)_V irreducible over C; Schur implies real d I8 for a Hermitian equivariant Hessian; delta_geom not fixed. |
| 191 | 5058–5065 | `p10:thm:native-gmor-scalar-coefficient` | `VERIFIED-CONDITIONAL` | Chiral leading mass-source coefficient defined by Sigma/F_pi² only if physical ordered Sigma and finite nonzero F_pi are supplied; not a geometric scale. |
| 192 | 5076–5093 | `p10:cor:v165-overlap-scalar-source-derivative` | `VERIFIED` | E3 exact D_m derivative gives R=(I−V)/2; a_R cancels at fixed sign kernel. |
| 193 | 5095–5126 | `p10:thm:v2158-overlap-cayley-scalar-response` | `VERIFIED` | E3 fresh 12×12 gamma5-Hermitian unitary V verifies Cayley factorization, anti-Hermitian D_c, resolvent and paired-phase trace to ≤3.1e−14. |
| 194 | 5142–5158 | `p10:cor:v2158-finite-volume-zero-mode-firewall` | `VERIFIED-CONDITIONAL` | Finite zero-mode determinant/trace mass powers follow from actual n0 and Nf; full positive normalized ensemble requires nonvanishing massless denominator and actual sector weights. |
| 195 | 5167–5173 | `p10:rem:v165-overlap-scalar-source-scope` | `FORMALIZED` | No MS-bar scheme, physical mass selection or universal overlap normalization follows from the finite scalar derivative. |
| 196 | 5201–5217 | `p10:thm:chiral-energy-source-certificate` | `VERIFIED-CONDITIONAL` | Direct variational E1 with Paper4B finite energy/source theorem; E3 random finite controls. Ordered liminf positive only from supplied q* and subextensive excess. |
| 197 | 5223–5237 | `p10:thm:chiral-pressure-energy-equivalence` | `VERIFIED-CONDITIONAL` | Finite convexity, Lipschitz, Legendre duality checked against Paper4B:909–955; diagonal sourced-ground argument gives states iff full compatible p(h) and positive slope; no full limit proved. |
| 198 | 5256–5275 | `p10:thm:weighted-chiral-mode-window` | `VERIFIED` | E3 positive scalar resolvent m/(lambda²+m²) bounded below on shrinking ±αm window; requires positive normalized action-dependent μ, not fixed spectral density. |
| 199 | 5288–5310 | `p10:thm:chiral-source-moment-certificate` | `VERIFIED-CONDITIONAL` | E3 50 independent Hermitian 7×7 random controls verify chi≥2M0²/(NM1) and variational source certificate; under simple invariant ground, nonzero M0, positive M1, assumed quadratic moments. |
| 200 | 5378–5391 | `p10:cor:v2186-finite-massive-before-ssb` | `REPRODUCED` | Finite-source and Schur/readout objects exist on designated physical source branch without condensate, APBI, pressure limit; full physical mass/source member remains imported. |
| 201 | 5402–5445 | `p10:def:v2186-xfe-constructor-pressure-split` | `FORMALIZED` | XFE-EXT-CAR constructed word kept distinct from XFE-PRESSURE-COMP limiting analytic certificate; no false promotion from mode density or finite CAR to pressure convergence. |
| 202 | 5483–5497 | `p10:prop:v2189-canonical-global-bundle` | `REPRODUCED` | Canonical j_x pullback and local chart compatibilities algebraically follow from supplied Paper3B/3F bundle owner; no new spin/topology selection. |
| 203 | 5512–5534 | `p10:prop:v2189-native-clock-car` | `VERIFIED-CONDITIONAL` | Base-fiber normalized pullback n^(−1/2) isometry and composition; isometric CAR/Fock embeddings and odd cover cofinality exact when repeated clutch and signs satisfy stated compatibility. |
| 204 | 5569–5589 | `p10:prop:v2189-native-clock-massive-tube` | `VERIFIED` | Unitary overlap D_m singular values bounded below by min(m,2/aR); Neumann complex tube and trace/logdet bounds q! verified algebraically for retained positive massive branch. |
| 205 | 5606–5623 | `p10:prop:v2189-native-clock-bloch-limit` | `VERIFIED-CONDITIONAL` | Finite Fourier Bloch blocks give Riemann sums and local uniform scalar derivatives given imported all-phase sign-kernel gap; only clock determinant pressure, not interacting QCD pressure. |
| 206 | 5675–5720 | `p10:thm:v2189-native-orbital-quark-constructor` | `REPRODUCED` | Current Paper5A quark restriction rank72 and Paper2C complete scalar bands matched; isometric frame R^−3/2 field/dual embedding conditional on admitted generated physical quark-action word. |
| 207 | 5750–5771 | `p10:prop:v2189-orbital-dirac-symbol` | `VERIFIED` | E3 SU(2) addition of j=n/2 with S=1/2 gives ± branches and exact (n+1)(n+2), n(n+1) ranks; totals 2D_m for each rank-two spin component. |
| 208 | 5787–5814 | `p10:prop:v2189-spatial-car-density` | `VERIFIED` | E3 D_m sum and rank72 give density 12 Λ_F³/π²; homothety factor and exact CAR creation/annihilation functor checked. Density is not full Fock dimension. |
| 209 | 5829–5851 | `p10:prop:v2189-spatial-quark-source-word` | `VERIFIED-CONDITIONAL` | Transporting full moving field frame M_g J_m gives exact covariance; compressed fixed-band multiplier not asserted; source jets require actual J derivatives. |
| 210 | 5881–5888 | `p10:thm:banks-casher-bridge` | `REPRODUCED` | Banks–Casher is an imported spectral theorem requiring mass-dependent measure and ordered thermodynamic/chiral convergence; finite zero count not enough. |
| 211 | 5893–5896 | `p10:thm:near-zero-dirac-universality` | `FORMALIZED` | Random-matrix microscopic universality only under matching symmetry/index/volume/epsilon-regime domain, not automatically a finite kernel identity. |
| 212 | 5901–5904 | `p10:thm:unit-topological-representative-finite-carrier` | `VERIFIED-CONDITIONAL` | If admissible GW/overlap index ν=±1 exists it is a unit sector by definition; shell topology alone does not supply required gauge/Dirac pair. |
| 213 | 5909–5916 | `p10:thm:primitive-topological-cell-extensivity` | `VERIFIED` | Direct finite covariance expansion Var(sum νx)=sum Cov; positive extensive normalized limit is an explicit independent dynamical condition. |
| 214 | 5921–5924 | `p10:thm:no-topological-quench` | `VERIFIED-CONDITIONAL` | Topological variance nonzero iff integer charge distribution not point mass under genuine normalized positive transfer measure; not implied by topology support. |
| 215 | 5929–5932 | `p10:thm:no-zero-mode-decoupling` | `VERIFIED` | Index equals net chirality of exact zero modes and imposes no unrelated source matrix element; logical independence correct. |
| 216 | 5937–5940 | `p10:thm:topological-cell-density-near-zero-support` | `VERIFIED` | Finite exact zero support does not imply volume-normalized near-zero spectral density; distinction verified by fixed number of zeros / growing volume counterexample. |
| 217 | 5945–5948 | `p10:thm:native-topological-chiral-condensation` | `VERIFIED` | Topology index/sector weights and action-weighted near-zero/chiral density are logically distinct computation targets. |
| 218 | 5953–5956 | `p10:thm:chiral-vacuum-alignment` | `VERIFIED-CONDITIONAL` | Minimization of explicit chiral potential on SU3 is correct given broken phase, mass spurion and positive Sigma; no finite unique-vacuum breaking inferred. |
| 219 | 5961–5968 | `p10:thm:native-chiral-coset-action` | `REPRODUCED` | Standard SU3 chiral LO two-invariant action conditional on local broken EFT, parity/covariance, matching F_pi and B0; not a native computed amplitude. |
| 220 | 5973–5976 | `p10:cor:leading-pseudoscalar-mass-pattern` | `VERIFIED-CONDITIONAL` | Quadratic spurion expansion gives standard LO octet mass matrix on supplied M_chi and F_pi/B0 normalization. |
| 221 | 5983–5990 | `p10:thm:visible-shell-light-chiral-spurion` | `REPRODUCED` | Mass spurion inherits current charged preterminal source owner; numerical mass eigenvalues at claim scale still require G16 RG/threshold transport and are not certified by H8. |
| 222 | 5995–5998 | `p10:cor:native-light-quark-ratio-package` | `VERIFIED-CONDITIONAL` | Mass ratios algebraic once matched physical M_chi furnished, not source-independent predictions. |
| 223 | 6003–6006 | `p10:thm:pseudoscalar-source-matrix-export` | `FORMALIZED` | Strict one-way Paper7A→7B data export and no reverse choice of QCD source/mass member. |
| 224 | 6011–6014 | `p10:thm:wzw-anomaly-normalization` | `REPRODUCED` | Anomaly matching fixes integer WZW level N_c=3 on constructed chiral EFT; amplitudes still depend on Goldstone normalization and mixing. |
| 225 | 6019–6022 | `p10:thm:anomaly-source-paper-xi-boundary` | `REPRODUCED` | UV anomaly coefficient separate from nonperturbative hadronic operator matrix elements; physical rates downstream. |
| 226 | 6027–6030 | `p10:thm:native-chiral-eft-hierarchy` | `VERIFIED-CONDITIONAL` | Derivative/mass power-counting follows on supplied local broken EFT with scale separation; extracting renormalized NLO coefficients from raw connected cumulants additionally consumes unresolved matching step BH-G-000146.; inherited/issues BH-G-000146 |
| 227 | 6035–6038 | `p10:cor:nlo-chiral-constants-native-targets` | `UNRESOLVED` | Connected generating functional at O(p⁴) contains Goldstone propagation/nonlocal loops, so direct basis projection does not uniquely extract renormalized local L_i without 1PI/loop subtraction and scheme (BH-G-000146).; inherited/issues BH-G-000146 |
| 228 | 6043–6046 | `p10:thm:native-leading-pseudoscalar-weak-decays` | `REPRODUCED` | Leading axial-source coefficient is the actual F_pi/F_K/F_eta matrix-element residue, not color count or Casimir. |
| 229 | 6051–6058 | `p10:thm:native-electromagnetic-form-factor-bridge` | `VERIFIED-CONDITIONAL` | Same-owner U(1)_em source normalization fixes Q_f at p=0; higher form-factor slopes dynamic, conditional physical quark/current branch. |
| 230 | 6068–6075 | `p10:thm:admissible-finite-topology-index` | `VERIFIED-CONDITIONAL` | Admissible GW/overlap index integer and locally constant on sign-kernel-gapped components; actual operator/domain premise retained. |
| 231 | 6080–6083 | `p10:cor:no-free-admissibility-constant` | `VERIFIED` | Index homotopy invariance does not determine regulator admissibility numerical threshold; mathematical scope clear. |
| 232 | 6088–6094 | `p10:thm:topological-sectors-survive` | `VERIFIED-CONDITIONAL` | Unit native topological character changes no admissible gauge components; existence of nonzero sectors requires separately generated regulator. |
| 233 | 6101–6114 | `p10:thm:native-topological-susceptibility-transfer-curvature` | `VERIFIED-CONDITIONAL` | E3 positive normalized integer-weight characteristic function gives -logZ curvature=Var/V; without positive normalized sector weights nonnegativity need not hold (guard not an in-domain refutation). |
| 234 | 6119–6126 | `p10:rem:v161-theta-fourier-source` | `FORMALIZED` | θ Fourier variable is an auxiliary cumulant source; physical CP-odd action requires an independently licensed sector character. |
| 235 | 6128–6139 | `p10:thm:primitive-unit-winding-theta-transfer-form` | `VERIFIED-CONDITIONAL` | E3 exact CP-even cosine series and ν=0,±1 truncation; r=2p1∈[0,1] requires positive sector weights, truncation independently justified. |
| 236 | 6144–6147 | `p10:thm:minimal-native-topological-susceptibility` | `VERIFIED` | Dimensional analysis cannot fix χ_t numerical prefactor or cell four-volume; definition remains variance/actual V map. |
| 237 | 6152–6155 | `p10:cor:topological-enhancement-readout` | `FORMALIZED` | Enhancement is computed variance/susceptibility ratio on specified two measures and defined positive reference denominator. |
| 238 | 6160–6169 | `p10:thm:orthogonal-hurwitz-adjoint-winding-variance` | `VERIFIED` | E3 direct covariance quadratic form wᵀCw; specific factors require weights/overlap and covariance matrix, not carrier count. |
| 239 | 6174–6177 | `p10:cor:full-primitive-topological-winding-block` | `VERIFIED-CONDITIONAL` | Full sector weights/characteristic function determines all finite cumulants; covariance matrix only second cumulant unless higher tensors additionally retained. |
| 240 | 6182–6189 | `p10:thm:light-quark-screened-full-qcd-topology` | `REPRODUCED` | LO chi_t=Sigma/(sum 1/m_f) from standard anomalous chiral potential on supplied physical masses and condensate; no finite-shell numerical value. |
| 241 | 6194–6208 | `p10:cor:native-full-qcd-theta-shape` | `VERIFIED` | Even C² Taylor yields 0.5 chi_t θ²+o(θ²), and C⁴ gives O(θ⁴), only with source-curvature/limit/physical-angle conditions. |
| 242 | 6219–6222 | `p10:thm:topological-index-bridge` | `REPRODUCED` | Regulated index=topological charge is imported continuum/GW theorem strictly on admissible regulator and index-matching domain. |
| 243 | 6227–6230 | `p10:thm:topology-induced-thooft-interaction` | `REPRODUCED` | Fermion zero-mode Grassmann saturation yields t Hooft flavor determinant conditional on index/sector and additional zero-mode overlap; coefficient dynamical. |
| 244 | 6235–6238 | `p10:thm:topological-singlet-pseudoscalar-bridge` | `REPRODUCED` | Witten–Veneziano mass relationship applies only on large-Nc, chiral and pure-YM susceptibility matching branch. |
| 245 | 6243–6250 | `p10:thm:native-anomalous-singlet-pseudoscalar-mass` | `VERIFIED-CONDITIONAL` | On Witten–Veneziano branch m0²=2N_f χ_YM/F0² plus cited asymptotic remainder; no known numerical χ or F0. |
| 246 | 6255–6258 | `p10:cor:primitive-u1a-singlet-pseudoscalar-mass-floor` | `VERIFIED` | No lower mass bound can follow from counts without positive χ_YM lower and F0² upper control. |
| 247 | 6263–6266 | `p10:thm:native-hopf-sectors` | `VERIFIED` | Every SU2 root quotient SU2/U1≅S² and π3(S²)=Z; transferring Hopf charge to gauge/QCD state requires actual map and weight. |


### Material unnamed steps consumed this batch

| Audit ID | Lines | Material step and result |
|---|---|---|

| `P7A-U004` | 5191–5199 | **FORMALIZED**. Stationary ground-energy pressure versus Euclidean clock-normalized scalar source: H(h)=H−hO and p=(E0(0)−E0(h))/(NfV) are source definitions. Euclidean overlap response comparison consumes separately licensed clock, transfer and state identifications; no equality is inferred automatically. |
| `P7A-U005` | 5331–5343 | **VERIFIED-CONDITIONAL**. Mixed source moment co-consumption and connected CAR variance route: Direct expansion O=Σ Oa verifies all mixed M0,M1 terms; M0=W+Xi and connected four-point return imported from Paper4B/current source under its bounded CAR hypotheses. No count substitutes for expectation. |
| `P7A-U006` | 5447–5465 | **REPRODUCED**. Quark-source constructor versus ordered condensate/pressure handoff: Current licensed spatial family provides algebra/action embeddings and mode density; matched QCD sea/clock/source, full pressure and ordered critical response remain separate stated consumers. |


### Typed conditions and assumption inheritance (first source owner, not duplicates)

The following table is a set of **uses/scopes** for final linkage into the single DAG. It does not re-introduce separate foundational or previously discharged assumption nodes. Every direct imported edge still needs a source-use witness and domain review when integrated into the Atlas.

| Condition alias | First known source/owner or boundary | Consumers | Present state |
|---|---|---|---|

| goldstone\_local\_QFT4\_OS\_current\_spectrum\_domain | Paper7C v2.195 OS/Wightman local reconstruction theorem; P7A 4977 consumes standard Goldstone theorem without proof-matched domain | P7A-183, P7A-187, P7A-188, P7A-219 | UNRESOLVED_AT_THIS_USE |
| positive\_vectorlike\_overlap\_massive\_branch | Paper7A existing P7A overlap sign operator and massive vectorlike branch 5076 | P7A-192, P7A-193, P7A-194, P7A-198, P7A-204, P7A-205 | PROVED_ON_DECLARED_FINITE_BRANCH |
| physical\_source\_member\_and\_action\_clock\_normalization | Paper5A/Paper3F licensed source constructor; Paper7A earlier generating-functional audit BH-G-000139 | P7A-183, P7A-187, P7A-196, P7A-200, P7A-201, P7A-206, P7A-209 | CONDITIONAL_SOURCE_MATCHING |
| unique\_invariant\_zero\_source\_ground\_and\_nonzero\_M0\_M1 | Paper7A 5288, with Paper4B source theorem owner for convexity | P7A-196, P7A-197, P7A-199 | CONDITIONAL |
| full\_compatible\_pressure\_limit\_and\_nonzero\_chiral\_slope | Paper7A 5223; pressure theorem conditional, separate from XFE constructor | P7A-197, P7A-201, P7A-218, P7A-219 | CONDITIONAL |
| native\_temporal\_clutched\_cover\_and\_all\_phase\_gap | Paper7A p10:thm:v199-native-clock-covers at 6415 (source later, direct proof-use by label); ancestor Paper1B cover transfer | P7A-203, P7A-204, P7A-205 | PROVED_SOURCE_CLAIM_PENDING_BATCH5_AUDIT |
| native\_spatial\_rank72\_action\_retained\_field\_and\_dual | Paper5A physical factorization 1038 and Paper3F finite-metric constructor | P7A-206, P7A-207, P7A-208, P7A-209 | CONDITIONAL_ON_LICENSED_QUARK_BRANCH |
| renormalized\_local\_chiral\_1PI\_L\_i\_matching | Paper7A 6032; clearer Paper7B v1.150 1294–1303 as downstream source matching clause | P7A-226, P7A-227 | UNRESOLVED_AT_THIS_USE |
| normalized\_nonnegative\_charge\_sector\_transfer\_measure | Paper7A positive vectorlike determinant and native pure heat theta=0 context; 6101 mathematical transfer charge | P7A-214, P7A-233, P7A-235, P7A-239 | CONDITIONAL |
| admissible\_GW\_overlap\_index\_gapped\_component | Paper7A earlier native overlap/GW; Paper7A 6068 gives conditional index theorem | P7A-212, P7A-230, P7A-232, P7A-242, P7A-243 | CONDITIONAL |
| physical\_topological\_theta\_action\_vs\_auxiliary\_fourier\_source | Paper7A 3805, 6119 and Paper5C strong CP boundary | P7A-233, P7A-234, P7A-235, P7A-240, P7A-241 | CONDITIONAL_PHYSICAL_IDENTIFICATION |


### Disposition, provenance and continuation

| Batch 4 disposition | Number |
|---|---:|

| VERIFIED | 21 |
| VERIFIED-CONDITIONAL | 23 |
| REPRODUCED | 14 |
| FORMALIZED | 7 |
| UNRESOLVED | 2 |
| **Total named statements** | **67** |

**Cumulative:** **247/314 named**, 67 remain; 6 material unnamed steps checked; 13 distinct issues (**2 new**). This is a bounded partial audit, not a completed target-paper or DAG release.

## Batch 5 — closing audit of source lines 6273–8831

**Disposition boundary:** All 67 remaining named source blocks (P7A-248–P7A-314), all substantive closing formulas and three material unnamed derivations. No new framework result or source edit. Earlier 13 issues remain open; two distinct missing-evidence issues are newly registered. Numerical proof checks are not confused with physical-realization proofs.

| ID | Lines | Exact source label | Disposition | Evidence-bound source finding |
|---|---|---|---|---|
| 248 | 6289–6314 | `p10:thm:v199-exact-cartan-links` | `REPRODUCED` | Cartan link, holonomy and curvature profiles source-matched to Paper1B; direct reflection and midpoint curvature bound replay, not a fresh full edge-by-edge spin calculation. |
| 249 | 6332–6355 | `p10:prop:v199-restricted-heat-dynamics` | `VERIFIED-CONDITIONAL` | Differentiating 96-face/96-ribbon restricted heat action gives the printed Euler equations; N=3 midpoint stationary by reflection. Restriction is not full action stationary point. |
| 250 | 6370–6394 | `p10:thm:v199-native-unit-component` | `UNRESOLVED` | Exact 864×864 inertia and >0.256 gap rely on 16-phase integer witness payload and verifier reported in Paper7D but absent from the supplied minimal/Atlas archives. Formulas and finite perturbation estimate replay only (BH-G-000147). |
| 251 | 6415–6441 | `p10:thm:v199-native-clock-covers` | `REPRODUCED` | Clock-cover Fourier block replication and index additivity follow if the exact 16-phase uniform-gap certificate is supplied; no independent integer replay of that premise (BH-G-000147). |
| 252 | 6467–6493 | `p10:thm:m8td-all-link-neighborhood` | `VERIFIED-CONDITIONAL` | Row/column norm b=6eps_s+2eps_t+eps_rho and Weyl stability valid for the printed Hermitian stencil, conditional on base exact gap and native link representation (BH-G-000147). |
| 253 | 6511–6525 | `p10:cor:m8td-overlap-continuity` | `VERIFIED` | On two gapped Hermitian matrices sign-resolvent difference is norm bounded by \|\|H-K\|\|/g, giving the displayed overlap bound and gauge-orbit covariance. |
| 254 | 6542–6564 | `p10:thm:v161-positive-primitive-native-sectors` | `VERIFIED-CONDITIONAL` | Every nonempty all-link SU3 neighborhood has positive Haar measure; a pointwise positive pure-heat product gives Z_{±1}>0 and primitive gcd, conditional on certified centers and positive-domain measure (BH-G-000147). |
| 255 | 6600–6615 | `p10:lem:next187-su3-haar-ball` | `VERIFIED` | SU3 torus Vandermonde rectangle bound and exact rational q*=7061881225/199022581174732616540136492402475008 independently rechecked, including factor normalization. |
| 256 | 6649–6672 | `p10:thm:next187-native-heat-interval` | `VERIFIED-CONDITIONAL` | Exact rational comparison 4(7/18)^1152 q*^720>1e-18796 E3 checked; positive masses and index-±1 product balls require exact center certificate not independently replayed (BH-G-000147). |
| 257 | 6706–6720 | `p10:cor:next187-primitive-auxiliary-return` | `VERIFIED` | Primitive characteristic-function lower bound follows from positive ±1 event weights; its least period 2π and unit-return set do not imply strict modulus bound. |
| 258 | 6757–6779 | `p10:thm:v2189-whole-vectorlike-determinant-bounds` | `VERIFIED` | Independent gamma5-Hermitian sign-unitary matrices verify positive determinant and singular-value bounds for all positive scalar flavor masses; no physical mass selection. |
| 259 | 6797–6824 | `p10:cor:v2189-massive-topological-interval` | `VERIFIED-CONDITIONAL` | Whole-weight sector lower bound multiplies heat Haar-ball bound and actual positive determinant ratio, conditional on ±1 certified centers, positive retained scalar masses and fixed Ω (BH-G-000147). |
| 260 | 6840–6860 | `p10:thm:v2189-zero-index-overlap-witness` | `REPRODUCED` | Zero-index center analytic temporal Fourier/polar lower bounds source-replayed for either spin sign; exact full 864-mode result not independently diagonalized, algebraic inequalities valid on displayed stencil. |
| 261 | 6908–6921 | `p10:thm:v2189-massless-topological-endpoint` | `VERIFIED-CONDITIONAL` | At least one unsaturated massless determinant kills \|ν\|>0; zero-index invertible positive-Haar ball prevents zero total partition, conditional on preceding center witness. |
| 262 | 6936–6974 | `p10:thm:v2217-temporal-gw-source` | `REPRODUCED` | GW source C_PP=\|\|Et Q Es\|\|², contact 72aR² and sum_t [D,Et]=0 algebraically rechecked; reducing uniform zero-index temporal sector/normalization not independently rebuilt. |
| 263 | 7016–7034 | `p10:cor:v2189-finite-chiral-topological-suppression` | `VERIFIED-CONDITIONAL` | Finite determinant zeros give χV≤Eν² and upper product O(∏x_f), conditional on fixed positive mass-independent domain containing invertible zero-index ball. |
| 264 | 7049–7082 | `p10:thm:v2189-topological-source-jet-hierarchy` | `VERIFIED` | Gamma5-hermitian unitary phase pairing gives nonnegative determinant polynomial coefficients, n0/parity lower order, and for F≥2 a zero first common mass derivative when Z(0)>0. |
| 265 | 7118–7132 | `p10:rem:v2189-weight-scoped-primitive-activity` | `FORMALIZED` | Distinct pure heat, real massive and unsaturated massless topology weight/domain branches cannot be equated; all keep actual finite index components. |
| 266 | 7144–7170 | `p10:thm:v202-native-overlap-locality` | `VERIFIED-CONDITIONAL` | Range-one Chebyshev/sign locality inherited Paper1B; exact substitution q=10941/11059 and prefactor 11000/(59 aR) independently checked; global spatial refinement not proved. |
| 267 | 7184–7206 | `p10:thm:v202-chiral-projector-transport` | `VERIFIED-CONDITIONAL` | Sign derivative bounds imported from Paper1B on fixed smooth gapped family; projector rank 431k conditional on unreplayed index center; connection curvature and ODE transport follow from finite projectors. |
| 268 | 7221–7244 | `p10:thm:v203-chiral-norm-ball-chart` | `VERIFIED-CONDITIONAL` | Projector chart bound follows by decomposing H into ± spectral subspaces; polar isometry, determinant overlap cocycle on a fixed local chart, not a gauge-global chiral measure. |
| 269 | 7266–7281 | `p10:cor:v204-native-chart-discharge` | `VERIFIED-CONDITIONAL` | Substitution of all-link neighborhood gap and M bound satisfies imported finite chart hypotheses; exact native center gap premise is not independently integer-replayed (BH-G-000147). |
| 270 | 7385–7402 | `p10:prop:v2220-edge-fan-baryon` | `VERIFIED` | Epsilon-color projection is invariant under common-endpoint SU3 transformations and symmetric in three faces; Haar triple fundamental integral gives same W_e with factor 1/6. |
| 271 | 7453–7478 | `p10:thm:v2220-conditional-spinflux` | `VERIFIED` | Spin-sector trace factor 1/12 and first nonflat flux coefficient verified through independent polarized three-leg calculation, not a physical baryon mass claim. |
| 272 | 7498–7507 | `p10:thm:v230-all-link-spinflux` | `VERIFIED` | Fresh matrix construction of C3,C4,C5 for six arbitrary noncommuting SU3 triples reproduces all-link D_e to <7e-16; correct first squared contrast at x8. |
| 273 | 7626–7647 | `p10:thm:v2220-sharp-flux-bounds` | `VERIFIED` | F(U)=\|z-1/2\|²-1/4, upper 3/2 and sharp three-face sums proven; edge-face double-count gives 1/96 face average=1/288 edge sum. |
| 274 | 7663–7678 | `p10:thm:v2220-haar-flux` | `VERIFIED` | Haar character orthogonality reproduces E(F)=1/9, Var(F)=11/162 and independent pairwise-face variance=11/15552; positive density yields strict variance. |
| 275 | 7718–7738 | `p10:prop:v235-triality-relative-source` | `VERIFIED` | 3×3 directed relative incidence M^T M=3I−J exact; equality to earlier label Hessian is on the D22 source-label block only. |
| 276 | 7748–7764 | `p10:cor:v235-common-relative-frame` | `VERIFIED` | Each face occurs in three edge fans; symmetric common/relative fan Gram adds to 9 I96, providing lossless formal face-frame decomposition. |
| 277 | 7774–7794 | `p10:def:v235-signed-fan-operators` | `REPRODUCED` | Signed chi/psi are gauge class functions under common rooted SU3 conjugacy; quaternionic orientation sign compensates face enumeration; color-C parity separated from physical CP. |
| 278 | 7796–7810 | `p10:thm:v235-rooted-weyl-cubic` | `VERIFIED` | Pauli/quaternionic cubic spin trace gives 6σ_e tr(V0V1V2−V0V2V1), hence 18 ψhat; no assertion that physical Hamiltonian contains that cubic. |
| 279 | 7822–7840 | `p10:prop:v235-signed-haar-norms` | `REPRODUCED` | Single-fan SU3 character integrations yield proposed 5/144 and 8/81 squared Haar norms; cross-edge orthogonality asserted via exclusive-link Haar integrals, full 96×96 exact group replay not conducted. |
| 280 | 7862–7879 | `p10:cor:v235-signed-electric-casimir` | `REPRODUCED` | Conditional link-Casimir counts 6×3=18 and 3+6×4/3=11 agree with stated representation types; not a physical interacting energy. |
| 281 | 7919–7932 | `p10:def:finite-qcd-core-datum` | `FORMALIZED` | Finite QCD core tuple explicitly distinguishes constructed operators, target maps, conditional chiral and topology packets, imported charge source and comparison calibrations. |
| 282 | 7934–7947 | `p10:cor:v152-finite-qcd-generated-descendant` | `REPRODUCED` | Structural descendant assertion source-matched to Paper2A co-realization grammar, conditional on actual licensed color, link and mass/source constructors; no new physical occurrence claim. |
| 283 | 7957–7963 | `p10:thm:completion-certificate` | `REPRODUCED` | Completion certificate is definition/computation-target closure only; unresolved gauge/local-source, string tension, chiral limits and nonperturbative mass-gap findings remain in audit. |
| 284 | 7968–7973 | `p10:cor:numerical-finite-qcd-export-package` | `VERIFIED-CONDITIONAL` | Exact 24-cell and Hodge numbers and finite δgeom earlier independently verified; RG crossing/mixed-clock values explicitly comparison-branch, not physical. |
| 285 | 7978–7986 | `p10:thm:paper-x-xi-boundary` | `FORMALIZED` | Paper7A→7B acyclic data interface and no downstream numerical back-selection; no new mathematical performance claim. |
| 286 | 8005–8014 | `p10:cor:v226-qcd-native-coefficients` | `VERIFIED` | Finite momentum factor End(K)⊗Mat_N expansion exists on actually factorized corner; physical signal status remains separate. |
| 287 | 8070–8100 | `p10:thm:v338-full-occupancy-secular` | `UNRESOLVED` | Formal 120-dimensional char-factorization and rank counts are internally consistent (60+60, t=0 spectrum), but the stated complete 2I character/integer certificate is not present for source-independent replay (BH-G-000148). |
| 288 | 8115–8136 | `p10:prop:v338-diagonal-occupancy-leakage` | `REPRODUCED` | Commutation of central character convolution projector with diagonal multiplier forces constant f once nonzero-kernel generating support holds; exact HS coupling table not independently verified from missing 2I certificate (BH-G-000148). |
| 289 | 8148–8154 | `UNLABELED:Paper7A:remark:8148` | `FORMALIZED` | Occupancy parameter t is unselected and the 120-dimensional comparison kernel is not the physical QCD Hamiltonian. |
| 290 | 8170–8191 | `p10:prop:v344-threeface-character-witness` | `REPRODUCED` | Character Fourier combination of existing edge-fan Wilson determinants is gauge invariant; one-link 4/9 witness replayed at counting level using Paper1C but no full eight-orbit independent certificate. |
| 291 | 8203–8215 | `p10:rem:v344-threeface-physical-boundary` | `FORMALIZED` | One-link witness is algebraic not certified action domain, and its Fourier mode is not a new particle/mass/source owner. |
| 292 | 8229–8251 | `p10:prop:v345-f40-qcd-source-obligation` | `REPRODUCED` | F40 fivefold disjoint group supports and proper Hamiltonian leakage/Schur readout follow on supplied group marking and actual isometry candidate; no action selection. |
| 293 | 8260–8268 | `p10:cor:v345-f40-symmetric-source-null` | `VERIFIED-CONDITIONAL` | A5-equivariant symmetric quotient annihilates mirror 3+3prime iff factoring only through the specified T_R+T_L map; antisymmetric channel algebraic only. |
| 294 | 8282–8297 | `p10:prop:v349-f40-source-eligibility` | `REPRODUCED` | 44-component/23 equation and missing A5 quintet claims imported with exact same-cycle and representation types; no universal physical source claim. |
| 295 | 8304–8314 | `p10:cor:v349-f40-linear-scalar-nogo` | `VERIFIED` | No A5-fixed vector in 3⊕3prime⊕3·5, giving zero invariant linear scalar; symmetric quadratic space dimension 1+1+6=8. |
| 296 | 8322–8331 | `p10:rem:v349-f40-source-action-open` | `FORMALIZED` | F40 geometric readouts are candidates; an actual SU3-singlet source, leakage and physical correlator residues remain open. |
| 297 | 8346–8359 | `p10:prop:v350-spinor-intertwining-certificate` | `VERIFIED` | Spinor low-band intertwining iff finite residual ED=0 is direct exact operator equality, not inferred from scalar 14-band proof. |
| 298 | 8368–8386 | `p10:thm:v350-local-gauss-projector` | `VERIFIED-CONDITIONAL` | Vertexwise compact Haar average is orthogonal projector, commutes with invariant H and is contained in global singlet; link/matter representation/truncation is explicit hypothesis (also BH-G-000138). |
| 299 | 8398–8418 | `p10:thm:v350-dynamical-source-hessian` | `VERIFIED` | Exact finite Duhamel/log-partition Hessian includes contact H_ab and centered Kubo correlation; corrects missing terms of earlier source rule (BH-G-000139/BH-G-000140 unresolved earlier scope). |
| 300 | 8430–8447 | `p10:prop:v350-three-face-polarization` | `VERIFIED` | Normalized epsilon singlet matrix coefficient establishes \|E(A,B,C)\|≤1 and three distinct transports not a determinant. |
| 301 | 8461–8472 | `p10:rem:v350-qcd-physical-firewalls` | `FORMALIZED` | Actual mass/source and dynamical-gap boundary distinguishes generated source, physical Gauss action, interacting spectrum and Haar statistics. |
| 302 | 8479–8496 | `p10:thm:v356-heat-star-cumulant` | `VERIFIED` | SU3 center triality kills lower moments; shared U gives exact connected third moment e^(−2t)/27 under declared heat law. |
| 303 | 8510–8517 | `p10:prop:v356-heat-star-cubic` | `VERIFIED` | Positive character coefficients and two singlet 3^3/conjugate 3^3 triple terms imply C3(t)≥54 e^(−2t), with no APBI action claim. |
| 304 | 8529–8545 | `p10:rem:v356-apbi-frontier` | `FORMALIZED` | Numerical heat-star representative explicitly conditional on heat time transport/APBI; not physical shell or measured QCD heat time. |
| 305 | 8553–8575 | `p10:prop:v357-spinflux-wilson-contrast` | `VERIFIED` | SU3 3⊗3bar=1⊕8 identity gives pointwise fundamental−adjoint flux formula and transfers to integrable positive expectations. |
| 306 | 8584–8593 | `p10:rem:v357-spinflux-wilson-scope` | `FORMALIZED` | Wilson-character contrast is only the selected comparison transfer, not a nonperturbative baryon mass splitting. |
| 307 | 8609–8623 | `p10:prop:v365-baryon-color-gram` | `VERIFIED` | Epsilon normalized vectors and Cauchy–Schwarz give W_e color Gram and \|W_e\|≤1; mesonic trace Gram likewise. |
| 308 | 8633–8642 | `p10:prop:v365-color-whitening` | `VERIFIED` | G^−1/2 G G^−1/2=I on support, with singular Moore–Penrose version; raw \|W\|² is not a branching fraction. |
| 309 | 8649–8670 | `p10:def:v365-apbi-hadron-presentation` | `FORMALIZED` | APBI same-physical-Hamiltonian isometry and Schur self-energy are necessary source test; physical embedding and pole overlap remain unestablished. |
| 310 | 8672–8685 | `p10:rem:v365-wilson-jets-scope` | `FORMALIZED` | Cartan 8/9 and jet ranks 3,8 explicitly kept candidate/reference-scoped; no physical rank/mass theorem. |
| 311 | 8697–8719 | `p10:prop:v366-hurwitz-character-hessian` | `VERIFIED` | C3 Fourier diagonalization 3I−J=3(Pchi+Pchibar); independent SU3 polarized determinant Taylor quadratic coefficient matches source to ≲1.2e−6 at eps=3e−4. |
| 312 | 8730–8751 | `p10:prop:v366-hurwitz-wilson-conjugation-grading` | `REPRODUCED` | Formal four inverse pairs yield 4+4 conjugation grading; full 8×8 one-link determinant claimed 2^20·3² but named v1_12 witness absent in supplied archives (BH-G-000148). |
| 313 | 8766–8787 | `p10:prop:v366-hurwitz-spin2-character-source` | `VERIFIED-CONDITIONAL` | Qχ normalized traceless spin-two tensor has vanishing dipole, and given factorized 5⊗2 representation X projectors yield 2/5 and 3/5 norms; not decay probabilities. |
| 314 | 8800–8828 | `p10:def:v366-hurwitz-stress-baryon-interface` | `FORMALIZED` | Final mixed-source test defines conditional physical isometry, C-even stress correlator and genuine O_B requirement; no new transition/width asserted. |

### Additional unnamed consumed calculations

- **`P7A-U007`**, lines 6291–6368, **REPRODUCED**: Native Cartan endpoint/face coefficient source from Paper1B; stationary midpoint is restricted heat action only; exact matrix phase gap remains in external certificate.
- **`P7A-U008`**, lines 7510–7607, **VERIFIED**: Independent six random SU3 triples, direct 8×8 polarized singlet spin traces give D_e coefficient at x8 with residual 6.66e−16.
- **`P7A-U009`**, lines 8065–8146, **REPRODUCED**: Full 60+60 polynomial degree and t=0 eigenvalue multiplicities rechecked; underlying named group-character and integer witness arrays absent from supplied artifacts.

### New Batch 5 issues: exact failure-to-verify certificates

#### BH-G-000147 — MISSING_EVIDENCE (moderate)

**Source:** `p10:thm:v199-native-unit-component`, `Paper7A-QCDKernel-v1_165.tex:6381–6400; controlling Paper7D-TechnicalMaterial-v1_46.tex:384–527`. **Lifecycle:** `OPEN`. **Claim layer:** `SOURCE-AS-PRINTED`.

**Exact source premise:** The exact integer certificate ... proves ... n_-(H_*)=433 ... min|Spec H_*|>0.256

**Evidence and limit:** Paper7D v1_46 at 389 says all witness arrays/verifier/results in release Audit directory; at 397–404 names active exact checker and restored phase05 v1_1. The supplied Paper00-PapersMinimal-v2_371(1)(1).zip contains only TeX/PDF/bib, and supplied Paper00-DAGAtlas-v1_116(1).zip lacks these Audit files; no 16-phase exact replay possible. Independent rational 417/7000 and 10^-18796 arithmetic succeeds but is downstream of that missing premise.

**Remaining certificate:** Supply exact active verifier, witness arrays and manifest for all 16 phases and independently replay integer inequalities. Do not infer a new physical topological theta action from successful replay.

**Effect/scope:** All-link 3k index and finite ±1 susceptibility certificates have a mathematically clear conditional proof from uniform gap/inertia, but the crucial exact numeric base certificate is not replayable from the supplied archives. No counterexample to index/inertia is asserted. This is lack of reproducible supplied numerical proof evidence, not an established inconsistency in the arithmetic result. Structural derivations under a uniform base gap remain correct.

**Confirmed source route(s):** p10:thm:v256-exact-native-inertia → p10:thm:v199-native-clock-covers → p10:thm:m8td-all-link-neighborhood, p10:thm:m8td-all-link-neighborhood → p10:thm:v161-positive-primitive-native-sectors, p10:thm:m8td-all-link-neighborhood → p10:thm:next187-native-heat-interval, p10:thm:m8td-all-link-neighborhood → p10:cor:v2189-massive-topological-interval

**Possible—not certified—downstream effects:** Paper7B physical topological responses require their own action/measure; no proved impact beyond the source-matched native index condition

#### BH-G-000148 — MISSING_EVIDENCE (moderate)

**Source:** `p10:thm:v338-full-occupancy-secular`, `Paper7A-QCDKernel-v1_165.tex:8070–8113; 8115–8146; 8730–8763`. **Lifecycle:** `OPEN`. **Claim layer:** `SOURCE-AS-PRINTED`.

**Exact source premise:** An exact character calculation and independent 60-by-60 and 120-by-120 numerical checks certify the factorization

**Evidence and limit:** Degree check: 13+10+20+3+2+4×3=60 even; odd 54+6=60, at t=0 even multiplicities z^18(z−30)^16(z−24)^25(z−120). Current Paper1C lines 25812–25819 refers to v1_10/v1_12 finite scripts; not shipped in current PapersMinimal or existing Atlas files. Source 8730 also cites verifier-normalized integer 2^20×3² without the actual 8×8 matrix.

**Remaining certificate:** Supply or independently reconstruct the full source-defined 2I incidence/group character and eight Wilson function evaluation matrices with exact normalization, then replay the factorizations and determinant; retain physical comparison status.

**Effect/scope:** The polynomial multiplicities/t=0 spectrum and central/odd rank bookkeeping pass internal checks, and independently verified Hurwitz spin/color formulas remain valid; the exact group-character factors and 8×8 rank certificate are not independently reproduced from available controlling data. No evidence of a false polynomial has been found. This is a missing independent group-representation certificate, not a refutation of the exact 120-mode spectral claim or of the separate eight-character functions.

**Confirmed source route(s):** p10:thm:v338-full-occupancy-secular → p10:prop:v338-diagonal-occupancy-leakage

**Possible—not certified—downstream effects:** Paper7B physical source comparisons are possible consumers, but source keeps t unselected and no actual Hamiltonian route certified

### Independent final-batch certificates

1. **Native finite topology arithmetic (E3):** `q* = 7061881225/199022581174732616540136492402475008` is an exact rational normalization. The source-weight inequality `4(7/18)^1152 q*^720 > 10^-18796` passes exact rational and controlled logarithmic comparison; `32/125-11/56=417/7000` and `(11000−59)/(11000+59)=10941/11059`. **The 864×864 integer-inertia witness is *not* reproduced** from the supplied inputs (BH-G-000147).
2. **All-link polarized determinant / baryon spin–flux (E3):** Independent epsilon-color determinants, cubic/quartic/quintic propagator expansions and 8×8 Pauli three-spin trace recover `D_e(U)=Σ_{f⊃e}(|tr(U_f)/3|²−Re(tr(U_f)/3))`; six noncommuting random SU(3) triple configurations have maximum absolute residual `6.66×10^-16`. These calculations are independent of the missing 2I occupancy character witness.
3. **Positive massive vectorlike determinant (E3):** Random finite gamma5-Hermitian sign-unitary matrix families satisfy the claimed positive determinant and singular-value factors for strictly positive scalar masses; this excludes unlicensed mass signs or a selected physical action.
4. **Finite Wilson/heat (E3):** Fundamental–adjoint character identity and polarized Taylor Hessian independently checked. Pure-heat star cumulant equals `exp(-2t_iso)/27 = 3.7272365646358e-7`. Haar mean, variance and centered covariance verified on the specified finite link measure.
5. **Evidence limits (E4):** The supplied minimal-paper/DAG archives do not carry Paper7D exact 16-phase integer arrays/checker nor the earlier 2I character/8×8 evaluation matrices. These are precise missing reproducibility inputs, *not* proofs that either stated result is false. Current exact source and claim-domain qualifiers remain authoritative.

### Explicit Batch 5 condition uses (no automatic new axioms)

Each row is an inherited or source-scoped predicate used by particular proof routes; it is **not** a new unconditional foundational postulate. See `DAG/AuditLayer/Paper7A-v1_5/AssumptionRegistry.json` in the successor Atlas for first-source ownership and per-route links.

| Scoped condition / interface | Named consumers | Current evidence boundary |
|---|---|---|
| `native_16_phase_exact_integer_inertia_certificate` | P7A-250, P7A-251, P7A-252, P7A-254, P7A-256, P7A-259, P7A-269 | PROOF_CERTIFICATE_REPLAY_PENDING ; first known `Paper7D v1_46 lines 384–527 (source-reported; executable witness absent)` |
| `positive_all_link_harr_product_on_fixed_gapped_omega` | P7A-254, P7A-256, P7A-259, P7A-261 | SOURCE_STIPULATED ; first known `Paper7A lines 6542–6553 and 6651–6659` |
| `strictly_positive_real_massive_vectorlike_source_branch` | P7A-258, P7A-259, P7A-263, P7A-264 | DECLARED_FINITE_BRANCH ; first known `Paper7A vectorlike branch 6757–6779, owner earlier P7A source and P7D 202 appendix` |
| `uniform_invertible_massless_zero_index_ball` | P7A-261, P7A-262, P7A-263, P7A-264 | SOURCE_PROVED_CONDITIONALLY ; first known `Paper7A 6840–6906` |
| `actual_gauge_compatible_same_hamiltonian_source_isometry_APBI` | P7A-309, P7A-314 | OPEN_PHYSICAL_REALIZATION ; first known `Paper7A prior APBI source owner; source-dependent formulation 8649–8670` |
| `A5_F40_one_cycle_coherent_frame` | P7A-292, P7A-293, P7A-294, P7A-295 | MATHEMATICAL_SCOPE_ONLY ; first known `Paper1C v1_59 v349 theorem; Paper7A 8282–8297` |
| `positive_full_support_pure_harr_link_weight` | P7A-274, P7A-279, P7A-312 | DECLARED_PURE_GAUGE_MEASURE ; first known `Paper7A 7663–7705` |
| `conditional_fixed_link_same_one_body_comparison_stencil` | P7A-271, P7A-272, P7A-273, P7A-305 | SOURCE_COMPARISON_ONLY ; first known `Paper7A 7420–7453` |
| `physical_HL_vertexwise_su3_action_invariant_truncation` | P7A-298, P7A-309, P7A-314 | DECLARED_CONDITIONAL ; first known `Paper7A 8368–8386` |

### Final disposition — source audit complete, mathematical issues preserved

| Status | Batch 5 formal blocks | Cumulative 314 formal blocks |
|---|---:|---:|
| `VERIFIED` | 24 | 90 |
| `VERIFIED-CONDITIONAL` | 15 | 85 |
| `REPRODUCED` | 14 | 64 |
| `FORMALIZED` | 12 | 59 |
| `INCONSISTENT` | 0 | 6 |
| `UNRESOLVED` | 2 | 10 |
| **Total** | **67** | **314** |

**Material unnamed consumed derivations:** 9 separately source-anchored; these are not added to the 314 formal denominator. **Issue roots:** 15 unique IDs, `BH-G-000134`–`BH-G-000148`, all retained, not silently closed. **Source coverage:** 8831/8831 source lines as a bounded source review; **source status:** `SOURCE-AS-PRINTED`, not rewritten.

**Final classification:** `FULLY_AUDITED_WITH_OPEN_GAPS`. This denotes completed claim-level triage; some independent E3 calculations or required physical/interface proofs remain unresolved. It is not a declaration that all Paper7A theorems or the whole framework are proved.

**Ancestry, impacts and release:** The updated DAG Atlas `Paper00-DAGAtlas-v1_117.zip` indexes source-labelled claim outcomes, per-route conditions, typed verified edges, 15 issues, quarantined citation candidates and computed verified paths. The separate proof-chain audit collection `Paper00-ProofChainAudits-v1_34.zip` includes one latest audit file per paper, including this `Paper7A-ProofChainAudit-v1_5.md`. All original `.tex` files remain unchanged.

**Evidence reproducibility:** Batch scripts and machine state are in the Atlas audit layer under `Evidence/` and `BatchEvidence/`. Historical source and audit dispositions are preserved with their separate evidence tiers and no new physical prediction is claimed.

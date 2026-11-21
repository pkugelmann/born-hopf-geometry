# Paper I-A — Source-repaired mathematical issue closure (audit addendum v1_9)

**Current source:** `Paper1A-Geometry-v5_178.tex` (Paper00-PapersMinimal-v3_021). **Prior audit:** v1_8, source-frozen v5_177 and reproduced verbatim below, not globally re-audited. **Current resolution layer:** `DAG/AuditLayer/Paper1Resolution-v1_1/Index.json`.

**BH-IA-SRC-000003 — RESOLVED (source and exact mathematical obstruction).** The nonformal rigidity table no longer asserts an ambiguous “level-one closure property”; it gives *first spinor–vector cutoff support*. After `p1:cor:H1-structure`, the repaired paper calculates

\[(\tfrac12,0)\otimes(\tfrac12,\tfrac12)=(0,\tfrac12)\oplus(1,\tfrac12),\qquad \Pi_1(\cdot)=(0,\tfrac12).\]

Unprojected tensor closure fails. The explicitly projected fusion is generally **nonassociative**, with `(A⋆A)⋆B = 2B` and `A⋆(A⋆B) = B` at `A=(1,0)`, `B=(1/2,0)`. The independent script `Paper1A-Level1CGScopeChecks-v1_1.py` checks the complete six-sector census, the 15-dimensional H1 and 43-dimensional block algebra, all 36 projected pair supports and both parenthesizations (**47 exact assertions, PASS**). This is a substantive counterexample to a stronger closure operation, not a change to the existing H1 or mp=1 theorem. No outstanding Paper I-A source issue from this audit remains.

No new physical/GP3 theorem is asserted. Historical 179-statement grade counts are unchanged for their source-matched claims; the source edit was not a full re-audit.

---

## Frozen prior audit for provenance (v1_8)

# Born–Hopf Paper I-A — Complete Current Proof-Chain Audit

**Audit artifact:** `Paper1A-ProofChainAudit-v1_8.md` (16 November 2026).
**Frozen authoritative paper:** `Paper1A-Geometry-v5_177.tex`, source 7,327 lines, SHA256 `0ddd521f70f237830ff4f018c8eebedb4bde43b62a0c9b92eb8c3ec3348f9f17` (PapersMinimal v3.018).
**Protocols:** RigorousVerificationDAG v2.4 (correctness verification only, no new theory or source edits); ProofChainAudit v1.1 as evidence-ancestry guard.
**Audit:** Six cumulative batches, all **179 of 179** formal objects dispositioned, plus material uncensused text/tables (including summary table row line 6017).
**Classification:** `FULLY_AUDITED_NO_CONFIRMED_OPEN_MATHEMATICAL_GAPS` for the 179 formal claims, **WITH_ONE_OPEN_NONFORMAL_SOURCE_SCOPE_ISSUE**. This is not a claim the whole Born–Hopf framework has been globally proved.

## Outcome by evidence level

| Audit property | Result |
|---|---|
| Formal source objects | 179/179 |
| VERIFIED | 100 source-replayed with applicable independent evidence |
| REPRODUCED | 31 source-replayed or imported, limited independent control; global imported proofs not independently reconstructed |
| FORMALIZED | 48 definitions, conventions and scoped remarks |
| UNRESOLVED among formally censused objects | 0 |
| Independently exercised batch checks | B1 2,112; B2 10,201; B3 49,363; B4 5,857; B5 7,982; B6 12,122, all with zero final failures |
| New or confirmed source theorem refutations | 0 within audited scope |
| Open nonformal table interpretation | BH-IA-SRC-000003 |
| DAG-only integration defects | BH-IA-DAG-000001 and BH-IA-DAG-000002, resolved in the v1.153 global graph |
| Other papers | No independent re-audit; no automatic physical status promotion |

## Audit trace and proof boundary

**Batches 1–2 (#1–40):** Marked Hopf normalization, general left-invariant scalar/Hodge/Dirac spectral compiler; Carnot–Carathéodory/sub-Riemannian theory, charges, horizontal heat, Hodge and spinor spectra. Independent checks reproduce exact operator and representation identities; imported CC and same-ball Poincaré results retain source hypotheses.

**Batch 3 (#41–75):** CK/TT/Rarita–Schwinger signed spectrum, curl decomposition, global geodesics and Clifford-torus geometry, CR and basic Dolbeault. Independent group/spin checks and primary cited imported theorem matching; no assumption added.

**Batch 4 (#76–116):** Clifford and quaternionic algebras, Spin(4) truncation, dimensions `dim H1=15`, sector algebra `43`, shell symbol, cone and Sobolev/heat. A false material edge from standard 3-Sasakian **example** to universal rigidity theorem was detected and quarantined.

**Batch 5 (#117–153):** Scalar-band POVM versus full Spin(4) carrier, Chern–Simons, Hopf/Reeb normalizations, contact/CS orientation, linking/helicity, round spectral eta and heat coefficients. A source table calls level-one support “closed”; the projected-cutoff vs unprojected-CG distinction is explicitly left unresolved, without casting doubt on H1 or mp=1.

**Batch 6 (#154–179):** Berger canonical variation, curvature budget (selected inequality; not physical axiom), GH collapse and fixed-cutoff spectral decoupling, Einstein TT gap and gauge, 3D spinor quaternionic doublets, finite binary SU(2) subgroups and normalizer fork. Primary literature checks for Hamilton and Fang–Levitin–Vassiliev; symbolic Koszul/Spin4, finite spectral and A4-normalizer controls.

## Every issue found in this six-batch run

**`BH-IA-DAG-000001` — `DAG_INTEGRITY`, minor with moderate integration risk; resolved in v1.153.** Prior active README had wrong version/source hash, old active combined-graph pointers, and former Berger-decoupling source locator. Current reference is `p1:cor:berger-decoupling` at 6782–6815; new layer uses source SHA256 above and current atlas references. Mathematical impact: none. No confirmed cross-paper proof consequence.

**`BH-IA-DAG-000002` — `DAG_COVERAGE`, moderate; resolved by quarantine in v1.153.** Edge `BH-IA-V176-EDGE-0030` incorrectly declared the *round S³ 3-Sasakian example* an indispensable premise of universal compact 3-dimensional 3-Sasakian rigidity (`p1:cor:3sasakian-rigidity`, 4606–4614). The source actually imports the general rigidity theorem. The spurious edge is removed from material ancestry AND-inputs and retained only as an issue-linked rejected candidate. The source theorem remains REPRODUCED at its stated scope; no certified downstream cross-paper descendants.

**`BH-IA-SRC-000003` — `TYPE_OR_DOMAIN / SOURCE_EVIDENCE_SCOPE`, moderate; open for source clarification.** The nonformal summary-table row at 6017 uses “Level-1 closure property.” True: the defined cutoff retains only `jL+jR≤1`. Strong unprojected tensor-product closure is false, because `(1/2,0) ⊗ (1/2,1/2) = (0,1/2) ⊕ (1,1/2)` with exterior component total spin 3/2. The row does not specify a projection/constructor operation, and cannot be used as an independent physical closure proof. This **does not affect** the H1=15 dimension theorem or the separate mp=1 selection derivation. Verified downstream material path: none; possible unconfirmed interpretations only. Exact obligation: clarify or source-prove the operation implicit in the table row; no paper edits made.

**Math / imported / DAG separation:** no current formal theorem was refuted. Imported global results are valid only within explicit hypotheses and sometimes remain REPRODUCED. Two DAG graph integrity failures are corrected, while one scope claim is unclarified in the frozen TeX. The artifact does not silently replace source interpretations.

## Complete current claim census

| # | Exact source ID | Source lines | Current verdict | Evidence / scope |
|---:|---|---:|---|---|
| 1 | `p1:prop:hopf-scale-dictionary` | 125–181 | VERIFIED | Source statement checked at stated scope |
| 2 | `p1:prop:contact-normalization` | 431–476 | VERIFIED | Source statement checked at stated scope |
| 3 | `p1:conv:global-orientation-signs` | 487–498 | FORMALIZED | Source statement checked at stated scope |
| 4 | `p1:prop:marked-hopf-inversion-transport` | 500–566 | REPRODUCED | Source statement checked at stated scope |
| 5 | `p1:prop:base_fiber_ratio` | 600–611 | VERIFIED | Source statement checked at stated scope |
| 6 | `p1a:theorem:atlas-hopf-map-as-a-riemannian-submersion-b3988b5` | 633–654 | REPRODUCED | Source statement checked at stated scope |
| 7 | `UNLABELED:Paper1A:remark:v5_177:663` | 663–667 | FORMALIZED | Source statement checked at stated scope |
| 8 | `p1:rem:euler-complex-dictionary` | 695–728 | FORMALIZED | Source statement checked at stated scope |
| 9 | `p1:lem:hopf-penalty` | 752–757 | VERIFIED | Source statement checked at stated scope |
| 10 | `p1a:proposition:atlas-milnor-normal-form-0d88235` | 797–824 | VERIFIED | Source statement checked at stated scope |
| 11 | `UNLABELED:Paper1A:remark:v5_177:846` | 846–858 | FORMALIZED | Source statement checked at stated scope |
| 12 | `p1:def:general-spectral-frame` | 869–895 | FORMALIZED | Source statement checked at stated scope |
| 13 | `p1:thm:general-left-invariant-scalar-spectrum` | 897–936 | VERIFIED | Source statement checked at stated scope |
| 14 | `p1:cor:general-spectral-consistency-and-recovery` | 964–999 | VERIFIED | Source statement checked at stated scope |
| 15 | `p1:thm:general-left-invariant-hodge-dirac-compiler` | 1011–1063 | VERIFIED | Source statement checked at stated scope |
| 16 | `p1:prop:general-spectral-cutoff-all-operators` | 1121–1152 | VERIFIED | Source statement checked at stated scope |
| 17 | `p1:thm:general-spectral-heat-and-limits` | 1197–1248 | VERIFIED | Source statement checked at stated scope |
| 18 | `p1:rem:general-spectral-compiler-scope` | 1334–1346 | FORMALIZED | Source statement checked at stated scope |
| 19 | `p1a:proposition:atlas-full-isotropy-forces-roundness-b0fac04` | 1351–1366 | VERIFIED | Source statement checked at stated scope |
| 20 | `UNLABELED:Paper1A:remark:v5_177:1385` | 1385–1387 | FORMALIZED | Source statement checked at stated scope |
| 21 | `UNLABELED:Paper1A:definition:v5_177:1396` | 1396–1409 | FORMALIZED | Convention/definition: not applicable. |
| 22 | `p1:thm:marked-cc-distance` | 1434–1455 | REPRODUCED | E3 scoped: independent path-class inclusion and right-translation check; source-matched imported optimal sy… |
| 23 | `p1:thm:marked-cc-global` | 1479–1485 | VERIFIED | The 2008 Boscain–Rossi global theorem names cut locus a full maximal vertical circle less identity; indepen… |
| 24 | `p1:prop:nilpotent-approx` | 1549–1562 | REPRODUCED | Independent symbolic Heisenberg vector-field bracket and grading; global Gromov–Hausdorff convergence still… |
| 25 | `p1:cor:hausdorff-dim` | 1631–1634 | VERIFIED | Independent Carnot degree sum Q=1+1+2, along with standard equiregular dimension theorem. |
| 26 | `p1:thm:sr-poincare` | 1696–1705 | VERIFIED | Independent cross-read H–K theorem 9.7 and Cor 9.8 with the stronger Jerison same-ball remark following the… |
| 27 | `p1:thm:sr-sobolev` | 1771–1779 | VERIFIED | Independent s=4,p=2 Sobolev exponent calculation and measure/mean factors; audited source applications of H–K. |
| 28 | `p1a:theorem:atlas-l-evy-gromov-concentration-on-the-round-3-sphe-59aa4cc` | 1807–1819 | REPRODUCED | Limited exact hemisphere cap calculation only; it is not an all-measurable-set isoperimetric proof. |
| 29 | `p1a:theorem:atlas-spectral-resolution-8f48b6f` | 1831–1841 | VERIFIED | E3 ALL k: harmonic bihomogeneous polynomials P_(a,b) on C² restrict to S³, degree k=a+b, Hopf q=a-b. Harmon… |
| 30 | `p1:thm:horizontal-spectral-dimensions` | 1848–1867 | VERIFIED | E3 ALL SPECTRUM: direct divisor Dirichlet generating series Σ_(u,v odd) (u+v)/2 (uv)^(-z)=(1-2^(1-z))(1-2^(… |
| 31 | `UNLABELED:Paper1A:remark:v5_177:1894` | 1894–1908 | FORMALIZED | This is only the explicitly defined factor-of-two Hopf-weight convention. |
| 32 | `p1:thm:scalar-spectrum-by-hopf-charge` | 1910–1924 | VERIFIED | E3 ALL k and q: homogeneous harmonic bihomogeneous polynomial kernel dimension k+1, q=a-b, k=a+b; parity an… |
| 33 | `p1:cor:hopf-charge-gap` | 1936–1944 | VERIFIED | Independent direct monotonicity of k(k+2), k≥/q/, q≠0. |
| 34 | `p1:prop:hopf-charge-line-bundle` | 1951–1961 | VERIFIED | E3 ALL q: in local Hopf sections s_j=e^{i alpha_ij}s_i, a weight-q equivariant function has coefficients ph… |
| 35 | `p1a:theorem:atlas-hodge-decomposition-a115d4d` | 2003–2013 | REPRODUCED | Source Green decomposition and integration by parts independently checked at the formal operator level; ker… |
| 36 | `p1a:corollary:atlas-cohomology-e382521` | 2050–2060 | VERIFIED | Independent CW complex one 0-cell and one 3-cell; H0=H3=R and H1=H2=0, then standard Hodge identification. |
| 37 | `p1:thm:hodge-one-form-spectrum` | 2071–2080 | VERIFIED | E3 ALL j: for orthonormal SU2 frame [E_i,E_j]=(2/R) ε_ijk E_k, on 1-forms ∇_i=-(i/R)(2J_i+S_i), S spin1. We… |
| 38 | `p1:thm:representation-harmonic-package` | 2109–2136 | VERIFIED | E3 ALL j: same Hodge Casimir coupling and Hopf opposite-of-frame orientation give curl=(2/R)(J·S+1), i.e. +… |
| 39 | `p1:thm:lichnerowicz-s3` | 2145–2163 | VERIFIED | E3 OPERATOR IDENTITY ALL j: (σ·J)^2=J²−σ·J. D=(2σ·J+3/2)/R ⇒ D²=(4J²+2σ·J+9/4)/R²; spin ∇*∇=(4J²+2σ·J+3/4)/… |
| 40 | `p1:prop:scalar-weyl-law` | 2173–2197 | VERIFIED | Independent finite-square summation and exact integer floor threshold; series expansion k=R sqrt(lambda)+O(… |
| 41 | `p1:lem:conformal-killing-exhaustion` | 2206–2225 | VERIFIED | Independent ambient-coordinate Hessian, 6+4 decomposition and bracket check, with analytic divergence right… |
| 42 | `p1:thm:tt-lichnerowicz-spectrum` | 2265–2291 | VERIFIED | Independent spin-j ⊗ spin-2 Casimir block matrices for j=0..8 in half steps, plus closed algebraic Casimir … |
| 43 | `UNLABELED:Paper1A:remark:v5_177:2416` | 2416–2426 | FORMALIZED | For a conventional definition/remark E3 not applicable. |
| 44 | `p1:cor:tt-counting` | 2428–2451 | VERIFIED | Sympy exact all-M summation and occupancy ratio, with 3,000 threshold-edge checks over five radii. |
| 45 | `p1:thm:quadratic-shell-conformal-killing` | 2476–2517 | VERIFIED | Independent ambient Lie-bracket calculation in 400 sampled points and direct Sym²(2⊕2) representation decom… |
| 46 | `p1:rem:symmetric-pair-bracket` | 2558–2569 | FORMALIZED | For a conventional definition/remark E3 not applicable. |
| 47 | `p1:thm:rarita-schwinger-spectrum` | 2571–2596 | VERIFIED | Primary signed Theorem 1 of Bures--Soucek n=3,j=1 matched to both branches; independent SU2×SU2 dimensions … |
| 48 | `p1a:proposition:atlas-triple-overlap-coefficients-9f2b958` | 2644–2658 | REPRODUCED | Imported theorem or global analytic classification scoped to cited primary mathematical result; not indepen… |
| 49 | `p1a:proposition:atlas-the-coexact-eigenspaces-of-1-further-decompose-59450fa` | 2673–2678 | VERIFIED | Direct Stokes pairing and d†=*d* on two-forms, as an all-form algebraic Hodge identity. |
| 50 | `p1a:theorem:atlas-spectrum-of-curl-d9aaa10` | 2696–2706 | VERIFIED | All-j SU2 spin-1 curl Casimir C=(2/R)(J·S+1) gives positive, zero and negative branches; 105 additional bra… |
| 51 | `UNLABELED:Paper1A:remark:v5_177:2762` | 2762–2774 | FORMALIZED | For a conventional definition/remark E3 not applicable. |
| 52 | `p1:rem:beltrami-not-eta-source` | 2776–2783 | FORMALIZED | For a conventional definition/remark E3 not applicable. |
| 53 | `p1:prop:adiabatic-decoupling` | 2920–2932 | VERIFIED | Independent q≠0 spectral bound; q=0 fixed eigenvalues and multiplicities at Hopf base radius R/2. Corollary… |
| 54 | `p1:prop:killing-implies-einstein` | 2942–2961 | VERIFIED | Independent Clifford contraction e_i R(X,e_i)=-Ric(X)/2 recovers factor 4(n−1)lambda²; nonzero c(v) inverti… |
| 55 | `UNLABELED:Paper1A:remark:v5_177:3002` | 3002–3014 | FORMALIZED | For a conventional definition/remark E3 not applicable. |
| 56 | `p1:prop:symmetry-scalar-multiplicity` | 3019–3031 | VERIFIED | Independent harmonic polynomial dimension and irreducible Spin(4) module dimension argument, all k. |
| 57 | `p1a:theorem:atlas-explicit-geodesics-9c8c444` | 3075–3084 | VERIFIED | Extrinsic ODE verification for 650 normalized random geodesics at varying radii. |
| 58 | `p1a:corollary:atlas-periodicity-62e926f` | 3091–3100 | VERIFIED | Explicit trigonometric least period and geodesic-return differentiation. |
| 59 | `p1a:theorem:atlas-cut-locus-and-conjugate-locus-4ac018a` | 3119–3129 | VERIFIED | Direct normal Jacobi equation y″+y/R²=0 with first positive root πR in each of two normal directions. |
| 60 | `UNLABELED:Paper1A:definition:v5_177:3146` | 3146–3149 | FORMALIZED | For a conventional definition/remark E3 not applicable. |
| 61 | `p1a:proposition:atlas-the-fibers-of-the-hopf-fibration-constitute-a-1e29697` | 3151–3160 | VERIFIED | Independent parametric first/second fundamental forms at 700 randomly sampled Clifford tubes, including mea… |
| 62 | `p1a:theorem:atlas-comparison-theorems-and-model-identities-12bca99` | 3194–3222 | REPRODUCED | Imported theorem or global analytic classification scoped to cited primary mathematical result; not indepen… |
| 63 | `p1a:corollary:atlas-volume-of-a-geodesic-ball-in-s-3-700f05e` | 3229–3242 | VERIFIED | Independent numerical polar integration for 400 radii/geodesic balls plus Taylor coefficient. |
| 64 | `p1:thm:round-extremal-facts` | 3259–3266 | REPRODUCED | Imported theorem or global analytic classification scoped to cited primary mathematical result; not indepen… |
| 65 | `p1a:theorem:atlas-s-3-t-1-0-s-3-is-a-strictly-pseudoconvex-cr-ma-885227d` | 3286–3291 | VERIFIED | Complex Hessian of defining function ρ=Σ/z_i/²−R² is identity, positive on all nonzero complex tangents; 50… |
| 66 | `p1a:theorem:atlas-for-the-standard-cr-sphere-equipped-with-the-c-5c675bb` | 3297–3301 | VERIFIED | U(2) transitivity and preservation of the chosen form eta0 provides an elementary all-point invariance argu… |
| 67 | `p1a:theorem:atlas-the-cr-automorphism-group-of-s-3-is-pu-2-1-90b1123` | 3307–3312 | REPRODUCED | Imported theorem or global analytic classification scoped to cited primary mathematical result; not indepen… |
| 68 | `p1:rem:cr-structure` | 3318–3324 | FORMALIZED | For a conventional definition/remark E3 not applicable. |
| 69 | `p1:thm:hopf-sasakian-dolbeault-hodge` | 3327–3360 | REPRODUCED | Imported theorem or global analytic classification scoped to cited primary mathematical result; not indepen… |
| 70 | `p1:thm:hopf-basic-dolbeault-index` | 3384–3419 | VERIFIED | CP1 cohomology and base S2 spectral formula, 2,505 independent mode/gap sample controls. |
| 71 | `p1:rem:basic-dolbeault-zero-mode-boundary` | 3435–3441 | FORMALIZED | For a conventional definition/remark E3 not applicable. |
| 72 | `p1:thm:hardy-szego-projection` | 3450–3457 | REPRODUCED | Imported theorem or global analytic classification scoped to cited primary mathematical result; not indepen… |
| 73 | `p1:rem:szego-not-finite-carrier` | 3465–3472 | FORMALIZED | For a conventional definition/remark E3 not applicable. |
| 74 | `p1a:theorem:atlas-paneitz-positivity-on-the-standard-cr-three-sp-8fa6a91` | 3477–3483 | REPRODUCED | Imported theorem or global analytic classification scoped to cited primary mathematical result; not indepen… |
| 75 | `p1a:theorem:atlas-cr-sphere-rigidity-package-38671ac` | 3491–3500 | REPRODUCED | Imported theorem or global analytic classification scoped to cited primary mathematical result; not indepen… |
| 76 | `UNLABELED:Paper1A:remark:v5_177:3512` | 3512–3517 | FORMALIZED | Source statement checked at stated scope |
| 77 | `p1a:theorem:atlas-the-3-sphere-admits-a-unique-spin-structure-as-7608b1a` | 3527–3535 | VERIFIED | Source statement checked at stated scope |
| 78 | `p1a:theorem:atlas-algebraic-structure-b08f94a` | 3548–3566 | VERIFIED | Source statement checked at stated scope |
| 79 | `p1:def:quaternions` | 3611–3614 | FORMALIZED | Source statement checked at stated scope |
| 80 | `p1:prop:scaled-unit-quaternions` | 3616–3632 | VERIFIED | Source statement checked at stated scope |
| 81 | `p1:prop:isom-s3-so4` | 3642–3647 | VERIFIED | Source statement checked at stated scope |
| 82 | `UNLABELED:Paper1A:remark:v5_177:3691` | 3691–3696 | FORMALIZED | Source statement checked at stated scope |
| 83 | `p1:prop:unit-quaternion-left-right-actions` | 3700–3708 | VERIFIED | Source statement checked at stated scope |
| 84 | `p1:thm:quat-projline` | 3752–3763 | VERIFIED | Source statement checked at stated scope |
| 85 | `p1:thm:borel-weil-cp1` | 3780–3788 | VERIFIED | Source statement checked at stated scope |
| 86 | `p1:cor:cp1-geometric-quantization` | 3795–3813 | VERIFIED | Source statement checked at stated scope |
| 87 | `UNLABELED:Paper1A:remark:v5_177:3819` | 3819–3826 | FORMALIZED | Source statement checked at stated scope |
| 88 | `p1:prop:hopf-marked-diagonal-base-comparison` | 3828–3855 | VERIFIED | Source statement checked at stated scope |
| 89 | `p1:thm:hopf-marked-diagonal-shell-symbol` | 3868–3918 | VERIFIED | Source statement checked at stated scope |
| 90 | `p1:rem:shell-symbol-not-hopf-pullback` | 3956–3969 | FORMALIZED | Source statement checked at stated scope |
| 91 | `UNLABELED:Paper1A:remark:v5_177:3971` | 3971–3973 | FORMALIZED | Source statement checked at stated scope |
| 92 | `UNLABELED:Paper1A:remark:v5_177:3991` | 3991–3996 | FORMALIZED | Source statement checked at stated scope |
| 93 | `p1:thm:hyperbolic-normal-form` | 4011–4020 | VERIFIED | Source statement checked at stated scope |
| 94 | `p1:thm:z3-elliptic` | 4036–4044 | VERIFIED | Source statement checked at stated scope |
| 95 | `p1:thm:cayley` | 4075–4088 | VERIFIED | Source statement checked at stated scope |
| 96 | `p1:thm:unit-quaternion-double-cover-so3` | 4101–4109 | VERIFIED | Source statement checked at stated scope |
| 97 | `p1:cor:left-invariant-global-frame-s3` | 4118–4140 | VERIFIED | Source statement checked at stated scope |
| 98 | `UNLABELED:Paper1A:remark:v5_177:4147` | 4147–4155 | FORMALIZED | Source statement checked at stated scope |
| 99 | `p1:def:spin4-truncation` | 4175–4188 | FORMALIZED | Source statement checked at stated scope |
| 100 | `p1:rem:scalar-vs-spin4` | 4190–4195 | FORMALIZED | Source statement checked at stated scope |
| 101 | `p1:prop:dimHm` | 4197–4205 | VERIFIED | Source statement checked at stated scope |
| 102 | `p1:prop:block-algebra-dimensions` | 4222–4243 | VERIFIED | Source statement checked at stated scope |
| 103 | `p1:cor:H1-structure` | 4267–4277 | VERIFIED | Source statement checked at stated scope |
| 104 | `p1:prop:spin4-low-degree-dictionary` | 4284–4319 | VERIFIED | Source statement checked at stated scope |
| 105 | `p1:thm:round-s3-3sasakian-model` | 4579–4591 | REPRODUCED | Source statement checked at stated scope |
| 106 | `UNLABELED:Paper1A:remark:v5_177:4601` | 4601–4604 | FORMALIZED | Source statement checked at stated scope |
| 107 | `p1:cor:3sasakian-rigidity` | 4606–4610 | REPRODUCED | Source statement checked at stated scope |
| 108 | `p1:thm:hyperkahler-cone` | 4620–4628 | VERIFIED | Source statement checked at stated scope |
| 109 | `p1:cor:flat-cone-canonical-scale` | 4658–4666 | VERIFIED | Source statement checked at stated scope |
| 110 | `p1:cor:flat-cone-four-density-homothety` | 4672–4691 | VERIFIED | Source statement checked at stated scope |
| 111 | `p1:thm:beckner-sobolev-s3` | 4709–4730 | REPRODUCED | Source statement checked at stated scope |
| 112 | `UNLABELED:Paper1A:remark:v5_177:4773` | 4773–4775 | FORMALIZED | Source statement checked at stated scope |
| 113 | `p1:thm:hopf-harmonic-morphism` | 4781–4791 | REPRODUCED | Source statement checked at stated scope |
| 114 | `p1:thm:heat-kernel-s3` | 4803–4823 | VERIFIED | Source statement checked at stated scope |
| 115 | `UNLABELED:Paper1A:remark:v5_177:4852` | 4852–4860 | FORMALIZED | Source statement checked at stated scope |
| 116 | `UNLABELED:Paper1A:remark:v5_177:4862` | 4862–4865 | FORMALIZED | Source statement checked at stated scope |
| 117 | `p1:thm:scalar-band-evaluation-povm` | 4867–4896 | VERIFIED | Source statement checked at stated scope |
| 118 | `p1:thm:isotypic-commutant` | 4971–4986 | VERIFIED | Source statement checked at stated scope |
| 119 | `p1:prop:homothetic-scaling-laws` | 4998–5061 | VERIFIED | Source statement checked at stated scope |
| 120 | `p1:prop:standard-contact-fill-tight` | 5233–5260 | REPRODUCED | Source statement checked at stated scope |
| 121 | `p1:def:cs-normalized` | 5283–5295 | FORMALIZED | Source statement checked at stated scope |
| 122 | `p1:prop:cs-gauge-ambiguity` | 5297–5312 | VERIFIED | Source statement checked at stated scope |
| 123 | `p1:thm:mc-generator` | 5326–5338 | VERIFIED | Source statement checked at stated scope |
| 124 | `p1:cor:cs-volume-relation` | 5351–5359 | VERIFIED | Source statement checked at stated scope |
| 125 | `UNLABELED:Paper1A:remark:v5_177:5366` | 5366–5368 | FORMALIZED | Source statement checked at stated scope |
| 126 | `UNLABELED:Paper1A:remark:v5_177:5374` | 5374–5388 | FORMALIZED | Source statement checked at stated scope |
| 127 | `p1:thm:boothby-wang-hopf` | 5393–5410 | REPRODUCED | Source statement checked at stated scope |
| 128 | `UNLABELED:Paper1A:remark:v5_177:5423` | 5423–5426 | FORMALIZED | Source statement checked at stated scope |
| 129 | `p1:thm:hopf-homotopy-exact-sequence` | 5431–5450 | REPRODUCED | Source statement checked at stated scope |
| 130 | `p1:prop:hopf-ensemble-isotropy` | 5476–5493 | VERIFIED | Source statement checked at stated scope |
| 131 | `p1:cor:hopf-class-no-axis` | 5520–5536 | VERIFIED | Source statement checked at stated scope |
| 132 | `p1:thm:canonical-hopf-u1` | 5549–5569 | VERIFIED | Source statement checked at stated scope |
| 133 | `UNLABELED:Paper1A:remark:v5_177:5589` | 5589–5599 | FORMALIZED | Source statement checked at stated scope |
| 134 | `p1:thm:hopf-normalization-package` | 5600–5632 | VERIFIED | Source statement checked at stated scope |
| 135 | `p1:cor:positive-reeb-lattice` | 5638–5660 | VERIFIED | Source statement checked at stated scope |
| 136 | `p1:prop:unit-cotangent-double-cover` | 5673–5680 | REPRODUCED | Source statement checked at stated scope |
| 137 | `UNLABELED:Paper1A:remark:v5_177:5686` | 5686–5689 | FORMALIZED | Source statement checked at stated scope |
| 138 | `p1:thm:poincare-topological-uniqueness` | 5693–5696 | REPRODUCED | Source statement checked at stated scope |
| 139 | `p1:thm:gysin-hopf-bundle` | 5804–5816 | REPRODUCED | Source statement checked at stated scope |
| 140 | `p1:prop:hopf-linking-helicity` | 5827–5846 | VERIFIED | Source statement checked at stated scope |
| 141 | `p1:thm:positive-hopf-link-open-book` | 5874–5879 | REPRODUCED | Source statement checked at stated scope |
| 142 | `p1:thm:hopf-fibers-great-circles` | 5889–5894 | VERIFIED | Source statement checked at stated scope |
| 143 | `UNLABELED:Paper1A:remark:v5_177:5902` | 5902–5907 | FORMALIZED | Source statement checked at stated scope |
| 144 | `p1:rem:great-circle-contact-rigidity` | 5909–5918 | REPRODUCED | Source statement checked at stated scope |
| 145 | `p1:thm:whitehead-integral-formula` | 5924–5944 | REPRODUCED | Source statement checked at stated scope |
| 146 | `UNLABELED:Paper1A:remark:v5_177:5953` | 5953–5957 | FORMALIZED | Source statement checked at stated scope |
| 147 | `p1:prop:hopf-reeb-beltrami` | 5959–5966 | VERIFIED | Source statement checked at stated scope |
| 148 | `p1:prop:chirality-factor-exchange` | 6040–6047 | VERIFIED | Source statement checked at stated scope |
| 149 | `p1:thm:yamabe-round-sphere` | 6125–6128 | REPRODUCED | Source statement checked at stated scope |
| 150 | `UNLABELED:Paper1A:remark:v5_177:6134` | 6134–6136 | FORMALIZED | Source statement checked at stated scope |
| 151 | `p1:prop:eta-round-zero` | 6143–6167 | VERIFIED | Source statement checked at stated scope |
| 152 | `UNLABELED:Paper1A:remark:v5_177:6183` | 6183–6185 | FORMALIZED | Source statement checked at stated scope |
| 153 | `p1:prop:integrated-heat-coefficients-s3` | 6203–6211 | VERIFIED | Source statement checked at stated scope |
| 154 | `p1:def:berger-canonical-variation` | 6293–6300 | FORMALIZED | Berger canonical variation sets only the vertical metric coefficient, not a new physical selector. |
| 155 | `p1:prop:submersion-fiber-length` | 6302–6316 | VERIFIED | Horizontal submersion is exact; Hopf psi-period 4pi gives fiber length 2pi R epsilon, intrinsic diameter pi… |
| 156 | `p1:lem:fibers-geodesic` | 6344–6346 | VERIFIED | Constant-length Killing vector integral curves satisfy ∇_K K=0. |
| 157 | `p1:thm:berger-sectional` | 6394–6405 | VERIFIED | Independent Koszul-symbolic derivation yields horizontal K=(4−3ε²)/R² and mixed K=ε²/R². |
| 158 | `p1:cor:berger-ricci` | 6437–6454 | VERIFIED | Ricci entries are sums of sectional curvatures; positivity thresholds and Einstein iff ε=1 follow exactly. |
| 159 | `p1:cor:berger-primitive-cap-rigidity` | 6471–6510 | VERIFIED | Curvature budget factor (ε²−1)(11ε²−13)/3 verified symbolically; collapse half-family 0<ε≤1 has only round … |
| 160 | `p1:rem:berger-primitive-cap-scope` | 6537–6543 | FORMALIZED | Scope remark correctly limits cap to the canonical Berger/Hopf variation. |
| 161 | `p1:cor:spinframe-hopf-shape-descendant` | 6545–6592 | VERIFIED | Spin(2) frame double-cover gives c1=1 from Euler=2; spherical shape normalization is homothety invariant; o… |
| 162 | `p1:rem:spinframe-hopf-shape-scope` | 6623–6629 | FORMALIZED | Radius b remains arbitrary; R enters comparison normalization, not a derived microscopic radius. |
| 163 | `p1:cor:berger-vol-diam` | 6631–6640 | VERIFIED | Volume scales ε; base horizontal lift plus fiber arc yields stated diameter upper bound. |
| 164 | `p1:thm:berger-gh` | 6653–6660 | VERIFIED | Graph of π is a correspondence with distortion ≤πRε; GH ≤(πRε)/2 in standard correspondence convention, so … |
| 165 | `UNLABELED:Paper1A:remark:v5_177:6691` | 6691–6695 | FORMALIZED | Bounded curvature follows from explicit K formula for ε∈(0,1]. |
| 166 | `p1:thm:berger-spectrum` | 6719–6733 | VERIFIED | Peter–Weyl Casimir and doubled vertical charges give λ_{ℓ,q}=[ℓ(ℓ+2)+(ε⁻²−1)q²]/R² with per-charge multipli… |
| 167 | `p1:cor:berger-first-positive-eigenvalue` | 6751–6763 | VERIFIED | First modes (ℓ,q)=(2,0) and (1,±1) cross at ε=1/√6, multiplicities 3,4,7; no omitted ℓ≥2 mode is lower. |
| 168 | `p1:cor:berger-decoupling` | 6782–6795 | VERIFIED | For q≠0 lower bound (ε⁻²−1)/R² diverges; q=0 only even ℓ and precisely base spectrum and multiplicities sur… |
| 169 | `p1:thm:einstein-uniqueness-s3` | 6822–6826 | VERIFIED | In dimension 3 Einstein implies constant sectional curvature; compact simply connected positive-curvature S… |
| 170 | `p1:thm:hamilton-ricci-flow-convergence` | 6848–6856 | REPRODUCED | Hamilton’s normalized-flow theorem source checked under compactness and initial Ric>0. No claim for Ric≤0. |
| 171 | `p1:cor:ricci-flow-round-stability` | 6863–6866 | REPRODUCED | Positive Ricci is C²-open, so Hamilton theorem applies to small round perturbations. |
| 172 | `p1:prop:infinitesimal-einstein-deformations` | 6877–6911 | VERIFIED | TT deformation Hessian, gap at 4/R² and gauge-Killing kernel checked; source Bianchi gauge solves and remov… |
| 173 | `p1:thm:lowest-dirac-pair-stability` | 6985–7003 | VERIFIED | Quaternionic C²=−I and [C,D]=0 force retained complex rank-two doublets; conformal covariance independently… |
| 174 | `p1a:theorem:atlas-finite-subgroup-classification-b4f160f` | 7073–7093 | REPRODUCED | SO(3) finite rotation classification lifts to binary cyclic/dicyclic and T/O/I; subgroup orders and odd-ord… |
| 175 | `p1:def:finite-support-atlases` | 7099–7122 | FORMALIZED | Finite epsilon-net atlas and finite subgroup-closed atlas are distinct; notation includes cyclic overlaps e… |
| 176 | `p1:prop:2O-two-cosets-not-product` | 7174–7191 | VERIFIED | Index-two H=2T in 2O yields two cosets; no involution outside H in SU2 => extension does not split. |
| 177 | `UNLABELED:Paper1A:remark:v5_177:7201` | 7201–7206 | FORMALIZED | Left–right Spin(4) 2T×2T is a different ambient carrier than one-sided SU2 subgroup. |
| 178 | `p1:prop:exceptional-nesting` | 7243–7250 | VERIFIED | Displayed groups give H⊂2O and H⊂2I; 2O⊄2I since 24 does not divide 60 after central quotient. |
| 179 | `p1:thm:exceptional-normalizer-fork` | 7264–7290 | VERIFIED | Permutation-group normalizers computed: N_{S4}(A4)=S4, N_{A5}(A4)=A4; hence N_SU2(H)=2O and N_I(H)=H, inter… |

## Historical issue provenance (not re-opened)

- `BH-IA-G-000102`, `000103`, `000104`, `000111`: earlier evidence gaps were closed in current v5.177 source via cited global CC/Poincaré, signed Rarita–Schwinger and all-spin compiler proofs. Imported literature remains correctly marked as imported rather than new Born–Hopf axioms.
- `BH-IA-G-000105`, `000106`: historical source type/global-projector defects resolved in earlier v5.176 geometry edits, retained as antecedent provenance.
- Obsolete exceptional-chamber source branches from earlier Paper1A versions were removed from the present 179-object census and are not retroactively declared proved.

## DAG route and archive validation

- All 179 IDs have source-matched original statement spans, fixed source SHA, E1 status and scoped E3/E4 lineage; one formal object is one canonical layer claim entry, not many copies in batch ledgers.
- Imported constraints remain canonical/typed and conditional; no new physical axioms or physical realizations were introduced.
- False `BH-IA-V176-EDGE-0030` was excluded from live material paths, AND inputs and transitive closure; unrelated cross-paper records are preserved.
- The next DAG Atlas is v1.153 built on the latest supplied v1.152; the companion archive is v1.66 built on v1.65. Keep one current Paper1A proofchain audit v1.8; every other paper audit remains the latest inherited version.
- Files are mathematical source/proof-chain objects; neither source TeX, macros, bibliography nor any PDFs were edited/generated.

**Audit release:** source-complete within the specified paper; one unresolved table-scope clarification remains. Do not infer wider physical laws or closure of downstream framework claims from these mathematical checks.

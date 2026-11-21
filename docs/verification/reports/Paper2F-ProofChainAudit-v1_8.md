# Source migration and repair-integration addendum — Paper2F-ProofChainAudit-v1_8.md

**Integration release:** `Paper00-PapersMinimal-v3_007.zip`, 14 November 2026.
**Current paper source:** `Paper2F-TechnicalMaterial-v1_67.tex`.
**Status:** `SOURCE_INTEGRATED; GLOBAL_SOURCE_REAUDIT_PENDING`. An inherited historical audit is not a correctness certificate for the newer current manuscript.
**Evidence policy:** Local algebraic proofs and scoped tests do not discharge physical source/observable interfaces or automatically alter the canonical proof DAG.

---

## Historical source-bound audit: Paper2F-ProofChainAudit-v1_7.md
# Born–Hopf Geometry Paper II-F — Rigorous proof-chain audit (Batches 1–7)

**Artifact:** `Paper2F-ProofChainAudit-v1_7.md`  
**Current source:** `Paper2F-TechnicalMaterial-v1_61.tex` (SHA-256 `48ddfbde3da7d9d3f13478d6a8c64ea9136c7b024c0aaa44c0ca0ef3401cd79e`)  
**Source corpus:** `Paper00-PapersMinimal-v2_370(1).zip`  
**Current DAG:** `Paper00-DAGAtlas-v1_94.zip` (Batch 7); prior batch baselines recorded in run ledger  
**Protocol:** `Paper00-RigorousVerificationDAGWorkProtocol-v2_4.md`  
**Coverage:** source lines 107–9555; 244 unique audited/formalized claim objects, all 223 formal declarations. Complete target source census, with inherited II-A open interfaces.

## Batch 2 result and issues

- 25 new source claim/proof records plus one reused statement (`BH-IIF-C-0003`), corresponding to **26 material units** in the batch.
- **Exact computational controls:** 24,799/24,799 PASS; source-specific mathematical inference remains governed by E1+E3+E4.
- **New confirmed mathematical gaps/defects:** 0. **New issue IDs:** none. No inherited issue is resolved by this partial audit.
- New conditions: four typed local branch predicates, not additional principles. The preexisting combined core-constructor and exceptional-occurrence guards are reused.
- Full source and index anchors updated to Paper II-F v1.61. Batch 1 corresponds to current source lines 107–618 after a single release banner insertion.
- The 24-point round code branch produces the **unmarked geometric orbit**; it does not, without its own type bridge, physically instantiate a group-closed support on fixed SU2 multiplication.
- At the time of Batch 2, all later statements (line 8467 onward) remained **NOT_AUDITED**; superseded by the final Batch 7 audit below.

## Batch 2 source claim census

| ID | v1.61 lines | Source theorem/proof owner | Verdict |
|---|---|---|---|
| `BH-IIF-C-0017` | 619–662 | Cocharacter proof of the rank-one Hopf inclusion (`p2:cor:v193-u1-su2-cocharacters`) | VERIFIED-CONDITIONAL |
| `BH-IIF-C-0018` | 663–690 | Faithful unitary trace metric and nonnegative curvature (`p2:thm:finite-mode-trace-metric`) | VERIFIED-CONDITIONAL |
| `BH-IIF-C-0019` | 691–728 | Compact completion and compact Lie consequences (`p2:thm:gp1-compact-geometric-consequences`) | VERIFIED-CONDITIONAL |
| `BH-IIF-C-0020` | 729–771 | Elliptic compact resolvent gives finite spectral bands (`p2:thm:gp1-bounded-spectrum-finite-carrier`) | VERIFIED |
| `BH-IIF-C-0021` | 772–813 | Toral-simple decomposition of compact connected H (`p2:thm:compact-connected-global-structure`) | VERIFIED |
| `BH-IIF-C-0022` | 814–834 | Maximal tori and exponential surjectivity (`p2:thm:maximal-torus-exponential`) | VERIFIED |
| `BH-IIF-C-0023` | 835–866 | One-parameter subgroup torus closure and periodicity (`p2:thm:one-parameter-operation-closure`) | VERIFIED |
| `BH-IIF-C-0024` | 867–900 | Left-regular homogeneous operation-value parent (`p2:thm:regular-homogeneity-closure`) | VERIFIED-CONDITIONAL |
| `BH-IIF-C-0025` | 901–939 | Left-right isometry kernel and inversion (`p2:thm:left-right-isometry-action`) | VERIFIED |
| `BH-IIF-C-0026` | 940–969 | Parallelizable, orientable, spin H and Euler zero (`p2:thm:parallelism-topology-closure`) | VERIFIED |
| `BH-IIF-C-0027` | 970–1007 | Finite-net distance-profile tomography 2ε bound (`p2:thm:finite-resolution-profile-tomography`) | VERIFIED |
| `BH-IIF-C-0028` | 1008–1048 | Finite point-resolution support requires occurrence token (`p2:thm:derived-finite-point-support-role`) | VERIFIED-CONDITIONAL |
| `BH-IIF-C-0029` | 1076–1115 | No isometry/automorphism natural embedded 24-set (`p2a:prop:no-natural-finite-exceptional-selector`) | VERIFIED |
| `BH-IIF-C-0030` | 1116–1139 | Conditional exceptional role entry after representative no-go (`p2a:cor:exceptional-support-status-after-no-go`) | FORMALIZED |
| `BH-IIF-C-0031` | 1140–1187 | Candidate-independent core/support bridge co-realization (`p2:cor:core-support-inheritance-no-duplicate-witness`) | VERIFIED-CONDITIONAL |
| `BH-IIF-C-0032` | 1188–1234 | Two alternative conditional entry routes to unmarked [2T] (`p2a:cor:two-conditional-2t-discharge-routes`) | VERIFIED-CONDITIONAL |
| `BH-IIF-C-0033` | 1235–1279 | Trimer/axis finite support range and generated C6 families (`p2:cor:conditional-trimer-axis-support-exhaustion`) | VERIFIED-CONDITIONAL |
| `BH-IIF-C-0034` | 1280–1304 | Stone-Weierstrass completion of distance tests (`p2:thm:generated-test-algebra-completion`) | VERIFIED |
| `BH-IIF-C-0035` | 1305–1391 | Universal separated test-image and effective operation quotient (`p2:thm:universal-gp3-reduction`) | VERIFIED |
| `BH-IIF-C-0036` | 1392–1444 | Metric Kuratowski/Banach isometry and faithful pullback action (`p2:thm:canonical-banach-realization`) | VERIFIED |
| `BH-IIF-C-0037` | 1445–1479 | Kernel criterion for faithful operation quotient (`p2:thm:faithful-quotient-kernel`) | VERIFIED |
| `BH-IIF-C-0038` | 1480–1511 | Normalized Haar, invariant averaging projection (`p2:thm:unique-haar-averaging`) | VERIFIED-CONDITIONAL |
| `BH-IIF-C-0039` | 1512–1534 | Intrinsic real-analytic Lie structure and maps (`p2:thm:derived-real-analyticity`) | VERIFIED-CONDITIONAL |
| `BH-IIF-C-0040` | 1535–1564 | Peter-Weyl complete harmonic decomposition (`p2:thm:peter-weyl-complete-reducibility`) | VERIFIED |
| `BH-IIF-C-0041` | 1565–1618 | Scalar Laplace-Casimir, heat kernel, and Weyl law (`p2:thm:laplace-casimir-heat-closure`) | VERIFIED-CONDITIONAL |
| `BH-IIF-C-0003` (reused) | 1049–1075 | Generic point resolution does not force exceptional support; source proof already audited in Batch 1 | VERIFIED-CONDITIONAL |

## Batch 2 evidence certificates

### BH-IIF-C-0017 — Cocharacter proof of the rank-one Hopf inclusion

**E1 source replay (619–662):** Apply the II-A SU2 parent and Paper-I-B circle cocharacter theorem: integer weight n, Weyl identifies sign and primitive |n|=1 is faithful.

**E3 independent check:** Direct character-lattice argument for U1->SU2 and integer root-kernel calculations; the marked Hopf embedding remains an upstream occurrence.

**E4 adversarial boundary:** A generic nonprimitive circle map is not a refutation of the particular primitive Hopf inclusion.

**Direct imported proof/use labels:** `p1b:result:circle-cocharacters`, `p2:lem:chosen-hopf-vector-parent-inclusion`.

### BH-IIF-C-0018 — Faithful unitary trace metric and nonnegative curvature

**E1 source replay (663–690):** Injective differential of a faithful finite unitary representation gives a positive trace inner product; cyclic trace yields Ad-invariance, and curvature is ||[X,Y]||^2/(4||X∧Y||^2).

**E3 independent check:** Independent Pauli-matrix su2 test yields metric I/2 and sectional curvature +1/2 in that normalization; general positivity follows directly for skew-Hermitian matrices.

**E4 adversarial boundary:** The trace metric does not grant every higher trace tensor GP2 physical retention, nor positivity when dρ fails injectivity.

**Direct imported proof/use labels:** `p2:thm:finite-mode-lie-regularity`.

### BH-IIF-C-0019 — Compact completion and compact Lie consequences

**E1 source replay (691–728):** Extreme value, finite injectivity radius, complete smooth flows, Haar unimodularity, no compact subgroup of additive R^n, and compact-power recurrence follow at distinct source-stated tiers.

**E3 independent check:** Separate compactness and power-subsequence arguments: if arbitrarily late a^n lie near same point, differences give positive powers near identity; real additive compact subgroups vanish.

**E4 adversarial boundary:** The compact comparison X alone does not supply a Riemannian manifold or a finite-dimensional Lie structure for claims (ii)-(iii).

**Direct imported proof/use labels:** `p2:thm:frc-automatic-compact-lie-closure`.

### BH-IIF-C-0020 — Elliptic compact resolvent gives finite spectral bands

**E1 source replay (729–771):** A positive-order nonnegative self-adjoint elliptic differential operator on a closed compact smooth finite-rank bundle has compact resolvent and hence finite spectral ranks below Λ.

**E3 independent check:** Independent torus Fourier computation for -∂_x^2-∂_y^2 gives finite disks of lattice modes; -∂_x^2 alone has infinite y multiplicity.

**E4 adversarial boundary:** Dropping ellipticity or boundary realization invalidates the conclusion; source explicitly excludes both cases.

### BH-IIF-C-0021 — Toral-simple decomposition of compact connected H

**E1 source replay (772–813):** The center and semisimple ideals integrate to a finite central isogeny (T^k×∏H_i)/F_0 and H=Z(H)^0[H,H].

**E3 independent check:** Independent Lie-algebra rank accounting and SU2×U1 modulo central kernel control both rank and finite central quotient.

**E4 adversarial boundary:** H connected and finite-dimensional are indispensable; arbitrary compact totally disconnected groups do not meet the premise.

### BH-IIF-C-0022 — Maximal tori and exponential surjectivity

**E1 source replay (814–834):** Compact connected maximal-torus theorem gives each element a toral container; surjective torus exponential lifts it into exp(h).

**E3 independent check:** Independent diagonalization of arbitrary SU2 unitary determinant-one matrices demonstrates toral log construction in rank one.

**E4 adversarial boundary:** This does not select a preferred torus or one logarithm and fails for general disconnected Lie groups.

### BH-IIF-C-0023 — One-parameter subgroup torus closure and periodicity

**E1 source replay (835–866):** Closed image of R in a compact connected abelian torus has lattice kernel iff it is a 1-torus; irrational higher-torus slopes are dense and nonperiodic.

**E3 independent check:** Independent rational versus irrational slope control in T2; kernel of t->(e^{it},e^{iαt}) is nonzero iff α rational.

**E4 adversarial boundary:** Compact recurrence must not be promoted to universal periodicity; X=0 is a separate trivial branch.

### BH-IIF-C-0024 — Left-regular homogeneous operation-value parent

**E1 source replay (867–900):** The unique group word a=yx^{-1} maps x to y and preserves every retained left-invariant metric. The distinguished identity is not a metrically preferred location.

**E3 independent check:** Independent finite group regular-action freeness/transitivity controls and direct smooth group translation calculation.

**E4 adversarial boundary:** Transitivity is on H acting on H, not on an unrelated external state space; g_F needs the optional FD+LR premise.

**Direct imported proof/use labels:** `p2:thm:operational-john-metric`.

**Actual scoped conditions:** `BH-IIA-A-FD-LR-001`.

### BH-IIF-C-0025 — Left-right isometry kernel and inversion

**E1 source replay (901–939):** The H×H left-right action has kernel diagonal center, stabilizer diagonal H modulo center, and inversion is a bi-invariant-metric isometry.

**E3 independent check:** Compute kernel from x=e and centrality for arbitrary x; SU2 verifies nontrivial ±I kernel; inversion reverses products.

**E4 adversarial boundary:** Inversion is a group automorphism only on the abelian branch. General left-invariant but not right-invariant metrics do not suffice.

### BH-IIF-C-0026 — Parallelizable, orientable, spin H and Euler zero

**E1 source replay (940–969):** Smooth trivialization by dL_{x^-1} makes TH trivial; spin obstruction w2=0; compact positive-dimensional H admits a nowhere-zero field.

**E3 independent check:** Independent circle and S3 global frames, zero Euler characteristic, and tangent bundle product verification.

**E4 adversarial boundary:** Spin-admissibility is existence, not a selected spin structure or orientation convention.

### BH-IIF-C-0027 — Finite-net distance-profile tomography 2ε bound

**E1 source replay (970–1007):** Reverse triangle gives upper Lipschitz bound; choose net point within ε of x and triangle inequality yields lower d(x,y)-2ε.

**E3 independent check:** Independent enumeration on finite cyclic geodesic metrics: every pair and all arithmetic-step finite nets satisfy the bound.

**E4 adversarial boundary:** A net gives finite approximate, not exact finite embedding; error vanishes only in the ε->0 family.

**Direct imported proof/use labels:** `p2:cor:gp1-resolution-completeness-derived`.

### BH-IIF-C-0028 — Finite point-resolution support requires occurrence token

**E1 source replay (1008–1048):** Finite ε-net + metric-curry test closure + object-typed G0 RESpt_ε occurrence yields the unmarked support class and 2ε reconstruction; no distinguished representative is inferred.

**E3 independent check:** Independent metric test tuple construction for finite cyclic controls and output-class separation of existence vs representative.

**E4 adversarial boundary:** GP1 alone does not actualize the point-reference role, and all nets are not themselves a single physically selected finite set.

**Direct imported proof/use labels:** `p2:cor:gp1-resolution-completeness-derived`, `p2:thm:finite-resolution-profile-tomography`, `p2:lem:gp2-canonical-construction`.

**Actual scoped conditions:** `BH-IIA-A-METRIC-CURRY-001`, `BH-IIF-A-0008`.

### BH-IIF-C-0029 — No isometry/automorphism natural embedded 24-set

**E1 source replay (1076–1115):** Transitivity of orientation-preserving Isom(S3) makes any invariant nonempty round subset all S3. Finite Aut(SU2)-invariant sets lie in center because other conjugacy orbits are infinite.

**E3 independent check:** Independent orbit-stabilizer and conjugacy sphere control for SU2 with eigenvalue parameter fixed.

**E4 adversarial boundary:** A natural unmarked orbit of finite supports is not an embedded natural representative; the theorem does not refute an added orbit-level minimization mechanism.

### BH-IIF-C-0030 — Conditional exceptional role entry after representative no-go

**E1 source replay (1116–1139):** Exact text lists typed possible support occurrence/constructor routes (a)-(e), GP2 retention, and the distinction between unmarked classes and labelled tokens.

**E3 independent check:** Each listed branch is separately checked for type and source provenance; the phrase "such as" is not an exhaustive mathematical iff classification.

**E4 adversarial boundary:** Do not infer universal co-realization from the representative no-go or from a mere unmarked finite net.

**Direct imported proof/use labels:** `p2a:prop:no-natural-finite-exceptional-selector`.

**Actual scoped conditions:** `BH-A-IIE-0010`.

### BH-IIF-C-0031 — Candidate-independent core/support bridge co-realization

**E1 source replay (1140–1187):** Under an occurring RESpt output, a frozen candidate-independent core constructor and a proved domain bridge, the complete unmarked [2T] orbit is a generated-role descendant and needs no second support occurrence.

**E3 independent check:** Independent constructor-typing check separates total output orbit from a chosen labelled Hurwitz representative and verifies each arrow condition.

**E4 adversarial boundary:** The unbridged generic point support does not itself instantiate a 2T group object. Existing stronger core/bridge condition is reused, not cloned.

**Direct imported proof/use labels:** `p2:thm:derived-finite-point-support-role`, `p2:def:finitely-presented-generated-role-descendant`, `p2:thm:generated-role-corealization`.

**Actual scoped conditions:** `BH-IIB-A-B2-CORE-CONSTRUCTOR-001`, `BH-IIF-A-0008`.

### BH-IIF-C-0032 — Two alternative conditional entry routes to unmarked [2T]

**E1 source replay (1188–1234):** Route (i) imports the uniqueness of a 24-point π/3 kissing orbit; route (ii) imports the same-role exceptional subgroup range and least class. They are alternative sufficient conditions, not consequences of ε-coverage.

**E3 independent check:** Independent rational Hurwitz 24-vertex dot products give max pairwise dot=1/2; finite binary group class inclusions supply the second conditional route.

**E4 adversarial boundary:** Orbit [2T] as round point support is not automatically a group-closed embedded representative on fixed SU2 multiplication; source distinguishes route (ii) subgroup input.

**Direct imported proof/use labels:** `p1:thm:s3one-classical-completions`, `p1:cor:conditional-exceptional-role-order`, `p2:cor:core-support-inheritance-no-duplicate-witness`.

**Actual scoped conditions:** `BH-IIF-A-0009`, `BH-IIF-A-0010`.

### BH-IIF-C-0033 — Trimer/axis finite support range and generated C6 families

**E1 source replay (1235–1279):** Group-closed Γ with -1 and an extra trimer/axis admissibility bridge has exactly the four unmarked classes C6grp,2T,2O,2I; the 2T core gives full C6 stabilizer/link families and no labelled vertex.

**E3 independent check:** Independent finite SO3 rotation-subgroup type analysis and exact group orders 6,24,48,120; index-2 2O/2T extension cannot split in SU2.

**E4 adversarial boundary:** Without the additional bridge, generic finite nets need not lie among four classes. C6 group and C6 link graph are distinct sorts.

**Direct imported proof/use labels:** `p1:thm:trimer-axis-binary-support-range`, `p1:cor:generated-c6-stabilizer-link-bridge`, `p1:prop:2O-two-cosets-not-product`, `p2:thm:generated-role-corealization`.

**Actual scoped conditions:** `BH-IIF-A-0011`, `BH-IIF-A-0008`.

### BH-IIF-C-0034 — Stone-Weierstrass completion of distance tests

**E1 source replay (1280–1304):** All distance profiles b_z are continuous, contain constants after unitalization and separate points; real Stone-Weierstrass gives dense C(Xhat,R).

**E3 independent check:** Independent exact distance-profile injection and algebraic separation on finite cyclic metric controls; general density by the real Stone-Weierstrass criterion.

**E4 adversarial boundary:** Uniform completion does not make all continuous functions primitive B-operations.

**Direct imported proof/use labels:** `p2:thm:canonical-metric-profile-separation`.

### BH-IIF-C-0035 — Universal separated test-image and effective operation quotient

**E1 source replay (1305–1391):** H-invariant tests produce closed state congruence, normal kernel K_B, compact evaluation image, faithful quotient H/K_B, and universal factorization for quotient pairs with specified inclusions.

**E3 independent check:** Independent explicit C12 action on residue-class tests mod3 gives K_B={0,3,6,9}, quotient C3, faithful action and both map factorization laws.

**E4 adversarial boundary:** An arbitrary quotient is not GP3-selected; the implication directions for π and q are necessary and source states them explicitly.

### BH-IIF-C-0036 — Metric Kuratowski/Banach isometry and faithful pullback action

**E1 source replay (1392–1444):** Sup metric difference of full distance profiles is exactly d(x,y); compactness closes the embedding. Isometries intertwine with pullback operators U_g, and separation gives faithfulness.

**E3 independent check:** Independent cyclic-geodesic finite metric computations yield exact equality for every ordered pair; direct substitution proves equivariance.

**E4 adversarial boundary:** U_g is faithful only on the effective generated isometry group, not on a prior action with kernel.

**Direct imported proof/use labels:** `p2:thm:canonical-metric-profile-separation`.

### BH-IIF-C-0037 — Kernel criterion for faithful operation quotient

**E1 source replay (1445–1479):** G-action on invariant tests descends to G/N iff N⊆kerρ; quotient action kernel is kerρ/N and is faithful iff N=kerρ.

**E3 independent check:** Independent modular C12/C3 test family explicitly computes all kernels and shows neither over- nor under-quotient is faithful.

**E4 adversarial boundary:** Full distance profiles imply trivial kernel only for genuine faithful isometry action, not every non-effective group action.

**Direct imported proof/use labels:** `p2:thm:canonical-metric-profile-separation`.

### BH-IIF-C-0038 — Normalized Haar, invariant averaging projection

**E1 source replay (1480–1511):** Haar probability on compact G is unique left/right; normalized bi-invariant metric volume coincides with Haar; averaging a finite representation yields idempotent projection onto fixed vectors.

**E3 independent check:** Independent exact finite Fourier/cyclotomic C_n character sums show averaging annihilates each nontrivial character and fixes the trivial one.

**E4 adversarial boundary:** A metric-volume formula requires a supplied bi-invariant metric; Haar itself needs no metric or statistical interpretation.

### BH-IIF-C-0039 — Intrinsic real-analytic Lie structure and maps

**E1 source replay (1512–1534):** Every established finite-dimensional Lie group admits the unique compatible analytic group structure and every continuous homomorphism between finite-dimensional Lie groups is analytic.

**E3 independent check:** Independent local BCH and analytic-matrix examples in compact group representations, plus standard analytic-Lie uniqueness theorem.

**E4 adversarial boundary:** This conclusion requires prior finite-dimensional Lie closure, not mere compactness or choice of analytic chart.

**Direct imported proof/use labels:** `p2:thm:frc-automatic-compact-lie-closure`, `p2:thm:finite-mode-lie-regularity`.

### BH-IIF-C-0040 — Peter-Weyl complete harmonic decomposition

**E1 source replay (1535–1564):** Haar-averaged Hermitian inner product gives complete reducibility; Peter-Weyl yields the full Vπ⊗Vπ* sum and uniform matrix-coefficient density.

**E3 independent check:** Independent U1 Fourier-character basis control plus finite representation invariant orthocomplement argument.

**E4 adversarial boundary:** Completeness of all irreducibles does not select a finite particle spectrum or physically identified mode.

**Direct imported proof/use labels:** `p2:thm:unique-haar-averaging`.

### BH-IIF-C-0041 — Scalar Laplace-Casimir, heat kernel, and Weyl law

**E1 source replay (1565–1618):** Bi-invariant g_F yields central quadratic Casimir -sum X_a², unique self-adjoint compact elliptic Laplacian, positive heat kernel and N(Λ)~ω_d Vol(H) Λ^{d/2}/(2π)^d.

**E3 independent check:** Independent S1 case: eigenvalues n², N(Λ)=2 floor√Λ+1, coefficient 2√Λ; exact 1D count controls check formula.

**E4 adversarial boundary:** Requires optional FD+LR to supply g_F; neither physical Hamiltonian nor spectral cutoff follows.

**Direct imported proof/use labels:** `p2:thm:operational-john-metric`.

**Actual scoped conditions:** `BH-IIA-A-FD-LR-001`.

## Open antecedents, not mathematical defects

- `BH-IIF-A-0008`: G0 physically realizes a positive-resolution point-reference readout RESpt_ε of a distinguishable metric comparison role; finite metric-curry test tuples are object-typed under its existing readout grammar.
- `BH-IIF-A-0009`: An occurring point support Z⊂S3 has exactly 24 points and minimum round angular distance π/3, in the same round metric and support orbit comparison used by Paper I-A optimal kissing theorem.
- `BH-IIF-A-0010`: An occurring finite support Γ⊂SU2 is a subgroup containing -1 in one common axis-free exceptional role, with independently licensed same-role subgroup-leastness comparison.
- `BH-IIF-A-0011`: The actually occurring support descendant Γ⊂SU2 is group-closed, has -1, and a separate bridge establishes the Paper-I-A trimer-or-axis-free admissibility disjunction for the same Γ.

Previously registered and reused: `BH-IIB-A-B2-CORE-CONSTRUCTOR-001`, `BH-A-IIE-0010`, `BH-IIA-A-METRIC-CURRY-001`, `BH-IIA-A-FD-LR-001`, and `BH-IIA-A-B15-RESTRICT-001`. The two conditional 2T sufficient routes are OR alternatives, not a single AND premise.

## Validation and honest scope

The ZIP/hash/schema/query checks are E0 integrity gates, not a mathematical proof. The 24-point enumeration establishes the displayed code and angular distance, not uniqueness of all optimal configurations; the latter is an exact Paper I-A import. Standard compact-Lie/Haar/Peter–Weyl/Weyl theorems are checked at their source hypotheses, not generalized beyond them. No source TeX is edited, and no unexamined downstream status is upgraded.

---

## Preserved Batch 1 audit report (original v1.60 source, current v1.61 +1 line mapping)

# Born–Hopf Geometry Paper II-F — Rigorous proof-chain audit (Batch 1)

**Artifact:** `Paper2F-ProofChainAudit-v1_1.md`  
**Target source:** `Paper2F-TechnicalMaterial-v1_60.tex` (SHA-256 `1b8a21ca84778028c3837d808fd28181ab8a3e028ae6f20b213954fcac5769cf`)  
**Source archive:** `Paper00-PapersMinimal-v2_369.zip`  
**DAG baseline:** `Paper00-DAGAtlas-v1_87.zip`  
**Audit protocol:** `Paper00-RigorousVerificationDAGWorkProtocol-v2_4.md`  
**Coverage:** 16 material statements/proof-owning units, lines 106–617 of 9,554. This is a partial audit, not global certification.

## Batch 1 result

- Source source-identity byte comparison: PASS.
- Exact independent symbolic controls: 134/134 PASS.
- **New confirmed mathematical defects: zero in inspected source slice.** This does not assert absence of undetected defects or completion of later sections.
- No new GAP IDs; no inherited gaps are closed or recertified automatically.
- Five rejected E4 challenges were type/antecedent mismatches, preserved in proof evidence.
- Conditional mathematical options and negative selectors are not new physically realized roles.

## Claim census and verdicts

| ID | Source lines | Claim and source label | Verdict |
|---|---|---|---|
| BH-IIF-C-0001 | 109–159 | Euclidean scalar stationarity and complete isotropy scope; `unnamed` | VERIFIED-CONDITIONAL |
| BH-IIF-C-0002 | 160–188 | Retained transverse covector obstructs zero fixed space; `p2a:prop:v2190-retained-mark-fixed-vector` | VERIFIED |
| BH-IIF-C-0003 | 201–238 | Generic epsilon-net excludes forced exceptional 24-cell support; `p2a:prop:generic-resolution-not-exceptional` | VERIFIED-CONDITIONAL |
| BH-IIF-C-0004 | 240–249 | Boundedness does not select a realization label — deferred proof; `p2:thm:no-cutoff-from-finiteness` | VERIFIED-CONDITIONAL |
| BH-IIF-C-0005 | 251–280 | Scalar-orientation inversion countermodel; `p2:prop:scalar-orientation-inversion-countermodel` | VERIFIED |
| BH-IIF-C-0006 | 283–305 | Finite spectral algebra under injective reparametrization; `p2:thm:finite-spectral-reparametrization-no-go` | VERIFIED |
| BH-IIF-C-0007 | 308–329 | Static-algebra selector boundary; `p2:cor:static-algebra-selector-boundary` | VERIFIED-CONDITIONAL |
| BH-IIF-C-0008 | 332–374 | GP1-TB sharpness: solenoid and weighted product torus; `p2:prop:gp1-clause-sharpness` | VERIFIED |
| BH-IIF-C-0009 | 377–394 | Boundedness plus origin does not select a family member; `p2:cor:gp1-gp2-no-family-member` | VERIFIED-CONDITIONAL |
| BH-IIF-C-0010 | 397–444 | Exact capacity of the admissible Paper-I-A module; `p2:cor:admissible-module-capacity` | VERIFIED-CONDITIONAL |
| BH-IIF-C-0011 | 457–470 | GP2 zero-defect and exact/faithful filter scope; `p2:rem:gp2-origin-filter-alone` | FORMALIZED |
| BH-IIF-C-0012 | 472–488 | GP2 chronological origin and anti-self-selection; `p2:rem:gp2-chronological-origin-alone` | FORMALIZED |
| BH-IIF-C-0013 | 490–515 | GP2 local generated closure equals identity component; `p2:thm:gp2-local-closure-connectedness` | VERIFIED-CONDITIONAL |
| BH-IIF-C-0014 | 519–559 | Candidate-internal and chronological infinitesimal retention; `p2:thm:gp2-alone-frame-natural-alternatives` | VERIFIED-CONDITIONAL |
| BH-IIF-C-0015 | 561–593 | Exact scope of GP2 alone; `p2:cor:gp2-no-existence-alone` | VERIFIED-CONDITIONAL |
| BH-IIF-C-0016 | 595–614 | Chronology before candidate self-data: T²/SU3 diagnostic; `p2:rem:mode-neutrality-load-bearing` | FORMALIZED |

## Source-bound evidence certificates

### BH-IIF-C-0001: Euclidean scalar stationarity and complete isotropy scope

**E1 source replay (109–159):** Given nonzero compactly supported Hermitian Phi1 and licensed scalar rescaling, Tr Phi1^4 integrates positively. The cubic derivative of a lambda^2+b lambda^4 is nonzero as a polynomial. The inversion fixes bare (beta,dt,X), not necessarily extra parent marks.

**E3 independent check:** Independent polynomial coefficient extraction, exact symplectic 3x3 check and same-owner differentiation of an invariant scalar.

**E4 domain/adversarial check:** Attempted to infer stationarity from symmetry alone; rejected, since invariance annihilates symmetry directions rather than all tangent variations.

**Direct registered condition uses:** `BH-IIF-A-0003`.

### BH-IIF-C-0002: Retained transverse covector obstructs zero fixed space

**E1 source replay (160–188):** Nondegenerate OmegaV identifies every fixed covector ell with a unique Z. Isotropy preserving OmegaV and ell must fix Z, and nonzero ell implies nonzero Z.

**E3 independent check:** Independent symplectic-matrix solve Omega Z=ell and uniqueness under stabilizer conjugation.

**E4 domain/adversarial check:** Reflection on bare comparison tensors is not an in-domain counterexample if it fails to retain ell.

**Direct registered condition uses:** `BH-IIF-A-0001`.

### BH-IIF-C-0003: Generic epsilon-net excludes forced exceptional 24-cell support

**E1 source replay (201–238):** Start with a finite epsilon/3-net; perturb in finite product of geodesic balls and avoid the finite union of proper real analytic relation/24-cell Gram loci; eps coverage persists. Coarse singleton independently defeats universal 24-cardinality.

**E3 independent check:** Independent dimension/count argument: the 24-cell Gram equalities constrain a finite-dimensional product of free round-3-sphere points to a proper analytic locus; generic perturbation exits while coverage persists.

**E4 domain/adversarial check:** The finite net is not required to be an actualized exceptional group support. Requiring group closure adds a hypothesis absent from the finite-resolution source role.

**Direct registered condition uses:** `BH-IIA-A-METRIC-CURRY-001`.

### BH-IIF-C-0004: Boundedness does not select a realization label — deferred proof

**E1 source replay (240–249):** Every member of the stipulated inequivalent family satisfies the given FRC restrictions and no prior operator distinguishes members, so no value is singled out by GP1.

**E3 independent check:** Direct quantifier check: a predicate true on each candidate has no unique satisfying index when two inequivalent candidates remain.

**E4 domain/adversarial check:** Would be invalid as a refutation of the separate II-B physical m_p=1 host-selection proof; that conclusion uses another constructor.

**Direct registered condition uses:** `BH-IIF-A-0004`.

### BH-IIF-C-0005: Scalar-orientation inversion countermodel

**E1 source replay (251–280):** Simultaneous primitive e_t and e_E reversal preserves their evaluation and the symplectic pairing while retaining independent Hopf orientation. HS_t must be absent as stipulated.

**E3 independent check:** Exact matrix J invariance for diagonal(-1,-1) and lattice duality e_E(e_t)=1.

**E4 domain/adversarial check:** Reinstating the specifically removed HS_t sign bridge invalidates the proposed alternative; no objection to marked source.

**Direct registered condition uses:** `BH-IIF-A-0005`.

### BH-IIF-C-0006: Finite spectral algebra under injective reparametrization

**E1 source replay (283–305):** Lagrange interpolation on finite distinct spectral values gives polynomial g with g(f(H))=H. Both share spectral idempotents and hence the generated represented finite algebra.

**E3 independent check:** Exact independent interpolant for eigenvalues [-2,0,3] under f(t)=t²+1; g(f(H))=H while spectra differ.

**E4 domain/adversarial check:** Noninjective f merges eigenspaces and would invalidate the claim, but injectivity is explicit in the source.

**Direct registered condition uses:** `BH-IIF-A-0002`.

### BH-IIF-C-0007: Static-algebra selector boundary

**E1 source replay (308–329):** A selector receiving only the unmarked generated algebra cannot distinguish all injective spectral generator relabelings; the parent filtered grammar is expressly excluded from its input.

**E3 independent check:** The independent interpolant provides two different numerical generators of the same represented algebra; parent differential symbols are absent from the input type.

**E4 domain/adversarial check:** Adding Fil Op(P_R) or Q_R,m breaks the premise and may permit selection; such enriched selectors are not excluded.

**Direct registered condition uses:** `BH-IIF-A-0002`.

### BH-IIF-C-0008: GP1-TB sharpness: solenoid and weighted product torus

**E1 source replay (332–374):** p-solenoid is compact 1-dimensional but lacks local connectedness, therefore LR fails; product weighted torus is compact with dimension at least n for all n and coordinatewise shortest-arc paths have metric length d, hence LR with constant 1.

**E3 independent check:** Independent coordinatewise path-length equality for the summable product metric and monotonicity of dimension on closed T^n; solenoid arc component provides the disconnected-local-path witness.

**E4 domain/adversarial check:** Neither group is an in-domain finite FRC affine-operation parent. Using them to refute the conditional compact-Lie theorem would omit its finite affine port.

**Direct registered condition uses:** `BH-IIA-A-FD-LR-001`.

### BH-IIF-C-0009: Boundedness plus origin does not select a family member

**E1 source replay (377–394):** GP1 bounds and GP2 forbids arbitrary generated-origin marks; the premise explicitly denies any source-distinguished member or prior legitimate GP3 structural ordering.

**E3 independent check:** Direct two-candidate symmetry/indistinguishability control under identical role signature and GP1+GP2 predicates.

**E4 domain/adversarial check:** A separately licensed structural GP3 comparison would change the premise and is correctly retained as an escape clause.

**Direct registered condition uses:** `BH-IIF-A-0004`.

### BH-IIF-C-0010: Exact capacity of the admissible Paper-I-A module

**E1 source replay (397–444):** For optional P_sli integer-family cutoff n=floor x, sum of all (a+1)(b+1) at a+b<=2n gives binomial(2n+4,4); count of ordered weight pairs is binomial(2n+2,2). m_p<=s_rho with m_p=1 implies x>=1, not x<2.

**E3 independent check:** Independent enumeration n=0..12 plus generating-function identity (1-z)^(-4); 110 rational floor controls including half-integer ceiling boundary.

**E4 domain/adversarial check:** Numerical 15 is only consistency with upstream one-copy H1, not a proof of physical level selection. The 2Punit bound requires m_adm=1 rather than m_p=1.

**Direct registered condition uses:** `BH-IIF-A-0006`.

### BH-IIF-C-0011: GP2 zero-defect and exact/faithful filter scope

**E1 source replay (457–470):** Source II-A GP2 defines no-insertion, no-omission, type/relation/closure faithfulness; role existence E_R is already constituted and GP3 remains separate.

**E3 independent check:** Matched comparison against current II-A GP2 2898–2950 and exact defect definition 2849–2894.

**E4 domain/adversarial check:** Do not read GP2 as creation of E_R or as a blanket theorem-consequence constructor.

**Direct registered condition uses:** None introduced; source-level premises referenced through the existing canonical atlas.

### BH-IIF-C-0012: GP2 chronological origin and anti-self-selection

**E1 source replay (472–488):** Frozen input at a step may not include the result being selected; later candidate-private symmetries cannot retroactively create prior marks.

**E3 independent check:** Independent source order/role typing check against current GP2 clauses and complete Geo_R definition.

**E4 domain/adversarial check:** No distinct mathematical countermodel is claimed; it is a constitutional scope explanation.

**Direct registered condition uses:** None introduced; source-level premises referenced through the existing canonical atlas.

### BH-IIF-C-0013: GP2 local generated closure equals identity component

**E1 source replay (490–515):** Any Lie group has exp-neighborhood generating G0. The primitive Geo_R rule supplies connected local reapplications; independently generated discrete component role is excluded unless in frozen grammar.

**E3 independent check:** Independent O(2) check: exp(so2) generates SO(2)=O(2)^0 but no reflection, exactly matching theorem scope.

**E4 domain/adversarial check:** Taking a full unmarked automorphism group with discrete components as the primitive generated parent is an invalid scope substitution.

**Direct registered condition uses:** `BH-IIF-A-0007`.

### BH-IIF-C-0014: Candidate-internal and chronological infinitesimal retention

**E1 source replay (519–559):** The Lie bracket is extracted from the candidate group commutator, so it is candidate-internal generated content. FD+LR optionally establish the F norm by the later exact-rate theorem; cross-candidate preservation is restricted to already frozen diagrams.

**E3 independent check:** Independent bracket-vs-multiplication consistency and invariant intrinsic metric argument on compact Lie groups; the downstream rate proof 2503–2702 was inspected as an indispensable import. Bi-invariant geodetic metrics have a full tangent Finsler norm.

**E4 domain/adversarial check:** One cannot promote a candidate-specific bracket to a pre-GP3 frozen mark; this would violate the chronology premise.

**Direct registered condition uses:** `BH-IIA-A-FD-LR-001`.

### BH-IIF-C-0015: Exact scope of GP2 alone

**E1 source replay (561–593):** GP2 filters already constituted candidates; compactness uses GP1 FRC plus finite faithful affine port, FD/LR are optional, and physical B-test availability requires metric-curry closure.

**E3 independent check:** Cross-matched the GP2 postulate, finite affine-Lie theorem, metric profile separation identity sup_z|d(x,z)-d(y,z)|=d(x,y), and explicitly conditional E_R role.

**E4 domain/adversarial check:** GP2 alone is not claimed to prove Lie closure, GP3 least, global form or a physical B-test apparatus.

**Direct registered condition uses:** `BH-IIA-A-METRIC-CURRY-001`.

### BH-IIF-C-0016: Chronology before candidate self-data: T²/SU3 diagnostic

**E1 source replay (595–614):** T² and SU3 compact faithful actions show mere compactness/effectiveness cannot imply rank-one; comparisons to smaller role-preserving candidates are explicitly conditional on Geo_R not requiring omitted relations.

**E3 independent check:** Independent subgroup test T² has characters, SU3 has SU2 root subgroup; comparing whole marked presentations is not licensed.

**E4 domain/adversarial check:** A richer Geo_R making the extra toral/root direction essential blocks the comparison and is expressly excluded.

**Direct registered condition uses:** None introduced; source-level premises referenced through the existing canonical atlas.

## Assumption identity and downstream scope

Seven new *typed local condition records*, not seven new physical axioms, were source-located with first-known priority; reused GP2, GP1, finite regularity and metric-curry nodes were not cloned.
No new issue-origin node was established, so no new blocked downstream observable follows. The technical proof of the generic-net proposition supports the physical-firewall conclusion only under its stated metric point-resolution role. The no-cutoff proof is independent of the established II-B momentum-seed carrier selection.

## Specific next coverage boundary

Lines **618–9554** remain **NOT_AUDITED**. There are 223 formal non-proof environments in the full manuscript; additional unnamed calculations and two explicitly deferred proof owners in this batch mean 223 is not a final complete substantive denominator. Next slice starts at line 618, Supplementary compact-Lie and elliptic consequences.

## Validation and disclaimer

E0 ZIP/JSON/hash/readback checks certify artifact integrity only; they are not E3 mathematical verification. No TeX, macros, bibliography, PDFs or prior audit reports were modified. Prior atlas claims and gap histories are preserved without global status upgrades.

---

## Batch 3 result and issues (v1.61 source lines 1619–2893)
Batch 3 audited **32 formal declarations** plus four ancillary source-scope paragraphs. **No newly confirmed mathematical defect** was established. The existing Paper II-A universal finite-port conditional frontier `BH-IIA-A-PORT-001` remains open at its original origin and was not adjudicated closed by this audit.
An index/condition-scope correction is now encoded: the source-defined FD and LR components from `p2:def:lie-regularity-conditions` are separate nodes in a single AND group, so the LR-only local-connectedness result does not spuriously inherit FD. This is DAG-only source-scope bookkeeping, **not** a counterexample to the manuscript.
**Independent exact controls:** 4,630/4,630 distinct controls passed (Riemannian Lie curvature, scalar spectra and counting, projective quotient, spin cohomology, nonrectifiable snowflakes, compression defects, and Schur transport). A finite test suite is not an independent proof of Montgomery–Zippin or Berestovskii.
**Conditional scope:** the source does not select a radius or metric scale, a finite spectral cutoff/physical carrier unless licensed, a universal group propagation speed, a spatial time orientation, or physical descent of unlicensed compressions. Optional FD/LR does not enter the source GP3 least-role allocation.
### Batch 3 claim census and verdicts
| Claim ID | Lines | Source formal result | Verdict |
|---|---:|---|---|
| `BH-IIF-C-0042` | 1619–1652 | Bi-invariant geodesic, curvature, and symmetric-space closure (`p2:thm:bi-invariant-global-symmetry`) | VERIFIED-CONDITIONAL |
| `BH-IIF-C-0043` | 1697–1719 | Equivalent intrinsic formulations of operational rank one (`p2:thm:rank-one-equivalence-package`) | VERIFIED-CONDITIONAL |
| `BH-IIF-C-0044` | 1743–1760 | Actual metric isotropy after operational rank one (`p2:thm:rank-one-actual-isotropy`) | VERIFIED-CONDITIONAL |
| `BH-IIF-C-0045` | 1776–1799 | Rank-one space forms and Einstein curvature (`p2:thm:rank-one-space-form-einstein`) | VERIFIED-CONDITIONAL |
| `BH-IIF-C-0046` | 1820–1840 | Exact automorphism and metric-isometry groups (`p2:thm:rank-one-exact-symmetry-groups`) | VERIFIED |
| `BH-IIF-C-0047` | 1861–1881 | Complete topology and spin-admissibility of the rank-one list (`p2:thm:rank-one-topology-spin`) | VERIFIED |
| `BH-IIF-C-0048` | 1897–1914 | Global geodesic periods, radii, and cut loci (`p2:thm:rank-one-geodesic-cut-locus`) | VERIFIED |
| `BH-IIF-C-0049` | 1930–1946 | Generated Cartan orientation on the nonabelian branch (`p2:thm:rank-one-cartan-orientation`) | VERIFIED |
| `BH-IIF-C-0050` | 1960–1992 | Rank-one irreducibles, scalar spectra, and central descent (`p2:thm:rank-one-representation-descent`) | VERIFIED |
| `BH-IIF-C-0051` | 2006–2041 | Exact scalar spectral counting functions (`p2:cor:rank-one-scalar-spectral-counting`) | VERIFIED |
| `BH-IIF-C-0052` | 2063–2072 | No canonical maximal torus on a nonabelian rank-one parent (`p2:thm:no-canonical-maximal-torus`) | VERIFIED |
| `BH-IIF-C-0053` | 2084–2093 | Rank-one flow periodicity (`p2:thm:rank-one-flow-periodicity`) | VERIFIED |
| `BH-IIF-C-0054` | 2104–2125 | Exhaustion of natural scalar polynomial invariants (`p2:thm:quadratic-invariant-exhaustion`) | VERIFIED |
| `BH-IIF-C-0055` | 2141–2162 | Operational resolution-growth dimension (`p2:thm:resolution-growth-dimension`) | VERIFIED |
| `BH-IIF-C-0056` | 2177–2215 | Sharp closure frontier of the compact-role chain (`p2:thm:gp-independence-frontier`) | VERIFIED-CONDITIONAL |
| `BH-IIF-C-0057` | 2278–2290 | Finite spectral realization follows after parent allocation (`p2:cor:dependency-complete-spectral-realization`) | VERIFIED-CONDITIONAL |
| `BH-IIF-C-0058` | 2314–2327 | Operation paths and realization length (`p2:def:generated-operation-path`) | FORMALIZED |
| `BH-IIF-C-0059` | 2329–2344 | Local rectifiable reachability (`p2:def:local-rectifiable-reachability`) | FORMALIZED |
| `BH-IIF-C-0060` | 2346–2351 | Local rectifiable reachability derives local connectedness (`p2:thm:gp1-reachability-local-connectedness`) | VERIFIED-CONDITIONAL |
| `BH-IIF-C-0061` | 2399–2421 | Polynomial packing is a sufficient criterion for (FD) (`p2:thm:gp1-capacity-finite-dimension`) | VERIFIED-CONDITIONAL |
| `BH-IIF-C-0062` | 2456–2472 | (FD)+(LR) regularize an abstract compact parent comparison (`p2:thm:finite-mode-lie-regularity`) | VERIFIED-CONDITIONAL |
| `BH-IIF-C-0063` | 2486–2491 | No small subgroups is a theorem (`p2:cor:nss-derived`) | VERIFIED-CONDITIONAL |
| `BH-IIF-C-0064` | 2504–2523 | Structure of the first-order rate (`p2:lem:rate-seminorm`) | VERIFIED-CONDITIONAL |
| `BH-IIF-C-0065` | 2572–2594 | Untimed first-order group rate follows from (FD)+(LR) (`p2:thm:gp1-propagation-derived`) | VERIFIED-CONDITIONAL |
| `BH-IIF-C-0066` | 2669–2678 | Uniform local linear operation-rate bound (`p2:lem:second-kind-uniform-propagation`) | VERIFIED-CONDITIONAL |
| `BH-IIF-C-0067` | 2687–2697 | The first-order displacement norm (`p2:cor:gp1-first-order-norm-derived`) | VERIFIED-CONDITIONAL |
| `BH-IIF-C-0068` | 2705–2723 | Sharp small-scale capacity exponent (`p2:cor:gp1-capacity-saturation`) | VERIFIED-CONDITIONAL |
| `BH-IIF-C-0069` | 2745–2755 | Operational norm derives a canonical quadratic comparison (`p2:thm:operational-john-metric`) | VERIFIED-CONDITIONAL |
| `BH-IIF-C-0070` | 2786–2808 | Natural functional coefficients and licensed sum constraints (`p2a:lem:repair-natural-functional-coefficients`) | VERIFIED |
| `BH-IIF-C-0071` | 2810–2827 | Operator graph descent, restriction, and compression (`p2a:lem:repair-operator-graph-descent`) | VERIFIED |
| `BH-IIF-C-0072` | 2829–2854 | Restricted functional calculus and the compression defect (`p2a:lem:repair-restricted-trace`) | VERIFIED |
| `BH-IIF-C-0073` | 2856–2889 | Nonlinear Hessian and stationary Schur transport (`p2a:lem:repair-hessian-schur-transport`) | VERIFIED |

### Source-bound correctness certificates (E1, E3, E4)

#### BH-IIF-C-0042 — Bi-invariant geodesic, curvature, and symmetric-space closure
**E1 source replay (1619–1652):** Koszul with Ad-invariance gives nabla_XY=[X,Y]/2; two commutator applications give R(X,Y)Z=-[[X,Y],Z]/4. Curvature trace is -B/4; inversion composed with translations yields s_h, so nabla R=0 and geodesic completeness.
**E3 independent verification:** Independent exact cross-product su2 curvature and Bianchi tests; trace ad_X^2<0 on noncentral compact semisimple ideals. Matrix Lie form of exp confirms complete one-parameter geodesics.
**E4 adversarial domain check:** Do not apply Riemannian formulas to a merely compact metric comparison without a retained bi-invariant smooth metric. Flat central tangent directions are not strictly positive Ricci.
**Exact source import labels:** none; self-contained finite/smooth calculation.  
**Canonical route conditions:** none directly; source-domain predicates still apply.

#### BH-IIF-C-0043 — Equivalent intrinsic formulations of operational rank one
**E1 source replay (1697–1719):** Commuting Lie algebra elements lie in toral subalgebras; maximal torus rank 1 iff commuting pairs are dependent. Dense irrational T2 slopes break universal periodicity. Curvature formula supplies equivalence with positive sectional curvature, and compact rank-one classification supplies Ad transitivity in optional F domain.
**E3 independent verification:** For u1 all nonzero Lie vectors have a discrete exp kernel; for su2 the centralizer of X≠0 is its real span, the adjoint image SO3 is unit-sphere transitive; for T2 independent commuting vectors and irrational flow give explicit negations.
**E4 adversarial domain check:** The sign-enhanced Ad isotropy clause (iv) requires the independently finite first-order norm F, not merely a smooth Ad metric. Do not infer metric scale or a chosen axis from equivalent rank-one statements.
**Exact source import labels:** `p2:thm:one-parameter-operation-closure`, `p2:thm:bi-invariant-global-symmetry`.  
**Canonical route conditions:** none directly; source-domain predicates still apply.

#### BH-IIF-C-0044 — Actual metric isotropy after operational rank one
**E1 source replay (1743–1760):** Lie rank-one global forms U1/SU2/SO3, and metric g_rk. Conjugation acts at identity by full SO3 on su2, inversion by -I, so stabilizer contains full O3; for U1 inversion exchanges tangent directions. Translation transports point stabilizers.
**E3 independent verification:** Explicit SO3×{-I} action is O3, and left translations are transitive; no reliance on external spatial isotropy assumption.
**E4 adversarial domain check:** The quadratic norm alone does not force isotropy for a general group; the actual global conjugation and inversion isometries are essential.
**Exact source import labels:** `p2:thm:regular-homogeneity-closure`, `p2:thm:left-right-isometry-action`, `p2:thm:rank-one-equivalence-package`.  
**Canonical route conditions:** none directly; source-domain predicates still apply.

#### BH-IIF-C-0045 — Rank-one space forms and Einstein curvature
**E1 source replay (1776–1799):** Unique Ad invariant positive form on su2 up to scale produces K=|lambda|²/4; completeness and simple connectivity identify SU2 as round S3(R); central antipodal quotient gives SO3=RP3(R). Contract constant curvature to Ric=2R^-2 g, Scal=6R^-2.
**E3 independent verification:** Cross-product orthonormal model with [X,Y]=2 X×Y/R reproduces constant sectional curvature 1/R² and Ric scalar. Cover by ±1 preserves local curvature and not global topology.
**E4 adversarial domain check:** Only the quotient comparison, not an independently GP2 allocated new parent, is SO3. Radius remains free; local Ricci cannot detect covering form.
**Exact source import labels:** `p2:thm:bi-invariant-global-symmetry`, `p2:thm:rank-one-equivalence-package`.  
**Canonical route conditions:** none directly; source-domain predicates still apply.

#### BH-IIF-C-0046 — Exact automorphism and metric-isometry groups
**E1 source replay (1820–1840):** Aut U1=±1, Aut SU2=Aut SO3=SO3. Round sphere Isom(S3)=O4 and Isom0=SO4; antipodal quotient Isom(RP3)=O4/{±I}, identity SO4/{±I}≅SO3×SO3; circle O2.
**E3 independent verification:** Independent double-cover Spin4→SO4 and quotient kernel ±I computation; isotropy of projective line has O3, bracket-preserving tangent SO3.
**E4 adversarial domain check:** Do not confuse automorphisms of group multiplication with general metric isometries, or mistake SO4×SO4 for the quotient.
**Exact source import labels:** `p2:thm:rank-one-space-form-einstein`.  
**Canonical route conditions:** none directly; source-domain predicates still apply.

#### BH-IIF-C-0047 — Complete topology and spin-admissibility of the rank-one list
**E1 source replay (1861–1881):** Cellular boundary of RP3 gives H0=H3=Z,H2=Z2 (cohomological grading), H1=0; S1 and S3 usual cohomology; left invariant frames imply spin existence; H1(-;Z2) torsor yields spin-structure counts 2,1,2.
**E3 independent verification:** Independent RP3 cellular boundary d2=2 and UCT, plus Hom(pi1,Z2) count. SU2 simply connected admits exactly one spin structure.
**E4 adversarial domain check:** Do not mistake Z2 integral H^2 torsion for integral H^1, and existence/count of spin structures for a canonical physical selection.
**Exact source import labels:** `p2:thm:parallelism-topology-closure`, `p2:thm:rank-one-space-form-einstein`.  
**Canonical route conditions:** none directly; source-domain predicates still apply.

#### BH-IIF-C-0048 — Global geodesic periods, radii, and cut loci
**E1 source replay (1897–1914):** Geodesics on S1(r) and S3(R) close after 2π radius, with antipodal cut points and inj=diam=π radius. On RP3 quotient, antipodal identification halves geodesic period and radial distance, with first cut locus RP2.
**E3 independent verification:** Independent unit quaternion great-circle formula exp(tX), quotient by q≈-q and angle minimization min(theta,π-theta) reproduces πR and πR/2 radii.
**E4 adversarial domain check:** S1 antipodal cut point is not a conjugate point; SO3 half-period is based on the quotient metric with the same cover radius, not the rotational angle convention.
**Exact source import labels:** `p2:thm:rank-one-space-form-einstein`.  
**Canonical route conditions:** none directly; source-domain predicates still apply.

#### BH-IIF-C-0049 — Generated Cartan orientation on the nonabelian branch
**E1 source replay (1930–1946):** Cartan three-form η(X,Y,Z)=g(X,[Y,Z]) is alternating by Ad invariance and closed by Jacobi (or 3D degree), nonzero for su2 and proportional to volume; Aut preserves bracket and metric, inversion maps η to -η.
**E3 independent verification:** Direct oriented su2 frame with bracket cross-product computes η(e1,e2,e3) nonzero and sign det(-I3)=-1; exact determinant controls.
**E4 adversarial domain check:** The canonical mathematical multiplication orientation is not a time orientation or selected external spatial frame. Inversion is an anti-automorphism, not operation automorphism.
**Exact source import labels:** `p2:thm:rank-one-space-form-einstein`.  
**Canonical route conditions:** none directly; source-domain predicates still apply.

#### BH-IIF-C-0050 — Rank-one irreducibles, scalar spectra, and central descent
**E1 source replay (1960–1992):** U1 characters n∈Z and circle Laplacian n²/r². SU2 irreps Vj have dim 2j+1; Peter-Weyl matrix coefficients give multiplicity (2j+1)² and eigenvalue ell(ell+2)/R². Central element -1 acts (-1)^ell, hence SO3 scalar modes are even ell.
**E3 independent verification:** Independent exact polynomial harmonics on S3 and antipodal parity: homogeneous degree ell functions change by (-1)^ell; enumerated eigenvalue multiplicities and central-even descent.
**E4 adversarial domain check:** The scalar L2 spectrum is not the fixed finite Paper I-A momentum module, and descent is not an independent GP2 globalization selector or a physical spin-sector choice.
**Exact source import labels:** `p2:thm:peter-weyl-complete-reducibility`, `p2:thm:rank-one-space-form-einstein`.  
**Canonical route conditions:** none directly; source-domain predicates still apply.

#### BH-IIF-C-0051 — Exact scalar spectral counting functions
**E1 source replay (2006–2041):** Solve n²≤r²Λ; ell(ell+2)≤R²Λ and even ell=2k bounds. Summing (ell+1)² or (2k+1)² yields the displayed cubic polynomials and first positive eigenvalues 1,3,8 in radius units.
**E3 independent verification:** Direct integer threshold enumeration across 340 eigenvalue windows for SU2/SO3 and 210 distinct circle windows; no floating floor approximations.
**E4 adversarial domain check:** Do not confuse eigenvalue counting with H_m module dimension or retain SO3 odd ell. Exact cutoff edge cases use non-strict ≤.
**Exact source import labels:** `p2:thm:rank-one-representation-descent`.  
**Canonical route conditions:** none directly; source-domain predicates still apply.

#### BH-IIF-C-0052 — No canonical maximal torus on a nonabelian rank-one parent
**E1 source replay (2063–2072):** All maximal tori of SU2/SO3 are conjugate; their Lie algebras correspond to axes in su2 modulo sign. Inner automorphisms rotate axes, so no single torus is invariant under all automorphisms.
**E3 independent verification:** Independent conjugation orbit of a noncentral su2 generator is a 2-sphere; the axis-orbit is RP2 with infinitely many elements.
**E4 adversarial domain check:** No canonical torus does not forbid a separately chosen, marked, generated Hopf axis or an unmarked family of all circles.
**Exact source import labels:** `p2:thm:maximal-torus-exponential`.  
**Canonical route conditions:** none directly; source-domain predicates still apply.

#### BH-IIF-C-0053 — Rank-one flow periodicity
**E1 source replay (2084–2093):** Every flow in rank-one form lies in a maximal circle and is exp(tX), trivial at X=0; every nonzero homomorphism R→circle has discrete nonzero kernel, hence periodic.
**E3 independent verification:** Explicit U1 and diagonal SU2 torus cocharacter calculations show positive period; SO3 period shortens under central quotient for fixed norm.
**E4 adversarial domain check:** Universal periodicity fails in rank≥2 tori with irrational flow. Period and flow parameter orientation are not fixed by the primitive axioms.
**Exact source import labels:** `p2:thm:one-parameter-operation-closure`.  
**Canonical route conditions:** none directly; source-domain predicates still apply.

#### BH-IIF-C-0054 — Exhaustion of natural scalar polynomial invariants
**E1 source replay (2104–2125):** O1 invariance on 1D forces polynomials in X². Ad SU2=SO3 invariance on R3 forces polynomials in |X|². The center of U(su2_C) is polynomial in Casimir, while U(u1) is polynomial in its generator but inversion restricts to even subalgebra.
**E3 independent verification:** Independent radial-polynomial restriction argument on 1D and R3; Casimir acts as degree-two generator. No additional odd invariant under the full specified symmetry.
**E4 adversarial domain check:** Bi-invariance alone on U1 would allow an odd first derivative; source explicitly requires constituted inversion/reflection. Polynomial result says nothing about energy identification.
**Exact source import labels:** `p2:thm:rank-one-exact-symmetry-groups`.  
**Canonical route conditions:** none directly; source-domain predicates still apply.

#### BH-IIF-C-0055 — Operational resolution-growth dimension
**E1 source replay (2141–2162):** Uniform small-ball volume bounds c ε^d≤vol B≤C ε^d on compact Riemannian d-manifold; maximal separated sets yield upper from disjoint ε/2-balls and lower from covering ε-balls. d=1 or 3 follows group classification.
**E3 independent verification:** Independent Euclidean ball-cover exponent and circle finite net controls; bilipschitz local manifold charts preserve packing exponent.
**E4 adversarial domain check:** Asymptotic exponent not a fixed packing constant or physical spectral level; requires metric g_rk rather than arbitrary snowflaked comparison.
**Exact source import labels:** `p2:thm:rank-one-space-form-einstein`.  
**Canonical route conditions:** none directly; source-domain predicates still apply.

#### BH-IIF-C-0056 — Sharp closure frontier of the compact-role chain
**E1 source replay (2177–2215):** Higher T2 and SU3 are candidatewise faithful complete nonleast models; imported master allocation and relation-minimal globalization give least rank-one local roles plus source SU2, contingent on Geo_R and branch grammar. Center-odd character is diagnostic; d_K^α snowflake gives exact operation but metric not proportional to Killing.
**E3 independent verification:** Independent snowflake d^α metric for 0<α<1 preserves topology/bi-invariance but ratio d^α/d=d^(α-1)→∞. Higher rank Lie examples demonstrate GP3 selection is logically distinct from compactness and GP2.
**E4 adversarial domain check:** Do not claim all admissible candidate parent closures have faithful affine ports: upstream BH-IIA-A-PORT-001 remains a conditional/unresolved universal port. Endpoint theorem has independent bypass; preserve explicit richer-Geo_R abstention.
**Exact source import labels:** `p2:thm:master-compact-role-allocation`, `p2:thm:relation-minimal-globalization`, `p2:thm:primitive-endpoint-lift-reachability`, `p2:lem:relation-exact-endpoint-models`, `p2:prop:admissible-globalization-operator`.  
**Canonical route conditions:** none directly; source-domain predicates still apply.

#### BH-IIF-C-0057 — Finite spectral realization follows after parent allocation
**E1 source replay (2278–2290):** Given allocated closed smooth compact parent and frozen grammar constituting a positive-order elliptic nonnegative operator, projection/subspace and FRC-b finite spectral window as physical scope, compact-resolvent theorem implies finite rank. Nothing fixes Λ or tower level.
**E3 independent verification:** Independent elliptic torus -Δ Fourier lattice has finite disk of eigenmodes below Λ; nonelliptic -∂x² on T2 has infinite degeneracies, confirming need for ellipticity.
**E4 adversarial domain check:** Mathematical finite spectral subspace is not automatically physical: the role-grammar occurrence and license are explicit. Do not treat the spectral bound as selected.
**Exact source import labels:** `p2:thm:gp1-bounded-spectrum-finite-carrier`, `p2:cor:gp1-boundedness-no-scale`.  
**Canonical route conditions:** `BH-IIF-A-0012`.

#### BH-IIF-C-0058 — Operation paths and realization length
**E1 source replay (2314–2327):** A continuous [0,1]→G curve is assigned metric length as supremum over partitions; bi-invariance preserves path length under left/right translations, with no physical time parameter.
**E3 independent verification:** Independent metric length definition and constant-translation invariance for finite metric groups and compact Lie paths.
**E4 adversarial domain check:** Path parameter is auxiliary; continuity alone does not imply finite length or a physical propagation rate.
**Exact source import labels:** `p2:thm:gp1-bounded-isometry-closure`.  
**Canonical route conditions:** none directly; source-domain predicates still apply.

#### BH-IIF-C-0059 — Local rectifiable reachability
**E1 source replay (2329–2344):** Explicit (LR) predicate requires a uniform C_R and κ for all nearby group points and completed-closure paths with length≤C_R D∞(g,e); D_X is the source comparison diameter.
**E3 independent verification:** Independent variable-scope inspection checks constants uniform in g and that paths live in completed G.
**E4 adversarial domain check:** Do not assume LR follows from GP1 total boundedness or from rectifiability in the nonclosed forward monoid.
**Exact source import labels:** `p2:def:intrinsic-operational-boundedness`, `p2:def:generated-operation-path`.  
**Canonical route conditions:** none directly; source-domain predicates still apply.

#### BH-IIF-C-0060 — Local rectifiable reachability derives local connectedness
**E1 source replay (2346–2351):** Define U_r of endpoints of identity paths of length<r; LR yields B_(r/C_R)⊂U_r⊂B_r. Prefixes and concatenation give path connectedness, LR at g^-1h shows U_r open; translations yield local path connectedness and open G0 of finite index.
**E3 independent verification:** Independent local quasi-convexity construction: any small D∞ ball has path-connected neighborhood trapped in a prescribed larger ball, and compactness turns open-component coset quotient finite.
**E4 adversarial domain check:** Requires uniform LR for completed G and bi-invariant D∞; path connectivity alone without local uniform length bound does not make U_r open.
**Exact source import labels:** `p2:def:local-rectifiable-reachability`.  
**Canonical route conditions:** `BH-IIA-A-LR-001`.

#### BH-IIF-C-0061 — Polynomial packing is a sufficient criterion for (FD)
**E1 source replay (2399–2421):** N_Y(ε)≤C ε^-n gives vanishing s-Hausdorff content for s>n from covering by ε-balls, hence dim_H≤n. Szpilrajn comparison bounds covering dimension. Perturb separated points of X into dense completed Xhat at ε/3 to transfer capacity exponent.
**E3 independent verification:** Independent finite-net perturbation inequality and power-law Hausdorff content scaling; topological dimension of a compact metric group never exceeds its Hausdorff dimension.
**E4 adversarial domain check:** Packing is an extra sufficient hypothesis, not GP1 or FRC; n need not be integer or optimal. No dimensional bound is inferred from total boundedness alone.
**Exact source import labels:** `p2:thm:gp1-bounded-isometry-closure`.  
**Canonical route conditions:** `BH-IIF-A-0013`.

#### BH-IIF-C-0062 — (FD)+(LR) regularize an abstract compact parent comparison
**E1 source replay (2456–2472):** Compact G from GP1, local path connectivity from LR, finite covering dimension FD. Montgomery-Zippin finite-dimensional locally compact locally connected group theorem makes G Lie; compact Peter-Weyl gives faithful finite unitary representation.
**E3 independent verification:** Independent check of theorem assumptions against G: compact metrizable implies locally compact and second countable; local connectedness excludes solenoid and disconnected p-adic limit countermodels. Compact Lie matrix image closed.
**E4 adversarial domain check:** Never infer a finite-dimensional matrix action of the entire untyped compact parent from GP1 alone; this proof is only the optional FD+LR branch, separate from source FRC finite-port route.
**Exact source import labels:** `p2:thm:gp1-bounded-isometry-closure`, `p2:thm:gp1-reachability-local-connectedness`.  
**Canonical route conditions:** `BH-IIA-A-FD-001`.

#### BH-IIF-C-0063 — No small subgroups is a theorem
**E1 source replay (2486–2491):** Local exp injectivity on B_2r: a subgroup inside exp(B_r) with nontrivial h=exp W forces an integer power exp((k+1)W) outside exp(B_r) while lying in exp(B_2r), contradicting injectivity.
**E3 independent verification:** Independent one-parameter torus control and general Lie exponential chart proof; source theorem needs only established Lie structure, not an extra NSS assumption.
**E4 adversarial domain check:** The conclusion is not a theorem for all compact topological groups (e.g., product of finite cyclic groups); it inherits the Lie domain.
**Exact source import labels:** `p2:thm:finite-mode-lie-regularity`.  
**Canonical route conditions:** none directly; source-domain predicates still apply.

#### BH-IIF-C-0064 — Structure of the first-order rate
**E1 source replay (2504–2523):** For continuous subadditive f_W(t)=D∞(exp tW,e), repeated subdivision gives limsup near zero equal sup f(t)/t; Euclidean division t with remainder plus continuity at zero gives matching liminf. Lie product formula gives triangle inequality in W; bi-invariance gives Ad invariance; nontrivial exp flow yields r(W)>0. S finite-rate subspace Ad-invariant hence ideal.
**E3 independent verification:** Independent Fekete-at-small-scale derivation using f_W(s)≤m f_W(t)+f_W(rem) with fixed s, and cross-product/Lie group subadditivity. Positivity uses existence of t0 with exp(t0W)≠e.
**E4 adversarial domain check:** May be infinite off S, so calling r an everywhere finite norm before LR would overstate. Continuity, exact Lie one-parameter groups, and bi-invariant D∞ are indispensable.
**Exact source import labels:** `p2:thm:finite-mode-lie-regularity`.  
**Canonical route conditions:** none directly; source-domain predicates still apply.

#### BH-IIF-C-0065 — Untimed first-order group rate follows from (FD)+(LR)
**E1 source replay (2572–2594):** LR makes intrinsic completed length metric D_ell finite and locally bilipschitz to D∞ on G0. Berestovskii classifies connected intrinsic Lie metrics as sub-Finsler; bi-invariance makes horizontal subspace Ad-invariant ideal; bracket generation forces full tangent, yielding Finsler D_F. Comparing D∞ lengths of exp(tW) with Finsler tangent norm identifies F0=r.
**E3 independent verification:** Independent bi-invariant sub-Finsler no-proper-ideal argument, metric-length tangent calculation, and explicit snowflake divergence control. External Berestovskii theorem checked in its connected Lie, intrinsic-geodesic domain.
**E4 adversarial domain check:** Does not provide a clock or physical speed ceiling; finite rate is relative to arbitrary path parameter. G0 only, not unconditional global Finsler across disconnected G.
**Exact source import labels:** `p2:def:generated-operation-path`, `p2:def:local-rectifiable-reachability`, `p2:lem:rate-seminorm`.  
**Canonical route conditions:** none directly; source-domain predicates still apply.

#### BH-IIF-C-0066 — Uniform local linear operation-rate bound
**E1 source replay (2669–2678):** D∞≤D_F and finite-dimensional equivalence of norms with the Finsler r norm; exp curve has length≤r(W), giving uniform local D∞(exp W,e)≤C||W||.
**E3 independent verification:** Independent equivalence of any two norms on compact finite-dimensional unit sphere, followed by exponential curve path length.
**E4 adversarial domain check:** Without FD+LR or established finite r, a snowflaked group metric need not obey a linear-in-W bound.
**Exact source import labels:** `p2:thm:gp1-propagation-derived`.  
**Canonical route conditions:** none directly; source-domain predicates still apply.

#### BH-IIF-C-0067 — The first-order displacement norm
**E1 source replay (2687–2697):** Lemma rate-seminorm supplies existence, supremum, homogeneity, triangle inequality, Ad invariance and positivity; propagation theorem supplies finite value in every Lie direction.
**E3 independent verification:** Independent reduction F=r to limit of displacement along exponential one-parameter group and finite Finsler tangent norm.
**E4 adversarial domain check:** GP1 alone does not establish finite rate; retain optional FD+LR in exact proof-route ancestry.
**Exact source import labels:** `p2:lem:rate-seminorm`, `p2:thm:gp1-propagation-derived`.  
**Canonical route conditions:** none directly; source-domain predicates still apply.

#### BH-IIF-C-0068 — Sharp small-scale capacity exponent
**E1 source replay (2705–2723):** Local D∞-D_F bi-Lipschitz equivalence makes small Haar-measure balls scale as ε^q; disjoint/covering ball arguments bound packing. Open G0 finite index scales only constants; q=0 yields finite group and eventual stable packing.
**E3 independent verification:** Independent Euclidean/Finsler local ball volume calculation and discrete q=0 case; exponent equals finite Lie dimension without selecting packing constants.
**E4 adversarial domain check:** If no full-dimensional Finsler metric or local bi-Lipschitz comparison, packing dimension can differ from topological dimension; do not weaken hypotheses.
**Exact source import labels:** `p2:thm:gp1-propagation-derived`.  
**Canonical route conditions:** none directly; source-domain predicates still apply.

#### BH-IIF-C-0069 — Operational norm derives a canonical quadratic comparison
**E1 source replay (2745–2755):** Finite Ad(G)-invariant norm has compact centrally symmetric convex unit ball. Unique maximum-volume John ellipsoid is centered at zero; its uniqueness and volume-density rescaling invariance give functorial linear isometry and Ad(G) invariance; translates give bi-invariant quadratic metric.
**E3 independent verification:** Independent convex-body affine-equivariance of maximal ellipsoid, with example l∞ unit square whose unique maximal inscribed Euclidean disk is symmetry-invariant.
**E4 adversarial domain check:** A canonical quadratic comparison does not identify primitive D∞ with g_F distance or choose a Killing radius. For zero-dimensional Lie algebra metric is the trivial case.
**Exact source import labels:** `p2:cor:gp1-first-order-norm-derived`.  
**Canonical route conditions:** none directly; source-domain predicates still apply.

#### BH-IIF-C-0070 — Natural functional coefficients and licensed sum constraints
**E1 source replay (2786–2808):** Every unitary-conjugation-invariant complex-linear End(H) functional is c_H Tr via trace pairing and scalar commutant. Independently arbitrary blocks in a licensed sum force c_K=c_H=c_J; normalization on C propagates only along connected licensed-sum class.
**E3 independent verification:** Independent matrix-unit conjugation and rank-one projections establish a single coefficient; Trace(H)/dim(H) supplies a disconnected normalized-class countermodel.
**E4 adversarial domain check:** No coefficient for disconnected carrier class can be asserted 1 without a licensed chain. Tensor multiplicativity alone does not replace sum compatibility.
**Exact source import labels:** none; self-contained finite/smooth calculation.  
**Canonical route conditions:** `BH-IIF-A-0014`.

#### BH-IIF-C-0071 — Operator graph descent, restriction, and compression
**E1 source replay (2810–2827):** qA=bar A q defined on D is representative-independent iff A ker q⊆ker q; for orthogonal P, invariance of E requires QAP=0, quotient descent via P requires PAQ=0, and A=A* makes these equivalent with [A,P]=0.
**E3 independent verification:** Independent exact random block-matrix checks identify upper-right vs lower-left obstruction and exhibit distinct restriction/compression behaviours.
**E4 adversarial domain check:** Do not equate compression PAP on E to restriction or physical descended operator without a separately licensed word.
**Exact source import labels:** none; self-contained finite/smooth calculation.  
**Canonical route conditions:** none directly; source-domain predicates still apply.

#### BH-IIF-C-0072 — Restricted functional calculus and the compression defect
**E1 source replay (2829–2854):** For [A,P]=0 finite-spectrum polynomial interpolation yields F(PAP)=PF(A)P on E and trace identity. Without it PA²P-(PAP)²=PAQAP=(QAP)*QAP positive semidefinite; zero trace iff QAP=0 for self-adjoint A.
**E3 independent verification:** Independent exact self-adjoint block-matrix Gram identity, positive trace and iff-commutator tests, including noncommuting examples.
**E4 adversarial domain check:** The equality fails generally for noncommuting compression, even if the compressed eigenvalues lie in a related numerical range; retained P insertion matters.
**Exact source import labels:** `p2a:lem:repair-operator-graph-descent`.  
**Canonical route conditions:** none directly; source-domain predicates still apply.

#### BH-IIF-C-0073 — Nonlinear Hessian and stationary Schur transport
**E1 source replay (2856–2889):** Second-derivative chain rule has dS(D²f) term; symmetry stationarity implies Hessian tangent radical only at full stationary point. Interior stationary y-branch with invertible Hyy gives the Schur complement; singular symmetric C admits all x stationary elimination iff cross block annihilates ker C.
**E3 independent verification:** Independent exact polynomial chain-rule and rational Schur energy calculations; solvability of Cy=-B^T x for every x equivalent to B ker C=0.
**E4 adversarial domain check:** Second derivative is coordinate-dependent absent specified C² coordinates/connection; source states coordinate domain. No stationary elimination at rank-changing or boundary points without extra conditions.
**Exact source import labels:** none; self-contained finite/smooth calculation.  
**Canonical route conditions:** none directly; source-domain predicates still apply.

### Batch 3 issue and dependency adjudication
- **New confirmed mathematical errors / missing proof:** 0; no new `BH-G` issue ID was certified in this bounded batch.
- **DAG-only scope correction:** original upstream FD and LR definitions now have separate first-origin canonical components; `BH-IIA-A-FD-LR-001` remains the AND conjunction. The use route `BH-IIF-C-0060` (LR→local connectedness) only requires `BH-IIA-A-LR-001`. This is not a new foundational principle.
- **Inherited upstream verification frontier:** `BH-IIA-A-PORT-001` remains at Paper II-A, not duplicated as a new issue and not treated as proof of universal faithful finite-state parent representations. The master GP3 endpoint route is distinct.
- **Explicit conditional frontier:** physical finite spectral carrier needs `BH-IIF-A-0012`; stronger polynomial packing is `BH-IIF-A-0013`; licensed independent sum compatibility is `BH-IIF-A-0014`; none is asserted as a new physical axiom or unconditionally discharged.
- **No new cross-paper verification status promotions:** only exact imported clauses have been checked; inherited global statuses retained, later II-F lines 2894–9555 remain NOT_AUDITED.

### Reproducible supporting exact controls
`Proofs/Paper2F-Batch3-v1_1-verify.py` generated `DAG/AuditLayer/Paper2F-v1_3/ExactCheckResults-Batch3.json`: 4,630 exact checks, all PASS, across 21 named categories. Checks are neither a substitute for proof nor a physical reconstruction.

**Next batch:** Current source line 2894, beginning the optional momentum towers/finite supports section.

---

## Batch 4 result and issues (v1.61 source lines 2894–4727)
**50 new formal source environments audited**: 13 `VERIFIED`, 20 `VERIFIED-CONDITIONAL`, 17 `FORMALIZED`. Two remarks are unlabelled in the source and have honest local line anchors, not invented theorem labels. **No new confirmed mathematical defects** (`BH-G` IDs) were established. These are bounded source-claim verdicts, not complete verification of 9,555 lines.
**Independent exact controls:** 2,607 / 2,607 PASS. Controls include exact 15×15 pair operators, Clifford brackets, double-commutator defect, Hopf charge/weight arithmetic, tower support, component floors, quotient descent and Gram kernels. Finite exact examples do not prove general compact-Lie/spin or physical occurrence claims.
**Scoped frontier:** C_PI, Bose port, P_sli, P_lvl, COORD, Pceil, exceptional 2T action, deck quotients, complete generated source spans, and whole-signature GP3 multiplicity comparison are optional role conditions, not new constitutional axioms. Earlier `BH-IIA-A-PORT-001` persists, not re-adjudicated.
### Batch 4 claim census and verdicts
| Claim ID | Lines | Source formal result / label | Verdict |
|---|---:|---|---|
| `BH-IIF-C-0074` | 2905–2955 | Exact phase-qualified pair presentation (`p2b:prop:v2174-geometric-pair-presentation`) | VERIFIED-CONDITIONAL |
| `BH-IIF-C-0075` | 2965–2986 | The native geometric grading fails the linear port identity (`p2b:prop:v2174-geometric-linear-port-defect`) | VERIFIED-CONDITIONAL |
| `BH-IIF-C-0076` | 2988–3008 | Restricted full-sublevel classification on this carrier (`p2b:prop:v2174-fifteen-dimensional-port-exclusion`) | VERIFIED-CONDITIONAL |
| `BH-IIF-C-0077` | 3023–3042 | Kinematic Lie algebra classification (`p2:thm:compact_selection`) | VERIFIED |
| `BH-IIF-C-0078` | 3060–3076 | Generality of the displayed brackets, and hypothesis usage (`p2:rem:bracket-generality`) | VERIFIED |
| `BH-IIF-C-0079` | 3078–3089 | Interpretation of the compact constitution (`p2b:rem:compact-branch-legacy`) | FORMALIZED |
| `BH-IIF-C-0080` | 3116–3142 | Residual coordinate-completion selector family (`p2b:rem:coordinate-completion-selector-family`) | VERIFIED-CONDITIONAL |
| `BH-IIF-C-0081` | 3144–3156 | Host-derived carrier and independent finite-cell imports (`p2:rem:series-selected-minimal-imports`) | FORMALIZED |
| `BH-IIF-C-0082` | 3158–3164 | Relation to a Hurwitz-link realization (`p2:rem:hurwitz-link-structural-carrier`) | FORMALIZED |
| `BH-IIF-C-0083` | 3166–3229 | Protected even Clifford algebra and cross-category count (`p2:thm:minimal-hilbert-structural-15`) | VERIFIED-CONDITIONAL |
| `BH-IIF-C-0084` | 3244–3250 | Seven-dimensional object is not a Hilbert complement (`p2:rem:no-seven-hilbert-complement-pointer`) | VERIFIED |
| `BH-IIF-C-0085` | 3252–3265 | Seed-carrier and protected Clifford count package (`p2:cor:protected-minimal-package-status`) | VERIFIED-CONDITIONAL |
| `BH-IIF-C-0086` | 3272–3302 | Noncommutative geometry without points (`p2:rem:noncommutative`) | VERIFIED-CONDITIONAL |
| `BH-IIF-C-0087` | 3312–3321 | Unique invariant mean on a finite transitive support (`p2:lem:finite-transitive-invariant-mean`) | VERIFIED |
| `BH-IIF-C-0088` | 3330–3365 | Symmetry-derived closure of the Paper-I-A octet descendants (`p2:cor:paper1-octet-descendant-weight-closure`) | VERIFIED-CONDITIONAL |
| `BH-IIF-C-0089` | 3393–3460 | Quotient kinematics are invariant restrictions (`p2:prop:quotient-restriction`) | VERIFIED-CONDITIONAL |
| `BH-IIF-C-0090` | 3461–3521 | Optional quotient branch (`Paper2F:unlabelled-remark-3461`) | FORMALIZED |
| `BH-IIF-C-0091` | 3526–3541 | Total-weight shells (`p2:def:total-weight-shells`) | FORMALIZED |
| `BH-IIF-C-0092` | 3543–3557 | Shell filtration relative to the total-weight cutoff of \(\mathcal H_m\) (`p2:thm:shell-filtration`) | VERIFIED |
| `BH-IIF-C-0093` | 3563–3566 | Shellwise spectral cutoffs (`p2:prop:shellwise-spectral-cutoff`) | VERIFIED |
| `BH-IIF-C-0094` | 3577–3582 | Compact branch comparison (`Paper2F:unlabelled-remark-3577`) | FORMALIZED |
| `BH-IIF-C-0095` | 3594–3622 | Nontrivial Hopf phase-direction coupling (`p2:prop:hopf-phase-direction-coupling`) | VERIFIED-CONDITIONAL |
| `BH-IIF-C-0096` | 3660–3673 | Mathematical word stages (`p2:def:spex-fit`) | FORMALIZED |
| `BH-IIF-C-0097` | 3675–3693 | Complete intrinsic coordinate-type retention (`p2:def:coord-role-antecedent`) | FORMALIZED |
| `BH-IIF-C-0098` | 3695–3707 | Word-budget lower-ideal identity (`p2:thm:finite-spectral-exhaustivity`) | VERIFIED |
| `BH-IIF-C-0099` | 3717–3730 | Sharpness and scope of the word grammar (`p2:rem:spex-seed-sharp`) | FORMALIZED |
| `BH-IIF-C-0100` | 3732–3741 | Logical boundary of the word-budget theorem (`p2:cor:psli-discharged`) | VERIFIED |
| `BH-IIF-C-0101` | 3743–3758 | Placement of the derived momentum seed in the word tower (`p2:thm:spex-fit-level-one`) | VERIFIED-CONDITIONAL |
| `BH-IIF-C-0102` | 3769–3776 | Former selector diagnostics (`p2:rem:why-coordinate-hypothesis`) | FORMALIZED |
| `BH-IIF-C-0103` | 3778–3785 | Status of optional spectral exhaustivity (`p2:rem:spex-proof-status`) | FORMALIZED |
| `BH-IIF-C-0104` | 3787–3797 | Optional tower machinery deferred (`p2b:rem:optional-tower-machinery-deferred`) | FORMALIZED |
| `BH-IIF-C-0105` | 3805–3819 | Complete half-integral lower-ideal envelopes (`p2:def:half-integral-complete-envelope`) | FORMALIZED |
| `BH-IIF-C-0106` | 3821–3850 | Directed finite tower (`p2:prop:directed-finite-tower`) | VERIFIED |
| `BH-IIF-C-0107` | 3860–3903 | Spectral-lower-ideal finite-role package (`p2:def:spectral-lower-ideal-finite-role-package`) | FORMALIZED |
| `BH-IIF-C-0108` | 3905–3919 | Level-ceiling hypothesis \(\mathsf P_{\rm lvl}(R,s)\) (`p2:def:ceiling-hypothesis`) | FORMALIZED |
| `BH-IIF-C-0109` | 3921–3947 | Equivariant truncation with explicit multiplicity boundary (`p2:lem:equivariant-truncation-no-insertion`) | VERIFIED |
| `BH-IIF-C-0110` | 3964–4019 | Conditional GP3 reduction of an unmarked multiplicity (`p2:prop:gp3-multiplicity-bound`) | VERIFIED-CONDITIONAL |
| `BH-IIF-C-0111` | 4035–4082 | Positive source-response descent: kernel and Gram certificates (`p2f:thm:v296-source-quadratic-quotient`) | VERIFIED-CONDITIONAL |
| `BH-IIF-C-0112` | 4084–4142 | Exact component-spectrum truncation theorem (`p2:thm:truncation`) | VERIFIED-CONDITIONAL |
| `BH-IIF-C-0113` | 4165–4179 | Envelope versus realized carrier (`p2:rem:maximal-envelope-versus-realized-carrier`) | FORMALIZED |
| `BH-IIF-C-0114` | 4181–4206 | Auxiliary ceiling versus sharp realized maximum (`p2:rem:pmax-selected-carrier-reading`) | VERIFIED-CONDITIONAL |
| `BH-IIF-C-0115` | 4208–4211 | Mathematical Nature of $\mathcal{H}_m$ (`p2:rem:extended-hilbert`) | VERIFIED |
| `BH-IIF-C-0116` | 4213–4226 | Terminology: coordinate-stable (`p2:rem:coordinate-stable-terminology`) | FORMALIZED |
| `BH-IIF-C-0117` | 4229–4236 | Level-one consistency inside an optional lower-ideal tower (`p2:cor:coord-plus-ceiling-m1`) | VERIFIED-CONDITIONAL |
| `BH-IIF-C-0118` | 4248–4255 | Support form of an optional level-one ceiling (`p2:prop:level-one-support-ceiling-bridge`) | VERIFIED-CONDITIONAL |
| `BH-IIF-C-0119` | 4273–4300 | Status of the integer coordinate-stable family (`p2:prop:integer-coordinate-stable-family`) | VERIFIED-CONDITIONAL |
| `BH-IIF-C-0120` | 4336–4339 | No literal seven-dimensional Hilbert complement (`p2:lem:no-literal-seven-hilbert-complement`) | VERIFIED |
| `BH-IIF-C-0121` | 4350–4408 | Maximal label-complete envelope within \(\mathsf P_{\rm sli}\) (`p2:thm:uniqueness`) | VERIFIED-CONDITIONAL |
| `BH-IIF-C-0122` | 4537–4577 | Classification inside the spectral-lower-ideal finite-role package (`p2:thm:gp2-exact-label-complete-level-class`) | VERIFIED-CONDITIONAL |
| `BH-IIF-C-0123` | 4603–4686 | Sharpness of spectral lower-ideal completeness (`p2:prop:spectral-lower-ideal-sharpness`) | VERIFIED |

### Source-bound correctness certificates (E1, E3, E4)

#### BH-IIF-C-0074 — Exact phase-qualified pair presentation
**E1 source replay (lines 2905–2955):** Read original C_a, A_a epsilon, four-mode symmetric Fock degree <=2, T columns, and all three coefficient blocks of X^D; exact 15-column presentation conditional on chosen phase C_PI and native coordinate class.
**E3 independent calculation/proof check:** Independently construct all four 15x15 compressed boson operators, dGamma(C_a), 15 orthonormal T columns, and 900 source matrix entries exactly in SymPy; all agree.
**E4 adversarial domain attack:** Swapping chiral phase or treating auxiliary B as a physical Bose field changes the marked native object; no license to promote this presentation to an interacting joint action.
**Source import labels:** `p2:thm:momentum-host-H1`, `p1:thm:intrinsic-tangential-coordinate-class`.  
**Conditional scope guards:** `BH-IIF-A-0015`.

#### BH-IIF-C-0075 — The native geometric grading fails the linear port identity
**E1 source replay (lines 2965–2986):** Degree gaps 0<->2 and within grade 2/1 make the double commutator act with factors 4 or 0. Sum native block HS contributions 9*2*(R/2)^2+2*3*(sqrt2 R/3)^2+4*(sqrt3 R/4)^2=79R²/12.
**E3 independent calculation/proof check:** Independent exact T-conjugated 15x15 matrix trace gives 79/12 for all four a at R=1; physical R factor follows homogeneity of X.
**E4 adversarial domain attack:** Only the specified N_geo and native coordinate are excluded; changing marked grading or relaxing the full linear port condition is outside the negation.
**Source import labels:** `p2b:prop:v2174-geometric-pair-presentation`.  
**Conditional scope guards:** `BH-IIF-A-0015`.

#### BH-IIF-C-0076 — Restricted full-sublevel classification on this carrier
**E1 source replay (lines 2988–3008):** Classify complete symmetric Bose sublevels with total dimension binom(N+d,d)=15. Six Spin4 irreducible components force the scalar degree 0, vector degree 1, bivectors degree 2, and chiral spinors adjacent nonzero degrees, incompatible with possible (N,d).
**E3 independent calculation/proof check:** Independent integer enumeration finds only (N,d)=(14,1),(4,2),(2,4),(1,14); grade one must contain a four-dimensional vector and 4+2 spinors cannot fit dim4 at (2,4).
**E4 adversarial domain attack:** Exclusion requires unique degree-zero unit, Spin4 commuting N, a full initial Bose sublevel and native X linear. It does not forbid arbitrary constrained quantizations.
**Source import labels:** `p2b:prop:v2174-geometric-pair-presentation`.  
**Conditional scope guards:** `BH-IIF-A-0023`.

#### BH-IIF-C-0077 — Kinematic Lie algebra classification
**E1 source replay (lines 3023–3042):** Rescale P/sqrt(|kappa|). For kappa=0 translations form abelian ideal, positive split L±=(J±K)/2 into commuting su2 ideals, and negative rotation/boost relations give so(3,1). Faithfulness identifies abstract six-dimensional source with operator image.
**E3 independent calculation/proof check:** Check bracket structure constants under the two changes of basis, Killing signature and independent dimension for iso3/so4/so3,1.
**E4 adversarial domain attack:** Nonfaithful images, nonzero hbar issue or different covariant [P,P] brackets are not hypotheses of this three-case assertion.
**Source import labels:** none used in this recorded source-local proof route.  
**Conditional scope guards:** none directly registered; mathematical theorem-local hypotheses still apply.

#### BH-IIF-C-0078 — Generality of the displayed brackets, and hypothesis usage
**E1 source replay (lines 3060–3076):** Most general so3-equivariant antisymmetric bilinear V wedge V into V⊕so3 is epsilon_ijk(a P_k+b J_k). A shift P to P-aJ/2 sends coefficient a to zero and b to b+a²/4.
**E3 independent calculation/proof check:** Direct expansion of [P-aJ/2,P-aJ/2] and Jacobi of eps brackets confirms shifted classification.
**E4 adversarial domain attack:** Shift mixes momentum and rotations; it is an algebraic basis change, not an automatic physical preservation of every marked operator role.
**Source import labels:** `p2:thm:compact_selection`.  
**Conditional scope guards:** none directly registered; mathematical theorem-local hypotheses still apply.

#### BH-IIF-C-0079 — Interpretation of the compact constitution
**E1 source replay (lines 3078–3089):** Source explicitly distinguishes classified Killing algebra so4 from selected group SU2 with Lie algebra su2; kappa=Rmom^-2 follows round parent radius.
**E3 independent calculation/proof check:** Compare dim so4=6 to dim su2=3 and round sphere curvature kappa>0; no equivalence of the group and its full Killing algebra claimed.
**E4 adversarial domain attack:** Algebraic trichotomy itself does not select kappa>0; constitutional selected parent is a separate imported statement.
**Source import labels:** `p2:thm:relation-minimal-globalization`.  
**Conditional scope guards:** none directly registered; mathematical theorem-local hypotheses still apply.

#### BH-IIF-C-0080 — Residual coordinate-completion selector family
**E1 source replay (lines 3116–3142):** Current I-A completion atlas has residual three nonnegative magnitudes after sector-rephase quotient, with normalized protected even-algebra independence only on rho_sp>0. No physical selection of a cone point from H1.
**E3 independent calculation/proof check:** Independently inspect four-arrow forest and three rephasing-invariant magnitudes; sample nonzero rho family preserves normalized Clifford relations at different geometric coefficients.
**E4 adversarial domain attack:** At rho_sp=0 inverse-normalized gamma is undefined. Do not extrapolate Paper II-C nondegenerate result there or assume that invariance fixes C_PI.
**Source import labels:** `p1:prop:general-protected-clifford-relation`.  
**Conditional scope guards:** none directly registered; mathematical theorem-local hypotheses still apply.

#### BH-IIF-C-0081 — Host-derived carrier and independent finite-cell imports
**E1 source replay (lines 3144–3156):** Separates structural seed from optional full-carrier GP3 rigidity, physical finite support and chosen C_PI intertwiner; same-object type boundaries explicitly frozen.
**E3 independent calculation/proof check:** Direct current-source cross-check of host-H1 and carrier-rigidity hypotheses.
**E4 adversarial domain attack:** Abstract iso H1 cannot generate completion coefficients or a group-valued Hurwitz support by relabeling.
**Source import labels:** `p2:thm:momentum-host-H1`, `p2b:thm:momentum-carrier-rigidity`.  
**Conditional scope guards:** none directly registered; mathematical theorem-local hypotheses still apply.

#### BH-IIF-C-0082 — Relation to a Hurwitz-link realization
**E1 source replay (lines 3158–3164):** States only algebra isomorphism type Cl^0(4,0)~Cl(0,3) with Hurwitz-link Walsh algebra, explicitly not a canonical support-to-H1 map.
**E3 independent calculation/proof check:** Real Clifford classification gives Cl^0(4,0)=H⊕H dimension 8, independently of either representation.
**E4 adversarial domain attack:** An algebra isomorphism does not supply a module intertwiner, source occurrence or same-owner comparison.
**Source import labels:** none used in this recorded source-local proof route.  
**Conditional scope guards:** none directly registered; mathematical theorem-local hypotheses still apply.

#### BH-IIF-C-0083 — Protected even Clifford algebra and cross-category count
**E1 source replay (lines 3166–3229):** Six Spin4 sector dimensions 1+4+3+3+2+2=15. Given C_PI Clifford vector on complex Dirac four-space, real faithful Cl4,0 image has even basis 1, six bivectors, volume. Trace kills seven nonscalar basis vectors.
**E3 independent calculation/proof check:** Independent exact 4x4 C-matrix construction gives 8 real-linearly independent even matrices, real traces (8,0,...,0), seven-dimensional traceless part.
**E4 adversarial domain attack:** The 7+8=15 comparison crosses real operator and complex Hilbert types and is not a 15D Clifford Hilbert decomposition. Without C_PI the protected vector does not automatically occur.
**Source import labels:** `p2:thm:momentum-host-H1`, `p1:thm:s3one-cliffordization`.  
**Conditional scope guards:** `BH-IIF-A-0015`.

#### BH-IIF-C-0084 — Seven-dimensional object is not a Hilbert complement
**E1 source replay (lines 3244–3250):** The purported seven-dimensional complement would have to equal a complex 11-dimensional complement, real dimension22; therefore not a Hilbert-space complement.
**E3 independent calculation/proof check:** Dimension check 15-4=11 complex =22 real independently; seven belongs to trace-kernel operator space.
**E4 adversarial domain attack:** Do not match dimensions over different scalar fields.
**Source import labels:** `p2:thm:minimal-hilbert-structural-15`.  
**Conditional scope guards:** none directly registered; mathematical theorem-local hypotheses still apply.

#### BH-IIF-C-0085 — Seed-carrier and protected Clifford count package
**E1 source replay (lines 3252–3265):** Combine current structural seed H1/m=1 with C_PI-specific Cl-even counts; numerical matching of 15 does not assert canonical physical identification.
**E3 independent calculation/proof check:** Compute 15 and 8+7 independently as direct sum representation dimensions and trace-kernel rank.
**E4 adversarial domain attack:** Removing C_PI specialization would incorrectly promote chosen coordinate algebra to the constitutional seed.
**Source import labels:** `p2:thm:m1-component`, `p2:thm:minimal-hilbert-structural-15`.  
**Conditional scope guards:** `BH-IIF-A-0015`.

#### BH-IIF-C-0086 — Noncommutative geometry without points
**E1 source replay (lines 3272–3302):** On chosen C_PI with rho_prot>0, X_a=(rho/2)C_a; anticommutators imply [X_a,X_b]=rho² C_a C_b/2 nonzero for a neq b. At m=0 only scalar compressed coordinate survives as zero.
**E3 independent calculation/proof check:** Compute C_aC_b invertible and explicit nonzero commutators; check I-A C_PI family rho>0, distinct from parent radius Rmom.
**E4 adversarial domain attack:** Countermodel rho_sp=0 outside C_PI positive family invalidates an unconditional variant, not the source. Noncommutativity never implies a lattice of points.
**Source import labels:** `p1:thm:s3one-cliffordization`, `p2:thm:minimal-hilbert-structural-15`.  
**Conditional scope guards:** `BH-IIF-A-0015`.

#### BH-IIF-C-0087 — Unique invariant mean on a finite transitive support
**E1 source replay (lines 3312–3321):** Finite transitive action sends any s to t and invariance equates weights; normalization fixes 1/|S|. Product group transitivity follows componentwise.
**E3 independent calculation/proof check:** Independent invariant-subspace argument: permutation representation of a transitive finite set has one-dimensional fixed space spanned by all-ones vector.
**E4 adversarial domain attack:** This does not assign uniform weights when the action is not transitive, or claim uniqueness of all quantum states.
**Source import labels:** none used in this recorded source-local proof route.  
**Conditional scope guards:** none directly registered; mathematical theorem-local hypotheses still apply.

#### BH-IIF-C-0088 — Symmetry-derived closure of the Paper-I-A octet descendants
**E1 source replay (lines 3330–3365):** For occurring Supp2T and constituted transitive actions, octet (Z2)^3, seven nonzero characters GL(3,2), and trimer pair Z3xZ3 give 1/8,1/7,1/9, hence products 1/56 and 1/72.
**E3 independent calculation/proof check:** Independent linear action GL(3,2) on all seven nonzero F2^3 characters, uniform orbit counting, and exact rational products.
**E4 adversarial domain attack:** Generic point support or a selected H1 level does not physically generate the exceptional 24-point orbit; physical later readouts require new occurrence theorems.
**Source import labels:** `p2:lem:finite-transitive-invariant-mean`, `p2:cor:core-support-inheritance-no-duplicate-witness`.  
**Conditional scope guards:** `BH-IIF-A-0020`.

#### BH-IIF-C-0089 — Quotient kinematics are invariant restrictions
**E1 source replay (lines 3393–3460):** For free finite orientation-preserving Gamma action, compatible scalar/trivial-bundle functions pull back as invariant sections; norm scales by |Gamma|^1/2 for raw volume, not normalized volume. Operators genuinely restrict iff (1-P)AP=0. Spin/twist choices stay quotient-local.
**E3 independent calculation/proof check:** Independent covering integral and operator block proof; oriented spherical 3-manifold is parallelizable/spin, deck representation in SO4 has Spin4 lift; explicit Z3 spin1 Jx yields Punit leakage. Quotient orientation-preserving isometries are normalizer/Gamma.
**E4 adversarial domain attack:** Require Gamma-equivariant truncation, free deck action, compatible lift/twist, and preservation of the chosen spin data; compressing unpreserved operators is not restriction and not physically licensed.
**Source import labels:** none used in this recorded source-local proof route.  
**Conditional scope guards:** `BH-IIF-A-0021`.

#### BH-IIF-C-0090 — Optional quotient branch
**E1 source replay (lines 3461–3521):** Spin/twist torsor only becomes live for an actually claimed quotient; simply connected momentum parent does not consume it.
**E3 independent calculation/proof check:** Check π1(S3)=0 versus π1(S3/Gamma)=Gamma, so quotient data cannot be carried back as a seed premise.
**E4 adversarial domain attack:** No hidden spin structure selector is needed for the original simply connected parent.
**Source import labels:** `p2:prop:quotient-restriction`.  
**Conditional scope guards:** none directly registered; mathematical theorem-local hypotheses still apply.

#### BH-IIF-C-0091 — Total-weight shells
**E1 source replay (lines 3526–3541):** Defines S_s by all sectors jL+jR=s and H_m by their finite direct sum; no existence of a physical level inferred.
**E3 independent calculation/proof check:** Enumerate m=1 shells dimensions 1,4,10 and their sum 15 directly.
**E4 adversarial domain attack:** Shell partition is relative to declared total-weight family, not a universal physical spectral decomposition.
**Source import labels:** none used in this recorded source-local proof route.  
**Conditional scope guards:** none directly registered; mathematical theorem-local hypotheses still apply.

#### BH-IIF-C-0092 — Shell filtration relative to the total-weight cutoff of \(\mathcal H_m\)
**E1 source replay (lines 3543–3557):** A finite direct sum of Spin4 irreducibles by total weight is invariant. N acts by distinct real weights, so orthogonal shell projectors are Lagrange interpolation polynomials.
**E3 independent calculation/proof check:** Independent polynomial Π_s=product_{r!=s}(N-rI)/(s-r) checked on finite shell weights; selfadjoint equivariance follows Schur decomposition.
**E4 adversarial domain attack:** The shell N is declared internally; does not imply it is the physical Hamiltonian.
**Source import labels:** `p2:def:total-weight-shells`.  
**Conditional scope guards:** none directly registered; mathematical theorem-local hypotheses still apply.

#### BH-IIF-C-0093 — Shellwise spectral cutoffs
**E1 source replay (lines 3563–3566):** For T=f(N) block-scalar over complete shells, every spectral projection groups shells with equal f values. Source distinguishes component-dependent kinetic Casimir from f(N).
**E3 independent calculation/proof check:** At weight one compare (1/2,1/2) Casimir 3/R² to (1,0) Casimir 4/R²; same weight but distinct eigenvalues, explicitly falsifying overstrong spectral-shell assertion.
**E4 adversarial domain attack:** The theorem is only for T=f(N); an arbitrary energy cutoff can split shells, as the source states.
**Source import labels:** `p2:thm:shell-filtration`, `p2:prop:component_spectrum`.  
**Conditional scope guards:** none directly registered; mathematical theorem-local hypotheses still apply.

#### BH-IIF-C-0094 — Compact branch comparison
**E1 source replay (lines 3577–3582):** Compact branch table deferred, not used in positive momentum allocation; a scope pointer without independent theorem.
**E3 independent calculation/proof check:** Compare optional quotient and integer envelope with current seed chronology.
**E4 adversarial domain attack:** Table is not a new physical parent selection proof.
**Source import labels:** none used in this recorded source-local proof route.  
**Conditional scope guards:** none directly registered; mathematical theorem-local hypotheses still apply.

#### BH-IIF-C-0095 — Nontrivial Hopf phase-direction coupling
**E1 source replay (lines 3594–3622):** Fix torus and Hopf representative. c1=±1 gives no section/product. In (j,j), U1 right weights m_R=-j,...,j yield integer q=2m_R with step2, left multiplicity 2j+1.
**E3 independent calculation/proof check:** Independent principal S1-bundle classification via unit c1 and exact spin-j weight enumeration/parity checks up to j=4.
**E4 adversarial domain attack:** Torus choice not canonical. q and k=q/2 differ; bundle fiber is not independently constituted scalar S1_A.
**Source import labels:** `p2:thm:rank-one-exact-symmetry-groups`.  
**Conditional scope guards:** none directly registered; mathematical theorem-local hypotheses still apply.

#### BH-IIF-C-0096 — Mathematical word stages
**E1 source replay (lines 3660–3673):** Defines word stage of two chiral fundamentals length<=2m, IrrSupp multiplicity-free, and registered later-role TWR/SPEX/FIT tags.
**E3 independent calculation/proof check:** Compute spin tensor recursion at nonnegative half-levels independently.
**E4 adversarial domain attack:** Mathematical tensor-word stage is a declared algebraic construction, not automatically GP2 physical closure.
**Source import labels:** none used in this recorded source-local proof route.  
**Conditional scope guards:** none directly registered; mathematical theorem-local hypotheses still apply.

#### BH-IIF-C-0097 — Complete intrinsic coordinate-type retention
**E1 source replay (lines 3675–3693):** Explicit COORD_R means whole irreducible (1/2,1/2) is a summand; it does not select an individual coordinate basis.
**E3 independent calculation/proof check:** SU2xSU2 tensor type has complex dimension4 and total weight1; no equivalence to retaining a single coordinate vector.
**E4 adversarial domain attack:** Many finite faithful roles omit this type, so it must remain an optional later-role interface.
**Source import labels:** `p2:thm:intrinsic-coordinate-sector`.  
**Conditional scope guards:** `BH-IIF-A-0017`.

#### BH-IIF-C-0098 — Word-budget lower-ideal identity
**E1 source replay (lines 3695–3707):** Every r-letter chiral word has jL<=rL/2 and jR<=rR/2; every label of total weight<=m is reached in a word of length 2jL+2jR; taking IrrSupp drops multiplicities.
**E3 independent calculation/proof check:** Independent exact Clebsch-Gordan step recursion for all lengths 0..12 yields the full triangle; 455 individual target memberships passed.
**E4 adversarial domain attack:** The identity does not require or establish physical unrestricted word generation or a realized tower ceiling.
**Source import labels:** `p2:def:spex-fit`.  
**Conditional scope guards:** none directly registered; mathematical theorem-local hypotheses still apply.

#### BH-IIF-C-0099 — Sharpness and scope of the word grammar
**E1 source replay (lines 3717–3730):** Two chiral primitives generate representation ring as a mathematical fact, but II-B host seed and optional GP3 rigidity are separate source routes.
**E3 independent calculation/proof check:** Explicit omission of a chiral primitive loses half-spin representations, while this does not alter host-H1 proof.
**E4 adversarial domain attack:** Mathematical generation is not a GP2 licensed constructor unless actual source role grammar says so.
**Source import labels:** `p2:thm:finite-spectral-exhaustivity`, `p2:thm:momentum-host-H1`.  
**Conditional scope guards:** none directly registered; mathematical theorem-local hypotheses still apply.

#### BH-IIF-C-0100 — Logical boundary of the word-budget theorem
**E1 source replay (lines 3732–3741):** A proven identity of declared word stages does not imply a universal statement that arbitrary realized roles are word prefixes. Source asserts only a logical nonimplication.
**E3 independent calculation/proof check:** Independent counterexample: finite Spin4 module E9 contains coordinate and chirals but is not a full total-weight lower ideal.
**E4 adversarial domain attack:** Cannot use mathematical IrrSupp result as physical spectrum-exhaustivity or selector.
**Source import labels:** `p2:thm:finite-spectral-exhaustivity`.  
**Conditional scope guards:** none directly registered; mathematical theorem-local hypotheses still apply.

#### BH-IIF-C-0101 — Placement of the derived momentum seed in the word tower
**E1 source replay (lines 3743–3758):** m=1 word-stage triangle equals six-type host-derived support; m_p=1 imported. Full GP3 endpoint H1 only if whole-structured comparison hypotheses are certified as in II-B.
**E3 independent calculation/proof check:** Direct enumerate m=1 6 sector types, dimension15 and match host theorem list; word stage not a selector.
**E4 adversarial domain attack:** The optional P_sli and coordinate completion are not upstream of the momentum host construction.
**Source import labels:** `p2:thm:finite-spectral-exhaustivity`, `p2:thm:momentum-host-H1`, `p2:thm:m1-component`, `p2b:thm:momentum-carrier-rigidity`.  
**Conditional scope guards:** none directly registered; mathematical theorem-local hypotheses still apply.

#### BH-IIF-C-0102 — Former selector diagnostics
**E1 source replay (lines 3769–3776):** Records that E9 and other weaker-signature countermodels are not positive-constructor candidates in revised host signature.
**E3 independent calculation/proof check:** Check E9 excludes adjoint sectors present in source-generated Killing object.
**E4 adversarial domain attack:** Do not use weaker-signature counterexample to refute stronger constructor-relative GP2 claim.
**Source import labels:** none used in this recorded source-local proof route.  
**Conditional scope guards:** none directly registered; mathematical theorem-local hypotheses still apply.

#### BH-IIF-C-0103 — Status of optional spectral exhaustivity
**E1 source replay (lines 3778–3785):** Source explicitly restricts spectral exhaustivity to a declared tower grammar and later roles with a separately proved boundary.
**E3 independent calculation/proof check:** Word-budget identity is a finite representation identity, not a physics of every realized cutoff.
**E4 adversarial domain attack:** No silent universal level assertion.
**Source import labels:** `p2:thm:finite-spectral-exhaustivity`.  
**Conditional scope guards:** none directly registered; mathematical theorem-local hypotheses still apply.

#### BH-IIF-C-0104 — Optional tower machinery deferred
**E1 source replay (lines 3787–3797):** Optional directed tower and spectral-lower-ideal package explicitly not consumed by constitutional seed theorem.
**E3 independent calculation/proof check:** Trace referenced optional definitions and distinguish from host-H1 proof route.
**E4 adversarial domain attack:** Do not move tower clauses upstream by citation or narrative similarity.
**Source import labels:** `p2:thm:momentum-host-H1`.  
**Conditional scope guards:** none directly registered; mathematical theorem-local hypotheses still apply.

#### BH-IIF-C-0105 — Complete half-integral lower-ideal envelopes
**E1 source replay (lines 3805–3819):** Defines half-integer complete lower-ideal envelope with one copy per label; at integer boundary underlying module equals Paper-I-A H_m, whereas coordinate maps require independent completion.
**E3 independent calculation/proof check:** Direct comparison with word_support(s), m integer and m+1/2 support sets.
**E4 adversarial domain attack:** No claim that all finite roles have this type-support.
**Source import labels:** `p2:thm:finite-spectral-exhaustivity`.  
**Conditional scope guards:** none directly registered; mathematical theorem-local hypotheses still apply.

#### BH-IIF-C-0106 — Directed finite tower
**E1 source replay (lines 3821–3850):** Nested half-integral label sets yield canonical equivariant direct sum embeddings J and orthogonal coordinate projections Pi. Their compositions/retractions are direct-sum identities.
**E3 independent calculation/proof check:** Independent finite set inclusion and matrix-block projector check for s<=t<=u; no multiplicity ambiguity within declared one-copy envelopes.
**E4 adversarial domain attack:** The infinite algebraic union/completion is a host presentation, not an infinite realized carrier.
**Source import labels:** `p2:def:half-integral-complete-envelope`.  
**Conditional scope guards:** none directly registered; mathematical theorem-local hypotheses still apply.

#### BH-IIF-C-0107 — Spectral-lower-ideal finite-role package
**E1 source replay (lines 3860–3903):** Defines optional P_sli total-weight preorder, full unmarked universe, mandatory lower-ideal supports and no sector deletions/chiral/multiplicity marks; explicitly not GP2-generated.
**E3 independent calculation/proof check:** Check preorder weight ties and that lower ideals in finite half-integer lattice are complete finite triangles.
**E4 adversarial domain attack:** The rule is an optional comparison grammar, not a result of round S3 geometry or component norm alone.
**Source import labels:** none used in this recorded source-local proof route.  
**Conditional scope guards:** `BH-IIF-A-0016`.

#### BH-IIF-C-0108 — Level-ceiling hypothesis \(\mathsf P_{\rm lvl}(R,s)\)
**E1 source replay (lines 3905–3919):** Defines optional P_lvl(R,s) support upper bound; no GP3 reduction and no numerical s selector.
**E3 independent calculation/proof check:** Direct support subset formula and consequence s_R<=s under P_sli.
**E4 adversarial domain attack:** Bound is not an equality of maximum level, nor a physical occurrence proof.
**Source import labels:** `p2:def:spectral-lower-ideal-finite-role-package`.  
**Conditional scope guards:** `BH-IIF-A-0018`.

#### BH-IIF-C-0109 — Equivariant truncation with explicit multiplicity boundary
**E1 source replay (lines 3921–3947):** Schur commutant for finite unitary Spin4 module gives Q=⊕I_V⊗Q_M; orthogonality forces Q_M orthoprojectors. Multiplicity-free restriction gives blocks either 0 or I.
**E3 independent calculation/proof check:** Independent double-commutant/isotypic block diagonalization; use dim2 multiplicity Q=diag(1,0) as exact counterexample to whole-isotypic retention.
**E4 adversarial domain attack:** Preservation of Spin4 symmetry does not force retention of all multiplicities and does not license arbitrary physical compression.
**Source import labels:** none used in this recorded source-local proof route.  
**Conditional scope guards:** none directly registered; mathematical theorem-local hypotheses still apply.

#### BH-IIF-C-0110 — Conditional GP3 reduction of an unmarked multiplicity
**E1 source replay (lines 3964–4019):** By definition GP3 irreducibility forbids an actual generated role-faithful proper whole-candidate comparison. Hypothesis explicitly supplies such witness whenever dim M>1; hence irreducible has dim M<=1.
**E3 independent calculation/proof check:** Independent reductio in structured preorder: if excess copy and comparison exists, irreducibility fails without iteration. Crosscheck operational quotient is not automatically such a comparison.
**E4 adversarial domain attack:** Unmarkedness alone, a non-generated rank-one projector, or hypothetical missing scalar trace is insufficient. Preserve any occurring trace/port and comparison licenses.
**Source import labels:** `p2:post:GP3`, `p2b:prop:v279-no-canonical-copy-selector`, `p2b:thm:v293-operational-multiplicity-quotient`.  
**Conditional scope guards:** `BH-IIA-A-B54-CMP-III-001`.

#### BH-IIF-C-0111 — Positive source-response descent: kernel and Gram certificates
**E1 source replay (lines 4035–4082):** Finite real PSD quadratic q factors through surjective L iff kernel L subset kernel G; equivalently trace of positive restricted Gram zero. Unique descended bilinear form follows polarization; full-response source occurrence is a separate physical premise.
**E3 independent calculation/proof check:** Independent exact rational Gram factorizations for 140 controls across quotient ranks and dimensions, plus polarization and norm-of-insertion reasoning.
**E4 adversarial domain attack:** Without positivity trace=0 may cancel, and one occurring source vector does not imply factorization on a full linear span; state/effect Q may have a different type.
**Source import labels:** `p2:prop:gp3-multiplicity-bound`.  
**Conditional scope guards:** `BH-IIF-A-0022`.

#### BH-IIF-C-0112 — Exact component-spectrum truncation theorem
**E1 source replay (lines 4084–4142):** On irreducible (jL,jR), component norm=Punit(jL+jR) from II-B. The half-grid exact admissibility cutoff is s_rho=floor(2rho)/2; integer Paper-I-A boundary has m=floor(rho), while optional one-copy maximal envelope requires P_sli.
**E3 independent calculation/proof check:** Exact rational threshold checks for 70 positive rho values and independent diagonal spin-weight operator norm argument; distinguish half-integer and integer ceilings.
**E4 adversarial domain attack:** Pceil is auxiliary and need not be attained. Neither allowed labels nor lower-ideal envelopes select a realized carrier or physical m_p.
**Source import labels:** `p2:prop:component_spectrum`, `p2:lem:equivariant-truncation-no-insertion`, `p2:prop:gp3-multiplicity-bound`.  
**Conditional scope guards:** `BH-IIF-A-0016`, `BH-IIF-A-0019`.

#### BH-IIF-C-0113 — Envelope versus realized carrier
**E1 source replay (lines 4165–4179):** Separates allowed labels, optional P_sli label completeness, conditional GP3 multiplicity comparison, and a later independently constituted role/carrier.
**E3 independent calculation/proof check:** E9 is a mathematically allowed proper component submodule and not a realization of the same lower-ideal role.
**E4 adversarial domain attack:** No assertion of unconditional one-copy physical outcome.
**Source import labels:** `p2:thm:truncation`, `p2:prop:gp3-multiplicity-bound`.  
**Conditional scope guards:** none directly registered; mathematical theorem-local hypotheses still apply.

#### BH-IIF-C-0114 — Auxiliary ceiling versus sharp realized maximum
**E1 source replay (lines 4181–4206):** For selected integer H_m, sharp Pmax=m Punit; arbitrary larger Pceil is nonsharp. Punit and Pmax scale together and do not fix Rmom. Carrier selection is an independent host theorem.
**E3 independent calculation/proof check:** Independent spin highest-weight extremum and ratio rescaling check, m=0 top zero, m=1 top Punit.
**E4 adversarial domain attack:** No need to identify Pceil with Pmax or use cutoff to derive m_p=1.
**Source import labels:** `p2:prop:component_spectrum`, `p2:thm:momentum-host-H1`.  
**Conditional scope guards:** none directly registered; mathematical theorem-local hypotheses still apply.

#### BH-IIF-C-0115 — Mathematical Nature of $\mathcal{H}_m$
**E1 source replay (lines 4208–4211):** Scalar Peter-Weyl L²(SU2) has only (j,j) sectors; H_m contains all Spin4 sectors with total weight<=m and is therefore not scalar L² truncation.
**E3 independent calculation/proof check:** Independent left-right regular representation decomposition via matrix coefficients, contrasted with six H1 types.
**E4 adversarial domain attack:** Does not exclude external sections or larger bundles, but those are not scalar L² functions.
**Source import labels:** `p2:def:half-integral-complete-envelope`.  
**Conditional scope guards:** none directly registered; mathematical theorem-local hypotheses still apply.

#### BH-IIF-C-0116 — Terminology: coordinate-stable
**E1 source replay (lines 4213–4226):** Coordinate-stable is a local term for Paper-I-A integer Toeplitz/truncation family; it is not a separate Paper-I-A theorem claim and does not derive physical m_p.
**E3 independent calculation/proof check:** Compare coordinate degree parity and half-integer component cutoff permitted at same rho.
**E4 adversarial domain attack:** No stronger universal integer restriction follows from component boundedness.
**Source import labels:** `p2:thm:momentum-host-H1`.  
**Conditional scope guards:** none directly registered; mathematical theorem-local hypotheses still apply.

#### BH-IIF-C-0117 — Level-one consistency inside an optional lower-ideal tower
**E1 source replay (lines 4229–4236):** COORD_R retains weight-one full sector; P_sli fills all lower weights; P_lvl(R,1) excludes higher weights. Therefore canonical one-copy complete type-support representative equals H1.
**E3 independent calculation/proof check:** Independent finite label triangle enumeration at weights <=1 gives exactly H1, 15 complex dimensions.
**E4 adversarial domain attack:** Do not infer every actual carrier is multiplicity-free: source P_sli controls type-support, and GP3 requires its separate generated comparison for duplicate copies.
**Source import labels:** `p2:def:coord-role-antecedent`, `p2:def:spectral-lower-ideal-finite-role-package`, `p2:def:ceiling-hypothesis`.  
**Conditional scope guards:** `BH-IIF-A-0016`, `BH-IIF-A-0017`, `BH-IIF-A-0018`.

#### BH-IIF-C-0118 — Support form of an optional level-one ceiling
**E1 source replay (lines 4248–4255):** P_lvl(R,1) is definitionally absence of all support labels weight>1; (1,1/2),(1/2,1) have weight3/2 and are necessarily absent. P_sli+COORD again implies H1 one-copy support representative.
**E3 independent calculation/proof check:** Independent half-grid weight table and both logical implications of support inclusion.
**E4 adversarial domain attack:** Absence of just those two first exterior spinors is not asserted sufficient for ceiling; the proposition requires absence of EVERY higher-weight label.
**Source import labels:** `p2:def:ceiling-hypothesis`, `p2:cor:coord-plus-ceiling-m1`.  
**Conditional scope guards:** `BH-IIF-A-0016`, `BH-IIF-A-0017`, `BH-IIF-A-0018`.

#### BH-IIF-C-0119 — Status of the integer coordinate-stable family
**E1 source replay (lines 4273–4300):** A coordinate tensor (1/2,1/2) changes jL+jR by an integer; scalar-seeded unital parity has integer total-weight boundaries, whereas half-integer terminal shell lies in spinorial module class. Integer family is Paper-I-A coordinate package convention, not universal cutoff theorem.
**E3 independent calculation/proof check:** Independent SU2 tensor parity and scalar Peter-Weyl coordinates; compare full half-integer ideals to integer boundary subfamilies.
**E4 adversarial domain attack:** Additional coordinate-completion maps are imported; a generic half-integer component cutoff is still mathematically valid.
**Source import labels:** `p2:prop:component_spectrum`, `p2:lem:equivariant-truncation-no-insertion`, `p2:def:spectral-lower-ideal-finite-role-package`.  
**Conditional scope guards:** `BH-IIF-A-0016`.

#### BH-IIF-C-0120 — No literal seven-dimensional Hilbert complement
**E1 source replay (lines 4336–4339):** Protected spinor complement in H1 has complex dimension 15-4=11, hence real dimension 22; no seven-real-dimensional Hilbert complement.
**E3 independent calculation/proof check:** Independent complex-to-real dimension check versus seven-dimensional trace-kernel of even Clifford algebra.
**E4 adversarial domain attack:** Cross-category 7+8 dimension equation is not an additive Hilbert decomposition.
**Source import labels:** `p2:thm:minimal-hilbert-structural-15`.  
**Conditional scope guards:** none directly registered; mathematical theorem-local hypotheses still apply.

#### BH-IIF-C-0121 — Maximal label-complete envelope within \(\mathsf P_{\rm sli}\)
**E1 source replay (lines 4350–4408):** Given fixed S3 parent, optional P_sli and auxiliary component ceiling, all allowed labels form triangle w<=s_rho; H_m is maximal integer-family member m=floor(rho), and every invariant submodule of one-copy envelope deletes whole irreducibles.
**E3 independent calculation/proof check:** Independent finite label enumeration and block-Schur projection argument; E9 shows why stronger global uniqueness without P_sli is false.
**E4 adversarial domain attack:** No classification of all compact quantum models, no exclusion of marked multiplicity, and no physical cutoff selection asserted.
**Source import labels:** `p2:thm:truncation`, `p2:def:spectral-lower-ideal-finite-role-package`, `p2:lem:equivariant-truncation-no-insertion`.  
**Conditional scope guards:** `BH-IIF-A-0016`, `BH-IIF-A-0019`.

#### BH-IIF-C-0122 — Classification inside the spectral-lower-ideal finite-role package
**E1 source replay (lines 4537–4577):** A nonempty finite lower ideal for total preorder w has maximal weight s and contains exactly all labels w<=s. The one-copy envelope is canonical type-support representative, not general physical carrier multiplicity claim.
**E3 independent calculation/proof check:** Independent order-theoretic proof and direct half-integer support enumeration; E5/E7/E9 violate P_sli while half-weight complete ideal satisfies it.
**E4 adversarial domain attack:** P_sli itself is not derived from GP2. An arbitrary proper representation submodule can be a separate role with a weaker grammar.
**Source import labels:** `p2:def:spectral-lower-ideal-finite-role-package`, `p2:prop:integer-coordinate-stable-family`.  
**Conditional scope guards:** `BH-IIF-A-0016`.

#### BH-IIF-C-0123 — Sharpness of spectral lower-ideal completeness
**E1 source replay (lines 4603–4686):** Explicit E5/E7L/E7R/E9 sector dimensions 5,7,7,9, faithfulness when a chiral spinor retained, swap symmetry for E9; E9 lacks both adjoints while satisfying former weaker signature. H<=1/2 is a genuine P_sli lower ideal without coordinate.
**E3 independent calculation/proof check:** Exact spin central-kernel intersections, Casimir sublevel λ<=3/2 and <=3, dimension table and weight-one sector coverage all checked independently.
**E4 adversarial domain attack:** These are representation-theoretic countermodels to weaker old selector, NOT counterexamples to current generated-host no-omission clause.
**Source import labels:** `p2:prop:component_spectrum`, `p2:thm:momentum-host-H1`.  
**Conditional scope guards:** none directly registered; mathematical theorem-local hypotheses still apply.

### Batch 4 dependency and open-status adjudication
- No new mathematical theorem gap was certified. No upstream theorem status was changed and no physical 2T/Clifford/multiplicity selector was generated by this audit.
- The chosen C_PI completion is not an automatic phase/coordinate selector. The auxiliary Bose system is an exact representation but has a nonzero marked native linear-port defect.
- The word-budget triangle equals the declared formal algebraic tensor-word support; P_sli is additional physical tower grammar. The spin-spectrum ceiling bounds *allowed labels*, not their occurrence.
- For an actually occurring full quadratic source response, Gram descent holds iff kernel containment is satisfied. Even then GP3 uses a separate generated, role-faithful whole-candidate comparison.
- Mathematical Hopf, quotient, 2T orbit and noncommutative coordinate identities are not promoted to physically realized support, specific cutoffs or a particle decay claim.
- The preexisting Paper II-A finite-port issue `BH-IIA-A-PORT-001` is still open at its original origin; no duplicate issue was opened.
- Coverage remains PARTIALLY_AUDITED, source lines 4728–9555 NOT_AUDITED.

### Reproducible Batch 4 exact controls
`Proofs/Paper2F-Batch4-v1_1-verify.py` and `DAG/AuditLayer/Paper2F-v1_4/ExactCheckResults-Batch4.json` record 2,607 exact checks in 20 categories, all PASS. External computational tools or single-branch samples are no replacement for source-level proof quantifiers.

**Next batch:** Paper II-F v1.61 line 4728.

---

## Batch 5 verdict and proof route (v1.61 source lines 4728–6599)
**44 source-bound audit objects** (36 formal declarations and eight unnamed mathematical/proof interfaces): **33 `VERIFIED`, 5 `VERIFIED-CONDITIONAL`, and 6 `FORMALIZED`**. The sample mathematical claims are not physical-role assertions. No new confirmed mathematical gaps. Previous inherited issues retain their origin and lifecycle.
**Independent model controls:** 307/307 exact symbolic/rational plus 854/854 numerical checks passed. These certify explicit finite identities, interpolation and matrices, not the physical occurrence of a selected localization detector.
**Crucial quantitative limits:** Native intrinsic first-moment localization at the sharp outcome radius `sqrt(3) R_mom`; the eight-point Q8 frame reproduces normalization/first moments but differs in the quadratic symbol map by factor three, while H24/2T strength five preserves the quadratic map. The endpoint-seed family preserves first moments but changes quadratic responses.
**Typed conditionality:** A mathematical positive covariant POVM is not yet an occurring physical localization test. A separate G0 occurrence, outcome-label-to-position map and if claimed native first-moment identification a chosen completion/matching map are needed. Faithful full-S3 antipodal discrimination is a further optional role, not a GP axiom.
### Batch 5 complete source-object census
| Claim | Source lines | Mathematical result / source label | Scope verdict |
|---|---:|---|---|
| `BH-IIF-C-0124` | 4736–4770 | H1 sectorwise orthonormal basis and dimension bookkeeping (`Paper2F:source-MATERIAL-4736`) | VERIFIED |
| `BH-IIF-C-0125` | 4784–4794 | Diagonal form of $\hat{P}_3$ (`p2:prop:P3_diag`) | VERIFIED |
| `BH-IIF-C-0126` | 4816–4832 | Block matrices for $\hat{P}_1$ and $\hat{P}_2$ (`p2:prop:P12_blocks`) | VERIFIED |
| `BH-IIF-C-0127` | 4847–4861 | Worked factorized-channel calibration (`p2:rem:factorized-channel-calibration-status`) | FORMALIZED |
| `BH-IIF-C-0128` | 4893–4924 | Explicit \(4\times4\) Clifford block (`p2:prop:X_spinor_block`) | VERIFIED |
| `BH-IIF-C-0129` | 4936–4950 | Noncommutativity on the spinor block (`Paper2F:source-remark-4936`) | VERIFIED |
| `BH-IIF-C-0130` | 4979–5015 | Exact geometric-coordinate radius entries (`p2:prop:geo-coordinate-admissibility-checks`) | VERIFIED |
| `BH-IIF-C-0131` | 5016–5033 | Status of coordinate tables (`Paper2F:source-remark-5016`) | FORMALIZED |
| `BH-IIF-C-0132` | 5047–5087 | Exact Toeplitz product and leakage identities (`p2:prop:toeplitz-leakage-identities`) | VERIFIED |
| `BH-IIF-C-0133` | 5113–5133 | Linear compact Heisenberg relation is projection-stable (`Paper2F:source-remark-5113`) | VERIFIED |
| `BH-IIF-C-0134` | 5155–5231 | Exact coordinate closure of the Casimir sublevel (`p2c:prop:e9-coordinate-closure`; aliases: p2c:thm:joint-coordinate-closure-locus) | VERIFIED-CONDITIONAL |
| `BH-IIF-C-0135` | 5359–5379 | Optional scaled-Casimir kinetic representative (`Paper2F:source-MATERIAL-5359`) | VERIFIED-CONDITIONAL |
| `BH-IIF-C-0136` | 5382–5415 | Symmetric-module factorization (`p2:thm:ambient-symmetric-carrier`) | VERIFIED |
| `BH-IIF-C-0137` | 5429–5435 | Ambient symmetric powers are classification, not GP2 closure (`p2c:rem:ambient-symmetric-not-gp2`) | FORMALIZED |
| `BH-IIF-C-0138` | 5444–5453 | Dilations on the metric cone (`p2:prop:cone-dilations`) | VERIFIED |
| `BH-IIF-C-0139` | 5464–5474 | Finite spectral traces versus unregularized infinite trace (`Paper2F:source-MATERIAL-5464`) | VERIFIED |
| `BH-IIF-C-0140` | 5476–5515 | Cone weights, phase isometry and Hopf/contact normalization (`Paper2F:source-MATERIAL-5476`) | VERIFIED-CONDITIONAL |
| `BH-IIF-C-0141` | 5516–5528 | Paper~I-A rigidity of the Hopf/contact data (`p2:rem:hopf-rigidity`) | VERIFIED-CONDITIONAL |
| `BH-IIF-C-0142` | 5538–5628 | Group-valued momentum table and local BCH truncation (`Paper2F:source-MATERIAL-5538`) | VERIFIED |
| `BH-IIF-C-0143` | 5655–5670 | Sector-dependent finite-coordinate Robertson bound (`p2:thm:spin-dependent-gup`; aliases: p2:thm:sector-dependent-coordinate-robertson) | VERIFIED |
| `BH-IIF-C-0144` | 5677–5714 | Protected spinor coordinate-uncertainty bound (`p2:cor:fermionic-precision`) | VERIFIED |
| `BH-IIF-C-0145` | 5772–5797 | Diagonal decomposition of the derived momentum carrier (`p2:def:diag-decomp-H1`) | VERIFIED |
| `BH-IIF-C-0146` | 5799–5802 | No single-fiducial full-module frame (`p2:prop:no-single-fiducial-povm`) | VERIFIED |
| `BH-IIF-C-0147` | 5809–5811 | Scope of the single-orbit obstruction (`Paper2F:source-remark-5809`) | FORMALIZED |
| `BH-IIF-C-0148` | 5813–5843 | Multi-fiducial finite-coordinate coherent POVM (`p2:def:multi-fiducial-povm`) | FORMALIZED |
| `BH-IIF-C-0149` | 5845–5851 | Diagonal-$SU(2)$-covariant multi-fiducial identity resolution (`p2:thm:multi-fiducial-resolution`) | VERIFIED |
| `BH-IIF-C-0150` | 5867–5886 | Diagonal-label center blindness and vanishing odd moments of the sectorwise frame (`p2:cor:sectorwise-povm-center-blind`) | VERIFIED |
| `BH-IIF-C-0151` | 5893–5904 | Faithful full-\(S_B^3\) localization firewall (`p2c:rem:center-blind-localization-firewall`) | VERIFIED-CONDITIONAL |
| `BH-IIF-C-0152` | 5906–5945 | Minimal diagonal-label-center-sensitive two-orbit frame (`p2:prop:center-sensitive-two-orbit-frame`) | VERIFIED |
| `BH-IIF-C-0153` | 5986–6002 | Protected diagonal-irrep coherent projections (`p2:rem:protected-sector-coherent-projections`) | FORMALIZED |
| `BH-IIF-C-0154` | 6046–6059 | Ball-valued POVM saturation forces commutativity on the saturated vector (`p2c:lem:povm-ball-saturation-commutativity`) | VERIFIED |
| `BH-IIF-C-0155` | 6083–6102 | Explicit Naimark saturation obstruction for X_D (`Paper2F:source-MATERIAL-6083`) | VERIFIED |
| `BH-IIF-C-0156` | 6112–6207 | Classical moment radius for the full coordinate atlas (`p2c:thm:full-atlas-povm-radius`) | VERIFIED |
| `BH-IIF-C-0157` | 6209–6239 | Intrinsic optimal-radius endpoint eigenvalues and lower trace bound (`Paper2F:source-MATERIAL-6209`) | VERIFIED |
| `BH-IIF-C-0158` | 6241–6264 | Finite Hurwitz-support attainment (`p2c:cor:optimal-hurwitz-povm`) | VERIFIED |
| `BH-IIF-C-0159` | 6266–6294 | Positive covariant map with the sharp harmonic kernel (`p2c:cor:optimal-povm-harmonic-kernel`) | VERIFIED |
| `BH-IIF-C-0160` | 6302–6335 | Quaternion-support attainment and its subgroup domain (`p2c:cor:v233-optimal-quaternion-povm`) | VERIFIED |
| `BH-IIF-C-0161` | 6337–6398 | Complete covariant seeds on the optimal intrinsic sphere (`p2c:thm:complete-intrinsic-endpoint-seeds`) | VERIFIED |
| `BH-IIF-C-0162` | 6407–6464 | A real endpoint slice with fixed native first moments (`p2c:prop:v233-endpoint-map-family`) | VERIFIED |
| `BH-IIF-C-0163` | 6466–6472 | Finite sampling exactness stops at its cubature degree (`Paper2F:source-MATERIAL-6466`) | VERIFIED |
| `BH-IIF-C-0164` | 6474–6492 | Map-independent total readout noise at the optimal sphere (`p2c:cor:optimal-endpoint-total-noise`) | VERIFIED |
| `BH-IIF-C-0165` | 6496–6526 | Fixed-map ranks and family-independent readout (`p2c:prop:endpoint-fixed-map-qualification`) | VERIFIED |
| `BH-IIF-C-0166` | 6529–6571 | Full quadratic endpoint-POVM exactness if and only if fourth-degree cubature (`p2c:thm:v268-endpoint-quadratic-iff-design4`) | VERIFIED |
| `BH-IIF-C-0167` | 6573–6594 | Universal factor-three quaternionic quadratic-readout defect (`p2c:cor:v268-q8-endpoint-factor-three`) | VERIFIED |

### Claim-specific independent proof certificates (E1/E3/E4)

#### BH-IIF-C-0124 — H1 sectorwise orthonormal basis and dimension bookkeeping (source 4736–4770)
**E1 source replay:** Source lists six Spin4 sectors and their ordered weights, totaling fifteen.

**E3 independent matched verification:** Independent direct representation dimensions 1+2+2+3+3+4 and 15 m_L,m_R labels match all rows.

**E4 adversarial scope / mutation check:** Basis ordering is a convention, not an invariant axis/physical particle label.

**Exact imported source labels:** none in this route.  
**Typed optional conditions:** none as separate condition nodes; source-local hypotheses remain binding.

#### BH-IIF-C-0125 — Diagonal form of $\hat{P}_3$ (source 4784–4794)
**E1 source replay:** Use L3^+|m_L>=m_L|m_L>, L3^-|m_R>=m_R|m_R> in the declared 15-state sector ordering.

**E3 independent matched verification:** Independently tabulate all fifteen (m_L-m_R) rational weights; every diagonal entry matches the printed vector.

**E4 adversarial scope / mutation check:** The right-spinor signs reverse relative to left; exchange these signs as a mutation and the declaration fails. The scale hbar/R is not inferred from a numerical momentum cutoff.

**Exact imported source labels:** none in this route.  
**Typed optional conditions:** none as separate condition nodes; source-local hypotheses remain binding.

#### BH-IIF-C-0126 — Block matrices for $\hat{P}_1$ and $\hat{P}_2$ (source 4816–4832)
**E1 source replay:** Tensor-product chiral su2 representation gives J_i^(jL) tensor I minus I tensor J_i^(jR) for each of six sectors.

**E3 independent matched verification:** Explicit Pauli (spin 1/2) and ladder-generator blocks reproduce both sign branches, with 1+2+2+3+3+4=15 dimensions.

**E4 adversarial scope / mutation check:** Do not confuse a difference of chiral generators with the single-chiral SU2 group-composition generator, or treat their commutator as closed translations.

**Exact imported source labels:** none in this route.  
**Typed optional conditions:** none as separate condition nodes; source-local hypotheses remain binding.

#### BH-IIF-C-0127 — Worked factorized-channel calibration (source 4847–4861)
**E1 source replay:** Source declares gamma=R/(2sqrt2) a worked factorized-channel calibration and distinguishes it from gamma=rho_prot/2 under C_PI.

**E3 independent matched verification:** Compare the two direct substitutions and the ambient-completion freedom in the exact II-C proof: no coefficient table is selected by the symbol alone.

**E4 adversarial scope / mutation check:** Reject inference gamma=R/2 or physical selection of one global completion from the m=1 carrier. gamma=0 is permitted in the unconstrained finite-block class.

**Exact imported source labels:** `p2:prop:ambient-completion-existence-nonuniqueness`, `p2:thm:ambient-symmetric-carrier`.  
**Typed optional conditions:** `BH-IIF-A-0015`.

#### BH-IIF-C-0128 — Explicit \(4\times4\) Clifford block (source 4893–4924)
**E1 source replay:** Insert the four displayed off-diagonal chiral matrices and the Pauli multiplication law.

**E3 independent matched verification:** Independent exact 4x4 matrix products give all Clifford anticommutators 2gamma^2delta and total quadratic radius 4gamma^2I.

**E4 adversarial scope / mutation check:** The algebra works at gamma=0, but only gamma>0 yields a noncommutative protected block. C_PI and worked calibration are separate scale branches.

**Exact imported source labels:** `p2:cor:protected-phase-normalization-freedom`.  
**Typed optional conditions:** none as separate condition nodes; source-local hypotheses remain binding.

#### BH-IIF-C-0129 — Noncommutativity on the spinor block (source 4936–4950)
**E1 source replay:** For unequal Clifford indices the vanishing anticommutator implies commutator 2gamma^2 C_mu C_nu.

**E3 independent matched verification:** Exact matrix products show C_mu C_nu is invertible for mu!=nu; if gamma>0 the commutator is nonzero, while at gamma=0 all coordinates vanish.

**E4 adversarial scope / mutation check:** Cannot promote noncommutativity to a state-independent positive uncertainty product or require it at zero protected scale.

**Exact imported source labels:** `p2:prop:X_spinor_block`.  
**Typed optional conditions:** none as separate condition nodes; source-local hypotheses remain binding.

#### BH-IIF-C-0130 — Exact geometric-coordinate radius entries (source 4979–5015)
**E1 source replay:** Build geometric sector from scalar↔vector edge R/2 and vector↔(anti)self-dual forms via T_a=(r+P+ +r-P-) W_a.

**E3 independent matched verification:** Independent symbolic wedge/Hodge 11x11 reconstruction gives exact scalar, vector, two adjoint radius entries, positive coefficients, and intrinsic values 1,11/12,4/9,4/9.

**E4 adversarial scope / mutation check:** Only a compatible chosen ambient action supplies r±. These coefficients do not force a unique 11x11 table or identify a physically retained global operator.

**Exact imported source labels:** `p2:cor:h1-coordinate-classification`.  
**Typed optional conditions:** none as separate condition nodes; source-local hypotheses remain binding.

#### BH-IIF-C-0131 — Status of coordinate tables (source 5016–5033)
**E1 source replay:** Source limits geometric tables to matrices for a declared ambient completion and specifies unitary basis permutation to group invariant blocks.

**E3 independent matched verification:** Finite Clebsch-Gordan graph has no retained geo↔spinor edge; scalar state is index 0, protected block indices 1–4, and remaining geo sectors 5–14.

**E4 adversarial scope / mutation check:** A raw contiguous sp⊕geo matrix in original global ordering would be false. Different ambient actions are not generally unitary-conjugate.

**Exact imported source labels:** `p2:cor:h1-coordinate-classification`.  
**Typed optional conditions:** none as separate condition nodes; source-local hypotheses remain binding.

#### BH-IIF-C-0132 — Exact Toeplitz product and leakage identities (source 5047–5087)
**E1 source replay:** Insert I=Pi+Q in Pi M_f Pi M_g Pi; use coordinate multiplication commutativity, sphere radius, and positivity of Q leakage.

**E3 independent matched verification:** Independent matrix compression m=0 and scalar m=1 yields E_0=R²I and E_1 diag(0,3R²/4,3R²/4,3R²/4,3R²/4); Peter-Weyl selection isolates terminal shell.

**E4 adversarial scope / mutation check:** The terminal-shell statement applies only to scalar diagonal Peter-Weyl projection and classical commuting multiplication; it is not a blanket extended-coordinate polynomial identity.

**Exact imported source labels:** `p2:prop:extended-coordinate-compression-identity`.  
**Typed optional conditions:** none as separate condition nodes; source-local hypotheses remain binding.

#### BH-IIF-C-0133 — Linear compact Heisenberg relation is projection-stable (source 5113–5133)
**E1 source replay:** Projection Pi_m^sc commutes with Spin4 generators, hence linear [P,PiMxPi]=Pi[P,Mx]Pi exactly.

**E3 independent matched verification:** Chiral difference-of-generators and vector transformation derive the two compact Heisenberg commutators independently of Toeplitz product leakage.

**E4 adversarial scope / mutation check:** For nonlinear coordinate products the middle Q terms survive, so projection-stability must not be extended to coordinate-coordinate commutators or uncompressed spectra.

**Exact imported source labels:** `p2:def:compact-momentum-generators`.  
**Typed optional conditions:** none as separate condition nodes; source-local hypotheses remain binding.

#### BH-IIF-C-0134 — Exact coordinate closure of the Casimir sublevel (source 5155–5231)
**E1 source replay:** Enumerate retained coordinate edges from E9 into each of V(1,0),V(0,1); each nonzero irreducible intertwiner generates its whole adjoint target.

**E3 independent matched verification:** Independent invariant-subspace reachability on the four-node retained geometric forest reproduces all four closure outcomes and the graph of kappa.

**E4 adversarial scope / mutation check:** The exact closure is relative to one chosen action and no-recompression least-subspace role; no r+ or r- nonvanishing or physical role selection is inferred from GP1–GP3.

**Exact imported source labels:** `p2:prop:h1-coordinate-coupling-graph`, `p2:cor:h1-coordinate-classification`.  
**Typed optional conditions:** none as separate condition nodes; source-local hypotheses remain binding.

#### BH-IIF-C-0135 — Optional scaled-Casimir kinetic representative (source 5359–5379)
**E1 source replay:** J=ℏ(L++L−), RP=ℏ(L+−L−) imply C=2(C_L+C_R), with diagonal k spectrum k(k+2).

**E3 independent matched verification:** Independent spin-j Casimir arithmetic reproduces Laplacian k(k+2)/R² and overall ℏ²/(2MR²).

**E4 adversarial scope / mutation check:** M can be negative; positivity requires M>0. Physical kinetic interpretation is not constituted.

**Exact imported source labels:** none in this route.  
**Typed optional conditions:** none as separate condition nodes; source-local hypotheses remain binding.

#### BH-IIF-C-0136 — Symmetric-module factorization (source 5382–5415)
**E1 source replay:** Use Sym^n(SL⊕SR)=⊕_{a+b=n}Sym^a SL⊗Sym^b SR and Sym^(2j) C²=V_j.

**E3 independent matched verification:** Independent bidegree dimension count gives sum_{n<=2m}binom(n+3,3)=binom(2m+4,4), including 15 at m=1 and one mixed (1/2,1/2) factor in Sym².

**E4 adversarial scope / mutation check:** An isomorphism of Hilbert-completed representation spaces does not license GP2 physical creation or unrestricted symmetric products.

**Exact imported source labels:** none in this route.  
**Typed optional conditions:** none as separate condition nodes; source-local hypotheses remain binding.

#### BH-IIF-C-0137 — Ambient symmetric powers are classification, not GP2 closure (source 5429–5435)
**E1 source replay:** The remark explicitly restricts symmetric powers to ambient classification.

**E3 independent matched verification:** The finite word algebra and a physical generated-role constructor have different required objects; the source supplies the former but not an unrestricted latter.

**E4 adversarial scope / mutation check:** Reject unlicensed implication ambient symmetric algebra⇒physical bosonic seed or tensor-power closure.

**Exact imported source labels:** `p2:thm:ambient-symmetric-carrier`.  
**Typed optional conditions:** none as separate condition nodes; source-local hypotheses remain binding.

#### BH-IIF-C-0138 — Dilations on the metric cone (source 5444–5453)
**E1 source replay:** For g~ = dr²+r²g_base, Lie differentiation along r∂r gives 2dr²+2r²g_base, and r action commutes with SO4 on base.

**E3 independent matched verification:** Independent coordinate pullback under r→exp(t)r gives phi_t^*g~=exp(2t)g~ for any fixed round base metric.

**E4 adversarial scope / mutation check:** Either round or unit-radius base gives homothety; no claim of RG dynamics or unique flat cone metric follows. Keep radial/base normalization explicit.

**Exact imported source labels:** none in this route.  
**Typed optional conditions:** none as separate condition nodes; source-local hypotheses remain binding.

#### BH-IIF-C-0139 — Finite spectral traces versus unregularized infinite trace (source 5464–5474)
**E1 source replay:** Positive elliptic scalar Laplacian on compact S3 has finite-multiplicity discrete spectrum and e^{-tΔ} trace class for t>0.

**E3 independent matched verification:** Explicit S3 eigenvalues k(k+2)/R² and multiplicities (k+1)² yield convergent sum at t>0, divergent sum at t=0.

**E4 adversarial scope / mutation check:** Compactness does not by itself make Tr I or all vacuum energies finite.

**Exact imported source labels:** none in this route.  
**Typed optional conditions:** none as separate condition nodes; source-local hypotheses remain binding.

#### BH-IIF-C-0140 — Cone weights, phase isometry and Hopf/contact normalization (source 5476–5515)
**E1 source replay:** Direct cone Laplace radial separation yields k(k+2)−α(α+2), hence α=k or −k−2 only for harmonic extension; normalized η and Chern sign depend on chosen Hopf representative.

**E3 independent matched verification:** Independent radial derivative and spherical-harmonic calculation; η∧dη/vol ratio 2/R for normalized round Hopf coframe.

**E4 adversarial scope / mutation check:** Laplacian eigenvalue alone does not generate a scaling dimension; no chosen orientation or physical charge is implied by the Chern magnitude.

**Exact imported source labels:** none in this route.  
**Typed optional conditions:** none as separate condition nodes; source-local hypotheses remain binding.

#### BH-IIF-C-0141 — Paper~I-A rigidity of the Hopf/contact data (source 5516–5528)
**E1 source replay:** Source imports Paper I-A Hopf class and tight-contact isotopy, conditions the Reeb form on representative, orientation and normalization.

**E3 independent matched verification:** Circle bundles over S² have first Chern class as isomorphism classifier, while Hopf absolute charge 1 and Reeb uniqueness follow once contact form is chosen.

**E4 adversarial scope / mutation check:** Do not infer an oriented physical charge, a preferred axis, or uniqueness of arbitrary contact forms from the unmarked round metric.

**Exact imported source labels:** none in this route.  
**Typed optional conditions:** none as separate condition nodes; source-local hypotheses remain binding.

#### BH-IIF-C-0142 — Group-valued momentum table and local BCH truncation (source 5538–5628)
**E1 source replay:** SU2 non-Abelian multiplication and local exponential chart yield BCH to cubic brackets with quartic remainder.

**E3 independent matched verification:** Independent su2 Pauli commutator and near-origin analytic BCH confirm 1/2 and 1/12 coefficients with local bounded remainder.

**E4 adversarial scope / mutation check:** BCH is local, and one-chiral group multiplication differs from Spin4 symmetric-pair transvections P_i; no global log or Cartesian bounded coordinates claimed.

**Exact imported source labels:** `p2:def:composition-versus-transvection`.  
**Typed optional conditions:** none as separate condition nodes; source-local hypotheses remain binding.

#### BH-IIF-C-0143 — Sector-dependent finite-coordinate Robertson bound (source 5655–5670)
**E1 source replay:** Apply Robertson to bounded Hermitian X_mu,P_i; substitute Sigma definition and [P_i,P_j]= i hbar eps_ijk J_k/R².

**E3 independent matched verification:** Independent Cauchy-Schwarz/variance derivation and explicit spinor Clifford commutator reproduce the factors R²/2 and hbar/(2R²).

**E4 adversarial scope / mutation check:** A state with vanishing commutator expectation has a trivial lower bound; theorem makes no nonzero universal minimum.

**Exact imported source labels:** `p2:def:compact-momentum-generators`.  
**Typed optional conditions:** none as separate condition nodes; source-local hypotheses remain binding.

#### BH-IIF-C-0144 — Protected spinor coordinate-uncertainty bound (source 5677–5714)
**E1 source replay:** For gamma>0 the extremal spin-density involution -iC_mu C_nu anticommutes with C_mu,C_nu, forcing zero means and gamma² variances.

**E3 independent matched verification:** Independent Clifford involution spectra and exact 4x4 products verify ±2gamma²/R² eigenvalues, exact Robertson saturation, and the gamma=0 boundary.

**E4 adversarial scope / mutation check:** Do not identify the scalar invariant vector with a dynamical vacuum; coordinate eigenstates yield zero variance and rule out state-independent positive precision.

**Exact imported source labels:** `p2:prop:X_spinor_block`, `p2:cor:protected-phase-normalization-freedom`.  
**Typed optional conditions:** none as separate condition nodes; source-local hypotheses remain binding.

#### BH-IIF-C-0145 — Diagonal decomposition of the derived momentum carrier (source 5772–5797)
**E1 source replay:** Restrict each Spin4 representation to diagonal SU2: (1/2,1/2)→0⊕1, other source sectors go to 0,1/2,1 as printed.

**E3 independent matched verification:** Independent Clebsch-Gordan multiplicity tally yields (dimM0,dimM1/2,dimM1)=(2,2,3), with total dimension 2+4+9=15.

**E4 adversarial scope / mutation check:** Diagonal center (-1,-1) is not single-chiral composition center (-1,1); do not transfer parity blindness between them.

**Exact imported source labels:** none in this route.  
**Typed optional conditions:** none as separate condition nodes; source-local hypotheses remain binding.

#### BH-IIF-C-0146 — No single-fiducial full-module frame (source 5799–5802)
**E1 source replay:** Use the deferred Schur proof at lines 6013–6025: one rank-one orbit has a multiplicity-space reduced density of rank ≤dimV_ell.

**E3 independent matched verification:** For ell=0 with dimV=1 and dimM=2, one orbit has rank≤1 after any uniform Haar twirl, never I_M0.

**E4 adversarial scope / mutation check:** Source remark limits the theorem to rank-one Haar-uniform diagonal action on all H1. A nonuniform/different action or a multi-orbit frame is outside the no-go.

**Exact imported source labels:** `p2:def:diag-decomp-H1`.  
**Typed optional conditions:** none as separate condition nodes; source-local hypotheses remain binding.

#### BH-IIF-C-0147 — Scope of the single-orbit obstruction (source 5809–5811)
**E1 source replay:** Explicitly narrows the no-single-fiducial claim to Haar-uniform diagonal SU2 rank-one orbits.

**E3 independent matched verification:** Schur multiplicity rank obstruction is no statement about arbitrary nonuniform effects, different covariance actions, or smaller irreducible subspaces.

**E4 adversarial scope / mutation check:** Avoid misreading a group orbit no-go as a universal finite POVM no-go.

**Exact imported source labels:** `p2:prop:no-single-fiducial-povm`.  
**Typed optional conditions:** none as separate condition nodes; source-local hypotheses remain binding.

#### BH-IIF-C-0148 — Multi-fiducial finite-coordinate coherent POVM (source 5813–5843)
**E1 source replay:** Define sectorwise fiducial ket and positive operator measure with d_ell/Vol Haar normalization.

**E3 independent matched verification:** Schur twirl formula assigns I_{Vell}⊗|e_a><e_a| to each fiducial under the specified coefficient, so defining density is positive and finite.

**E4 adversarial scope / mutation check:** Haar convention is fixed explicitly; no selection of a physical apparatus or nonzero coordinate moment is part of the definition.

**Exact imported source labels:** `p2:def:diag-decomp-H1`.  
**Typed optional conditions:** none as separate condition nodes; source-local hypotheses remain binding.

#### BH-IIF-C-0149 — Diagonal-$SU(2)$-covariant multi-fiducial identity resolution (source 5845–5851)
**E1 source replay:** Schur averaging integral of a rank-one projector on V_ell equals Vol/d_ell I_{Vell}; summing over multiplicity bases resolves I_H1.

**E3 independent matched verification:** Independently apply Schur orthogonality to all three diagonal isotypic pieces and verify exact 2+4+9-dimensional identity.

**E4 adversarial scope / mutation check:** Normalization/covariance does not imply faithfulness of antipodal labels or match a chosen nonzero X_a as first moment.

**Exact imported source labels:** `p2:def:multi-fiducial-povm`.  
**Typed optional conditions:** none as separate condition nodes; source-local hypotheses remain binding.

#### BH-IIF-C-0150 — Diagonal-label center blindness and vanishing odd moments of the sectorwise frame (source 5867–5886)
**E1 source replay:** Use deferred proof lines 6027–6038: each sector fiducial has one diagonal-center parity, so projector density is even.

**E3 independent matched verification:** Independently under g↦-g, the action contributes a scalar sign in each single ell component, cancelling in |ket><ket|; odd coordinates integrate to zero.

**E4 adversarial scope / mutation check:** This parity result is for the diagonal label group, not for one-chiral composition, and does not cover mixed-parity two-orbit fiducials.

**Exact imported source labels:** `p2:def:multi-fiducial-povm`.  
**Typed optional conditions:** none as separate condition nodes; source-local hypotheses remain binding.

#### BH-IIF-C-0151 — Faithful full-\(S_B^3\) localization firewall (source 5893–5904)
**E1 source replay:** If the physical position test is required to distinguish g and -g, any even diagonal-label POVM identifies outcomes and cannot realize that exact faithful readout.

**E3 independent matched verification:** Independent quotient-map test: E(-B)=E(B) for all B implies image factors through S3/{±1}≈SO3, contradicting an injective antipodal position label map.

**E4 adversarial scope / mutation check:** No general mandate that all physical localization apparatus be faithful or exact first-moment matched is asserted; occurrence remains separate.

**Exact imported source labels:** `p2:cor:sectorwise-povm-center-blind`.  
**Typed optional conditions:** `BH-IIF-A-0025`, `BH-IIF-A-0024`.

#### BH-IIF-C-0152 — Minimal diagonal-label-center-sensitive two-orbit frame (source 5906–5945)
**E1 source replay:** Partial trace of two explicitly displayed fiducials gives (1,2I2,3I3) on stabilizer multiplicity blocks, resolving identity by Schur averaging.

**E3 independent matched verification:** Independent two-orbit reduced-density and center-parity check: both orbit norms 15/2, I_M0 rank two, mixed integer/half-integer cross block survives.

**E4 adversarial scope / mutation check:** One orbit fails because M0 has rank 2; the construction does not establish moment matching to a specific X_a or minimal outcomes for unrelated POVMs.

**Exact imported source labels:** `p2:def:diag-decomp-H1`.  
**Typed optional conditions:** none as separate condition nodes; source-local hypotheses remain binding.

#### BH-IIF-C-0153 — Protected diagonal-irrep coherent projections (source 5986–6002)
**E1 source replay:** Protected chiral irreps restrict singly to diagonal V1/2, without the full H1 multiplicity obstruction.

**E3 independent matched verification:** An SU2 irreducible of dim2 has a normalized Haar single-orbit twirl 2|gv><gv|; charge-sector V_q is an unrelated decomposition.

**E4 adversarial scope / mutation check:** No full-module one-orbit identity or Hopf/Reeb charge sector coherent POVM is thereby proved.

**Exact imported source labels:** `p2:prop:no-single-fiducial-povm`.  
**Typed optional conditions:** none as separate condition nodes; source-local hypotheses remain binding.

#### BH-IIF-C-0154 — Ball-valued POVM saturation forces commutativity on the saturated vector (source 6046–6059)
**E1 source replay:** Naimark dilation E=V*PV and commutative Z_a yields positive sum of sphere-radius deficiency and leakage terms; zero on psi kills leakage Z_a Vpsi.

**E3 independent matched verification:** Independent operator Kadison inequality/stinespring multiplicative-domain-on-vector argument: saturation gives each Z_a Vpsi=VX_a psi and forces [Xa,Xb]psi=0.

**E4 adversarial scope / mutation check:** Commutativity is only on the saturated vector, not globally; strict ball support R and all first moments are essential.

**Exact imported source labels:** none in this route.  
**Typed optional conditions:** none as separate condition nodes; source-local hypotheses remain binding.

#### BH-IIF-C-0155 — Explicit Naimark saturation obstruction for X_D (source 6083–6102)
**E1 source replay:** Paper I-A scalar fingerprint saturates R² on e0 while two native coordinate edges give [X_a^D,X_b^D]e0=√2 R² w_ab/3 nonzero.

**E3 independent matched verification:** Independent wedge calculation from X_a e0=Ru_a/2 and X_a u_b=Rδ_ab e0/2+(√2 R/3) w_ab reproduces the commutator.

**E4 adversarial scope / mutation check:** This excludes exact X_D first moments in classical ball radius R, but not POVMs of radius≥√3R or approximate/unmatched apparatus.

**Exact imported source labels:** `p2c:prop:exact-intrinsic-classical-moment-no-go`, `p2c:lem:povm-ball-saturation-commutativity`.  
**Typed optional conditions:** none as separate condition nodes; source-local hypotheses remain binding.

#### BH-IIF-C-0156 — Classical moment radius for the full coordinate atlas (source 6112–6207)
**E1 source replay:** Sphericalize ball POVM without changing first moments; Spin4 covariantize. Stabilizer singlet/triplet/half-spin seeds obey a+3B=4, a≥b² and B≥d±², |4rho/r|≤1.

**E3 independent matched verification:** Independent Schur complement gives r²≥R²+6max(r+²,r-²) and r≥4rho; construct K_geo(q)⊕K_sp(q), verify positivity and all first moments using rational Haar moments.

**E4 adversarial scope / mutation check:** General necessity is for all normalized ball-valued measures, not only a preset polynomial density; r is an outcome-domain radius, not a generated momentum metric or apparatus.

**Exact imported source labels:** `p2:cor:h1-coordinate-classification`, `p2:prop:geo-coordinate-admissibility-checks`, `p2:prop:X_spinor_block`.  
**Typed optional conditions:** none as separate condition nodes; source-local hypotheses remain binding.

#### BH-IIF-C-0157 — Intrinsic optimal-radius endpoint eigenvalues and lower trace bound (source 6209–6239)
**E1 source replay:** Native r+=r−=√2R/3 and rho=√3R/4 make max bounds sqrt(7/3)R and sqrt3R; explicit K0 has PSD eigenvalues and trace witness.

**E3 independent matched verification:** Independent Clifford trace ∫Tr((x·C)Esp)=16rho=4sqrt3R≤4r gives r≥sqrt3R, while direct K_c pointwise eigenvalues check attainment.

**E4 adversarial scope / mutation check:** Endpoint positivity and radius are mathematical POVM facts, not proof of physical occurrence of a radius or chosen measurement channel.

**Exact imported source labels:** `p2c:thm:full-atlas-povm-radius`.  
**Typed optional conditions:** none as separate condition nodes; source-local hypotheses remain binding.

#### BH-IIF-C-0158 — Finite Hurwitz-support attainment (source 6241–6264)
**E1 source replay:** Evaluate the positive polynomial K(q) on H24; its constant/linear normalization integrands have degree≤3, so 5-design quadrature preserves them.

**E3 independent matched verification:** Independent exact rational check of all 126 S3 monomials of degree≤5 on the 24 Hurwitz points, plus explicit 15x15 sampled density normalization and moments.

**E4 adversarial scope / mutation check:** A fixed 24-point subset is not Spin4-invariant; covariance is across transported support family, and the 5-design is not 8-design for all quartic degree-two observables.

**Exact imported source labels:** `p2c:thm:full-atlas-povm-radius`.  
**Typed optional conditions:** none as separate condition nodes; source-local hypotheses remain binding.

#### BH-IIF-C-0159 — Positive covariant map with the sharp harmonic kernel (source 6266–6294)
**E1 source replay:** K is polynomial degree≤2; Haar orthogonality kills E_k for k≥3, while E0,E1 and E2 maps are nonzero and distinct irreducible types.

**E3 independent matched verification:** Independent exact fourth moment gives Phi(q1²−q2²)|V=diag(1,-1,0,0)/27; numerical rank of the degree≤2 map is 14.

**E4 adversarial scope / mutation check:** The all-band kernel concerns continuous Haar integration. Sampling at 24 points may alias higher harmonics; positivity/CP does not make Φ multiplicative.

**Exact imported source labels:** `p2c:thm:full-atlas-povm-radius`.  
**Typed optional conditions:** none as separate condition nodes; source-local hypotheses remain binding.

#### BH-IIF-C-0160 — Quaternion-support attainment and its subgroup domain (source 6302–6335)
**E1 source replay:** Q8 has strength-three spherical sampling. K degree≤2 makes normalizations and first moments degree≤3; cyclic finite SU2 subgroup lies in a real 2-plane.

**E3 independent matched verification:** Exact rational cubature over Q8 through total degree3 and 15x15 K sample identities; Clifford linear independence prohibits a 2-plane exact four-vector moment.

**E4 adversarial scope / mutation check:** Minimum eight is among finite subgroup supports, not arbitrary finite POVMs; different incomparable noncyclic subgroups prevent a subgroup least element.

**Exact imported source labels:** `p1b:thm:v233-subgroup-sampler-classification`, `p2c:thm:full-atlas-povm-radius`.  
**Typed optional conditions:** none as separate condition nodes; source-local hypotheses remain binding.

#### BH-IIF-C-0161 — Complete covariant seeds on the optimal intrinsic sphere (source 6337–6398)
**E1 source replay:** All Spin4-covariant endpoint measures are stabilizer-seed transports. S0 positivity gives a≥4/3; T0 Schur complement gives u=d²/B≤1, |zeta-u|≤1-u and a≤20/9.

**E3 independent matched verification:** Independent Schur-complement algebra, polynomial wedge/Hodge form, and 5×5 boundary/random complex seed PSD checks give precisely the asserted three-real-dimensional disk family.

**E4 adversarial scope / mutation check:** Do not extend classification to interior-support ball measures or instruments; no uniqueness of a physical detector or of the integration map follows from first moments.

**Exact imported source labels:** `p2c:thm:full-atlas-povm-radius`.  
**Typed optional conditions:** none as separate condition nodes; source-local hypotheses remain binding.

#### BH-IIF-C-0162 — A real endpoint slice with fixed native first moments (source 6407–6464)
**E1 source replay:** At a=4/3 the tangent/two-form 2×2 principal minors require 3c−1≥0; complement two-form block requires 1−c≥0.

**E3 independent matched verification:** Independent eigenvalue check of K_c(e4) and exact S3 fourth moments reproduce c∈[1/3,1], vector map D/27 and two-form c diag(0,1,1,-1,-1,0)/6.

**E4 adversarial scope / mutation check:** Changing c changes quadratic images without changing native coordinate moments; finite Q8 quadrature is only 3-design and not a full quadratic-map equality.

**Exact imported source labels:** `p2c:thm:complete-intrinsic-endpoint-seeds`.  
**Typed optional conditions:** none as separate condition nodes; source-local hypotheses remain binding.

#### BH-IIF-C-0163 — Finite sampling exactness stops at its cubature degree (source 6466–6472)
**E1 source replay:** K polynomial degree≤2: first-moment integrands degree≤3, quadratic-symbol integrands degree≤4, quartic tests of degree-two fields reach degree8.

**E3 independent matched verification:** Independent monomial degree counts and explicit Q8 fourth moment mismatch show Q8 preserves first moments but not quadratic map; H24 degree5 does.

**E4 adversarial scope / mutation check:** Do not elevate an eight-point or 24-point exact first moment to all-band equality or degree-eight exactness.

**Exact imported source labels:** `p2c:cor:v233-optimal-quaternion-povm`, `p2c:cor:optimal-hurwitz-povm`.  
**Typed optional conditions:** none as separate condition nodes; source-local hypotheses remain binding.

#### BH-IIF-C-0164 — Map-independent total readout noise at the optimal sphere (source 6474–6492)
**E1 source replay:** Sphere radius sqrt3R enforces sum x_a²=3R² on all effects, so total noise is 3R² I−Q_D.

**E3 independent matched verification:** Subtract each independently known Q_D eigenvalue: obtain 2,25/12,23/9,23/9,9/4,9/4 times R².

**E4 adversarial scope / mutation check:** Total readout noise is invariant across endpoint maps but individual quadratic readouts are not; it is not the intrinsic operator variance.

**Exact imported source labels:** `p2c:thm:intrinsic-tangential-coordinate-class`.  
**Typed optional conditions:** none as separate condition nodes; source-local hypotheses remain binding.

#### BH-IIF-C-0165 — Fixed-map ranks and family-independent readout (source 6496–6526)
**E1 source replay:** All K are degree≤2; the coefficient a−B=4(a−1)/3 never vanishes on admitted a≥4/3, so E2 image is injective.

**E3 independent matched verification:** Independent polynomial-moment map rank control gives 1+4+9=14, while the real-slice c difference injectively detects any nonzero E2 symbol.

**E4 adversarial scope / mutation check:** Do not confuse fixed operator-word X^D invariance with equality of every classical quadratic symbol map, or the common five nonzero readouts with full map equality.

**Exact imported source labels:** `p2c:thm:complete-intrinsic-endpoint-seeds`, `p2c:prop:v233-endpoint-map-family`.  
**Typed optional conditions:** none as separate condition nodes; source-local hypotheses remain binding.

#### BH-IIF-C-0166 — Full quadratic endpoint-POVM exactness if and only if fourth-degree cubature (source 6529–6571)
**E1 source replay:** K density degree≤2 makes weighted 4-design sufficient; scalar block 1 fixes degree≤2 moments and vector coefficient a−B>0 forces all ν(f q_i q_j)=σ values.

**E3 independent matched verification:** Independent monomial splitting shows degree≤4 generated by P2 and P2·q_iq_j, while weighted evaluation isometry on P2 is equivalent to product degree4 exactness.

**E4 adversarial scope / mutation check:** At forbidden a=1 the converse can fail, but all admitted a≥4/3 exclude this; a Q8 3-design is a counterexample to quadratic-map exactness, not to first moments.

**Exact imported source labels:** `p1b:lem:v233-weighted-band-products`, `p2c:thm:complete-intrinsic-endpoint-seeds`.  
**Typed optional conditions:** none as separate condition nodes; source-local hypotheses remain binding.

#### BH-IIF-C-0167 — Universal factor-three quaternionic quadratic-readout defect (source 6573–6594)
**E1 source replay:** For f=q1²−q2² use q_i^4 and q_i²q_j² moments of Q8 and Haar to isolate vector-block coefficient.

**E3 independent matched verification:** Exact rational moments give Q8(fqq*)=D/4 versus Haar D/12 for all allowed a, so the Q8 vector quadratic image is precisely factor3.

**E4 adversarial scope / mutation check:** This does not invalidate Q8 8-outcome normalization or native first moments; H24/2T is a 5-design and preserves the quadratic map.

**Exact imported source labels:** `p2c:thm:v268-endpoint-quadratic-iff-design4`.  
**Typed optional conditions:** none as separate condition nodes; source-local hypotheses remain binding.

### Issue adjudication and inherited frontier
- **New confirmed gaps:** none. There is no conjectural new repair inserted into the framework. Any scope not checked after line 6599 remains `NOT_AUDITED`.
- The earlier unresolved Paper II-A finite-port condition remains at its original node; this batch does not re-evaluate or close it.
- No physical existence or moment matching is inferred from covariant POVM existence, normalization, or finite cubature. The source explicitly forbids this conflation.
- One rank-one orbit cannot saturate the scalar two-copy multiplicity resolution. Center-blind frames cannot realize an *optionally* faithful full S3 role, but need not be faulty apparatus in other roles.
- The continuous endpoint POVM seed family fixes first moments but is not unique as a quadratic measurement map. Q8 quadratic aliasing is an exact counterexample, not a normalization defect.
- Keep cone radial metrics and Hopf orientations in their stated normalization; neither selects an RG flow nor a physical particle identification.

### Reproducible controls and completeness
`Proofs/Paper2F-Batch5-v1_1-verify.py` reproduces `307` distinct exact rational/symbolic and `854` numerical controls. These run alongside source-specific E1/E3/E4 textual certificates.
**Coverage remains PARTIALLY_AUDITED:** 167 total source-claim objects / 156 of 223 formal declarations; 67 formal declarations from line 6600 onward remain `NOT_AUDITED`.
**Next batch:** Paper II-F source line 6600.

---

## Batch 6 verdict and proof route (v1.61 source lines 6600–8466)
**47 source-bound audit records:** 39 formal declarations and eight line-anchored material proof/interfaces. **{'VERIFIED': 20, 'FORMALIZED': 7, 'VERIFIED-CONDITIONAL': 20}**. No newly confirmed mathematical error. Precisely seven source-scoped optional conditions are registered as conditions rather than new physical axioms.
**Independent replay:** 983/983 exact finite symbolic/rational/matrix checks passed, including 600-cell/2I character sums, 2T natural adjacency and cubature, scalar zeta residue, Fourier/Berry holonomies, and signed RS Casimir branches. These finite checks corroborate, not universally prove, the source results.
**Critical proof dependency:** Cross-check Proposition `p2:prop:rs-spectrum-cross-check` uses Theorem `p2f:thm:v260-signed-rs-s3` for the A-series conclusion. Conversely, the theorem imports only the independent Frobenius/CG/twistor subproof from lines 7827–7865, recorded separately as a material proof unit. It does not import the full proposition. The DAG must avoid an artificial whole-proposition cycle.
**Physical frontier:** No finite support, exceptional group, oscillator spectrum, Berry winding, finite response, or natural Hurwitz intertwiner is treated as a new physical particle occurrence or momentum-seed selection. Existing Paper II-B carrier and m_p=1 are unchanged.
### Batch 6 complete source-object census
| Claim | Source lines | Exact source result | Verdict |
|---|---:|---|---|
| `BH-IIF-C-0168` | 6603–6646 | Exact finite-fibre barycentre of a continuous endpoint POVM (`p2f:thm:v273-finite-fibre-povm-barycentre`) | VERIFIED |
| `BH-IIF-C-0169` | 6648–6693 | Twin-icosahedral Reynolds mean and exact non-idempotence (`p2f:thm:v273-twin-projector-spectral-identity`) | VERIFIED |
| `BH-IIF-C-0170` | 6695–6718 | Unmarked twirl gives a scalar trace fraction, not a sharp projector (`p2f:cor:v273-icosahedral-projector-twirl`) | VERIFIED |
| `BH-IIF-C-0171` | 6720–6738 | Sharp distinction between cubature and invariant-sector readouts (`p2f:rem:v273-finite-readout-versus-projection`) | FORMALIZED |
| `BH-IIF-C-0172` | 6748–6764 | Historical selector nonpremise (`Paper2F:source-MATERIAL-6748`) | FORMALIZED |
| `BH-IIF-C-0173` | 6765–6808 | Displayed background classes of this paper (`Paper2F:source-REMARK-6765`) | FORMALIZED |
| `BH-IIF-C-0174` | 6810–6826 | Renormalization and dispersion scope tuples (`Paper2F:source-MATERIAL-6810`) | FORMALIZED |
| `BH-IIF-C-0175` | 6827–6881 | Downstream dispersion domain and distinct speed symbols (`p2d:rem:dispersion-speed-details`) | VERIFIED-CONDITIONAL |
| `BH-IIF-C-0176` | 6884–6923 | Classical scalar spectral finite-part prescription conditional on free dispersion (`p2:prop:casimir-classical`) | VERIFIED-CONDITIONAL |
| `BH-IIF-C-0177` | 6948–7018 | Exact finite spectral oscillator sums under a typed dispersion (`p2:prop:casimir-fuzzy`) | VERIFIED-CONDITIONAL |
| `BH-IIF-C-0178` | 7046–7058 | Real intertwiner frames and the time-reversal cycle criterion (`p2d:lem:time-reversal-cycle-criterion`) | VERIFIED-CONDITIONAL |
| `BH-IIF-C-0179` | 7113–7120 | Antipodal Eigenstates (`p2:cor:antipodal-eigenstates`) | VERIFIED |
| `BH-IIF-C-0180` | 7125–7132 | An anti-unitary square is invariant under scalar rephasing (`p2:lem:antiunitary-phase-square`) | VERIFIED |
| `BH-IIF-C-0181` | 7145–7172 | Externally supplied two-state exchange (`p2:prop:independent-internal-doublet`) | VERIFIED-CONDITIONAL |
| `BH-IIF-C-0182` | 7185–7215 | Protected module versus real operator Clifford complement (`Paper2F:source-MATERIAL-7185`) | VERIFIED |
| `BH-IIF-C-0183` | 7216–7233 | Diagonal-weight projection (`p2:prop:diagonal-weight-projection`) | VERIFIED |
| `BH-IIF-C-0184` | 7252–7263 | Diagonal-weight isolation of the protected carrier at \(m=1\) (`p2:cor:protected-diagonal-weight-carrier`) | VERIFIED |
| `BH-IIF-C-0185` | 7283–7341 | Projected Reeb-weight doubled-orbit data (`p2:def:berry-connection`) | FORMALIZED |
| `BH-IIF-C-0186` | 7350–7361 | Arbitrary-real Reeb-form diagnostic (`p2d:prop:arbitrary-real-reeb-form-diagnostic`) | VERIFIED |
| `BH-IIF-C-0187` | 7370–7391 | Global Berry trivialization on \(S^3\) (`p2:lem:global-berry-trivialization`) | VERIFIED |
| `BH-IIF-C-0188` | 7419–7437 | Integrality on a constant-ray principal orbit (`p2:cor:global-berry-weight-integrality`) | VERIFIED-CONDITIONAL |
| `BH-IIF-C-0189` | 7457–7464 | Hopf normalization (`p2:lem:hopf-normalization`) | VERIFIED |
| `BH-IIF-C-0190` | 7470–7487 | Homogeneous uniqueness of the Reeb-normalized connection (`p2:rem:berry-connection-status`) | VERIFIED-CONDITIONAL |
| `BH-IIF-C-0191` | 7500–7514 | Conditional global homogeneous Berry normalization (`p2d:cor:global-homogeneous-berry-normalization`) | VERIFIED-CONDITIONAL |
| `BH-IIF-C-0192` | 7530–7555 | Fibre-basic Berry integral without homogeneity (`p2d:cor:fibre-basic-berry-cs`) | VERIFIED-CONDITIONAL |
| `BH-IIF-C-0193` | 7588–7605 | \texorpdfstring{$\mathbb{CP}^1$}{CP1} geometric quantization (`p2:cor:cp1-geometric-quantization`) | VERIFIED-CONDITIONAL |
| `BH-IIF-C-0194` | 7620–7622 | Unlabelled remark at source line 7620 (`Paper2F:source-REMARK-7620`) | FORMALIZED |
| `BH-IIF-C-0195` | 7630–7635 | Geodesic Closure (`p2:prop:geodesic-closure`) | VERIFIED |
| `BH-IIF-C-0196` | 7641–7652 | Momentum-space geodesic-parameter periodicity (`p2:cor:momentum-space-geodesic-periodicity`) | VERIFIED |
| `BH-IIF-C-0197` | 7668–7690 | Magnetic Monopole Analogy (`p2:prop:monopole`) | VERIFIED |
| `BH-IIF-C-0198` | 7715–7728 | Constant-annihilating form counterfamily (`p2d:prop:form-zero-order-counterfamily`) | VERIFIED |
| `BH-IIF-C-0199` | 7771–7824 | Representation-theoretic cross-check of the Rarita--Schwinger import (`p2:prop:rs-spectrum-cross-check`) | VERIFIED-CONDITIONAL |
| `BH-IIF-C-0200` | 7827–7865 | Independent RS representation-and-twistor subproof (`Paper2F:source-MATERIAL-7827`) | VERIFIED-CONDITIONAL |
| `BH-IIF-C-0201` | 7875–7958 | Direct signed Rarita--Schwinger spectrum from the round parent (`p2f:thm:v260-signed-rs-s3`) | VERIFIED |
| `BH-IIF-C-0202` | 7959–7965 | Domain and provenance of the signed derivation (`Paper2F:source-REMARK-7959`) | FORMALIZED |
| `BH-IIF-C-0203` | 7970–7978 | Coordinate-generated rotations and native Casimir scope (`Paper2F:source-MATERIAL-7970`) | VERIFIED-CONDITIONAL |
| `BH-IIF-C-0204` | 7979–7998 | Coefficient errors on a supplied kinetic pair (`p2d:prop:v226-coefficient-spectral-error`) | VERIFIED-CONDITIONAL |
| `BH-IIF-C-0205` | 8010–8023 | Complete frequency comparison has finite tests (`p2d:cor:v227-frequency-tests`) | VERIFIED-CONDITIONAL |
| `BH-IIF-C-0206` | 8052–8115 | Legacy carrier-selection diagnostic and fixed-action closure alternative (`p2e:prop:carrier-selection-boundary`) | VERIFIED-CONDITIONAL |
| `BH-IIF-C-0207` | 8156–8173 | Joint-family condition graph of legacy carrier supports (`Paper2F:source-MATERIAL-8156`) | VERIFIED-CONDITIONAL |
| `BH-IIF-C-0208` | 8183–8210 | Exact protected-scale specializations (`p2e:cor:protected-scale-branches`) | VERIFIED-CONDITIONAL |
| `BH-IIF-C-0209` | 8221–8243 | Optional factorized protected-channel representative (`Paper2F:source-MATERIAL-8221`) | VERIFIED-CONDITIONAL |
| `BH-IIF-C-0210` | 8244–8289 | Unlabelled proposition at source line 8244 (`p2e:prop:joint-protected-scale-loci`) | VERIFIED-CONDITIONAL |
| `BH-IIF-C-0211` | 8309–8344 | Unlabelled proposition at source line 8309 (`p2e:prop:empty-spinor-species-rescaling-locus`) | VERIFIED |
| `BH-IIF-C-0212` | 8356–8372 | Natural 2T fixed-space nonisomorphism boundary (`Paper2F:source-MATERIAL-8356`) | VERIFIED |
| `BH-IIF-C-0213` | 8373–8429 | Sharp rank of the natural Hurwitz comparison (`p2e:prop:sharp-natural-2t-rank`) | VERIFIED |
| `BH-IIF-C-0214` | 8431–8446 | Natural scalar-Hurwitz blindness to the left chiral adjoint (`p2e:cor:v261-natural-hurwitz-v3-blindness`) | VERIFIED |

### Source-first independent proof certificates (E1/E3/E4)

#### BH-IIF-C-0168 — Exact finite-fibre barycentre of a continuous endpoint POVM (6603–6646)
**E1 source replay:** Coset-independent atomic POVM follows from right Gamma permutation; a spherical t-design integrates each degree-two K; Haar disintegration yields equality of every Borel-event barycentre.
**E3 independent verification:** Exact Hurwitz 24-vertex moments through degree five independently reproduce normalized quadratic and cubic integrals.
**E4 adversarial domain gate:** Coset POVMs are mathematical and only low-degree individual moments match; Borel-event identity holds after the quotient integral, not per fibre.
**Direct proof imports:** none.  
**Canonical source-scope conditions:** none beyond the stated theorem-local domain.

#### BH-IIF-C-0169 — Twin-icosahedral Reynolds mean and exact non-idempotence (6648–6693)
**E1 source replay:** Imported I-plus/I-minus twin-completion theorem supplies the pair relative to H; character average fixes ranks and overlap; involution decomposition gives the coefficients.
**E3 independent verification:** Constructed exact 120 golden-ratio quaternions: fixed ranks H=2,O=1,I=1 and U12(a gamma) mean -5/16; squared eigenvalues give -231/1024.
**E4 adversarial domain gate:** A_H is not an idempotent or an occurrence selector; dimensions and scalar multiplicities refer only to Sym12 and E12.
**Direct proof imports:** `p1:thm:v273-two-icosahedral-completions`.  
**Canonical source-scope conditions:** none beyond the stated theorem-local domain.

#### BH-IIF-C-0170 — Unmarked twirl gives a scalar trace fraction, not a sharp projector (6695–6718)
**E1 source replay:** Twirl on irreducible left V has scalar factor fixed by trace rank; the right factor is unchanged.
**E3 independent verification:** At k=12 rank(P_I)=13, full shell=169, twirl I/13 of rank 169; exact trace ratio 1/13.
**E4 adversarial domain gate:** A rank-169 scalar twirl cannot be identified with rank-13 sharp projector, even with the same trace fraction.
**Direct proof imports:** `p2f:thm:v273-twin-projector-spectral-identity`.  
**Canonical source-scope conditions:** none beyond the stated theorem-local domain.

#### BH-IIF-C-0171 — Sharp distinction between cubature and invariant-sector readouts (6720–6738)
**E1 source replay:** Remark explicitly contrasts cubature on finite designs and sharp invariant-sector projection, with a separate physical constructor bridge.
**E3 independent verification:** Degree-five 2T and degree-eleven 2I finite moments can be exact while a nontrivial projector remains finite-rank, confirming type separation.
**E4 adversarial domain gate:** Neither finite quadrature nor operator availability establishes a physical comb or labelled icosahedral branch.
**Direct proof imports:** `p1b:thm:v273-triple-icosahedral-nineteen-design`, `p1:cor:v273-twins-sharp-common-invariants`.  
**Canonical source-scope conditions:** none beyond the stated theorem-local domain.

#### BH-IIF-C-0172 — Historical selector nonpremise (6748–6764)
**E1 source replay:** Current host seed H1,m_p=1 is independent of TWR/SPEX and E9; appendix is explicitly historical.
**E3 independent verification:** Dimension 9 E9 != 15 H1 independent of declared-stage supports.
**E4 adversarial domain gate:** Do not add former selector paths as source-required proof ancestry.
**Direct proof imports:** none.  
**Canonical source-scope conditions:** none beyond the stated theorem-local domain.

#### BH-IIF-C-0173 — Displayed background classes of this paper (6765–6808)
**E1 source replay:** Historical TWR/SPEX/E9 and background classes are explicitly declared nonpremises of the II-B momentum host derivation.
**E3 independent verification:** A nine-dimensional E9 sublevel and a fifteen-dimensional H1 are distinct finite supports despite the same declared tower schema.
**E4 adversarial domain gate:** Do not import retired selector conditions into the constituted m_p=1 proof.
**Direct proof imports:** none.  
**Canonical source-scope conditions:** none beyond the stated theorem-local domain.

#### BH-IIF-C-0174 — Renormalization and dispersion scope tuples (6810–6826)
**E1 source replay:** REN and DISP are separate optional physical data, not intrinsic spectrum outputs.
**E3 independent verification:** Separate heat pole finite-part from ordinary finite oscillator sums.
**E4 adversarial domain gate:** A defined mathematical FP is not a selected physical REN scheme; neither tuple changes II-B seed.
**Direct proof imports:** none.  
**Canonical source-scope conditions:** `BH-IIF-A-0027`.

#### BH-IIF-C-0175 — Downstream dispersion domain and distinct speed symbols (6827–6881)
**E1 source replay:** Containment of identified field histories gives c_field <= c_op; equality uses named undeformed same-owner principal theorem.
**E3 independent verification:** Independent order relation: a subset supremum cannot exceed its parent; strict subsets show inequality need not be equality.
**E4 adversarial domain gate:** A photon or continuum operator identification and empirical clock are not obtained from kinematics alone.
**Direct proof imports:** `p2a:thm:undeformed-host-principal-inheritance`.  
**Canonical source-scope conditions:** none beyond the stated theorem-local domain.

#### BH-IIF-C-0176 — Classical scalar spectral finite-part prescription conditional on free dispersion (6884–6923)
**E1 source replay:** Under continuum scalar dispersion, lambda_k=k(k+2)/R^2 and d_k=(k+1)^2; a2=Vol/(2R^4) gives a genuine zeta pole and mathematically defined finite part.
**E3 independent verification:** Independent 3-sphere curvature invariant yields a2=pi^2/R; res at s=-1/2 equals -1/(16R), nonzero.
**E4 adversarial domain gate:** No analytic-continuation ordinary value at the pole; a physical vacuum energy still needs a renormalization owner; no continuum theorem is inferred from finite dispersion.
**Direct proof imports:** `p2:prop:spectral-zeta-continuation`.  
**Canonical source-scope conditions:** `BH-IIF-A-0026`.

#### BH-IIF-C-0177 — Exact finite spectral oscillator sums under a typed dispersion (6948–7018)
**E1 source replay:** Declared scalar dispersion yields diagonal k sum; separately DEFINED full-module frequencies yield distinct jL,jR sum.
**E3 independent verification:** Independent enumeration H1 dimension 15 and m=1 exact evaluation 4sqrt(3/2)+12+4sqrt3; no infinite subtraction needed.
**E4 adversarial domain gate:** The off-diagonal sum is a representative, not free scalar modes; operator identification and speed remain conditional.
**Direct proof imports:** none.  
**Canonical source-scope conditions:** `BH-IIF-A-0026`.

#### BH-IIF-C-0178 — Real intertwiner frames and the time-reversal cycle criterion (7046–7058)
**E1 source replay:** Anti-linear involution on one-dimensional intertwiner lines permits real frames; sector phases solve spanning forest exactly when cycle holonomies satisfy the criterion.
**E3 independent verification:** Independent phase-coboundary multiplication and T^2 invariance check; no nonzero coefficient is divided by zero.
**E4 adversarial domain gate:** The lift is assumed sector-preserving and edge graph multiplicity-free; cycle criterion is not a physical time reversal selector.
**Direct proof imports:** `p2d:prop:finite-completion-discrete-symmetry-scope`.  
**Canonical source-scope conditions:** none beyond the stated theorem-local domain.

#### BH-IIF-C-0179 — Antipodal Eigenstates (7113–7120)
**E1 source replay:** Degree-k homogeneous harmonic polynomial restricts to S3 and transforms by (-1)^k under x->-x.
**E3 independent verification:** Direct tests k=0,1,2 and polynomial homogeneity.
**E4 adversarial domain gate:** Antipodal Z2 differs from spatial parity fixing one coordinate.
**Direct proof imports:** none.  
**Canonical source-scope conditions:** none beyond the stated theorem-local domain.

#### BH-IIF-C-0180 — An anti-unitary square is invariant under scalar rephasing (7125–7132)
**E1 source replay:** Antiunitarity conjugates scalar z, giving (zT)^2=z conj(z) T^2.
**E3 independent verification:** Exact antiunitary square tests with Pauli-real T^2=-I and unit scalar phases.
**E4 adversarial domain gate:** Rephasing does not switch Kramers sign; different internal factor is a distinct construction.
**Direct proof imports:** none.  
**Canonical source-scope conditions:** none beyond the stated theorem-local domain.

#### BH-IIF-C-0181 — Externally supplied two-state exchange (7145–7172)
**E1 source replay:** Pauli sigma1 is unitary involution commuting with geometric tensor factors and anticommuting with sigma3.
**E3 independent verification:** Explicit 2x2 Pauli multiplication verifies all identities.
**E4 adversarial domain gate:** C2 internal factor is EXTERNALLY supplied, not generated Hopf charge.
**Direct proof imports:** none.  
**Canonical source-scope conditions:** `BH-IIF-A-0028`.

#### BH-IIF-C-0182 — Protected module versus real operator Clifford complement (7185–7215)
**E1 source replay:** Protected Sprot is 4 complex =8 real; grade complement seven belongs to the real operator algebra.
**E3 independent verification:** Independent dimensions 4C=8R, Cl(0,3) real8, nonidentity seven.
**E4 adversarial domain gate:** Do not assert a 15=8+7 Hilbert-space decomposition.
**Direct proof imports:** none.  
**Canonical source-scope conditions:** none beyond the stated theorem-local domain.

#### BH-IIF-C-0183 — Diagonal-weight projection (7216–7233)
**E1 source replay:** Four-pi Fourier averaging orthogonally selects each half-integral spectral eigenspace.
**E3 independent verification:** Exact 4pi Fourier orthogonality for weights -1,-1/2,0,1/2,1.
**E4 adversarial domain gate:** Two-pi period would alias half-integral phases; no physical low-energy interpretation follows.
**Direct proof imports:** none.  
**Canonical source-scope conditions:** none beyond the stated theorem-local domain.

#### BH-IIF-C-0184 — Diagonal-weight isolation of the protected carrier at \(m=1\) (7252–7263)
**E1 source replay:** Weight table dimensions (2,2) and Fourier projectors identify Spin4 module V(1/2,0)+V(0,1/2).
**E3 independent verification:** Independent finite Spin4 type accounting 4 complex=8 real, and full H1 has dimension 15.
**E4 adversarial domain gate:** The seven Clifford complement counts operator basis components, not a Hilbert 15=8+7 decomposition.
**Direct proof imports:** `p2:prop:diagonal-weight-projection`.  
**Canonical source-scope conditions:** none beyond the stated theorem-local domain.

#### BH-IIF-C-0185 — Projected Reeb-weight doubled-orbit data (7283–7341)
**E1 source replay:** Definition distinguishes r in half Z on the 4pi doubled orbit from a 2pi principal orbit Berry lift.
**E3 independent verification:** Exact holonomy e^{-4pi ir}=1 for all half-integer r; e^{-2pi ir}=-1 for odd halves.
**E4 adversarial domain gate:** A double-cover normalized lift does not create a global half-integer principal Berry one-form.
**Direct proof imports:** none.  
**Canonical source-scope conditions:** none beyond the stated theorem-local domain.

#### BH-IIF-C-0186 — Arbitrary-real Reeb-form diagnostic (7350–7361)
**E1 source replay:** Quadratic CS scaling Q[r eta]=r^2 Q[eta], independent of whether r is integral.
**E3 independent verification:** Exact algebra r=+/-1/2 yields 1/4 and q=+/-1 gives 1.
**E4 adversarial domain gate:** Quadratic diagnostic is not the global Berry invariant of half-integer projected data.
**Direct proof imports:** `p2:prop:hopfion-charge`.  
**Canonical source-scope conditions:** none beyond the stated theorem-local domain.

#### BH-IIF-C-0187 — Global Berry trivialization on \(S^3\) (7370–7391)
**E1 source replay:** H2(S3;Z)=0 trivializes the pullback line; H1(S3;Z)=0 gives global phase chi, and exact gauge correction integrates to zero.
**E3 independent verification:** Independent first cohomology and Stokes check of A-dchi; no large U1 gauge component on S3.
**E4 adversarial domain gate:** A globally trivial ray line need not possess a prescribed half-integer vertical homogeneous lift.
**Direct proof imports:** none.  
**Canonical source-scope conditions:** none beyond the stated theorem-local domain.

#### BH-IIF-C-0188 — Integrality on a constant-ray principal orbit (7419–7437)
**E1 source replay:** On a constant-ray principal orbit a globally normalized lift winds by an integer; A=r eta-dchi fixes integral 2pi r.
**E3 independent verification:** Exact principal/double period phase tests separate integral and half-integral r.
**E4 adversarial domain gate:** Requires genuinely orbit-constant ray and global connection gauge; no separate homogeneous gauge premise is consumed here.
**Direct proof imports:** `p2:lem:global-berry-trivialization`.  
**Canonical source-scope conditions:** `BH-IIF-A-0032`.

#### BH-IIF-C-0189 — Hopf normalization (7457–7464)
**E1 source replay:** Principal fibre integral 2pi times base curvature 2pi yields 4pi^2.
**E3 independent verification:** Independent fibre-integration normalization 2pi*2pi.
**E4 adversarial domain gate:** Orientation convention is inherited from Paper I-A; no physical charge assignment.
**Direct proof imports:** `p2:prop:hopfion-charge`.  
**Canonical source-scope conditions:** none beyond the stated theorem-local domain.

#### BH-IIF-C-0190 — Homogeneous uniqueness of the Reeb-normalized connection (7470–7487)
**E1 source replay:** Homogeneous gauge under commuting right SU2 and left U1 kills horizontal invariant covectors by U1 isotropy.
**E3 independent verification:** At the identity, U1 rotation on 2D horizontal plane has no invariant covectors; winding forces r integral.
**E4 adversarial domain gate:** Homogeneity of the CONNECTION, not merely the ray, and principal-orbit constancy are necessary.
**Direct proof imports:** `p2:lem:global-berry-trivialization`, `p2:cor:global-berry-weight-integrality`.  
**Canonical source-scope conditions:** `BH-IIF-A-0029`.

#### BH-IIF-C-0191 — Conditional global homogeneous Berry normalization (7500–7514)
**E1 source replay:** Given homogeneous normal form A=r eta-dchi, exact terms integrate to zero, Q=r^2.
**E3 independent verification:** Substitution with normalized 4pi^2 Hopf integral reproduces r^2.
**E4 adversarial domain gate:** Not valid for half-integral doubled-orbit lift or arbitrary inhomogeneous ray without suitable branch.
**Direct proof imports:** `p2:rem:berry-connection-status`, `p2:lem:hopf-normalization`.  
**Canonical source-scope conditions:** `BH-IIF-A-0029`.

#### BH-IIF-C-0192 — Fibre-basic Berry integral without homogeneity (7530–7555)
**E1 source replay:** Fibre-basic pullback associated line has Chern number n; any two descended connections differ by base beta, and beta mixed term is exact on S2.
**E3 independent verification:** Independent differential-form expansion: 3-base-degree terms vanish, integral of n eta wedge pi*d beta is zero, leaving n^2.
**E4 adversarial domain gate:** A general non-fibre-basic S3 ray may have arbitrary CS; stronger connection identity beta=0 is not implied.
**Direct proof imports:** `p2:prop:hopfion-charge`, `p2:lem:global-berry-trivialization`, `p2:lem:hopf-normalization`.  
**Canonical source-scope conditions:** `BH-IIF-A-0030`.

#### BH-IIF-C-0193 — \texorpdfstring{$\mathbb{CP}^1$}{CP1} geometric quantization (7588–7605)
**E1 source replay:** Borel-Weil identifies H0(CP1,O(k)) as Sym^k C2, dimension k+1; k=0 is not symplectic quantization of (S2,0).
**E3 independent verification:** Monomial basis x^a y^(k-a) has k+1 members for k=0,...,5.
**E4 adversarial domain gate:** The ordinary symplectic branch requires k>=1 and integral curvature normalization.
**Direct proof imports:** none.  
**Canonical source-scope conditions:** none beyond the stated theorem-local domain.

#### BH-IIF-C-0194 — Unlabelled remark at source line 7620 (7620–7622)
**E1 source replay:** Parity of k in j=k/2 describes integral and half-integral spins as separate line-bundle levels.
**E3 independent verification:** Direct arithmetic even k -> integer j, odd k -> half-integer j.
**E4 adversarial domain gate:** This is a representation dictionary, not creation of a spinor particle.
**Direct proof imports:** none.  
**Canonical source-scope conditions:** none beyond the stated theorem-local domain.

#### BH-IIF-C-0195 — Geodesic Closure (7630–7635)
**E1 source replay:** Round-sphere geodesics are unit-speed great circles, with cut antipode at pi R and least geodesic closure 2pi R.
**E3 independent verification:** Independent explicit great circle x(t)=R(u cos(t/R)+v sin(t/R)) has norm R and least period 2pi R.
**E4 adversarial domain gate:** Constant geodesic excluded; no global Euclidean coordinate or time parameter is asserted.
**Direct proof imports:** none.  
**Canonical source-scope conditions:** none beyond the stated theorem-local domain.

#### BH-IIF-C-0196 — Momentum-space geodesic-parameter periodicity (7641–7652)
**E1 source replay:** Substitute Punit=hbar/R into 2pi R; period concerns arclength geodesic parameter.
**E3 independent verification:** Dimensional algebra 2pi R=2pi hbar/Punit.
**E4 adversarial domain gate:** A physical time period requires an independently established trajectory dynamics and clock.
**Direct proof imports:** `p2:prop:geodesic-closure`.  
**Canonical source-scope conditions:** none beyond the stated theorem-local domain.

#### BH-IIF-C-0197 — Magnetic Monopole Analogy (7668–7690)
**E1 source replay:** Hopf U1 equivariance turns charge-q functions into L2 sections of associated degree-q line; diagonal cutoff admits k>=|q| with matching parity.
**E3 independent verification:** Independent SU2 j weight rule |q|<=k and k-q even; k<=m selects exact scalar diagonal finite pieces.
**E4 adversarial domain gate:** Full Spin4 Hm is not one scalar monopole sector and magnetic field is a geometric analogy.
**Direct proof imports:** `p2:prop:hopfion-charge`.  
**Canonical source-scope conditions:** none beyond the stated theorem-local domain.

#### BH-IIF-C-0198 — Constant-annihilating form counterfamily (7715–7728)
**E1 source replay:** Zero-order i tau(A-A*) preserves principal symbol and commutators; curl eigenpair yields lambda shifted by tau/R.
**E3 independent verification:** Explicit 2x2 Hermitian matrix on span{alpha,*alpha} has squared value (lambda+tau/R)^2, including Killing lambda=+/-2/R.
**E4 adversarial domain gate:** Isolated coincidence tau values do not undermine nonrigidity; zero-order deformation is not canonical Dirac input.
**Direct proof imports:** none.  
**Canonical source-scope conditions:** none beyond the stated theorem-local domain.

#### BH-IIF-C-0199 — Representation-theoretic cross-check of the Rarita--Schwinger import (7771–7824)
**E1 source replay:** Frobenius reciprocity and diagonal CG isolate differences 1/2 and 3/2; explicit external twistor identity gives B series. Full gap assertion consumes the later direct signed A-series theorem only, not vice versa.
**E3 independent verification:** Independent CG inventory and homogeneous signed Casimir matrix verify A/B multiplicities and gaps; separate partial proof slice at lines 7827-7865 avoids a false theorem cycle.
**E4 adversarial domain gate:** A-series cannot be obtained by representation theory alone; represent the proposition as item-wise route, not a whole-proposition proof input to its signed theorem.
**Direct proof imports:** `p2f:thm:v260-signed-rs-s3`.  
**Canonical source-scope conditions:** none beyond the stated theorem-local domain.

#### BH-IIF-C-0200 — Independent RS representation-and-twistor subproof (7827–7865)
**E1 source replay:** Diagonal CG, Frobenius reciprocity and external twistor identity determine sector inventory and B-series without using the signed A theorem.
**E3 independent verification:** Independent spin coupling and exact Dirac m->k=m-1 multiplicity give B k+5/2 over 3R.
**E4 adversarial domain gate:** This partial unit is the ONLY RS input to the signed theorem; a full-proposition import would create a spurious cycle.
**Direct proof imports:** none.  
**Canonical source-scope conditions:** none beyond the stated theorem-local domain.

#### BH-IIF-C-0201 — Direct signed Rarita--Schwinger spectrum from the round parent (7875–7958)
**E1 source replay:** Levi-Civita homogeneous connection plus angular momentum projection yields D=(4/3R)S·J+5/2R; each total spin h gives four signed branches.
**E3 independent verification:** Independent exact spin-Casimir enumeration at 38 allowed (j,h) pairs matches eigenvalues and complex multiplicities per sign.
**E4 adversarial domain gate:** Proof uses only representation/twistor SUBCLAIMS of earlier cross-check, not its A-gap/full result. Physical spin-3/2 excitation is not implied.
**Direct proof imports:** none.  
**Canonical source-scope conditions:** none beyond the stated theorem-local domain.

#### BH-IIF-C-0202 — Domain and provenance of the signed derivation (7959–7965)
**E1 source replay:** Explicit scope statement fixes smooth round self-adjoint elliptic spin3/2 operator without zero-order deformation.
**E3 independent verification:** Finite Casimir eigenvalue formula matches smooth canonical domain at low spins.
**E4 adversarial domain gate:** No physical field, source, or particle mass is obtained from a round mathematical spectrum.
**Direct proof imports:** `p2f:thm:v260-signed-rs-s3`.  
**Canonical source-scope conditions:** none beyond the stated theorem-local domain.

#### BH-IIF-C-0203 — Coordinate-generated rotations and native Casimir scope (7970–7978)
**E1 source replay:** Coordinate-polynomial rotations and their projectors are imported from Paper I-A within the intrinsic class.
**E3 independent verification:** Direct distinction between native generator polynomials and an independent kinetic matrix.
**E4 adversarial domain gate:** No physical clock, kinetic operator equivalence, or RG mechanism follows.
**Direct proof imports:** `p1:thm:v226-rotations`.  
**Canonical source-scope conditions:** none beyond the stated theorem-local domain.

#### BH-IIF-C-0204 — Coefficient errors on a supplied kinetic pair (7979–7998)
**E1 source replay:** Dual coefficients bound Hermitian operator norm by epsilon; congruence with Z^-1/2 and Hermitian min-max give eigenvalue error and square-root denominator.
**E3 independent verification:** Independent Weyl/min-max norm argument; bound is monotone and holds for positive g threshold.
**E4 adversarial domain gate:** Requires a fixed actual supplied kinetic pair and common positive normalization Z, with clock if roots called frequencies.
**Direct proof imports:** `p1b:thm:v226-dual-coefficients`.  
**Canonical source-scope conditions:** none beyond the stated theorem-local domain.

#### BH-IIF-C-0205 — Complete frequency comparison has finite tests (8010–8023)
**E1 source replay:** Upper-half-plane nonreal tests count zeros of Hermitian rational response numerators through source-jet degree; real zero retains coupled modes.
**E3 independent verification:** Independent sample degree inequality 2s>(k+1)(m1+m2) and pole term BP0B* vanishing iff BP0=0.
**E4 adversarial domain gate:** Equality at finitely many fixed curvature samples does not prove arbitrary curvature dependence.
**Direct proof imports:** `p1b:thm:v227-finite-response`, `p1b:cor:v227-response-jets`, `p1b:cor:v227-zero-mode-comparison`.  
**Canonical source-scope conditions:** none beyond the stated theorem-local domain.

#### BH-IIF-C-0206 — Legacy carrier-selection diagnostic and fixed-action closure alternative (8052–8115)
**E1 source replay:** Tower stage support SPEX does not constrain independently realized Fp: E9 is 9D and not Hm. Same-action nonzero channels yield complete H1 under a level-one ceiling.
**E3 independent verification:** Independent Hm dimensions 1,15,70,... and E9=9; CG map onto V(1,0),V(0,1) is surjective when nonzero.
**E4 adversarial domain gate:** Historical TWR route is not the current physical m_p=1 proof; closure requires same action and no recompression.
**Direct proof imports:** `p2:prop:word-budget-lower-ideal`, `p2c:prop:e9-coordinate-closure`.  
**Canonical source-scope conditions:** `BH-IIF-A-0016`.

#### BH-IIF-C-0207 — Joint-family condition graph of legacy carrier supports (8156–8173)
**E1 source replay:** E9, E9+left, E9+right and H1 co-realize only with the matching zero/nonzero adjacency channel magnitudes.
**E3 independent verification:** Four boolean channel patterns yield exactly four closure dimensions 9,12,12,15.
**E4 adversarial domain gate:** Separate support and coordinate classes are not an unconstrained Cartesian product; historical only.
**Direct proof imports:** `p2c:prop:e9-coordinate-closure`.  
**Canonical source-scope conditions:** `BH-IIF-A-0016`.

#### BH-IIF-C-0208 — Exact protected-scale specializations (8183–8210)
**E1 source replay:** C_PI assumes sum Xsp^2=rho_prot^2 and raw Clifford gives 4 varrho^2; positive square root yields varrho=rho_prot/2.
**E3 independent verification:** Direct symbolic substitution and optional rho=R produces R/2 without inferring rho=R.
**E4 adversarial domain gate:** Protected scale matching is an additional owner calibration, not fixed by H1 alone.
**Direct proof imports:** none.  
**Canonical source-scope conditions:** `BH-IIF-A-0015`.

#### BH-IIF-C-0209 — Optional factorized protected-channel representative (8221–8243)
**E1 source replay:** F_R sets varrho=R/(2sqrt2), sum X^2=R^2/2 on independently calibrated completion.
**E3 independent verification:** Direct squared-parameter substitution and C_PI+F_R joint solution rho=R/sqrt2.
**E4 adversarial domain gate:** This calibration is not generated by H1, C_PI, or the canonical CD coordinate branch.
**Direct proof imports:** `p2e:cor:protected-scale-branches`.  
**Canonical source-scope conditions:** `BH-IIF-A-0031`.

#### BH-IIF-C-0210 — Unlabelled proposition at source line 8244 (8244–8289)
**E1 source replay:** C_PI gives varrho=rho/2; M_R rho=R; F_R varrho=R/(2sqrt2); two pairwise intersections differ and triple is empty for R>0.
**E3 independent verification:** Exact algebra solves C_PI+F_R: rho=R/sqrt2, incompatible with rho=R.
**E4 adversarial domain gate:** Only SAME completion constraints conflict. Two distinct physical representatives may coexist without shared-object equality.
**Direct proof imports:** `p2e:cor:protected-scale-branches`.  
**Canonical source-scope conditions:** `BH-IIF-A-0015`, `BH-IIF-A-0031`.

#### BH-IIF-C-0211 — Unlabelled proposition at source line 8309 (8309–8344)
**E1 source replay:** Spinor traces 4 lambda q and 4 lambda^3 q^3 cannot equal species 2q and 2q^3 for nonzero q at a single positive lambda.
**E3 independent verification:** Exact equations force lambda=1/2 vs 2^(-1/3); at q=0 both vanish.
**E4 adversarial domain gate:** Cannot merge trace owners by charge rescaling away from zero; zero locus matches.
**Direct proof imports:** none.  
**Canonical source-scope conditions:** none beyond the stated theorem-local domain.

#### BH-IIF-C-0212 — Natural 2T fixed-space nonisomorphism boundary (8356–8372)
**E1 source replay:** Natural left invariant dimensions are 6 for H1 and 1 for E15, so no equivariant isomorphism of whole modules.
**E3 independent verification:** Schur multiplicities 6·1 vs 1·1 supply exact obstruction independent of rank bound.
**E4 adversarial domain gate:** Does not prohibit a different transported action or an unstructured vector-space isomorphism.
**Direct proof imports:** `p1:prop:h1-e15-left-2t-obstruction`.  
**Canonical source-scope conditions:** none beyond the stated theorem-local domain.

#### BH-IIF-C-0213 — Sharp rank of the natural Hurwitz comparison (8373–8429)
**E1 source replay:** Natural left 2T restriction H1=6·1+3·V2+V3; target=1·1+2·V2; Schur gives Hom dimension12 and rank<=5.
**E3 independent verification:** Exact 24-vertex Hurwitz adjacency has eigenspace dimensions 1,4,9 at 8,4,0 and regular rank8 control.
**E4 adversarial domain gate:** Cannot transfer result to arbitrary transported actions, fibre-valued sampling, or physical Hurwitz occurrence.
**Direct proof imports:** `p1:prop:h1-scalar-hurwitz-evaluation-bridge`.  
**Canonical source-scope conditions:** none beyond the stated theorem-local domain.

#### BH-IIF-C-0214 — Natural scalar-Hurwitz blindness to the left chiral adjoint (8431–8446)
**E1 source replay:** No V3 irreducible appears in the E15 natural target, so all 2T intertwiners annihilate source V3=V(1,0).
**E3 independent verification:** Representation decompositions give Hom(V3,1+2V2)=0.
**E4 adversarial domain gate:** Only natural scalar vertex readout, not every tensor-channel or Born exchange. 
**Direct proof imports:** `p2e:prop:sharp-natural-2t-rank`.  
**Canonical source-scope conditions:** none beyond the stated theorem-local domain.

### Findings and continuation
- **Newly confirmed defects:** none. The RS cross-reference is split at a genuinely independent source proof subunit to avoid false cyclic DAG ancestry; no theorem statements or papers are modified.
- **Conditional interfaces:** seven optional typed conditions are recorded at their source-defining locations. The mathematical zeta finite part needs no physical REN scheme; physical interpretation would.
- **Inherited issues:** Earlier Paper II-A finite-port limitation remains open at its prior origin; no new reclassification.
- **Coverage:** `PARTIALLY_AUDITED`, 214 audited/formalized claim objects / 195 of 223 formal declarations. Next 28 formal declarations, source lines 8467–9555, are `NOT_AUDITED`.
- **Independent controls:** `Proofs/Paper2F-Batch6-v1_1-verify.py`, 983/983 passed in the declared finite/model domains.

---

## Batch 7 — Final source-first audit (current Paper II-F v1.61, lines 8467–9555)

**Verdict:** `FULLY_AUDITED_WITH_INHERITED_OPEN_UPSTREAM_GAPS`, no new confirmed Paper II-F mathematical proof defect. **28 formal source declarations plus two inspected standalone constitutional/interface paragraphs.** No new physical axioms, no new canonical conditions; 34 prior conditions and all upstream issues preserved. The 223/223 formal census is complete; earlier audits and E1/E3/E4 scope certificates remain in this cumulative report.

**Independent E3 controls:** 1,355/1,355 checks passed across 23 exact groups: fourth-moment quadratic inversion, spin-3/2 projector/Casimir, 15-dimensional PVM, 252 Petersen five-probe ranks, A5 transporter quotient, Hodge-star and 137 native effects. They check stated finite cases and algebraic identities, not every universal imported theorem.

**Validated physical boundary:** finite mathematical POVM/rank/Gram/tomography and occurrence of a detector/GP2 outcome grammar/complete GP3 comparison are distinct. A finite cubature matches any fixed polynomial degree but is never the continuous endpoint POVM on all Borel events. A mathematical 15-dimensional A5 incidence sector does not reconstitute the physical 15-dimensional H1 momentum carrier.

### All Batch 7 source objects

| Claim ID | Lines | Source result | Status |
|---|---:|---|---|
| `BH-IIF-C-0215` | 8470–8479 | Retrospective operator-identity and readout selection boundary (`Paper2F:source-MATERIAL-8470`) | FORMALIZED |
| `BH-IIF-C-0216` | 8481–8566 | Unrestricted positive-operator dual certificate for the coordinate moment radius (`p2f:thm:v260-full-atlas-dual-radius`) | VERIFIED |
| `BH-IIF-C-0217` | 8568–8675 | First-order homogeneous Casimir-difference formula for the round Rarita--Schwinger operator (`p2f:thm:v260-rs-signed-casimir`) | VERIFIED |
| `BH-IIF-C-0218` | 8677–8732 | Quadratic-moment inverse of the complete intrinsic covariant seed family (`p2f:thm:v260-quadratic-moment-inverse`) | VERIFIED |
| `BH-IIF-C-0219` | 8734–8771 | Maximal instrument-independent harmonic readout inside the covariant endpoint family (`p2f:cor:v260-common-harmonic-readout`) | VERIFIED |
| `BH-IIF-C-0220` | 8773–8804 | Exact nonselection of a physical POVM or instrument from first moments (`p2f:prop:v260-readout-nonselection`) | VERIFIED |
| `BH-IIF-C-0221` | 8806–8837 | Individual-coordinate sharp readout without a joint-POVM selector (`p2f:cor:v260-sharp-coordinate-pvm`) | VERIFIED |
| `BH-IIF-C-0222` | 8843–8850 | II-B carrier vs retrospective II-C/III-F/V-A origin firewall (`Paper2F:source-MATERIAL-8843`) | FORMALIZED |
| `BH-IIF-C-0223` | 8851–8886 | Sharp positive scalar multiplication defect (`p2f:prop:v264-sharp-scalar-compression-defect`) | VERIFIED |
| `BH-IIF-C-0224` | 8888–8906 | Exact native indistinguishability counterexample (`p2f:prop:v264-native-state-nonconverse`) | VERIFIED |
| `BH-IIF-C-0225` | 8908–8930 | Zero-fermion first jet cannot create the missing odd source (`p2f:prop:v264-action-jet-obstruction`) | VERIFIED-CONDITIONAL |
| `BH-IIF-C-0226` | 8932–8946 | Scope of the paired-exchange contraction (`p2f:rem:v264-action-pair-cert-status`) | FORMALIZED |
| `BH-IIF-C-0227` | 8950–8960 | Homogeneous covariant readout does not decide a detector or instrument (`p2f:rem:v270-homogeneous-readout-firewall`) | FORMALIZED |
| `BH-IIF-C-0228` | 8966–9025 | Arbitrary finite polynomial endpoint moments admit exact positive finite presentations (`p2f:cor:v274-finite-endpoint-moment-presentations`) | VERIFIED-CONDITIONAL |
| `BH-IIF-C-0229` | 9030–9073 | Exact positive finite endpoint-readout tower and its sharp topology (`p2f:cor:v275-endpoint-finite-tower`) | VERIFIED-CONDITIONAL |
| `BH-IIF-C-0230` | 9078–9109 | Finite observable-history certificate with a whole-candidate firewall (`p2f:cor:v297-outcome-history-gp3-firewall`) | VERIFIED-CONDITIONAL |
| `BH-IIF-C-0231` | 9114–9142 | Informational completeness compresses the outcome-port audit (`p2f:cor:v298-ic-one-step-gp3-firewall`) | VERIFIED-CONDITIONAL |
| `BH-IIF-C-0232` | 9147–9182 | Exact covariance selects the continuous IC audit route (`p2f:cor:v299-covariant-ic-gp3-firewall`) | VERIFIED-CONDITIONAL |
| `BH-IIF-C-0233` | 9186–9218 | Mathematical instrument availability does not register a GP3 comparison (`p2f:cor:v300-instrument-existence-gp3-firewall`) | VERIFIED-CONDITIONAL |
| `BH-IIF-C-0234` | 9222–9269 | Conditional naturality certificate for all momentum measurement histories (`p2f:cor:v301-gauge-naturality-gp3-certificate`) | VERIFIED-CONDITIONAL |
| `BH-IIF-C-0235` | 9277–9302 | Matrix and incidence certificates for the ten-axis frame (`p2f:prop:v318-ten-axis-matrix-certificate`) | VERIFIED |
| `BH-IIF-C-0236` | 9304–9329 | Five-probe rank and exact combinatorial count (`p2f:lem:v318-five-probe-count`) | VERIFIED |
| `BH-IIF-C-0237` | 9331–9356 | Finite reciprocal product readout versus real bilocal correlations (`p2f:prop:v318-reciprocal-real-effect-certificate`) | VERIFIED |
| `BH-IIF-C-0238` | 9358–9368 | Reproducibility, spectral types, and typed limits (`p2f:rem:v318-certificate-status`) | FORMALIZED |
| `BH-IIF-C-0239` | 9376–9408 | Rank-fifteen cochain descent and non-descending cell exclusion (`p2f:prop:v339-projector-descent-certificate`) | VERIFIED-CONDITIONAL |
| `BH-IIF-C-0240` | 9410–9428 | Constitutional status: which observable is owned? (`p2f:rem:v339-petersen-gp2-gp3-firewall`) | FORMALIZED |
| `BH-IIF-C-0241` | 9435–9474 | No rank-twenty-five register/kernel identification (`p2f:prop:v340-projective-binary-orthogonality`) | VERIFIED-CONDITIONAL |
| `BH-IIF-C-0242` | 9475–9482 | Finite certification scope (`p2f:rem:v340-ranktwo-proof-scope`) | FORMALIZED |
| `BH-IIF-C-0243` | 9488–9516 | Centre-even descent of class-tomography coefficients (`p2f:prop:v342-class-frame-descent-scope`) | VERIFIED-CONDITIONAL |
| `BH-IIF-C-0244` | 9521–9552 | Independent symmetry, matched readouts and GP3 limits (`p2f:prop:v343-signed-owner-firewall`) | VERIFIED-CONDITIONAL |

### Source-bound proof replay and adversarial certificates (E1/E3/E4)

#### BH-IIF-C-0215 — Retrospective operator-identity and readout selection boundary (8470–8479)
**E1 source replay:** Source explicitly identifies prior signed theorem, POVM-radius and readout branches as mathematical statements on the declared native carrier.

**E3 independent checking:** Source checked against exact prior labels and the dual moment proof; no independent physical detector inference.

**E4 boundary challenge:** Not a new derivation or physical operator selection, and not counted among the 28 formal declarations.

**Direct consumed theorem labels:** none; direct calculation or source-scope text. **Canonical conditions:** no newly introduced condition; source-local hypotheses retained.

#### BH-IIF-C-0216 — Unrestricted positive-operator dual certificate for the coordinate moment radius (8481–8566)
**E1 source replay:** For each chirality construct Y_a,Z; four scalar and three chiral 2x2 PSD blocks make Z-q·Y>=0 on the unit sphere and ball. The full POVM moment identity gives Tr Z=4S, sum Tr(YX)=4S², forcing r>=S. Protected Clifford compression gives 16ρ<=4r; the previously constructed covariant density attains the maximum.

**E3 independent checking:** Independently computed scalar/vector and chiral trace coefficients from S3 fourth moments and W_q†P±W_q=(I-qq†)/2; Clifford generators independently satisfy C(q)²=1 and protected trace dimension four.

**E4 boundary challenge:** Dual only bounds arbitrary positive POVMs with the exact prescribed first moments and fixed compatible block; does not construct detector occurrence or pick a physical branch. Cited constructive theorem supplies sharpness, not independent physical existence.

**Direct consumed theorem labels:** `p2c:thm:full-atlas-povm-radius`. **Canonical conditions:** no newly introduced condition; source-local hypotheses retained.

#### BH-IIF-C-0217 — First-order homogeneous Casimir-difference formula for the round Rarita--Schwinger operator (8568–8675)
**E1 source replay:** Clebsch–Gordan projection of the spin-half factor onto spin-3/2 is 1/3 of total spin; in the round frame the projected twisted Dirac equals -2/(3R)(C_L-C_R). Frobenius/CG sectors with |j_L-j_R|=3/2 and 1/2 give both signed k-series and dimensions.

**E3 independent checking:** Constructed the 6x6 spin1⊗spin1/2 projector independently and verified all three projected-generator relations exactly; calculated 302 Casimir eigenvalues and 302 sector dimensions through k=150 without using the theorem formula.

**E4 boundary challenge:** Operator convention and self-adjoint compact round S3 domain are essential; neither branch yields an experimentally assigned particle mass. Prior full RS theorem need not cite this later cross-check, so no proof cycle.

**Direct consumed theorem labels:** `p2f:thm:v260-signed-rs-s3`. **Canonical conditions:** no newly introduced condition; source-local hypotheses retained.

#### BH-IIF-C-0218 — Quadratic-moment inverse of the complete intrinsic covariant seed family (8677–8732)
**E1 source replay:** Use E[q_i^4]=1/8 and E[q_i²q_j²]=1/24 to integrate f=q1²-q2² against the complete endpoint seeds. The vector diagonal reads (a-1)/9; the oriented two-form diagonal/offdiagonal read Reζ/6 and -iImζ/6. Invariance of domain gives a three-real-coordinate local lower bound.

**E3 independent checking:** Independent exact fourth-moment integration produced all 36 entries of ∫fH_q=D/6 and the vector coefficients; checked *e13=-e24, star D anti-commutes and endpoint parameter region has nonempty three-dimensional interior.

**E4 boundary challenge:** The inverse is within the stipulated covariant seed family only; a physical action-generated quadratic effect and coherent off-diagonal preparation are separate occurrence obligations, not proved by injectivity.

**Direct consumed theorem labels:** `p2c:thm:complete-intrinsic-endpoint-seeds`. **Canonical conditions:** no newly introduced condition; source-local hypotheses retained.

#### BH-IIF-C-0219 — Maximal instrument-independent harmonic readout inside the covariant endpoint family (8734–8771)
**E1 source replay:** K(q) has harmonic degrees at most two, so E2-orthogonal f are mapped entirely by the fixed constant/linear coefficient. Variable vector-block parameter a detects any E2 nonzero traceless quadratic H. Sphere support fixes the total second moment and added-noise operator.

**E3 independent checking:** Independent fourth-moment identity gives ∫(q^T Hq)(qq^T-I/4)=H/12 for traceless H; tested polynomial seed degree and q linear moment coefficient 4/r0, and all parameter variations in an open interval.

**E4 boundary challenge:** Maximality is relative to the declared covariant endpoint seeds, not arbitrary detectors. Degree>=3 is in common kernel of quadratic-density maps only, not necessarily every imaginable GP2-generated readout.

**Direct consumed theorem labels:** `p2c:thm:complete-intrinsic-endpoint-seeds`. **Canonical conditions:** no newly introduced condition; source-local hypotheses retained.

#### BH-IIF-C-0220 — Exact nonselection of a physical POVM or instrument from first moments (8773–8804)
**E1 source replay:** Two real admissible seeds at a=4/3, ζ=1/3 versus ζ=1 have the same normalized first moments but quadratic e13 expectation differs by R²/3; fixed POVM effects admit distinct Lüders and measure-and-prepare CP instruments.

**E3 independent checking:** Independent exact seed-domain check u=2/3, both ζ endpoints inside the closed disk and the quadratic expectation difference equals R²/3. CP maps are different on generic pure preparations despite equal event effects.

**E4 boundary challenge:** Nonselection is only from these structural inputs; an extra actually generated action–apparatus incidence may pick a detector. This is not a universal no-go for all possible physical selection.

**Direct consumed theorem labels:** `p2c:thm:complete-intrinsic-endpoint-seeds`. **Canonical conditions:** no newly introduced condition; source-local hypotheses retained.

#### BH-IIF-C-0221 — Individual-coordinate sharp readout without a joint-POVM selector (8806–8837)
**E1 source replay:** Rotate a to one unit vector, split geometric coordinate into one R/2 scalar/radial edge, three sqrt(2)R/3 tangent edges, three kernel bivectors, and protected sqrt(3)R/4 Clifford block. The spectral polynomial Pλ(X) constructs each sharp PVM.

**E3 independent checking:** Independently checked anticommuting 4x4 Clifford generators, each with ± eigenvalue of multiplicity two; explicit block counts produce fifteen eigenvalues with listed multiplicities and zero eigenspace dimension three.

**E4 boundary challenge:** A spectral projection exists mathematically for each coordinate; neither performed measurement nor postmeasurement CP update is inferred.

**Direct consumed theorem labels:** none; direct calculation or source-scope text. **Canonical conditions:** no newly introduced condition; source-local hypotheses retained.

#### BH-IIF-C-0222 — II-B carrier vs retrospective II-C/III-F/V-A origin firewall (8843–8850)
**E1 source replay:** Source fixes strict chronological order of the constitution and retrospective action/operator checks.

**E3 independent checking:** Cross-paper source labels agree with an II-B prior seed; independent operator type/domain check shows downstream branches do not backgenerate it.

**E4 boundary challenge:** Chronology alone does not prove a new physical occurrence or allow importing a later action as a GP2 constructor.

**Direct consumed theorem labels:** none; direct calculation or source-scope text. **Canonical conditions:** no newly introduced condition; source-local hypotheses retained.

#### BH-IIF-C-0223 — Sharp positive scalar multiplication defect (8851–8886)
**E1 source replay:** Inserting P+(I-P) between ambient coordinate multipliers gives the positive leakage square. The exact round S3 second/fourth moments leave eigenvalues zero, R²/4 and R²/6 (threefold) on E0⊕E1.

**E3 independent checking:** Independently computed the 5x5 leakage diagonal from S3 moment ratios and checked the exact spectral norm for multiple rational radii.

**E4 boundary challenge:** This obstruction holds for the stated scalar harmonic compression and ambient multiplication; it is not a statement about a separately licensed native coordinate word.

**Direct consumed theorem labels:** none; direct calculation or source-scope text. **Canonical conditions:** no newly introduced condition; source-local hypotheses retained.

#### BH-IIF-C-0224 — Exact native indistinguishability counterexample (8888–8906)
**E1 source replay:** The difference between coherent and incoherent states lies in Hg–Hs off-block matrix entries, Hilbert–Schmidt orthogonal to all block-diagonal native tests.

**E3 independent checking:** Independently evaluated all 11²+4² native matrix units against the explicit rank-two off-block coherence: all 137 evaluations vanish while the matrix difference is nonzero.

**E4 boundary challenge:** Failure of full M15 tomography does not refute full tomography within the actual native M11⊕M4 observable algebra.

**Direct consumed theorem labels:** none; direct calculation or source-scope text. **Canonical conditions:** no newly introduced condition; source-local hypotheses retained.

#### BH-IIF-C-0225 — Zero-fermion first jet cannot create the missing odd source (8908–8930)
**E1 source replay:** For S_B+c_F barPsi D(B;Y)Psi the derivative at Psi=0 is zero and the mixed second derivative is a paired-index even operator. The printed action has no provided map from its protected/internal owner to the specific II-B central-odd Hg←Hs slot.

**E3 independent checking:** Independently differentiated the bilinear polynomial and checked parity under simultaneous fermionic sign reversal; type/domain mismatch prevents identifying the operator kernels without a bridge.

**E4 boundary challenge:** Only the uninserted local bilinear printed in III-F is excluded; source does not rule out inserted spinor roles or a separately generated mixed Hessian.

**Direct consumed theorem labels:** none; direct calculation or source-scope text. **Canonical conditions:** no newly introduced condition; source-local hypotheses retained.

#### BH-IIF-C-0226 — Scope of the paired-exchange contraction (8932–8946)
**E1 source replay:** The scope remark distinguishes the invariant algebraic paired-exchange tensor K from any physical two-system action Hessian, owner, bath or collision law.

**E3 independent checking:** Source-label and type/owner audit confirms an abstract mixed tensor contraction is not a nonzero measured exchange probability by itself.

**E4 boundary challenge:** No mathematical universal nonexistence claim is made; a registered action/source and its explicit two-system maps are independent obligations.

**Direct consumed theorem labels:** `p2b:thm:v264-canonical-paired-exchange`. **Canonical conditions:** no newly introduced condition; source-local hypotheses retained.

#### BH-IIF-C-0227 — Homogeneous covariant readout does not decide a detector or instrument (8950–8960)
**E1 source replay:** Scope-only statement preserves the separation of the continuously covariant six-channel IC construction, endpoint blindness and noncovariant finite 137-outcome frame.

**E3 independent checking:** Independent dimensions check 137=11²+4²; readout nonselection follows from the explicit earlier endpoint seed countermodel.

**E4 boundary challenge:** No new exact finite continuous-covariance equivalence or detector selection is claimed.

**Direct consumed theorem labels:** none; direct calculation or source-scope text. **Canonical conditions:** no newly introduced condition; source-local hypotheses retained.

#### BH-IIF-C-0228 — Arbitrary finite polynomial endpoint moments admit exact positive finite presentations (8966–9025)
**E1 source replay:** Carathéodory applied to the Haar evaluation vector on P_{r+2} produces at most d_{r+2} positive nodes; degree-two polynomial K makes every fK with deg f<=r integrable exactly. Imported degree-19/coset and twin convolution results supply the specific alternative designs and decaying error.

**E3 independent checking:** Independently checked d_{r+2}=∑_{k=0}^{r+2}(k+1)² for r=0..100, the 14·120=1680 bound, and the polynomial degree transfer. Source-verified twin bound uses scalar dual norm and u,v matrix elements.

**E4 boundary challenge:** Finite exactness holds only through the stated polynomial band. Branch independence is relative to a supplied H, not a physical H selector; finite support never retains exact continuous covariance by itself.

**Direct consumed theorem labels:** `p1b:thm:v273-triple-icosahedral-nineteen-design`, `p1b:cor:v273-positive-coset-mixture-no-ceiling`, `p1b:thm:v274-branch-symmetric-twin-convolution`. **Canonical conditions:** no newly introduced condition; source-local hypotheses retained.

#### BH-IIF-C-0229 — Exact positive finite endpoint-readout tower and its sharp topology (9030–9073)
**E1 source replay:** The imported degree-2m exact positive ν_m integrates degree-two K exactly and fK through degree 2m. Polynomial density/positivity gives norm convergence for each fixed continuous f. A single finite event B_m simultaneously has E_m(B_m)=I and Haar-continuous E(B_m)=0.

**E3 independent checking:** Independently reconstructed the degree bookkeeping, finite-versus-nonatomic event witness and distinction between weak convergence and supremum over Borel events.

**E4 boundary challenge:** Uniform event/topological equality explicitly fails; weak-continuous moments do not establish physically performed finite measurements.

**Direct consumed theorem labels:** `p1b:thm:v275-nested-positive-resolution-tower`. **Canonical conditions:** no newly introduced condition; source-local hypotheses retained.

#### BH-IIF-C-0230 — Finite observable-history certificate with a whole-candidate firewall (9078–9109)
**E1 source replay:** For a registered effect/outcome grammar, Paper IV-A closure O_{N²-d} spans all finite pullbacks. All histories descend through state restriction Q iff that closure lies in A_sa; GP3 still requires preservation of every other frozen source/port and a proper generated comparison.

**E3 independent checking:** Independent linear-algebra check of finite stabilization and off-algebra trace-orthogonal witness; confirmed the imported theorem makes no unconditional physical subgrammar registration claim.

**E4 boundary challenge:** Test is only terminal-observable-history faithfulness, not complete state-update or whole-candidate GP3 minimization.

**Direct consumed theorem labels:** `p4a:thm:v297-finite-outcome-word-saturation`, `p2b:thm:v293-operational-multiplicity-quotient`, `p2:prop:gp3-multiplicity-bound`, `p4a:prop:v297-specific-versus-full-process`. **Canonical conditions:** no newly introduced condition; source-local hypotheses retained.

#### BH-IIF-C-0231 — Informational completeness compresses the outcome-port audit (9114–9142)
**E1 source replay:** For an explicitly registered IC effect frame spanning A_sa, one-step inclusion Ψ_i*(E_j) in A is equivalent to invariance Ψ_i*(A)⊂A and descent of all finite histories. Finite 43 and 137 frames give 43b/137b membership checks.

**E3 independent checking:** Independent span argument proves checking a basis of A_sa suffices for all linear Ψ_i*; 137=11²+4² and 43b/137b counts verified without enlarging the role grammar.

**E4 boundary challenge:** A mathematical IC frame is not evidence that an actual instrument or all GP3-frozen sources/trace ports were generated.

**Direct consumed theorem labels:** `p4a:thm:v298-ic-one-step-outcome-descent`, `p4a:cor:v298-kinematic-43-effect-frame`, `p2c:cor:v298-amplified-coordinate-ic-one-step`, `p2:prop:gp3-multiplicity-bound`. **Canonical conditions:** no newly introduced condition; source-local hypotheses retained.

#### BH-IIF-C-0232 — Exact covariance selects the continuous IC audit route (9147–9182)
**E1 source replay:** Connected Spin4 maps to a finite permutation group trivially on a fixed unmarked outcome set; invariant effects lie in six-dimensional type commutant and cannot span the 137-dimensional native test space. Separate continuous covariant six-channel readout has 137 measurable events and conditional finite 137b tests.

**E3 independent checking:** Independent connected-to-finite-group continuity argument and Hermitian dimension comparison; rechecked importing 137-event basis and finite-history theorem at their stated scope.

**E4 boundary challenge:** A continuously rotating marked family is not a single permutation-covariant finite-outcome POVM; no physically registered readout is inferred.

**Direct consumed theorem labels:** `p2c:thm:v299-finite-covariant-six-ceiling`, `p2c:cor:v299-directed-tangent-137-event-basis`, `p4a:thm:v299-continuous-ic-event-test`, `p2:prop:gp3-multiplicity-bound`. **Canonical conditions:** no newly introduced condition; source-local hypotheses retained.

#### BH-IIF-C-0233 — Mathematical instrument availability does not register a GP3 comparison (9186–9218)
**E1 source replay:** Cited directed-tangent Lüders instrument is a mathematical covariant CP construction preserving the native quotient; compatible post-unitary updates are in the stated normalizer. A separate swap witness has same effects but can fail descent.

**E3 independent checking:** Independent CP square-root update and effect probability identity review; verified that sharing E_j cannot alone fix all Ψ_j outputs.

**E4 boundary challenge:** Existence and compatible-history closure are mathematics. No occurrence of the outcome instrument or generated whole-candidate GP3 comparison is asserted.

**Direct consumed theorem labels:** `p2c:cor:v300-directed-tangent-luders`, `p2c:prop:v300-coordinate-normalizer`, `p4a:prop:v300-swap-instrument-witness`, `p2:prop:gp3-multiplicity-bound`. **Canonical conditions:** no newly introduced condition; source-local hypotheses retained.

#### BH-IIF-C-0234 — Conditional naturality certificate for all momentum measurement histories (9222–9269)
**E1 source replay:** When every actually registered word has complete-input automorphism gauge and fixed outcome label, Paper II-A same-owner equivariance gives each outcome map naturality. IV-A invariance of the intrinsic fixed-point algebra then yields history descent, not full GP3 comparison.

**E3 independent checking:** Independent fixed-point/commutant argument tests the conditional implication; source cross-check shows Spin4 covariance alone admits the cited non-gauge-natural countermodel.

**E4 boundary challenge:** Complete-presentation gauge invariance is a substantive antecedent and must not be inferred from unmarked carrier or Spin4 covariance alone; proper physical whole-candidate comparison remains independent.

**Direct consumed theorem labels:** `p2c:thm:v301-intrinsic-gauge-fixedpoints`, `p2a:thm:v368-same-owner-unmarked-equivariance`, `p4a:thm:v301-gauge-natural-instrument-descent`, `p4a:prop:v301-spin4-same-povm-leak`, `p2:prop:gp3-multiplicity-bound`. **Canonical conditions:** no newly introduced condition; source-local hypotheses retained.

#### BH-IIF-C-0235 — Matrix and incidence certificates for the ten-axis frame (9277–9302)
**E1 source replay:** Five-core pair incidence has D^T D=3I+J. Its trace-free 10-axis projector is I-D(D^TD)^-1D^T=(4I+2A_P-J)/6, matching the quadrupole Gram and isotropic 10-vector frame.

**E3 independent checking:** Independent exact 10x5 binary incidence and Petersen adjacency give projector equality, idempotence, rank five and symmetry. The stipulated Gram Q=(4/3)P_Q follows from Paper I-A actual angular construction.

**E4 boundary challenge:** Projector and POVM existence are mathematical features of a supplied axis frame, not physical 2I axis occurrence or a new native detector.

**Direct consumed theorem labels:** none; direct calculation or source-scope text. **Canonical conditions:** no newly introduced condition; source-local hypotheses retained.

#### BH-IIF-C-0236 — Five-probe rank and exact combinatorial count (9304–9329)
**E1 source replay:** Because ker Φ=im D and D injective, ker Φ_S ≅ker D_T, so rank Φ_S=rank D_T. A five-edge graph on five vertices has full unsigned incidence rank iff no bipartite component; the odd cycle cases are 12 pentagons and 150 triangle-with-attachments.

**E3 independent checking:** Independently enumerated all 252 five-edge subsets with exact integer determinant and rank: 162 have rank five and 90 have rank four.

**E4 boundary challenge:** The count is for exactly five selected pair labels in the specified unsigned incidence and quadrupole map; it does not select a physical five-probe ensemble.

**Direct consumed theorem labels:** none; direct calculation or source-scope text. **Canonical conditions:** no newly introduced condition; source-local hypotheses retained.

#### BH-IIF-C-0237 — Finite reciprocal product readout versus real bilocal correlations (9331–9356)
**E1 source replay:** Symmetric part of End(Vx⊗Vp) splits as Sym²Vx⊗Sym²Vp (36) plus Λ²Vx⊗Λ²Vp (9). Product real-symmetric effects span only the former.

**E3 independent checking:** Independently assembled real symmetric/skew 3x3 matrix bases and verified transpose parity of all 36 plus nine tensor basis blocks, giving total 45.

**E4 boundary challenge:** The nine-dimensional null sector is only for this local real-symmetric product effect grammar; additional entangled or complex effects might see it.

**Direct consumed theorem labels:** none; direct calculation or source-scope text. **Canonical conditions:** no newly introduced condition; source-local hypotheses retained.

#### BH-IIF-C-0238 — Reproducibility, spectral types, and typed limits (9358–9368)
**E1 source replay:** Reproducibility remark lists exact verifier scope, rank identities and physical limitations for supplied 2I packet.

**E3 independent checking:** Independent rank enumeration, Petersen incidence exact projector and 252 choices replayed; historical cited verifier is not treated as proof of 2I physical presence.

**E4 boundary challenge:** No observed energy, mass, particle-number or dynamical rule is established.

**Direct consumed theorem labels:** none; direct calculation or source-scope text. **Canonical conditions:** no newly introduced condition; source-local hypotheses retained.

#### BH-IIF-C-0239 — Rank-fifteen cochain descent and non-descending cell exclusion (9376–9408)
**E1 source replay:** B*B T=30T for the imported five-core incidence and tracefree Q⊗Q projection, so Π15=BTB*/30 squares to itself and has rank fifteen. Deleting one coordinate from a kernel P⊗Q word produces a nonzero Q⊗Q image, forbidding quotient descent.

**E3 independent checking:** Independently reconstructed A5 60x25 transporter B_tr and its rank 17; verified B_tr^T B_tr acts as 15 on Q⊗Q, hence the double-cover singular value 30. Explicit coordinate deletion of a P⊗Q kernel vector has nonzero B image.

**E4 boundary challenge:** The rank-15 image and 24/25 self-exclusion register are distinct; no physical export to the independent II-B H1 is made.

**Direct consumed theorem labels:** `p1:prop:v339-incidence-rank15-contrast`. **Canonical conditions:** no newly introduced condition; source-local hypotheses retained.

#### BH-IIF-C-0240 — Constitutional status: which observable is owned? (9410–9428)
**E1 source replay:** Scope remark differentiates exact group-incidence matrix outputs from G0 occurrence, action readout owner, and independent Spin4/H1 momentum constitution.

**E3 independent checking:** Independent representation-type and operator-domain audit confirms a real A5 rank-15 module need not be a spinorial Spin4 momentum owner.

**E4 boundary challenge:** A dimension coincidence cannot certify a GP2-licensed physical constructor or GP3 whole-candidate dominance.

**Direct consumed theorem labels:** none; direct calculation or source-scope text. **Canonical conditions:** no newly introduced condition; source-local hypotheses retained.

#### BH-IIF-C-0241 — No rank-twenty-five register/kernel identification (9435–9474)
**E1 source replay:** Normalized binary pullback iota is an isometry; each transporter cell includes both lifts, giving Bhat=sqrt(2)iota B_tr and Bhat^T Bhat=2Btr^TBtr. Imported central 4-isotypic image has rank 16 plus constants, orthogonal to rank-25 5-isotypic shell kernel; branching yields 15⊕10.

**E3 independent checking:** Independently constructed A5 transporter incidence rank 17, its Q⊗Q sector singular² 15, and the double-cover norm; checked orthogonal projector dimension and type distinctions under I/A5.

**E4 boundary challenge:** The shell-walk zero eigenspace uses a specifically declared nearest-shell character premise; numerical 25 equality alone is no module identification.

**Direct consumed theorem labels:** `p1:prop:v340-transporter-hexagon-intersection`. **Canonical conditions:** no newly introduced condition; source-local hypotheses retained.

#### BH-IIF-C-0242 — Finite certification scope (9475–9482)
**E1 source replay:** Verifier-scope remark limits exact rational/integer incidence checks to finite theorem content and excludes GP3 and detector claims.

**E3 independent checking:** Existing rank-two exact verifier and fresh direct A5 rank-17/15 checks are mathematical controls, not independent physical occurrence evidence.

**E4 boundary challenge:** No cross-owner particle assignment is licensed.

**Direct consumed theorem labels:** none; direct calculation or source-scope text. **Canonical conditions:** no newly introduced condition; source-local hypotheses retained.

#### BH-IIF-C-0243 — Centre-even descent of class-tomography coefficients (9488–9516)
**E1 source replay:** For normalized pullback through 2I→A5 each frame row appears twice scaled 1/sqrt2; its outer-product frame sum is unchanged, so the fifteen-dimensional three-cycle class frame and eigenvalues descend exactly.

**E3 independent checking:** Independently verified the double-copy isometry for explicit finite coefficients and the exact rank conservation under pullback; compared imported class-frame statement and its class-owner limitations.

**E4 boundary challenge:** Frame positivity is not necessarily a POVM effect prescription or physical chirality; GP3 still needs generated whole-candidate comparison.

**Direct consumed theorem labels:** `p1:thm:v342-class-frame-three-cycle-tomography`, `p1:rem:v342-class-frame-observable-firewall`. **Canonical conditions:** no newly introduced condition; source-local hypotheses retained.

#### BH-IIF-C-0244 — Independent symmetry, matched readouts and GP3 limits (9521–9552)
**E1 source replay:** Under independent A5 factors no invariant bilinear exists because both W factors lack invariant vectors; under matched diagonal A5, W=3⊕3′⊕4⊕5 gives one invariant per sector. Outer interchange swaps the two threefold sectors, leaving one odd invariant line generated by the signed contrast L.

**E3 independent checking:** Independent Schur multiplicity count reproduces four diagonal invariants, one outer-odd line and no independent-factor scalar, with source-confirmed 15-dimensional decomposition.

**E4 boundary challenge:** Double-odd tensor direction requires an explicit ownership and symmetry marking. Action coefficient, detector occurrence and GP3 momentum comparison remain open interfaces, not consequences of Born exchange.

**Direct consumed theorem labels:** `p1b:thm:v343-doubleodd-contrast`, `p1:prop:v343-fivefold-signed-contrast`. **Canonical conditions:** no newly introduced condition; source-local hypotheses retained.

### Final all-paper classification and unresolved interfaces

- **Formal target census:** 223/223; **source-bound audit objects:** 244 (223 formal declarations plus 21 material/deferred proof/interface records). All seven batches are retained with cumulative evidence.
- **New confirmed II-F mathematical errors in Batch 7:** 0. **New global condition nodes:** 0. **New gap IDs:** none; the Paper II-A open `BH-IIA-PORT-001` remains rooted and unresolved in the global atlas.
- **Physics-conditional boundaries, not mathematical flaws:** complete action-generated quadratic readout/coherent preparation; physically registered outcome maps; owner-preserving action/source traces; a genuine generated whole-candidate GP3 comparison; actual exceptional/group support and finite detectors. These must not be upgraded from mathematical existence.
- **Gaps not claimed closed:** The conditional physical universality of the full momentum carrier through the inherited II-A port. No source modifications or theory extensions were made.
- **Source authority:** Paper II-F v1.61 SHA-256 `48ddfbde3da7d9d3f13478d6a8c64ea9136c7b024c0aaa44c0ca0ef3401cd79e`, from PapersMinimal v2.370. All imports resolve in the current source atlas; no remote paper independently re-audited.
- **Completion qualification:** Prior batch evidence is carried forward, not re-signed by independent agents. The 1,355 checks are E3 finite controls, not automatic proof of universal statements.

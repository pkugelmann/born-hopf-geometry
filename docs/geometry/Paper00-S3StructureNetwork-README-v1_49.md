# S³ Structure Network v1_49 — downstream geometry integrated into current papers

Parent v1_48, with exact geometric compilers/certificates preserved byte-identically.
Current paper release: `Paper00-PapersMinimal-v3_075.zip`.

**Source integration only:** The exact local 20-pair lift, Lie-defect kernel,
minimal A5-compatible 28-dimensional SU3 representation, scoped no-go and
explicit 99,470-dimensional exact-current dilation now have formal owners in
Paper I-B v1.26. Paper V-A imports mass-polynomial transport, V-C retains its
full decay certificate, VII-A defines the native same-action current/Hessian/
Gauss matching tests, and VII-B imports the finite N9/56 source Gram.

The 28/99,470 constructions are independent **alternative** representations;
neither is selected as physical. The stronger simultaneous A5-equivariant
unchanged-current completion remains open. Native QCD source-derivative equality,
local Gauss, real pole/daughter and physical widths remain open.

The previous latest *research* report `reports/Paper00-DownstreamGeometryClosure-v1_7.md`
is retained; this version adds only a source-integration register and the
reproducibility source hashes. It is not a new proof-chain audit.

## Exact replay

Run `python scripts/Paper00-ReplayFullCarrierCurrent-v1_1.py`,
`python scripts/Paper00-ReplayFlavorAlgebraSelection-v1_1.py`, and
`OPENBLAS_NUM_THREADS=1 python scripts/Paper00-ReplayProtectedFlavorLift-v1_1.py`.
These do not certify all imported physical statements.

---

# S³ Structure Network v1_48 — explicit exact finite full-carrier flavor currents

**Parent:** v1_47 exact Lie-defect carrier selection and minimal-SU3 obstruction. **Current report:** `reports/Paper00-DownstreamGeometryClosure-v1_7.md`. **Scope:** constructive exact finite representation/charge compression, **not** a native Born/QCD action or physical particle-decay certificate.

- **Complete current without changing one-hop K(H):** a 99,470-dimensional genuine U(3) representation with an explicit 20-state isometry `J` such that `J† Qhat(H) J = K(H)` for **all Hermitian flavor H**. Three protected modes remain an invariant fundamental U(3). Nine pure-state tomography duals and positive/negative complementary spectral parts give the exact formula; tensor degree `n=24` is certified sufficient by a rational-outward Gershgorin bound `||Σ B_s²||∞ <64`, followed by a functional-calculus bound `Σ |B_s| <24 I17`.
- **Exact tomography checks:** nine complementary squared Hilbert–Schmidt norms `(57,57,57,42,18,42,18,42,18)` and 81 exact duality identities; one-hop matrix-unit reconstructions independently crosschecked. This construction gives a *nonminimal existence witness*, not a canonical A5-intertwining source embedding; the original K compression remains A5-covariant.
- **Minimal harmonic 28 alternative:** retain the exact A5-equivariant `Sym1+Sym3+Sym4` representation, but its global current changes the original off-flavor 17-state matrix elements. On 28, each rotation-current compression has squared strength `45/2` (not original `5`). Triplet source leakage into its 8 auxiliary harmonics vanishes. Each normalized quintet generator leaks with exact squared strength `42/25` (Sym3) plus `104/21` (Sym4), summing over five generators to `3482/105`.
- **No physical promotion:** Neither auxiliary representation is established to be an isometric component of the actual Gauss-reduced native CAR action. Tensor degrees are **not** quark numbers or new physical particles. The actual source derivative, Duhamel/contact jets, on-shell pole residues and decay channels remain open.

**New compiler:** `scripts/Paper00-FullCarrierCurrentCompiler-v1_1.py`; **replay:** `scripts/Paper00-ReplayFullCarrierCurrent-v1_1.py`; **certificate:** `data/Paper00-FullCarrierCurrent-v1_1.json`; **typed overlay:** `graph/Paper00-FullCarrierCurrent-v1_1.graphml`; **report:** `reports/Paper00-DownstreamGeometryClosure-v1_7.md`.

Historical geometry certificates, source papers, canonical proof DAG and audit bundles are not rewritten. Only the latest downstream-closure research report is retained in this archive.

---

# S³ Structure Network v1_47 — exact Lie-defect flavor selection, harmonic closure and minimal SU3 dilation firewall

**Parent:** v1_46 exact one-hop flavor lift. **Current report:** `reports/Paper00-DownstreamGeometryClosure-v1_6.md`. **Status:** rigorous finite geometry/representation theorem; native physical-action/current and particle decay remain unproved.

- The one-hop `K(H)` has an exact local Lie-algebra commutator defect `D12=[K(E12),K(E21)]−K(E11−E22)` with **rank 17**, squared Hilbert–Schmidt norm **124**, and exact kernel the protected flavor `3`. The leading 17×17 scaled minor is **7 modulo 11**. A basis-independent positive Lie-defect sum selects the same flavor projector as its unique zero eigenspace.
- The original directed-pair `A5` module is exactly `1+3+3'+2·4+5`. Its harmonic representation is `H0+H1+H3+H4`; the exact 20×20 vertex evaluation determinant is **8 mod 11**. The full 25-dimensional degree-≤4 harmonic evaluation has a 5-dimensional kernel.
- Minimal full SU3 *representation* space containing the 20-state A5 module is **25**; preserving the existing three-state sector as an invariant fundamental SU3 requires **28**. The explicit minimal module is `Sym1(C3)+Sym3(C3)+Sym4(C3)` and its eight-mode A5 complement is `3+5`.
- Crucial new no-go: **no minimal 28-dimensional SU3 completion can reproduce the whole 20-state one-hop flavor current** in the same normalization. An SO3 rotation generator has squared HS strength at least **15/2** on the unavoidable spin-3 plus fundamental blocks, whereas `K(lambda_a/2)` has strength **5**. This is not a failed physical prediction: it separates representation extension from actual action-derived source compression.
- Conditional native Ward test: CAR vector charges obey their exact current algebra on a Gauss-compatible source domain. If their 20-graph compression is `K(H)`, the nonzero local Lie defect forces external charge leakage; the 3-state protected subspace has no such algebra defect. **No hadron masses, pole amplitudes or decay widths are promoted.**

**Exact certificate:** `data/Paper00-FlavorAlgebraSelection-v1_1.json`  
**Compiler / replay:** `scripts/Paper00-FlavorAlgebraSelectionCompiler-v1_1.py`, `scripts/Paper00-ReplayFlavorAlgebraSelection-v1_1.py`  
**Typed graph:** `graph/Paper00-SU3FlavorMinimalDilation-v1_1.graphml`  
**Unmodified:** all inherited geometry certificates, canonical source papers, DAG atlas and proofchain audit bundles. Only latest downstream-closure report is retained.

---

# S³ Structure Network v1_46 — exact one-hop flavor algebra and complete first-order axial source lift

**Parent:** v1_45 exact finite geometry. **Current report:** `reports/Paper00-DownstreamGeometryClosure-v1_5.md`. **Scoped status:** the full geometric flavor/source matrix calculus is constructed on the selected three-dimensional five-core carrier; occurrence in the actual finite QCD action, physical state selection and widths remain unproved.

- Exact local neighbor frame: `sum_(k~j) u_k u_k^T = I/2+u_j u_j^T` at each of the 20 dodecahedral vertices.
- Universal one-hop *-preserving flavor operator `K(H)_(jk)=2A_(jk) u_j^T H u_k - 2 delta_(jk) u_j^T H u_j` with **exact** `K(H)Q=QH` for all `H in M3(C)`, not just a triplet or quintet.
- Full eight-dimensional traceless flavor algebra, scalar and arbitrary Hermitian three-flavor mass words lift locally. The new quintet first-order current is the unique preserving one in the specified real-symmetric A5-equivariant one-hop class; the old curvature triplet is its imaginary-skew part.
- One source-linear, self-adjoint 24-axis geometric Hamiltonian has exact spin-flavor reduction, all 24 normalized `2G_iA` currents on the symmetric 56, and zero complementary Schur coupling **within that action**. It has different second source contacts from the v1_45 positive nonlinear spin-link action; selection between them remains an actual-action issue.
- Proof certificates: 180 exact neighbor identities, 540 exact all-matrix intertwiners, 60 exact A5 action checks, exact local quintet rank-three witness, independent gradient triplet leakage witness. Source-response comparison predicts distinct exact finite reference Hessians; **none is promoted as a physical QCD susceptibility**.

**New certificate:** `data/Paper00-ProtectedFlavorLift-v1_1.json`  
**New typed overlay:** `graph/Paper00-ProtectedFlavorLift-v1_1.graphml`  
**Compiler and deterministic replay:** `scripts/Paper00-ProtectedFlavorLiftCompiler-v1_1.py`, `scripts/Paper00-ReplayProtectedFlavorLift-v1_1.py`.  
**Baseline preservation:** no edits to parent geometry certificates, canonical source paper ZIP, proof DAG or proof-chain audits. Only the superseded downstream-closure research report is replaced.

---

# S³ Structure Network v1_45 — second jet, quartic Schur return and Gauss-safe baryon source

**Parent:** v1_44 unchanged except the superseded downstream research report; no updated canonical papers, DAG or audit bundles. **Classification:** exact finite geometric comparison plus an explicitly scoped link-dependent local-Gauss-invariant trial-source construction, not an actual QCD action, hadron pole or physical decay certificate.

- The first jet generates triplet currents; the **second jet of the same positive spin-link action** generates all five real flavor quadrupole response directions with no independently fitted coefficient. 81/81 tensor equalities verified exactly in `Z[sqrt(5)]`.
- All-order direct-source parity: the compressed action has only `1_spin x (1+5)_flavor` and `3_spin x 3_flavor` operators. `3_spin x 5_flavor` is **not** a direct source jet; it is generated by commutators. This restriction is essential when interpreting axial vertices.
- The first complementary Feshbach return from the selected flavor triplet is `O(b^4)` in a rank-one spin-link source, with exact nonzero strengths `1/80` and `1/40` into `3prime` and `4odd`.
- Any complex selected light-flavor plane has six isovector `A5` channel strengths fixed by one invariant `kappa=tr(P_heavy P_heavy^T)`, with sum 15. A supplied physical flavor mass operator fixes its projector spectrally.
- Promoting the existing rooted color/Wilson 56 source to a link-dependent Haar wavefunction gives a **genuine Gauss-invariant trial isometry** and exact on-site CAR charge compression. The full interacting physical Hamiltonian and axial source still require matching.

**Historical report:** `Paper00-DownstreamGeometryClosure-v1_4.md` is superseded and omitted from this release; retained second-jet certificate remains valid.  
**New exact certificate** `data/Paper00-SecondJetGaussIsospin-v1_1.json`.  
**New scoped graph** `graph/Paper00-SecondJetGaussIsospin-v1_1.graphml`.  
**Replay** `OPENBLAS_NUM_THREADS=1 python scripts/Paper00-ReplaySecondJetSource-v1_1.py`.  
Inherited v1_44 spin-flavor, v1_43 midpoint and all earlier exact graph data remain available and have unchanged status.

---

# S³ Structure Network v1_44 — curvature spin–flavor and meson–baryon source bridge

Parent local derived v1_43; user-supplied v1_41 geometry preserved. **Exact mathematical comparison only; no physical QCD action / Gauss-reduced current / actual decay widths identified.** No source-paper or DAG/audit proof status changed.

- Exact invariant 20-pair **non-gradient curl** `C_a`, with `Q† C_a Q=-lambda_a/2` and full `[P3,C_a]=0`. Its algebraic `3+5` completion gives all eight traceless Hermitian three-flavor matrices.
- Positive unitary spin-link Dirichlet action produces the primitive spin×flavor triplet source without separately imposed transition vertices. The canonical symmetric three-constituent source 56 (16 octet + 40 decuplet) reproduces exact triplet 15, quintet 25, total 40 and all A5-resolved channels, in integer-pair `Z[sqrt(5)]` arithmetic.
- Exact isometry `Herm(3) <-> N9=1+3+5` of constant/linear/quadrupole dodecahedral harmonics, including rank-eight meson-octet to baryon-transition **tight-frame factor five**. A real light-flavor-plane selector produces isospin `(1 triplet + 2 quintet)` with six rational source strengths.
- Scoped reference placement through *existing* rooted Wilson/CAR 56 source port; no claim of equality with the dynamical physical current.

**Historical report:** `Paper00-DownstreamGeometryClosure-v1_3.md` is superseded and omitted from this release. **Exact certificate:** `data/Paper00-CurvatureSpinFlavorBridge-v1_1.json`. **Typed graph:** `graph/Paper00-CurvatureMesonBaryonPorts-v1_1.graphml`. **Replay:** `OPENBLAS_NUM_THREADS=1 python scripts/Paper00-ReplayCurvatureSpinFlavor-v1_1.py`. Previous v1_43 midpoint graph, scripts, numerical certificates and complete inherited network retained.

---

# S³ Structure Network v1_43 — single-action midpoint triplet spectral closure

Parent local derived v1_42; user-supplied base v1_41, parent core data and all existing proof owners preserved. **This is a new mathematical comparison overlay, not a source-paper rewrite, a global proof-status promotion, or a physical particle decay model.**

- Complete local Hermitian triplet current classification on the 20 directed core pairs: **4 real directions**.
- Unique nearest-edge shift-preserving **symmetric Dirichlet current** (up to a common normalization), with exact diagonal/contact term and non-gauge spectral response.
- All six finite spectral sectors, **five** mathematically descending transition pairs, exact squared strengths and selection zeros from the same current.
- Exact finite `5`-sector second-order Feshbach return, normalized trace susceptibility and mean second-order energy response.
- Precisely typed `W56` spin–flavor comparison via normalized spin CG, including the unselected cubic-four embedding angle; **no widths or physical currents claimed**.

Historical report: `Paper00-DownstreamGeometryClosure-v1_2.md` is superseded and omitted from this release. New exact certificate: `data/Paper00-MidpointTripletResponse-v1_1.json`. New typed visualization: `graph/Paper00-MidpointTripletTransitions-v1_1.graphml`. New deterministic replay: `python scripts/Paper00-ReplayMidpointResponse-v1_1.py`. Historical 600-cell core, eight-orbital algebra, 20-triplet global space, dodecahedral Hodge, internal Clifford and their v1_42 certificates remain available **without modification**.

---

# S3 Structure Network v1.41 — mathematical closure overlay

Parent v1.40; native vertex and incidence data preserved, graph-closure overlay added. No physical decay Hamiltonian is selected.

# S³ Structure Network v1_40 — finite electromagnetic geometry and literature comparison

Parent: v1_39. Current source: `Paper00-PapersMinimal-v3_040.zip` (SHA-256 `1c5f95211d4ce90aa09f868024f5c71fd080f59a9c7228558d295be4ce23de34`).

New data: `data/v140_literature_integration.json` records the **exact 24-cell unit-incidence edge-curl spectrum**, its 23 gauge gradients and 73 nonzero modes, the **conditional positive face-weight comparison**, and typing distinctions for SU(2) localization, local Maxwell, and temporal current response.

**No physical charged-current packet was computed**. No physical fine-structure constant, Coulomb-core regularization, orbit confinement, or particle decay selection is promoted. Previously existing structural data, mappings and provenances are preserved unchanged.

---

# S3 Structure Network v1_39 — scoped action-incidence exclusion overlay

Parent: v1_38, inherited effective geometry graph unchanged. Current source: Paper00-PapersMinimal-v3_039.zip.

New `data/v139_action_incidence_exclusions.json` records five exact mathematical constraint claims, a type-safe open physical hierarchy-origin certificate and two possible future noncircular proof routes. No geometric object was newly asserted to occur as a physical chiral source. `Cert_hier` remains OPEN. No new physical transition edges or observed mass predictions.

The prior README is carried below as historical provenance; it is not a current re-audit.

---

# S³ Structure Network v1_38 — charged action-origin typed frontier

Inherits v1_37 effective geometry, without altering mathematical nodes or promoting physical action edges. New separate GraphML candidate network and JSON ledger identify the missing typed Hopf/triality geometry-to-charged-action constructor.

## Inherited README (historical)

# Born–Hopf S³ Structure Network — v1_36 (Batch 25: current harmonic neutral-boundary and GP3 owner diagnostics)

**Parent:** `Paper00-S3StructureNetwork-v1_35.zip`; **source:** `Paper00-PapersMinimal-v3_029(1).zip` current TeX. The updated **effective mathematical graph** now has **879 objects, 1424 typed relations, 250 joint conditions, 189 compositions** and S³-root weak component **872**. All v1_35 historical base graph/JSON and its 24 source-guarded mathematical replay certificates are preserved byte-for-byte; they remain *conditional* and do not prove actual physical occurrences.

**New independently replayed geometry:** the native 6-point Hurwitz evaluation of 169-dimensional degree-12 round S³ harmonics has Gram `156I₆+13J₆`, coisometry `B=G^(-1/2)E`, orthogonal `163+5+1` decomposition, ordinary kinetic Green cross-return `5/168` **before** Schur elimination and residual `163/168` **after** it. S₃ regular-action and character computations give a `135`-dimensional Hom space between kernel and augmentation modules; rank and symmetry alone therefore do not select a physical coupling. The normalized rotational scalar `U₁₂(Re q)` has projector weights `(1/39,0,38/39)`, not the rank-count fractions. The formal terminal rank magnitudes `(1/√163, √5, √163)` remain **conditional mathematical ports**, not masses.

**Critical source-branch correction:** Paper V-B v5_201 identifies the older D₄ inverse/direct/closed-Gram neutral word `(x⁻¹,x,x²)` as **historical only on the newer harmonic-rank branch**. Accordingly the mathematical replay `G32-056` remains true on its old constructor, but is explicitly classified `HISTORICAL_D4_ONLY_ON_NEW_HARMONIC_BRANCH` on the v1_36 effective graph. The general native `E56` row-energy scale remains a valid conditional source rule. The actual action-owned harmonic K56 constructor, its complete Green/Schur consumption and a physical neutral pole readout are **not generated by these geometric checks**.

**GP3 whole-candidate diagnostic:** on Paper V-A's `M12(C)⊕M36(C)` factor grammar, any *occurring frozen same-owner unnormalized heat trace* distinguishes nontrivial faithful multiplicity ampliations. This tests and can obstruct a proposed whole-candidate comparison; it does **not** itself generate GP3's proper comparison or establish one physical copy. The actual relative meson Hamiltonian and its reducing sector remain open too. **Zero physical claims promoted.**

**Read first:** [`reports/BATCH25_CURRENT_NEUTRAL_HARMONIC_GP3_OWNER.md`](reports/BATCH25_CURRENT_NEUTRAL_HARMONIC_GP3_OWNER.md), then [`data/v136_frontier_resolution.json`](data/v136_frontier_resolution.json). **Effective graph:** `graph/mathematical_structure_network_effective_v136.graphml`; focused graph `graph/batch25_current_neutral_harmonic_GP3.graphml`; exact certificate `data/v136_exact_harmonic_gp3_certificate.json`; source locator/hash ledger `data/v136_current_source_anchors.json`. Use `python verify_batch25_v136.py`, `python validate_geometry.py --fast`, `python verify_graph_exports.py`, `python verify_manifest.py`; query `python geometry_verified_query_v136.py --summary` or `--boundary`. Older base counters in `validate_geometry.py` intentionally describe the preserved historical 862/1392 graph, while `verify_batch25_v136.py` tests the 879/1424 **effective** extension.

---

# Born–Hopf S³ Structure Network — v1_35 (Batch 24: complete guarded mathematical replay, owner boundaries retained)

**Parent:** `Paper00-S3StructureNetwork-v1_34.zip`. The three remaining guarded mathematical relation maps (`G32-052`, `G32-056`, `G32-072`) now have independent **source-scoped conditional finite mathematical replays**: the exact Hurwitz source frame and commuting color/family `M9(C)` algebra, the `E56` three-role response-jet algebra, and the color-singlet reducing meson-Hamiltonian spectral compression with an exact nonreducing counterexample. The cumulative **conditional** map replay layer reads **24/24**, but **all three targeted source-owner selection boundaries remain open** and all 21 earlier maps retain their guards. No physical particle mass, action, GP3 whole-candidate owner, source theorem or occurrence is promoted.

**Key mathematical refinement:** physical invariant-sector interpretation requires `[P_sector,H_L]=0`; without this, `P_sector H_L P_sector` yields only compressed Ritz levels. Color invariance alone does not prove that a selected `JPC`/flavor subblock is invariant. The reported exact example does not assert that the physical source violates that condition.

**Graph and files:** original 862 objects, 1,392 typed mathematical relations, 242 guarded joint conditions, 183 compositions are **unchanged**. Effective dual-axis graph is `graph/mathematical_structure_network_effective_v135.graphml`, with focused `graph/batch24_scoped_math_and_owner_frontier.graphml`. The source-owner frontier is `data/v135_source_owner_frontier.json`; mathematical replay is `data/v135_scoped_math_replays.json`; full TeX source hashes and labels are `data/v135_source_anchor_ledger.json`. Graph is not the proof DAG and is not a decay/mass compiler.

**Full report:** [`reports/BATCH24_HURWITZ_NEUTRAL_MESON_DUAL_AXIS_VERIFICATION.md`](reports/BATCH24_HURWITZ_NEUTRAL_MESON_DUAL_AXIS_VERIFICATION.md). **Release checks:** `python verify_batch24_v135.py`, `python validate_geometry.py --fast`, `python verify_graph_exports.py`, `python verify_manifest.py`. **Interactive text query:** `python geometry_verified_query_v135.py --owner-pending`. Source-TeX rehash requires the current separately supplied `.tex` directory.

---

# Born–Hopf S³ Structure Network — v1_34 (Batch 23: exceptional geometry, CAR and matter-map replays)

**Parent:** `Paper00-S3StructureNetwork-v1_33.zip`. Conditional mathematical verification advances from **17/24** to **21/24** guarded source maps. **Four newly independently replayed:** `G32-059` (actual nonzero finite CAR **pair algebra given occurrence**, not K16 occurrence), `G32-061` (exact 48-element binary octahedral quotient/sign projector rank-three conditional carrier), `G32-066` (48D finite matter-role projector and rational hypercharge decomposition on the **given** generated `Fcore⊗G` carrier), `G32-070` (full 72-root E6, Clifford signed isometry, and `J₆†J₆=I₆`).

**Three still awaiting independent source selection/owner proof:** `G32-052` Hurwitz independent color-family composition/GP2–GP3 multiplicity, `G32-056` terminal word excludes an independent dimensionless κ56 port, `G32-072` selected relative meson Hamiltonian and physical pole bridge. The archive contains **exact independent counterfamily/boundary tests**, not fabricated closures. Paper V-A explicitly makes physical K16 boundary-pair occurrence conditional. **Zero source theorems or physical occurrences promoted.**

**Topology unchanged:** 862 objects, 1392 typed relations, 242 joint guards, 183 compositions; S³-root component 855, five deliberate non-identification isolates and one historical two-object Gram component. Original v1_32 GraphML and JSON are preserved, as are all v1_33 graph/evidence files. **Effective status** must be read from `data/v134_verified_frontier_status.json` or `graph/mathematical_structure_network_effective_v134.graphml`, **not** from the historical base GraphML. `python geometry_verified_query_v134.py --pending` or `--new` queries the current layer.

**Batch 23 full report:** [`reports/BATCH23_EXCEPTIONAL_CAR_REPRESENTATION_AND_FRONTIER.md`](reports/BATCH23_EXCEPTIONAL_CAR_REPRESENTATION_AND_FRONTIER.md). Reproduce `python verify_batch23_v134.py`, `python validate_geometry.py --fast`, `python verify_graph_exports.py`, `python verify_manifest.py`. External current-TeX rehash, when the separate corpus is available: `BH_PAPERS_TEX_DIR=/path/to/tex python verify_boundary_v134.py --check --strict-sources`. **Historical full regeneration not rerun; global semantic exhaustiveness not claimed.**

---

# Born–Hopf S³ Structure Network — v1_33 (Batch 22, exact mathematical-proof overlay)

Parent `v1_32`. This release independently replays **17/24 guarded source-scoped mathematical maps**, retaining **7 pending** and all physical/source-selection boundaries. The original network topology is unchanged (**862 objects, 1392 typed relations, 242 joint guards, 183 compositions; 855 S³-root objects; 5 intentional isolates + separate abstract Gram pair**). The source files/hashes and graph history are preserved. **No entire physical theorem, meson pole, rest mass, cosmological source or proof-DAG condition is promoted.**

**New exact results:** all three 15D A5-equivariant rooted Hodge exterior modules; full rational 10D trimer-flavor Jacobian; exhaustive Z6 finite representation kernel; full finite Pauli/Fischer shell ranks; independently checked finite-current/terminal-support laws. The paper's finite-collar norm bound is sharpened universally to `LambertW(1/e)/L` (~0.27846/L). Every replay is **conditional on precisely preserved source-domain guards**, and 7 maps remain unverified.

**Current effective graph:** `graph/mathematical_structure_network_effective_v133.graphml`, certificate-only `graph/batch22_verified_scoped_math_maps.graphml`; `data/v133_verified_frontier_status.json` is the indexed effective verification layer. The historical `data/mathematical_relations.json` and `graph/mathematical_structure_network.graphml` remain bytewise unchanged from v1_32 so all inherited validators still work. Query `python geometry_verified_query_v133.py --summary`, `--pending` or `--edge G32-051`. Replay `python verify_batch22_v133.py`, `python validate_geometry.py --fast`, `python verify_manifest.py`.

**Detailed new report:** [`reports/BATCH22_INDEPENDENT_SCOPED_MATH_REPLAYS.md`](reports/BATCH22_INDEPENDENT_SCOPED_MATH_REPLAYS.md). The v1_32 README and earlier batch records follow below for history.

---

# Born–Hopf S³ Structure Network — v1_32 (geometry-only Batch 21, full source-map inventory)

A **finite mathematical object and typed relation network**; not the global proof DAG, and not a physical particle mass model. Parent `v1_31`. **53/53** previously isolated current-source labels/hashes checked, **48 source-scoped mathematical maps now linked**, **5 intentional non-identifications remain separate**, and one original abstract two-node Gram component has not been assigned a false isometry.

| Graph | v1_31 | **v1_32** |
|--|--:|--:|
| Objects/operators | 849 | **862** |
| Typed relations | 1,320 | **1392** |
| Joint-input conditions | 185 | **242** |
| Compositions | 171 | **183** |
| Isolated objects | 53 | **5** |
| S³-root weak component | 794 | **855** |

**Certificate status.** Eight new exact/numerical mathematical computations, including the exact Q(sqrt5) A5 rank-nine projector, Hurwitz quadratic even10 kernel, ten-axis frame, Petersen exterior map, round S³ spectrum and 62-node sky frame; plus finite A2/anomaly/Z6 arithmetic cross-checks. **24 additional guarded source-formula maps still need independent exact proof replay**. Link presence does not mean a source-selected physical action, state, meson pole, spacetime field, or observable was derived.

**Files and commands.** `reports/BATCH21_S3_STRUCTURAL_CLOSURE_AND_FRONTIER.md`, `data/v132_remaining_frontier_classification.json`, `data/structure_closure_v132_instance.json`, `data/v132_second_pass_guarded_math_checks.json`, updated cumulative and batch21 GraphML/DOT. Run `python verify_batch21_v132.py`, `python verify_graph_exports.py`, `python validate_geometry.py --fast`, `python verify_manifest.py`, `python verify_parent_v131_integrity_v132.py`, `python scripts/rebuild_structure_graph_v132.py --check`, and `python geometry_query.py --batch21 --closure-frontier`.

**Meaning of finished:** all preexisting isolated source-map candidates have an explicit verified, conditional, or deliberate no-identification classification. Full independent proof of all 24 conditionally connected mathematical maps and global semantic completeness **NOT CLAIMED**.

---

# Born–Hopf S³ Structure Network — v1_31 (geometry-only Batch 20)

**A cumulative mathematical-object-and-map network; NOT the proof/evidence DAG.** Parent `v1_30`. This batch constructs a **marked** `S³=SU(2)→SU(3)` embedding; its invariant normalized Cartan/Hopf 3-form; a finite `3⊗3̄=1⊕8` Casimir and two-dimensional centralizer; exact two-vertex Haar/Gauss projectors; and an explicit, gauge-natural finite path-refinement example. These are mathematical structures, **not independently realized QCD dynamics**.

| Geometric graph | v1_30 | **v1_31** |
|---|---:|---:|
| Objects/operators | 832 | **849** |
| Typed relations | 1,279 | **1,320** |
| Joint-input conditions | 175 | **185** |
| Mathematical compositions | 162 | **171** |
| Isolated records | 63 | **53** |
| Main connected component | 767 | **794** |

**Verified new identities:** `ι^*(-Tr(θ^3)/(24π²))=vol_round/(2π²)` with marked orientation; `Σ_a L_a²=3(I−P₁)` on the selected `9D` conjugation carrier; rational centralizer rank `79/81` implying `C⊕M₈` generated algebra and `C⊕C` commutant; two-vertex product-Haar projection `P₁⊗P₁`, rank 1, with Casimir spectrum `0(1),3(16),6(64)`; and ordered path-holonomy refinement preserving endpoint gauge conjugation. The `9×9` singlet projector is entrywise identical to the matrix already in `v1_30`.

**Precision:** 17 new actual mathematical objects and 41 maps, of which 26 are exact for their specified model and 15 guarded. Ten older isolated records gain connections, but a connection to a source-labelled QCD object is not validation of that full operator. A two-object Gram component remains separate; the constitutional `S¹` role remains distinct. No proof-DAG nodes or physical transitions are added.

Reproduce with `python verify_batch20_v131.py`, `python verify_graph_exports.py`, `python validate_geometry.py --fast`, `python verify_manifest.py` and query `python geometry_query.py --batch20`, `--hopf-su3`, `--two-vertex-gauss`, `--path-refinement-example` or `--geometry-coverage`. Eleven current-source TeX label/hashes were checked against `Paper00-PapersMinimal-v3_029(1).zip` and stored as provenance only. **Full historical regeneration was not run.**

**Details:** [`reports/BATCH20_HOPF_SU3_HAAR_GAUSS_PATH_GEOMETRY.md`](reports/BATCH20_HOPF_SU3_HAAR_GAUSS_PATH_GEOMETRY.md). **Exact matrices:** `data/hopf_su3_v131_instance.json`. **Coverage ledger:** `reports/geometry_completeness_v131.json`. The mathematical network remains **non-exhaustive**.

---

# Born–Hopf S³ Structure Network — v1_30 (geometry-only Batch 19)

**Cumulative mathematical object network, not the proof/evidence DAG.** Parent `v1_29`. Batch19 adds exact all-support Petersen compression calculations and separately scoped SU(3) finite invariant tensor geometry. **Do not identify** the new SU(3) tensor examples with the full QCD color/gauge compiler, or turn Petersen eigenvalues into observed masses.

| Network quantity | v1_29 | v1_30 |
|---|---:|---:|
| Mathematical object/operator records | 818 | **832** |
| Typed mathematical relationships | 1,239 | **1,279** |
| Joint-input mathematical conditions | 167 | **175** |
| Derivation records | 154 | **162** |
| Isolated records | 75 | **63** |
| Largest connected component | 743 | **767** |
| Separate nontrivial components | 0 | **1** |

**New exact operator identity:** uniform k-subset averaging of the squared Petersen mirror compressions gives `a_k P6+b_k(I−P6)` with coefficients k=2 `(1/25,1/25)`, k=3 `(9/50,2/25)`, k=4 `(12/25,2/25)`, k=5 `(1,0)`; verified by full exact `15×15` matrix equality. All 32 support characteristic polynomials agree with Paper VII-D. Also regenerated finite `SU(3)` invariant tensor projectors and Fierz/Casimir contractions using exact matrices; these are **mathematical conditional models** on a selected color trimer, not an independent derivation of physical QCD.

**Scope status:** Twelve prior records gained graph links, but only **four direct Petersen connections** constitute exact identified mathematical suboperators; **eight links** are guarded partial finite-tensor examples. A two-node abstract Gram component remains deliberately separate from the S³ component. Neither 63 graph isolates nor source inventory suffices to certify exhaustive geometry.

**Verification:** `python verify_batch19_v130.py`, `python verify_graph_exports.py`, `python validate_geometry.py --fast`, `python verify_manifest.py`. Query: `python geometry_query.py --petersen-core-compression` or `--su3-finite-invariants` or `--geometry-coverage`. The **full historical regeneration suite was not run** in this batch.

**New artifacts:** `data/finite_invariant_geometry_v130_instance.json`, `data/batch19_current_tex_witnesses.json`, `graph/batch19_*`, `reports/BATCH19_PETERSEN_COMPRESSION_SU3_FINITE_INVARIANTS.md`, and `reports/geometry_completeness_v130.json`.

---

# Born–Hopf S³ Structure Network — v1_29 (geometry-only Batch 18)

**Cumulative mathematical object-and-relation network, not an evidence DAG.** Parent `v1_28`. This batch independently regenerates the `2T` Hurwitz Cayley graph, its `Q8` weighted quotient, the exact rank-two `−4` spectral projector, oriented 24-cell cellular Hodge chain, and associated local tangent/relative quotient geometry. The 96-face Hodge characteristic polynomial is **already in Paper VII-A**; this release adds its exact regeneration, explicit boundary matrices, the dual-cell adjacency map and cross-network links.

| Quantity | v1_28 | v1_29 |
|---|---:|---:|
| Mathematical object/operator records | 799 | **818** |
| Typed geometric relations | 1,185 | **1,239** |
| Joint-input conditions | 158 | **167** |
| Derivation/composition records | 144 | **154** |
| Isolated records | 88 | **75** |
| Largest connected mathematical component | 711 | **743** |

**Added:** 19 objects, 54 relations, nine guards, ten mathematical compositions; 13 existing isolates linked. Of 75 outstanding isolated records, 3 are foundational/technical and 72 are later-paper operators. **Not exhaustive.**

**Exact results:** the Hurwitz quotient by `Q8` is weighted `4K3`, with `P_-4(q,r)=(3 1_{qQ8=rQ8}-1)/24` of rank 2; the cellular chain ranks are `(23,73,23)` and `H¹=H²=0`; the unit-weight 96-face Hodge spectrum is independently regenerated, with 73+23 exact/coexact dimensions; and the dual 24-cell facet graph is explicitly isomorphic to the vertex adjacency. Mixed source operator names only receive guarded mathematical-suboperator links. No action or decay is derived.

**Verification:** `python verify_batch18_v129.py`, `python verify_graph_exports.py`, `python validate_geometry.py --fast`, `python verify_manifest.py`; queries include `--hurwitz-hodge`, `--hurwitz-q8`, `--geometry-coverage`. The full historical suite is included but was not rerun in full.

**Detailed report:** [`reports/BATCH18_HURWITZ_CAYLEY_HODGE_COMPLETENESS.md`](reports/BATCH18_HURWITZ_CAYLEY_HODGE_COMPLETENESS.md). **Data:** `data/hurwitz_cellular_v129_instance.json`, `data/batch18_current_tex_witnesses.json`, `reports/geometry_completeness_v129.json`. Source paper TeX remains in the separate PapersMinimal ZIP; the graph contains no theorem nodes or physical transitions.

---

# Born–Hopf S³ Structure Network — v1_28 (geometry-only Batch 17)

**Cumulative mathematical graph, not an evidence DAG.** Parent `v1_27`.

**New independently regenerated relations:** the exact `2I`/ten-`C6` icosahedral harmonic tower `H6,H10,H15`; the primary-left-Hopf `Φ12=H6(q̄ i q)` and right-`2I` invariant scalar shell; and the *entrywise exact* identity `Bu Buᵀ−B5 B5ᵀ=24Π25`, connecting Petersen pair coefficients, the 25 translated Hurwitz cells and the 600-cell Chebyshev zero band. Also added round-`S³` mean-zero scalar Green and finite momentum-`S³_p` harmonic-count maps. The 25-block `T6` chamber return remains explicitly source-attested at its input and independently checked only at the indicated contrast eigenvalue.

| Counts | v1_27 | v1_28 |
|---|---:|---:|
| Objects/operators | 785 | **799** |
| Typed mathematical relations | 1,134 | **1,185** |
| Joint-input conditions | 148 | **158** |
| Derivation/composition records | 135 | **144** |
| Isolated records | 99 | **88** |
| Largest connected component | 686 | **711** |

**Reproduce:** `python verify_batch17_v128.py`; `python validate_geometry.py --fast`; `python verify_graph_exports.py`; `python verify_manifest.py`.

New exact data: `data/icosahedral_harmonics_v128_instance.json`, `data/petersen_pair_coefficients_v128_instance.json`, `data/scalar_spectral_compositions_v128_instance.json`. Query: `python geometry_query.py --batch17`, `--icosahedral-harmonics`, `--pair-gram`, `--s3-green`, or `--geometry-coverage`.

**Detailed report:** [`reports/BATCH17_ICOSAHEDRAL_HOPF_PETERSEN_INCIDENCE.md`](reports/BATCH17_ICOSAHEDRAL_HOPF_PETERSEN_INCIDENCE.md). **Source evidence:** `data/batch17_current_tex_witnesses.json` (current `PapersMinimal v3_028` TeX labels/hashes, not full papers). No physics, decay, or theorem-record nodes. **Not exhaustive.** Historical full regeneration remains separate and was not rerun to completion.

---

# Born–Hopf S³ Structure Network — v1_27

**Geometry-only Batch 16: exact foundational-gap bridging, M8 Hodge/exchange, Clifford energy-character source, Petersen comparison, and 600-cell twisted 25D projector.** This is a standalone cumulative mathematical network, not the existing proof/evidence DAG.

**Main independently regenerated result:** the 120×120 degree-four quaternion character projector satisfies `Π25²=Π25`, `rank Π25=25`, and `Ran Π25=ker A600`, with a modularly certified exact rank of the 600-cell adjacency. It is orthogonal to the old 16D `−3` transporter projector. Independently, the `C6`/Petersen flux gives `K Kᵀ=5 I3` and a rank-two fixed-axis Gram. These are mathematical, not physical, statements.

## Progress

| Mathematical graph count | Parent v1_26 | Current v1_27 |
|---|---:|---:|
| Objects and operators | 772 | **785** |
| Typed mathematical relationships | 1,076 | **1,134** |
| Joint input bundles | 137 | **148** |
| Derivations/compositions | 123 | **135** |
| Main weak component | 648 | **686** |
| Isolated records | 115 | **99** |
| Disconnected nontrivial components | 2 | **0** |

**Remaining isolation:** 3 foundational/technical objects (independent S¹ constitutional role and two operator-realization branches) and 96 later-paper operator records. **Global exhaustiveness is not certified.**

Read [`reports/BATCH16_COMPLETENESS_CLIFFORD_M8_TWISTED25.md`](reports/BATCH16_COMPLETENESS_CLIFFORD_M8_TWISTED25.md) for the exact constructions, conditions, equations, source scopes and limitations; [`reports/geometry_completeness_v127.json`](reports/geometry_completeness_v127.json) for every remaining isolation; and [`data/geometry_bridges_v127_instance.json`](data/geometry_bridges_v127_instance.json) plus [`data/twisted25_v127_instance.json`](data/twisted25_v127_instance.json) for the actual matrices. The batch includes regenerating verifiers and source-hash provenance, but **does not copy the proof DAG or physical transitions**.

## Quick checks

```bash
python verify_batch16_v127.py
python verify_twisted25_v127.py
python verify_graph_exports.py
python validate_geometry.py --fast
python verify_manifest.py
python geometry_query.py --twisted25
```

The longer historical all-batch regeneration is available separately; `--fast` is not a substitute for it.

---

# Born–Hopf S³ Structure Network — v1_26

# Geometry-only Batch 15 — v1_26

**Purpose:** Begin a systematic *geometric completeness* audit of the actual mathematical object network, closing explicit maps without importing theorem/proof-DAG nodes or physics. The previous release is `v1_25`.

## Real additions (independent calculations)

1. **600-cell to Petersen total graph:** In a fixed marked quaternionic `2I`, the real-half shell `D20` and the zero-real shell `Z30` give the induced total graph `T(D20)` with 50 vertices and 150 edges. Quaternion inversion is a free graph automorphism and yields the 2-fold graph covering `T(D20) → T(P10)` with 25 vertices and 75 edges. All vertices, 50/150 and 25/75 edges, the twofold vertex map, the 50×25 adjacency intertwiner and both exact characteristic polynomials are included. The graph theorem itself is source-attested in Paper I-B; the characteristic polynomial is an additional exact calculation.
2. **Milnor scalar-operator branch:** The metric-dependent left-invariant SU(2) frame is now connected to the finite spin-`j` Peter–Weyl blocks `H_j=Σa_i^-2 J_i²`, their step-two Jacobi/parity chains, and the spin-one unordered metric-weight reconstruction from pairwise sums. Exact symbolic regenerators test all spins `j=0,1/2,...,4` with four weight triples and give a proof-algebra check of the Casimir spectral bound. **Do not identify** the metric-adapted left Milnor frame with the primary right Hopf/ Berger frame without inversion, orientation and homothety. The complete Hodge/Dirac and infinite heat trace links are **source-attested only**, not independently regenerated in this batch.
3. **Ten C6 axis-line projectors:** The pairwise intersections of the five marked `2T` cores yield ten exact rational-Q(√5) 3×3 rank-one projectors. Their five local sums are `(4/3) I_3` and the global sum is `(10/3) I_3`. This independently closes another previously isolated geometric-object node. These formulas are already given in Paper III-C and upstream Paper I-A; the batch reproduces them from actual 600-cell quaternionic coordinates.

## Cumulative network and audit

| Network quantity | Parent v1_25 | Current v1_26 |
|---|---:|---:|
| Mathematical object records | 759 | **772** |
| Typed mathematical relationships | 1,043 | **1,076** |
| Joint-input constraints | 132 | **137** |
| Derived/composed results | 117 | **123** |
| Largest weak component | 628 | **648** |
| Isolated geometric object records | 122 | **115** |
| Weak components | 125 | **118** |

**Important:** A graph component is not a proof of geometry and an object count is not a count of inequivalent geometric structures. **This is not yet exhaustive**. 19 foundational/technical source-attested objects and 96 later-paper mathematical operator records remain isolated. Two nontrivial components of sizes 6 and 3 remain outside the main connected component.

### Current source provenance check

Used the current supplied `Paper00-PapersMinimal-v3_027(1).zip` for label-presence and source-hash checking (the TeX corpus itself is *not* bundled). This is a version audit, **not** independent proof review.

- Nodes: 236 exact source-hash-and-label matches; 263 labels found in changed source versions without semantic re-verification; 273 records without a direct TeX-label witness in that graph record.
- Relations: 231 exact matches; 124 labels preserved in newer source files; 721 with no direct TeX-label witness in the relation record, including independently computed relations.

The missing-witness count **must not** be conflated with mathematical invalidity: new coordinate verifications can have no paper label. Similarly, a preserved TeX label does **not** establish unchanged theorem content.

## Regeneration commands

```bash
python verify_batch15_v126.py
python verify_graph_exports.py
python validate_geometry.py --fast
python geometry_query.py --geometry-coverage
python geometry_query.py --petersen-total
python geometry_query.py --milnor-spectral
python geometry_query.py --c6-tight-frame
python verify_manifest.py
```

The long historical all-batches regeneration remains separate; use `python validate_geometry.py` without `--fast` if needed. **Do not describe it as completed unless executed.**

### Future mathematical focus

Use `reports/geometry_completeness_v126.json` as the closure ledger, separating missing **actual mathematical maps**, source-only objects needing classification, and genuine nonidentification constraints. High-value next targets include the disconnected scalar/exchange heat component, the protected Clifford response component, the twisted 25-dimensional projector, and the general spherical-spaceform classification. Prioritize exact commuting maps and obstructions rather than automatically connecting isolated nodes by shared vocabulary.

---

# Born–Hopf S³ Structure Network — v1_25

**Geometry-only Batch 14:** Exact completion of the signed Petersen oriented-edge `4⊕5⊕6` geometry. The remaining five-sector admits **two independent A5-equivariant partial isometries** into the Hopf-axis ten-sector, linked by the actual right `C3` deck action, and has `Q600=0`, weighted-E8 Gram eigenvalue `164`. The six-sector admits a natural **alternating centered-incidence wedge** isometry to the signed exterior-Hodge `3⊕3′` space, with eigenvalues `±√5`. Exact character orthogonality proves there is **no A5-equivariant map of the six-sector into the Hopf-axis permutation space**; the maximal rank of the full signed Petersen-to-axis map is `9`.

This release adds **19 mathematical objects, 42 typed geometric relations, nine joint-input constructions and eight derived compositions**. It preserves all earlier geometry-only data, including the rank-four Petersen–600/E8 map. All statements use the same marked `2I/2T/Q8` finite-group embedding; a three-way choice of equivariant unoriented-edge/axis bijection is **not canonical**.

| Cumulative mathematical records | v1_24 | v1_25 |
|---|---:|---:|
| Objects and specified operators | 740 | **759** |
| Typed geometric relations | 1001 | **1043** |
| Joint-input constructions | 123 | **132** |
| Derivation/composition records | 109 | **117** |

**Detailed mathematical report:** [`reports/BATCH14_PETERSEN_FIVE_SIX_HODGE_AXIS_MORPHISMS.md`](reports/BATCH14_PETERSEN_FIVE_SIX_HODGE_AXIS_MORPHISMS.md).  
**Independent verifier:** `python verify_petersen_five_six_v125.py`.  
**Cumulative fast validation:** `python validate_geometry.py --fast`.  
**Data inspection:** `python geometry_query.py --petersen-five-six` or `--petersen56-matrix wedge6`.

No evidence-DAG or source-statement nodes, physical interactions, or decay relations have been added. The historical full regeneration suite remains available and should not be treated as run unless separately completed.

---

# S³ Structure Network v1_24 — Geometry-only Batch 13

**Standalone cumulative pure geometry network** (parent `v1_23`). No proof-DAG or evidence-catalog nodes, physical decay edges, or particle assignments.

## New exact A5-equivariant Petersen → 600-cell / E8 four-space

The fifteen *oriented Petersen edges* have an exact `4⊕5⊕6` Hodge splitting. The separate signed ten-pair Hodge carrier has `4⊕3⊕3`. The rank-four part of **each** is now mapped by explicit, normalized integer/radical matrices to the five-block contrast in the 15 Hopf axes, and thence to the right-Q8-fixed 600-cell minus-three sector and E8 weighted-Gram 296 eigenspace.

The main partial isometry is `T=R Cᵀ D/(3√5)`, with `TᵀT=P_Petersen4` and `TTᵀ=P_axis4`, and `ρ_axis(g)T=Tρ_signed-edge(g)` verified on all 60 marked A5 elements. The quintet and six-dimensional Petersen complements are annihilated. The **unique** core-order reconciliation against the actual quaternionic action is `σ=(0,2,3,4,1)`.

All new matrices, source labels/hashes, 43 geometric relationships, 7 joint-input constructions and 7 mathematical compositions are in the cumulative ZIP. The map is a source-independent *cross-instance composition* of earlier geometry, not a new physical coupling. The older separate `15D` mathematical carriers remain distinct.

**Full proof and boundaries:** [`reports/BATCH13_PETERSEN_A5_600_E8_EQUIVARIANT_BRIDGE.md`](reports/BATCH13_PETERSEN_A5_600_E8_EQUIVARIANT_BRIDGE.md).

| Cumulative | v1_23 | v1_24 |
|---|---:|---:|
| Mathematical objects/operators | 722 | **740** |
| Typed geometric relationships | 958 | **1001** |
| Joint-input mathematical constructions | 116 | **123** |
| Derivation/composition records | 102 | **109** |

Run:

```bash
python verify_petersen_a5_bridge_v124.py
python geometry_query.py --petersen-a5-intertwiner
python geometry_query.py --petersen-intertwiner-matrix Z15
python validate_geometry.py --fast  # current batch + graph checks + inherited-data integrity
python validate_geometry.py         # slower: also rerun all historical exact verifiers
python verify_graph_exports.py
python verify_manifest.py
```

**Scope:** fixed marked 2I/2T/Q8 embedding; verified mathematical maps only; geometry still non-exhaustive.

---

# Born–Hopf S³ Structure Network — v1_23

**Geometry-only Batch 12:** Exact 4+4+4+4 rational character resolution of the 600-cell adjacency `−3` eigenspace under the **marked right Q8 action**, including 120×120 regenerated idempotents; direct A5 `W4⊗W4*` matrix-coefficient interpretation of the 16D projective cyclic-polygon projector; explicit **rank-four isometry** between the right-Q8-fixed space and the weighted-E8 15-axis Gram projector; and exact right-C3 action on all 722 cyclic polygon cosets. This is a standalone cumulative mathematical graph release; the pre-existing proof/evidence DAG is not copied.

| Release measure | v1_22 | v1_23 |
|---|---:|---:|
| Actual mathematical object/operator records | 702 | **722** |
| Typed geometric maps and relations | 916 | **958** |
| AND-input constructions | 109 | **116** |
| Derived/composed mathematical results | 94 | **102** |

Main exact identities (all denominators and marking conventions fully defined in the report):

\[
W_{-3}^{600}=V_1^{(4)}\oplus V_{\chi_i}^{(4)}\oplus V_{\chi_j}^{(4)}\oplus V_{\chi_k}^{(4)}.
\]

\[
P_4=rac{Q_{600}(Q_{600}-12I)}{45}
=-rac{(G_{E8}-164I)(G_{E8}-896I)}{79200}.
\]

The `Q8`-fixed summand of `W16` is **isometric** to this common four-dimensional `P4` range using the actual 120×15 Hopf-fibre indicator `F/√8`; the full 16-space is **not** identified with a four-space. For source-independent calculations, proofs, preservation of left/right markings, exact polygon orbit counts, and non-identifications, read [`reports/BATCH12_A5_Q8_C3_SPECTRAL_AND_POLYGON_GEOMETRY.md`](reports/BATCH12_A5_Q8_C3_SPECTRAL_AND_POLYGON_GEOMETRY.md).

Regenerate and check:

```bash
python verify_a5_q8_projector_v123.py
python verify_graph_exports.py
python validate_geometry.py --fast  # current batch + graph checks + inherited-data integrity
python validate_geometry.py         # slower: also rerun all historical exact verifiers
python verify_manifest.py
python geometry_query.py --a5-coefficient --q8-fourier --e8-projector-bridge --polygon-c3
```

Dataset: `data/a5_q8_projector_v123_instance.json`; generating algorithm `scripts/a5_q8_projector_v123.py`. Focused exact geometric object graph and actual group permutation exports are in `graph/batch12_*`. **No physics, decay, citation, source-claim, or proof-DAG edges.** The overall mathematical network remains non-exhaustive and inherited unverified source-attested objects are not upgraded by this batch.

---

# Born–Hopf S³ Structure Network — v1_22

**Geometry-only Batch 11:** Exact right-`2T` action on the marked 600-cell yields a **24-fold regular graph covering** onto the five-vertex **`3K5` multigraph** (three parallel edges per core pair). Its `Q8 ⊳ 2T` factorization gives `120 → 15 → 5` vertices and `720 → 90 → 30` edges with eightfold and threefold regular covers. **All thirty** right-`2T` edge-orbit matchings coincide exactly with the weight-two matchings of the independent golden-`E8` fifteen-axis tensor. This identifies the local matching `C3` rotations with the actual quaternionic deck group `2T/Q8`.

The matching differences obey an **alternating five-core parity law**, and an explicit `Z3` voltage construction establishes exact closed-path holonomies, discrete Bianchi identities, and **81 flat choices among 59,049** possible assignments of one matching to each core pair. Nonzero curvature is *choice-dependent*, not canonically forced. The weighted-design symmetry group is refined to the split extension `Aut(T) ≅ C3 ⋊_sign S5`.

| Cumulative content | v1_21 | v1_22 |
|---|---:|---:|
| Mathematical objects/operators | 684 | **702** |
| Typed geometric relations | 883 | **916** |
| Joint-input constructions | 102 | **109** |
| Independent derivation records | 87 | **94** |

This is **pure finite mathematics**, not a proof-DAG duplication, physics interaction graph, or claim of exhaustive `S³` coverage. Full derivation and limitations: [`reports/BATCH11_RIGHT_2T_C3_HOLONOMY_AND_600_E8_MATCHINGS.md`](reports/BATCH11_RIGHT_2T_C3_HOLONOMY_AND_600_E8_MATCHINGS.md).

Run after extraction:

```bash
python verify_axis15_holonomy_v122.py
python validate_geometry.py --fast  # current batch + graph checks + inherited-data integrity
python validate_geometry.py         # slower: also rerun all historical exact verifiers
python verify_graph_exports.py
python verify_manifest.py
python geometry_query.py --holonomy-tower
python geometry_query.py --holonomy-core-pair 0 1
python geometry_query.py --holonomy-triangle 0 1 2
```

Exact data: `data/axis15_holonomy_v122_instance.json`; generator: `scripts/axis15_holonomy_v122.py`; graph maps: `graph/batch11_*.graphml`. Source premises remain anchored to the same mathematical witness bank as v1_21, and no reference-theorem nodes are copied.

---

# Earlier release — v1_21

**Geometry-only Batch 10:** The exact 15-axis weighted `E8` root-triple tensor reproduces the five tetrahedral core blocks **intrinsically** through its 15×15 Gram matrix, with `G=164I+44SameCore+40J=164I−23Q600+7Q600²`. Exact rational projectors give a `1+4+10` cubic sector analysis, including the vanishing `4×4×10` component. The tensor contains ten locally matched `3×3×3` incidence cubes, ten cyclic `K3,3` matching factorizations, and a complete **360-element automorphism group**, with `C3` kernel over all five-block permutations `S5`. **These are finite geometric statements, not physical couplings or decay restrictions.**

| Cumulative content | v1_20 | v1_21 |
|---|---:|---:|
| Mathematical objects and defined operators | 668 | **684** |
| Typed geometric relationships | 855 | **883** |
| Joint-input mathematical constructions | 96 | **102** |
| Derived/composed mathematical results | 81 | **87** |

Detailed proof, exact certificates and limitations: [`reports/BATCH10_AXIS15_CUBIC_SPECTRAL_AND_MATCHINGS.md`](reports/BATCH10_AXIS15_CUBIC_SPECTRAL_AND_MATCHINGS.md).

Run after extraction:

```bash
python verify_axis15_cubic_v121.py
python validate_geometry.py --fast  # current batch + graph checks + inherited-data integrity
python validate_geometry.py         # slower: also rerun all historical exact verifiers
python verify_graph_exports.py
python verify_manifest.py
python geometry_query.py --axis-cubic
python geometry_query.py --axis-local-core-triple 0 1 2
python geometry_query.py --axis-core-pair 0 1
```

New source-independent mathematical instance: `data/axis15_cubic_v121_instance.json`; exact construction script `scripts/axis15_cubic_v121.py` (adds `numpy>=1.24` to cumulative requirements). Geometric exports include the full graph, focused Batch 10 graph, 15-axis Gram metric graph, and actual weight-2/weight-8 hypergraph. **No proof/evidence DAG nodes or physical transition data are added.** The network remains non-exhaustive; earlier source-attested objects retain their original status.

---

## Earlier release — v1_20

**Geometry-only Batch 9:** A verified, marked **common 15-axis quotient** of the quaternionic 600-cell and the two-sheet golden-E8 root-addition geometry. Quaternion inversion relates distinct left and right Q8 operations. The 600-cell quotient operator is `Q600=A(K_{3,3,3,3,3})`, while the E8 root-addition equitable quotient is `QE8=4(J15−I15)`, giving the exact five-triangle correction `QE8−4Q600=4A(5K3)`. The 2240 E8 zero-sum root triples descend to a **weighted 2-(15,3,8) incidence design**, and the triality 24-node orbit system maps two-to-one onto 12 non-D4 axes. No proof-DAG/physical nodes are included.

| Cumulative content | v1_19 | v1_20 |
|---|---:|---:|
| Mathematical objects and defined operators | 648 | **668** |
| Typed exact/source-scoped geometric maps | 811 | **855** |
| Joint-input mathematical constructions | 88 | **96** |
| Derived/composed mathematical results | 73 | **81** |

Full derivation and exact limitations: [`reports/BATCH9_Q8_HOPF_E8_COMMON_AXES.md`](reports/BATCH9_Q8_HOPF_E8_COMMON_AXES.md).

Run after extraction:

```bash
python verify_q8_hopf_e8_v120.py
python validate_geometry.py --fast  # current batch + graph checks + inherited-data integrity
python validate_geometry.py         # slower: also rerun all historical exact verifiers
python verify_graph_exports.py
python verify_manifest.py
python geometry_query.py --q8-hopf-e8
python geometry_query.py --axis-e8 0
python geometry_query.py --axis-triples 0
```

Data: `data/q8_hopf_e8_bridge_v120_instance.json`; geometric graphs `graph/batch9_common_axis15_operators.graphml`, `graph/batch9_E8_axis15_weighted_2design.graphml`, `graph/batch9_triality24_to_hopf15.graphml`, `graph/batch9_triality_axis12_weighted_hypergraph.graphml`, and focused mathematical construction network `graph/batch9_q8_hopf_e8_axis_bridges.graphml`.

**Precise status:** new *source-independent, exact-arithmetic compositions* of source-established mathematical input structures. Not claimed to be literature-novel; no new mass formula, decay rate or physical realization. The full S³ geometry graph remains non-exhaustive and inherited source-attested objects are not automatically re-proven.

---

## Earlier release — v1_19


**Geometry-only Batch 8:** free *left*-Q8 action on the three golden-E8 triality 64-root sectors; exact 8×8 weighted orbit-incidence matrices of rank 5; 24-vertex/104-hyperedge orbit geometry; full rank-25 Q8 character decomposition; affine-D4 McKay restriction via Q8 giving a separate **rank-three** E7↔E8 map. Cumulative standalone release, with all earlier geometric constructions preserved and no proof-DAG or physical-transition nodes.

**Source premises:** the explicit E8/2T/2I coordinates from Papers I-B/I-D already source-anchored in v1_18. The batch's new results are regenerated mathematically; the source labels are provenance only. See [`reports/BATCH8_Q8_TRIALITY_MCKAY_RESULTS.md`](reports/BATCH8_Q8_TRIALITY_MCKAY_RESULTS.md).

| Content | v1_18 | v1_19 |
|---|---:|---:|
| Mathematical objects / operators | 628 | **648** |
| Typed mathematical relationships | 770 | **811** |
| Joint-input mathematical constructions | 81 | **88** |
| Derivation / composition records | 66 | **73** |

**Important:** there are now two independent five-dimensional constructions (Q8-fixed triality image and common-2T cross-McKay image). Their natural Gram spectra are different. No canonical isometry or equivariant identification has been proved; the actual deeper Q8-mediated McKay correspondence has **rank three**, with eigenmodes −2,0,2. No particle assignment, decay rate or Lie-bracket sign is constructed.

Quick validation:

```bash
python verify_q8_triality_v119.py
python validate_geometry.py --fast  # current batch + graph checks + inherited-data integrity
python validate_geometry.py         # slower: also rerun all historical exact verifiers
python verify_graph_exports.py
python verify_manifest.py
python geometry_query.py --q8-triality
python geometry_query.py --q8-orbit-pair 01
python geometry_query.py --q8-mckay
```

Full dataset: `data/q8_triality_v119_instance.json`. Focused exports: `graph/batch8_q8_triality_mckay_bridges.graphml`, `batch8_q8_triality_24orbit_weighted.graphml`, `batch8_q8_triality_104hyperedges.graphml`, `affine_mckay_Q8_D4.graphml`, and the diagram SVG. **The network is still not exhaustive**; source-only legacy structures retain their original verification classification.

---

## Earlier release — v1_18


**Geometry-only Batch 7:** exact affine `E6/E7/E8` McKay representations of `2T/2O/2I`, source-indexed character rings, two genuine subgroup restriction maps, a **rank-five affine E7↔E8 intertwiner through common 2T**, and an explicit **orthogonal Clifford/golden-E8 root action** by one marked `2I` and its left/right product. This is a **standalone cumulative ZIP containing only its latest `v1_18` package**; there is no copied proof DAG or particle model.

**Release date:** 2026-11-16 · **Parent:** `Paper00-S3StructureNetwork-v1_17` · **Primary mathematical source:** `Paper1B-ExceptionalGeometry-v1_14.tex`, inside the separately supplied `Paper00-PapersMinimal-v3_023` (SHA-256 provenance stored internally). For a complete proof sketch and every boundary, see [`reports/BATCH7_MCKAY_CLIFFORD_ROOT_RESULTS.md`](reports/BATCH7_MCKAY_CLIFFORD_ROOT_RESULTS.md).

## Cumulative graph

| Measure | v1_17 | v1_18 |
|---|---:|---:|
| Pure mathematical objects/operators | 596 | **628** |
| Typed geometric relations | 700 | **770** |
| Joint-input mathematical constructions | 70 | **81** |
| Derivation/composition records | 55 | **66** |
| Largest weak connected component | 464 | **497** |
| Directly reachable from `geo:s3` | 360 | **467** |

Batch 7 adds **32 mathematical objects** and **70 genuine mathematical relations**, plus **11 AND-input construction bundles** and **11 derivation certificates**. Neither citations nor theorem/claim statements appear as geometry nodes. Source claim labels remain **metadata only**.

## Two particularly useful cross-geometry results

**Affine ADE bridge.** From the same marked `2T⊂2O` and `2T⊂2I`, exact irreducible character restrictions give `B_O` (7×8), `B_I` (7×9), and

```
X = B_O^T B_I,             A_E7 X = X A_E8,
rank(X) = 5,
spec(X^T X) = 10,10,4,4,2,0,0,0,0.
```

This supplies the actual five-eigenmode overlap between affine E7 and affine E8 **despite the absence of a group embedding `2O⊂2I`**. It is an induction/restriction correspondence through the common `2T`.

**Clifford-to-root map.** The two real embeddings of `Q(√5)` give an algebra splitting `H(Q(√5))⊗R ≅ H⊕H ≅ Cl(0,3)` and a positive weighted metric exactly equal to the golden coefficient Euclidean metric. Every marked `2I` element acts by an explicit orthogonal eight-dimensional matrix on the 240 E8 roots. Two-sided quaternion multiplication yields an effective subgroup of **7,200 root automorphisms**. Its `2T` stabilizer permutes the three `64`-root triality sectors through `2T/Q8≅C3`.

The **affine E8 McKay diagram and the E8 root lattice remain distinct mathematical structures**. The original golden coefficient map is not an algebra homomorphism, and the Galois spinor is not automatically a second marked 2I completion. Nothing in this package is a physical interaction or decay operator.

## Explore and verify

```bash
python verify_mckay_clifford_v118.py
python validate_geometry.py --fast  # current batch + graph checks + inherited-data integrity
python validate_geometry.py         # slower: also rerun all historical exact verifiers
python verify_graph_exports.py
python verify_manifest.py
python geometry_query.py --mckay-cross
python geometry_query.py --mckay-group 2T
python geometry_query.py --mckay-group 2O
python geometry_query.py --mckay-group 2I
python geometry_query.py --mckay-restrict 2I
python geometry_query.py --clifford-e8
```

Python 3.10+ and `sympy>=1.12` and `networkx>=3.0` support the mathematical regeneration. The new verifier uses **exact rational and algebraic arithmetic throughout**; `numpy` is not required to check the included character tables. Graphviz `dot` is only needed to regenerate SVG. The full inherited validators from v1_12–v1_17 are retained.

## Scope and next research

The graph is still **not** an exhaustive semantic classification of every `S³` mathematical object in Papers I–VII; source-attested legacy objects without admitted maps remain. The next useful geometry-only step is to examine whether the new rank-five common-ADE intertwiner and the existing `64×64` rank-25 triality modules share a **specific equivariant intertwining functor or common exact character decomposition**. Neither rank/dimension coincidence nor adjacency similarity alone is sufficient. All three new bridges must continue to be checked as mathematical maps, independently of their potential observable significance.
# Source migration and repair-integration addendum — Paper7D-ProofChainAudit-v1_6.md

**Integration release:** `Paper00-PapersMinimal-v3_007.zip`, 14 November 2026.
**Current paper source:** `Paper7D-TechnicalMaterial-v1_54.tex`.
**Status:** `SOURCE_INTEGRATED; GLOBAL_SOURCE_REAUDIT_PENDING`. An inherited historical audit is not a correctness certificate for the newer current manuscript.
**Evidence policy:** Local algebraic proofs and scoped tests do not discharge physical source/observable interfaces or automatically alter the canonical proof DAG.

---

## Historical source-bound audit: Paper7D-ProofChainAudit-v1_5.md
# Paper7D — v2.372 source repair addendum (13 November 2026)

**Successor:** `Paper7D-ProofChainAudit-v1_5.md`.  
**Current source:** `Paper7D-TechnicalMaterial-v1_47.tex`.  
**Current SHA-256:** `75a5cd7fc23e7e4cdd0472254e7b689c6755e27a55081ab03735b0cb27eadf50`.  
**Historical audit:** `Paper7D-ProofChainAudit-v1_4.md`.  
**Source repair scope:** 1 distinct issue(s); 2 textual corrections.  
**Disposition:** `SOURCE_REPAIRED_WITH_SCOPED_CHECKS; FORMAL_REAUDIT_PENDING` for only the listed IDs. Other issues and all original evidence statuses unchanged.

| Issue ID | New source line(s) | Repaired issue |
|---|---|---|
| `BH-VIID-G-0004` | 1861, 1888 | Combined primitive span projector is supp(ΣPχ); the positive spectrum is on its range, not on the whole Hilbert space. |

The historical report below refers to the previous source version and explicitly marks those same issue IDs as `OPEN` **as of that old version**. Those specific historical labels are superseded only as source-edit dispositions by the addendum above; the original audit text is retained to prevent loss of evidence or false global certification. Other issues are unchanged. Recheck the updated source theorem and its proof/use dependencies before promoting an issue to closed in the canonical DAG.

---

## Historical predecessor audit (unchanged text; former source version)

# Paper VII-D — Complete rigorous proof-chain and DAG audit, Batches 1–4

**Artifact:** `Paper7D-ProofChainAudit-v1_4.md`. **Target:** `Paper7D-TechnicalMaterial-v1_46.tex`; source SHA-256 `0a2e3731cf8fca6f614409c5805af87861ced175718448044d49ec8494c1e312`; **6,757 source lines**. **Protocol:** `Paper00-RigorousVerificationDAGWorkProtocol-v2_4.md` with proof-chain scope guard. **Authoritative corpus:** `Paper00-PapersMinimal-v2_371.zip`; latest supplied DAG/archive baselines v1.120/v1.37. Papers/TeX were not modified; neighboring papers were read only at indispensable import locations.

**Classification:** `FULLY_AUDITED_WITH_OPEN_GAPS`: **248** source-bound claim, definition, remark and material dispositions across **132** proof environments and all four contiguous source batches. This label means all the target claims were assigned verified, conditional, formalized, reproduced, or unresolved dispositions; it does **not** mean 248 independently proved results, or that the native continuum QCD physics has been fully realized.

**Outcome histogram:** `VERIFIED` **45**, `VERIFIED-CONDITIONAL` **97**, `FORMALIZED` **65**, `REPRODUCED` **26**, `UNRESOLVED` **15**. The count of `UNRESOLVED` claim objects differs from the **13 distinct OPEN issue certificates** because some unresolved claims inherit one issue; other explicit frontier statements are valid conditional claims. Named claims **154**; explicit source definitions **21**; source-bound substantive unnamed blocks **73**. All non-validated material is flagged as such rather than promoted to a physical result.

**Batch boundaries:** 1–1240 (Batch 1), 1241–2816 (Batch 2), 2817–4546 (Batch 3), 4547–6757 (Batch 4). Scope remains mathematical/physical proof correctness, not visual/PDF review, new theory development or paper rewrite.

## Complete issue register (stable first-origin IDs)

**Batches 1–3:** The complete original first-nine issue certificates are reproduced below, with the exact independent checks and per-claim census from those batches retained for provenance. No earlier issue has been silently merged, closed, or rekeyed.

## Issue register — carry-forward, Batch 1–2

### Carry-forward issues from Batch 1 (unchanged)

**BH-VIID-G-0001 — minor / TYPE_OR_DOMAIN.** Source `p10:prop:v2159-holonomy-cotangent-firewall`, lines 266–300: ordinary cotangent pullback requires the fibered basepoint; holonomy alone does not supply a canonical map `T*G^E → T*A`. The source's *negative* full-phase-space descent conclusion remains supported. The current Paper VII-C 4030 is a scope-firewall citation, not a failed observable. **Obligation:** type the actual cotangent relation and keep the negative theorem.

**BH-VIID-G-0002 — major EVIDENCE_MISSING (verification bottleneck, not a refutation).** `p10:thm:v256-exact-native-inertia`, lines 383–535: claimed sixteen exact dyadic witness arrays, checker and result files for the native `864×864` inertia/gap remain unavailable. Their **conditional algebraic consequence** was checked, but witness and native-stencil compatibility cannot be re-executed. Current VII-A 6420, 6802, 7169, 7293 directly reuse the claimed native gap. **Obligation:** provide/replay exact witness arrays, verifier, rational result files and active-source hash compatibility before E3 promotion.

### New Batch 2 issue certificates

#### BH-VIID-G-0003 — minor / MISSING_EVIDENCE / OPEN

**Origin:** explicitly claimed chiral/source checker provenance, lines **1465–1485** (`p10:app:numerical-chiral-certificate`). The source names `Paper00-MomentumCartanChiralDensityChecks-v1_0.py`, `Paper00-ChiralSourceMomentChecks-v1_0.py`, `Paper00-ChiralFourPointChecks-v1_0.py` and `Paper00-InteractingChiralCertificateChecks-v1_0.py` as packaged. None is in the supplied papers, latest DAG Atlas, or latest proof-chain audits archives. The asserted Gershgorin/trial quadratic-form computer certificate has no attached inputs or results in that passage. The **error-carrying finite response inequality itself remains algebraically valid**, independent of those scripts, and the source expressly leaves the physical ordered condensate open.

**Earliest missing evidence:** the named packaged comparison programs and their claimed executed inputs/outputs, not a failure of the Rayleigh–Ritz inequality. **Upstream:** current VII-A source/finite CAR moment packet; **conditions:** specified finite Hamiltonian/operator, certified norm errors and numerical trial state. **Proven impacted observable paths:** none. **Possible effects:** comparators' executable reproducibility only. **Exact resolution:** supply the four scripts and ground-energy/trial arithmetic outputs with compatible source identity, or mark the computational results `REPORTED`. Do not promote their absence into a counterexample to the underlying algebra.

#### BH-VIID-G-0004 — moderate / MISSING_CONDITION / OPEN

**Origin:** `p11:thm:explicit-primitive-support-transfer-block`, lines **1858–1874**. The theorem writes `P_prim=Σχ Pχ`, assumes only that its constituents reduce `H_L`, and then invokes contractive **projection** compression to claim transfer eigenvalues in `(0,1]` and nonnegative energies via `−t⁻¹ log λ`. Individual reducing projections need **not** be mutually orthogonal; their sum need not be a projection or contraction. Independent exact adversarial witness: with `H=0` on `C²`, `P1=|e1><e1|` and `P2=|+><+|` with `|+>=(|e1>+|e2>)/sqrt(2)`, both are rank-one reducing projections but `P_prim²` has largest eigenvalue `(1+1/sqrt(2))² > 1`. This proves that **the printed reduction hypothesis alone does not justify the spectral upper bound**. It does **not** refute the intended actual primitive channel decomposition if it is already known to be pairwise orthogonal.

**First failed step:** identification of the sum of channel projectors with a single contractive orthogonal projector. **Upstream:** VII-B generic spectral/conserved-sector projector grammar, current VII-D finite primitive block. **Condition actually needed:** pairwise orthogonality or a separately established `P_prim²=P_prim=P_prim*`; the energy extraction is on `ran P_prim` with `t>0` and `H−E0≥0`. **Direct consequence:** the composite transfer-block `(0,1]` bound is unresolved as printed, while individually reducing sector compressions and later independent physical Hamiltonian spectra are unaffected by this attack. **Obligation:** point to or prove the existing primitive projector decomposition and its orthogonality; no new physical projector is authorized.

#### BH-VIID-G-0005 — moderate / MISSING_EVIDENCE / OPEN

**Origin:** `p11:cor:finite-face-incidence-glue-residues`, lines **2295–2306**. The source reports exact triangular face-incidence source factors `2/3`, `1/3` and `1/6` on adjacency eigenspaces. Neither its statement nor proof supplies the underlying **normalized incidence/source operator**, adjacency matrix/eigenspace data, or the alleged exact finite operator relation. Its equation reference (`p11:eq:triangle-incidence-source-operator`) is only a `\phantomsection\label` anchor. No matching explicit factor derivation was found in the relevant current VII-A/VII-B owner text. The arithmetic **conditional** consequence `(2/3)²:(1/3)²:(1/6)² = 16:4:1` is exact; the antecedent factors themselves are **not independently checkable** from the supplied evidence. The source expressly says that these factors are not physical glue pole residues without the actual Hamiltonian/source eigenvector projections.

**First missing certificate:** the operator and eigenprojector calculation establishing the three geometric source factors. **Upstream:** VII-A finite Hodge face/adjacency geometry and VII-D claimed triangular source. **Conditions:** normalized geometric source vectors and specified adjacency eigenspaces; separately computed physical pole overlaps for any physical use. **Directly impacted:** only this geometric corollary's asserted factors. **Possibly affected:** a future glue-residue comparison; **no established physical spectrum failure**. **Obligation:** produce the exact normalized incidence/source matrix and eigenspaces and verify the claimed factors. Do not use `16:4:1` as a measured spectral ratio.


## Mathematical checks and key protected scope boundaries

**Exact finite algebra (E3):** The Gram \(\| (I-V)/2\|_{HS}^2=(d-\operatorname{Re}\operatorname{Tr}V)/2\), group-compression leakage \(-PM_g(1-P)M_hP\), chiral spectral pairing with the fixed grading, the massive overlap Hermitian-part bound \(1/\max(m,2/a_R)\), free-gluon zeta energy \(11\hbar c_{op}/(15R_x)\), and Hurwitz face area \(3\arccos(1/3)-\pi\) check out. A literal spectral \(E_{32}/\sqrt{240}\) equality is **not** claimed or inferred from the Gram.

**Petersen full finite E3 certificate:** Starting independently from Paper I-A's ten explicit unit axes (lines 3769–3776), constructed the fifteen signed cross-product columns, both Galois-conjugate projectors, and \(D=\Pi_3-\Pi_{3'}\) over \(\mathbb Q(\sqrt5)\). Exact arithmetic verified \(\Pi_3\Pi_{3'}=0\), \(D^3=D\), rank 6, trace 0, and evaluated **all 32 core subsets**, not merely one representative per cardinality. The six characteristic-polynomial rows at VII-D lines 1178–1210 and all sharp coherence bounds at 1212–1227 match. This is a finite source theorem: it is **not** a measured hadronic spectrum.

**Conditional physical realization is preserved, not reopened:** The cylinder pure-YM kink and chiral zero-mode results import explicit I-C/I-B theorems with a specified extra Euclidean branch, not an unconditional physical transition. The electric heat kernel result assumes a **same-owner finite cylindrical kinetic realization**; it does not construct it, pick a magnetic nonlinear face action, or derive a physical extensive continuum. The supplied global Dirac spectral band has a stipulated elliptic self-adjoint operator and gauge-domain covariance; its CAR lift does not license a new physical cutoff or gauge regulator. Finite moment/heat tail estimates do not imply uniform RG norm convergence. `BND-VIID-B1-001` documents these boundaries and rejects the unsupported accusation that an optional comparison branch is being physically constituted.

**E2 high-precision numerical controls:** Independently re-evaluating the \(SU(3)\) Casimir sum at \(t_0=14383/2500\) gives \(h(t_0)-1/(2\pi^2)\approx2.6468\times10^{-6}>0\), and the unique heat root \(t\approx5.753295846633\). These are corroborating numerical controls, **not** a substituted exact rational certificate for the source's supplied-arithmetic claim. The independently derived heat-tail majorant at \(L=17\) is \(3.970950225\times10^{-117}\) at \(t_0\) and \(3.952155037\times10^{-117}\) at the root, consistent with the distinct source bounds.

## Claim ledger for audited range

| Claim ID | Current label or bounded source block | Lines | Status |
|---|---|---|---|
| BH-VIID-C-0001 | `p10:prop:exroot-overlap-gram` | 85–102 | VERIFIED |
| BH-VIID-C-0002 | `p10:prop:v2180-compressed-local-gauge-no-go` | 140–152 | VERIFIED |
| BH-VIID-C-0003 | `p10:prop:v2180-finite-holonomy-dirac-no-go` | 160–166 | VERIFIED |
| BH-VIID-C-0004 | `p10:lem:v2180-positive-mass-chiral-antihermitian` | 176–189 | VERIFIED-CONDITIONAL |
| BH-VIID-C-0005 | `p10:rem:v2180-graph-laplacian-extension-candidate` | 197–215 | FORMALIZED |
| BH-VIID-C-0006 | `p10:rem:v2180-fuzzy-gauge-extension-candidate` | 217–225 | FORMALIZED |
| BH-VIID-C-0007 | `p10:prop:v2159-fixed-hurwitz-area-nogo` | 240–256 | VERIFIED-CONDITIONAL |
| BH-VIID-C-0008 | `p10:prop:v2159-holonomy-cotangent-firewall` | 266–285 | UNRESOLVED |
| BH-VIID-C-0009 | `p10:thm:v2159-conditional-electric-heat` | 301–331 | VERIFIED-CONDITIONAL |
| BH-VIID-C-0010 | `p10:rem:v258-phase05-payload` | 392–407 | UNRESOLVED |
| BH-VIID-C-0011 | `p10:thm:v256-exact-native-inertia` | 409–432 | UNRESOLVED |
| BH-VIID-C-0012 | `p10:prop:v199-cartan-transgression` | 652–662 | VERIFIED-CONDITIONAL |
| BH-VIID-C-0013 | `p10:prop:v199-yang-mills-kink` | 682–704 | VERIFIED-CONDITIONAL |
| BH-VIID-C-0014 | `p10:prop:m8td-kink-zero` | 738–754 | REPRODUCED |
| BH-VIID-C-0015 | `p10:prop:v245-singlet-projected-free-gluon-trace` | 793–821 | VERIFIED-CONDITIONAL |
| BH-VIID-C-0016 | `p10:prop:v245-free-gluon-spectral-zeta` | 823–838 | VERIFIED-CONDITIONAL |
| BH-VIID-C-0017 | `p10:prop:v245-cubic-gluon-selection-filters` | 840–865 | VERIFIED-CONDITIONAL |
| BH-VIID-C-0018 | `p10:prop:v202-vectorlike-positive` | 955–961 | VERIFIED-CONDITIONAL |
| BH-VIID-C-0019 | `p10:thm:v167-overlap-resolvent-accretive` | 985–1016 | VERIFIED-CONDITIONAL |
| BH-VIID-C-0020 | `p10:cor:v167-positive-mass-source-interval` | 1033–1044 | VERIFIED-CONDITIONAL |
| BH-VIID-C-0021 | `p10:rem:v167-g16-scope` | 1046–1052 | FORMALIZED |
| BH-VIID-C-0022 | `p10:prop:v2186-covariant-dirac-band-car` | 1069–1099 | VERIFIED-CONDITIONAL |
| BH-VIID-C-0023 | `p10:rem:v2186-band-source-scope` | 1119–1144 | FORMALIZED |
| BH-VIID-C-0024 | `p13:prop:v323-petersen-charpolys` | 1178–1198 | VERIFIED |
| BH-VIID-C-0025 | `p13:cor:v323-petersen-coherence-bound` | 1212–1223 | VERIFIED |
| BH-VIID-C-0026 | `<unnamed:p13:rem:1229>` | 1229–1237 | FORMALIZED |
| BH-VIID-C-0027 | `Native topology/measure boundary after G20 retirement` | 343–362 | FORMALIZED |
| BH-VIID-C-0028 | `Supplementary unit-clutching numerical stress test` | 363–383 | UNRESOLVED |
| BH-VIID-C-0029 | `Historical floating-product residual evidence (retired)` | 537–597 | FORMALIZED |
| BH-VIID-C-0030 | `Topology-resolving comparison and sampled-clutch alias` | 598–632 | VERIFIED-CONDITIONAL |
| BH-VIID-C-0031 | `Representation heat tail and block truncation estimates` | 870–923 | VERIFIED-CONDITIONAL |
| BH-VIID-C-0032 | `Rational native heat-root and tail certificate` | 924–949 | REPRODUCED |


## Independent correctness checks and conditional boundaries, Batch 2

**Chiral and native spatial checks (lines 1260–1620).** The CAR algebra ` [β,[h,β]]=−4h` for a chirally anti-commuting one-body Hamiltonian was checked independently. The fixed-frontier free response formulas and the distinction between one- and two-symbol near-zero densities are analytically coherent; the shared `SU(3)` trial covariance is indeed a projection with the correct Haar-restored Wick/collective split. The `SU(3)` Casimir singlet/octet factors `−4/3,1/6`, the `D₁=5` orbital count and `360` physical quark component modes are consistent with the stated finite owners. Exact Haar moment reduction of the quaternion `SU(3)` multiplier reproduces leakage `Tr[I−(P₁M_gP₁)†(P₁M_gP₁)]=6` on the declared orbital/color convention. `Tr Q²=1/2`, `Tr S²=36`, and CAR tracial variance `9` reproduce exactly. None asserts a condensate for the physical, interacting ordered QCD operator.

**Topology and native-index checks (lines 1638–1832).** The normalized Weyl torus class density has the correct factor `1/[6(2π)²]`. The claimed rational ball fraction is **exactly** `7061881225/199022581174732616540136492402475008` at `ε=1/256`; `q(1/4096)=2^-32 q(1/256)`. Both explicit huge-integer bounds `10^-18796 < 4(7/18)^1152 q_*^720 < 10^-18795` pass exact-integer comparison; no rounded floating logarithm used. The ball sign constants `b/(2g)=9/2030` and `η=1139/200970` match. The finite zero-index center's sign-resolvent argument is separate from **the unresolved nonzero-index sixteen-mesh witness issue G-0002**. The characteristic-function proof correctly distinguishes `φ(θ)=1` from the stronger false `|φ(θ)|<1` for all other θ.

**Hadron/kernel and spectrum boundaries (lines 1850–2522).** Direct rational diagonalization reproduces all `n_f=3,4,5,6` DGLAP second-moment eigenvalues and fixed points; the normalization/momentum columns sum to zero. `B₀(m_i+m_j)`, PCAC, Feynman–Hellmann derivatives, soft chiral kernels and Dashen relations are **conditional on their actual quark-source/low-energy data**, not native mass predictions. Rayleigh–Ritz, the relative group quotient, identity-fibre degeneracy, finite Hodge local scalar diagonal moment `10` and the Schur effective-pole formula follow on their printed domains. The purported `16:4:1` glue ratio lacks its defining geometric factor certificate (G-0005), and the combined `P_prim` transfer needs orthogonality (G-0004). Wilson-area/string tension, open-channel poles, meson/baryon masses, hyperfine differences, nuclear contact coefficients and deuteron binding remain explicitly dependent on supplied physical operator/state/limit members. No experiment was used to fix them.

**Optional LFRep and finite-QFT limits (lines 2531–2816).** The source correctly preserves the distinction between the exact finite `LFRep_L` species/occupation representation (VII-A clauses R1–R6), physical null/source owner, the VII-B selected state and claim-local L1–L5 limits, and VII-C scattering clauses. Under R3–R4 and fixed `p_h^+>0`, the positive commuting species fraction operators sum to the sector identity, the finite parton number and momentum operator measures have `M_i(dx)=xN_i(dx)`, and finite net-flavor/charge/momentum rules are algebraic. Neither the Hausdorff moment proof nor the bounded-Lipschitz Cauchy proof requires an assumed PDF density; both correctly separate weak positive measure limits from renormalized collinear PDFs and small-`x`/zero-mode control. The compression-commutator leakage identity was independently checked with exact rational matrices. No `LFRep_L` occurrence or physical continuum PDF has been proved by these finite conditional identities.

## Claim census — Batch 2 (41 named + 19 unnamed)

| Claim ID | Exact label / audited unnamed mathematical block | Source lines | Disposition |
|---|---|---:|---|
| `BH-VIID-C-0033` | p10:prop:numerical-chiral-certificate | 1447–1459 | VERIFIED-CONDITIONAL |
| `BH-VIID-C-0034` | p11:thm:explicit-primitive-support-transfer-block | 1858–1870 | UNRESOLVED |
| `BH-VIID-C-0035` | p11:thm:explicit-positive-topological-winding-block | 1886–1910 | VERIFIED-CONDITIONAL |
| `BH-VIID-C-0036` | p11:cor:explicit-second-moment-dglap-blocks | 1916–1947 | VERIFIED-CONDITIONAL |
| `BH-VIID-C-0037` | p11:cor:explicit-leading-pseudoscalar-blocks | 1968–1986 | REPRODUCED |
| `BH-VIID-C-0038` | p11:thm:finite-hurwitz-heavy-source-kernel-package | 1992–2006 | VERIFIED-CONDITIONAL |
| `BH-VIID-C-0039` | p11:cor:leading-finite-heavy-1s-variational-readout | 2012–2022 | VERIFIED-CONDITIONAL |
| `BH-VIID-C-0040` | p11:thm:kaplan-manohar-ambiguity-absent | 2034–2039 | REPRODUCED |
| `BH-VIID-C-0041` | p11:cor:universal-dashen-lift-native | 2045–2051 | VERIFIED-CONDITIONAL |
| `BH-VIID-C-0042` | p11:cor:pcac-pseudoscalar-density-native | 2057–2067 | VERIFIED-CONDITIONAL |
| `BH-VIID-C-0043` | p11:cor:goldstone-sigma-native | 2073–2083 | VERIFIED-CONDITIONAL |
| `BH-VIID-C-0044` | p11:cor:native-soft-pipi-pik-scattering | 2089–2102 | REPRODUCED |
| `BH-VIID-C-0045` | p11:cor:native-eta-to-three-pi-source | 2111–2128 | REPRODUCED |
| `BH-VIID-C-0046` | p11:cor:native-neutral-transition-ff | 2138–2144 | REPRODUCED |
| `BH-VIID-C-0047` | p11:cor:native-charged-pseudoscalar-weak-kernels | 2150–2156 | REPRODUCED |
| `BH-VIID-C-0048` | p11:cor:native-two-pseudoscalar-thresholds | 2162–2173 | VERIFIED-CONDITIONAL |
| `BH-VIID-C-0049` | p11:cor:primitive-flavor-floors-native | 2182–2192 | VERIFIED-CONDITIONAL |
| `BH-VIID-C-0050` | p11:cor:pseudoscalar-hrg-native | 2198–2211 | VERIFIED-CONDITIONAL |
| `BH-VIID-C-0051` | p11:thm:hurwitz-relative-support-lift | 2224–2233 | VERIFIED-CONDITIONAL |
| `BH-VIID-C-0052` | p11:thm:geometric-pure-glue-relative-block-corrected | 2240–2247 | VERIFIED-CONDITIONAL |
| `BH-VIID-C-0053` | p11:thm:finite-plaquette-hodge-curvature-hessian | 2253–2271 | VERIFIED-CONDITIONAL |
| `BH-VIID-C-0054` | p11:cor:cell-local-scalar-curvature-stiffness | 2277–2288 | VERIFIED-CONDITIONAL |
| `BH-VIID-C-0055` | p11:cor:finite-face-incidence-glue-residues | 2295–2302 | UNRESOLVED |
| `BH-VIID-C-0056` | p11:cor:native-string-tension-and-relative-glue-ratios | 2309–2331 | REPRODUCED |
| `BH-VIID-C-0057` | p11:thm:light-qqbar-relative-meson-block | 2341–2347 | REPRODUCED |
| `BH-VIID-C-0058` | p11:thm:three-quark-determinant-geometry-baryon-multiplets | 2353–2360 | REPRODUCED |
| `BH-VIID-C-0059` | p11:cor:leading-baryon-current-scalar-response-package | 2366–2372 | REPRODUCED |
| `BH-VIID-C-0060` | p11:thm:native-ope-and-nn-contact-block | 2378–2388 | VERIFIED-CONDITIONAL |
| `BH-VIID-C-0061` | p11:prop:leading-deuteron-contact-ope-block | 2394–2401 | VERIFIED-CONDITIONAL |
| `BH-VIID-C-0062` | p11:cor:distribution-moment-fingerprint-kaon-odd | 2418–2426 | VERIFIED-CONDITIONAL |
| `BH-VIID-C-0063` | p11:cor:single-trace-thermal-lock-signature | 2432–2438 | VERIFIED-CONDITIONAL |
| `BH-VIID-C-0064` | p11:cor:nn-contact-ratio-log-hamiltonian-distinction | 2444–2455 | VERIFIED-CONDITIONAL |
| `BH-VIID-C-0065` | p11:cor:scalar-glue-correlated-residue-validation-target | 2461–2488 | VERIFIED-CONDITIONAL |
| `BH-VIID-C-0066` | p11:prop:mixed-cb-hyperfine-validation-target | 2500–2519 | REPRODUCED |
| `BH-VIID-C-0067` | p11:thm:constructed-light-front-fraction-operators | 2545–2564 | VERIFIED-CONDITIONAL |
| `BH-VIID-C-0068` | p11:thm:light-front-fraction-povms | 2575–2609 | VERIFIED-CONDITIONAL |
| `BH-VIID-C-0069` | p11:thm:v264-optional-finite-wilson-povm-identification | 2623–2648 | REPRODUCED |
| `BH-VIID-C-0070` | p11:thm:v264-optional-finite-pdf-sum-rules | 2663–2687 | VERIFIED-CONDITIONAL |
| `BH-VIID-C-0071` | p11:thm:hausdorff-pdf-moment-limit | 2702–2718 | VERIFIED-CONDITIONAL |
| `BH-VIID-C-0072` | p11:thm:bounded-lipschitz-pdf-limit | 2732–2767 | VERIFIED-CONDITIONAL |
| `BH-VIID-C-0073` | p11:prop:v199-compression-defect | 2790–2802 | VERIFIED |
| `BH-VIID-C-0074` | Protected rank and density limit | 1260–1267 | VERIFIED-CONDITIONAL |
| `BH-VIID-C-0075` | Momentum-symbol/clock zero responses; Schur sign and bounded-source no-go | 1269–1305 | VERIFIED-CONDITIONAL |
| `BH-VIID-C-0076` | CAR chiral source double commutator and moment bound | 1308–1328 | VERIFIED-CONDITIONAL |
| `BH-VIID-C-0077` | Fixed-frontier free Clifford response, M0 and M1 | 1331–1358 | VERIFIED-CONDITIONAL |
| `BH-VIID-C-0078` | Shared SU3 flavor orbit, variance, energy cost, and color Casimir | 1361–1408 | VERIFIED-CONDITIONAL |
| `BH-VIID-C-0079` | Conditional three-flavor SU3 anomaly divisibility | 1412–1441 | VERIFIED-CONDITIONAL |
| `BH-VIID-C-0080` | Claimed packaged finite chiral/source numerical checker programs | 1465–1485 | UNRESOLVED |
| `BH-VIID-C-0081` | Orbital Dirac modes, 72/144 rank and gauge-owner distinction | 1498–1537 | REPRODUCED |
| `BH-VIID-C-0082` | Transported SU3 gauge covariance, exact 6 leakage | 1540–1556 | VERIFIED |
| `BH-VIID-C-0083` | Connection/Gauss/clock and scalar insertion owner boundaries | 1560–1583 | FORMALIZED |
| `BH-VIID-C-0084` | Source norm, 360 mode frontier and finite tracial variance 9 | 1587–1620 | VERIFIED-CONDITIONAL |
| `BH-VIID-C-0085` | SU3 Weyl torus Haar density normalization | 1638–1653 | VERIFIED |
| `BH-VIID-C-0086` | Rational Haar ball, link/face counts and huge-integer heat floor | 1655–1696 | VERIFIED |
| `BH-VIID-C-0087` | Heat-tail scope and characteristic real-return versus modulus | 1699–1715 | VERIFIED-CONDITIONAL |
| `BH-VIID-C-0088` | Zero-index overlap center, sign continuity and rational margins | 1719–1777 | VERIFIED-CONDITIONAL |
| `BH-VIID-C-0089` | Mass normalization and finite source/measure-domain exclusions | 1780–1832 | VERIFIED-CONDITIONAL |
| `BH-VIID-C-0090` | Inherited complete finite-sector/measure execution scope | 1876–1884 | FORMALIZED |
| `BH-VIID-C-0091` | G0 source owner, G16 transport and chiral spurion interface | 2028–2032 | FORMALIZED |
| `BH-VIID-C-0092` | Optional LFRep exact finite-versus-continuum scope | 2531–2543 | FORMALIZED |


## Batch 3 — Source analysis and independent verification

### 1. Positive finite blocking and source interpolation (2817–3286)

The path-holonomy restriction theorem proves contravariant composition, edge products, gauge equivariance, and the pushforward/pullback dual *given* compatible oriented groupoids. The Haar projectivity step additionally uses interior-disjoint independent fine edge chains. The source correctly presents these as finite auxiliary presentation hypotheses rather than deriving a new microscopic position lattice. For a positive integrable finite weight, disintegration, conditional-score differentiation and source covariance are valid on dominated source domains. The sharp `TV ≤ tanh(osc/4)` inequality was independently saturated using a two-point probability model; finite-level action-oscillation telescoping and cumulant partition counting reproduce. Exact measurable presentation transport contributes no error, but it is not a proof of native inter-level renormalization. `SURG` propagates bounded, source-owned moments under its common complex source-domain bound; it expressly does not settle unbounded composite fields or nontriviality/gap.

### 2. Polymer, crossover and scale-split certificates (3287–3761)

The cluster expansion of `1+u_t` is a standard hard-core polymer expansion on the **face edge-overlap graph**; the Kotecký–Preiss sum and the `B e^a ε/(1-C e^a ε)` sufficient inequality are correct at the stated strict margin. The SU(3) character majorant follows from the dimension and Casimir formula. The `t↓0` divergence of `||K_t−1||∞` and fixed strong-heat/lattice-spacing no-go are conditional comparison results, not a native compact-momentum obstruction. The exact finite RG recurrence, heat-Hessian stiffness-to-activity inequality `R₀(t) ≤ 6κ/(1−6κ)` for `κ<1/6`, and complete-action stopping algebra pass. The proof correctly keeps multi-face/source activity domination **as a separate supplied condition** rather than inferring it from a Hessian. 

**Issue G-0006** identifies a gap only in the broader M1→G78 UV telescoping assertion: the printed general `g_j^p` recurrence does not force summability. This does not invalidate the more detailed finite-interval `g_j⁴` comparison result or an alternate direct QFT4 covariance certificate. **Issue G-0007** identifies a missing rank-one vacuum/state guard in the *earlier* two-scale theorem; its later QFT4g–j same-side proof and mixed-state alternative explicitly supply the required route controls and remain sound.

### 3. Tier-2 QFT4, locality and RG coordinates (3762–4216)

The same-side vacuum-line bound `r≤ηᴷ/(1−q*)`, the pure-state expectation comparison and the no-gap trace-norm comparison are correct under their actual spectral/state hypotheses. Duhamel yields `ηᴷ≤t₀ηᴴ` without a global excited-state intertwining requirement. The Toeplitz highest-weight leakage example correctly warns that smooth-symbol density is insufficient for interacting state comparison. Positive exact finite quadrature follows by Carathéodory convexity and preserves the retained Yang–Mills bilinear form when the two-point densities lie in the quadrature space. Normal-chart geometric exhaustion gives an `O(ρ²/R²)` metric defect; interacting local-flat covariance still needs the observable/state comparison. 

**Issue G-0008** is limited to the asserted quantitative operator-locality inference: a scalar window-kernel estimate is not *alone* an operator-commutator inequality for general interacting representative words. The conditional finite-local-net provider in Paper IV-C is preserved as a bypass when its assumptions hold. **Issue G-0009** concerns only the overstrong sentence claiming all running coefficients are determined by local expectation matching; for a **known** fixed complete action and retained operator basis, the resolution-boundary response remains valid. The finite affine-support modified-Legendre theorem is located in `Paper1C-TechnicalMaterial-v1_59.tex` (label `p1b:thm:finite-flow`, lines 20317–20379) and is source-matched to the current finite flow. The imported Standard Model one-loop coefficients match Paper V-C's explicit beta calculation; no independent physical beta fit is asserted.

### 4. Optional affine-F4/D4 comparisons and momentum factor (4217–4546)

The exact `U(1)` valence-three Fourier integral leaves coupled face modes and excludes a product of three independent one-face heat kernels; its SU(3) epsilon-tensor analogue has the same claimed *comparison* obstruction. For the optional affine-F4 incidence bound, the B3-rooted graph yields the stated safe combinatorial constants `B=76`, `C=300`. Independently enumerating the standard D4 24-cell's 24 root vertices and 96 triangular faces yields the exact six-dimensional bivector outer-product sum **`16 I₆`**, not merely its trace. The D4/Hessian heat roots, strong-heat threshold, stopping budget and two-variable recursion numerical values reproduce. This verifies the *comparison member*, not M0–M2 native action provenance. The 137-coefficient fixed momentum-algebra expansion is an operator-norm implication once the actual coefficient maps are supplied and uniform; scalar vacuum moments alone do not discharge its norm hypotheses.

### Independent replay outputs (`Paper7D-Batch3IndependentChecks-v1_1.py`)

| Test | Independent result | Verdict |
|---|---|---|
| Two-point sharp TV | `tanh(1/2)=0.46211715726000975850` is attained at action oscillation 2 | PASS |
| SU(3) Hessian root | `t_Hess=5.7532958466330601`; `t_D4=4.4209988618076133` | PASS |
| Group heat at native Hessian | `R₀(t_Hess)=0.4050885697203126`; `R₀(3t_Hess)=0.00018114408523715` | PASS |
| KP affine-F4 threshold | `εcrit=0.00128940526998577`, `tcrit=14.31595771721708`, `κmax=0.000214624140832706` | PASS |
| Optional 3t-Hessian heat budget | `Q=0.01900311527638205`, spare `0.23099688472361795`, `r_max=0.1908606490007033` | PASS |
| D4 orbit identity | 24 vertices, 96 triangular faces; exact `Σ_f b_f⊗b_f=16I₆` | PASS, EXACT |
| D4 rooted two-variable iteration | `FN=0.00444401791097287<0.01`, `FB=0.70743260603255727<0.8` | PASS |
| Optional std heat | `R₀(2π²)=0.000034688563381327<0.000034689` | PASS |
| UV recurrence stress | `ρ=1/2`, `p=2`, `g_j²=R_j=1/(j+1)` obey recurrence with divergent residual sum | E4, demonstrates G-0006 needed guard |
| Rank-two gapped transfer | `K=diag(1,1,1/3)` with `η=ξ=0` but vacuum expectations alternate `±1` | E4, in abstract under-guarded theorem, not native-sector refutation |
| Hidden coupling identifiability | factorized Gibbs states have identical visible local expectations with arbitrary hidden coupling | E4, narrower G-0009 logical scope |

### Newly opened Batch 3 issue certificates

#### BH-VIID-G-0006 — moderate / MISSING_CONDITION / OPEN

**First defective/unresolved use:** `p12:thm:g78-msrg-consequence`, `Paper7D-TechnicalMaterial-v1_46.tex` lines 3453-3514. **Source-as-printed passage:** “Iterating M1 controls all ultraviolet telescoping differences and source derivatives.”

**Evidence and adjudication:** M1 permits an unspecified exponent p and supplies a contraction-forcing inequality but no demonstrable summability of total UV telescoping/source errors. With rho=1/2, g_j^2=1/(j+1), p=2 and residual r_j=1/(j+1), the displayed recurrence holds, g_j has standard one-loop asymptotic-freedom scaling, but Σ_j r_j diverges. Even a summable remainder must be linked to the actual action/state telescoping step.

**Exact audit obligation (no theory repair):** Source-establish a summable estimate for the actual UV coarse-action/state/source telescoping increments, with the flow exponent/rates and source derivatives in the same owner; do not infer it solely from the M1 recurrence.

**Verified affected path:** p12:def:g78-msrg -> p12:thm:g78-msrg-consequence -> G7b/QFT4 claim at 3488-3498 (conditional route; unresolved summability).

**Existing valid alternative:** p12:thm:effective-action-stability-qft4 via direct covariance bound; p12:thm:qft4hij-local-state-convergence via same-side residuals.

**Scope limit:** This is a logical sufficiency/quantification issue in a conditional certificate, not a refutation of any demonstrated physical RG trajectory.

#### BH-VIID-G-0007 — moderate / MISSING_CONDITION / OPEN

**First defective/unresolved use:** `p12:thm:two-scale-comparison-qft4`, `Paper7D-TechnicalMaterial-v1_46.tex` lines 3714-3755. **Source-as-printed passage:** “Let P_L be the rank-one vacuum projection of K_L.”

**Evidence and adjudication:** The cited two-scale definition explicitly assumes a gap between vacuum and non-vacuum spectrum but does not specify a rank-one vacuum eigenline and consistent chosen state; proof step 3733 consumes rank one without deriving it. Exact finite counterexample: K=diag(1,1,1/3), J=I, A=diag(1,-1,0), η=ξ=0, uniform gap 2/3; alternate selected vacuum vectors e1,e2, and expectations alternate ±1 (not Cauchy). The later source QFT4d and Lemma qft4g add rank-one hypotheses, so those separate branches are not challenged.

**Exact audit obligation (no theory repair):** Tie the earlier two-scale theorem to its later rank-one selected-vacuum/normalized-transfer hypothesis or supply actual state naturality on a degenerate vacuum block; maintain both branches as distinct route guards.

**Verified affected path:** p12:def:two-scale-gapped-comparison -> p12:thm:two-scale-comparison-qft4 proof 3733 -> QFT4.

**Existing valid alternative:** p12:thm:qft4hij-local-state-convergence, with explicit rank-one hypothesis; p12:prop:v2211-mixed-state-refinement-bound for degenerate densities; p12:thm:effective-action-stability-qft4 direct measure comparison.

**Scope limit:** Counterexample refutes the under-guarded abstract implication only; it does not establish a degenerate vacuum in native QCD.

#### BH-VIID-G-0008 — moderate / MISSING_CONDITION / OPEN

**First defective/unresolved use:** `p12:lem:tier2-asymptotic-locality`, `Paper7D-TechnicalMaterial-v1_46.tex` lines 4049-4069. **Source-as-printed passage:** “The commutator can only receive a contribution from the overlap of the two finite localization kernels.”

**Evidence and adjudication:** An off-diagonal decay estimate for a scalar window kernel does not, by itself, give the displayed operator commutator bound for every bounded local representative. The proof needs a claim-matched algebraic locality/overlap inequality for the actual operator families, including graded CAR/gauge-constraint treatment, normalization and support-volume constants. Paper IV-C states a finite local-net theorem under an explicit finite-locality assumption, but the lemma does not demonstrate that the A_L(f), B_L(g) here obey its hypotheses or its quantitative almost-disjoint analogue.

**Exact audit obligation (no theory repair):** Identify the actual finite operator/source constructors and prove a uniform bound of ||[A_L(f),B_L(g)]||_omega by the overlap of their retained support kernels, with parity/constraint and support constants; or state it as an explicit branch guard.

**Verified affected path:** spectral-window decay hypothesis -> p12:lem:tier2-asymptotic-locality claimed asymptotic locality.

**Existing valid alternative:** Paper IV-C finite local-net theorem when its explicit finite-locality hypotheses are satisfied; Paper VII-C QFT locality as an independent certificate obligation.

**Scope limit:** No actual in-domain counterexample to the Native CAR/gauge operator branch was identified; the asserted deduction is under-evidenced, not proven physically false.

#### BH-VIID-G-0009 — minor / LOGICAL_GAP / OPEN

**First defective/unresolved use:** `p12:prop:rg-not-new-input`, `Paper7D-TechnicalMaterial-v1_46.tex` lines 4076-4082. **Source-as-printed passage:** “Any scale-dependent coefficient that appears in a representative action or observable is fixed by the requirement that representatives of the same local question have compatible expectations”

**Evidence and adjudication:** Approximate local expectation compatibility determines a continuum state on the queried local algebra, not necessarily every coefficient in the full finite action. A factorized finite Gibbs family can vary an unobserved hidden-sector coupling at every level while giving identical expectations on the same visible local cylinders and identical CP comparison maps. This does not challenge the valid narrower statement that couplings are coordinates of a supplied, already fixed action and operator-basis projection.

**Exact audit obligation (no theory repair):** Distinguish bookkeeping for known action coordinates from uniqueness/inference of every finite running coupling solely through the QFT4 local expectation compatibility inequalities.

**Verified affected path:** p12:def:bh-renormalization-map -> p12:prop:rg-not-new-input attribution of all couplings.

**Existing valid alternative:** p12:thm:v2140-rg-boundary-response on a differentiable fixed complete finite action and fixed retained basis.

**Scope limit:** No failure of the imported finite Wetterich/modified-Legendre flow or of derived Standard Model one-loop coefficients is claimed.

## Claim census — Batch 3 (35 named results + 9 definitions + 17 material blocks)

Every item below is an existing source claim/condition, with source line location and an explicit disposition. `VERIFIED-CONDITIONAL` retains antecedents without classifying those antecedents as physical occurrences. `UNRESOLVED` retains the narrower issue reference in the machine-readable ledger.

| Claim ID | Existing statement/definition or mathematical block | Lines | Disposition |
|---|---|---:|---|
| `BH-VIID-C-0093` | `p12:thm:v251-inherited-path-coarse-map` | 2827–2890 | VERIFIED-CONDITIONAL |
| `BH-VIID-C-0094` | `p12:cor:v251-finite-same-owner-block-square` | 2917–2939 | REPRODUCED |
| `BH-VIID-C-0095` | `p12:thm:v199-rgas-disintegration` | 2961–2986 | VERIFIED |
| `BH-VIID-C-0096` | `p12:cor:v199-rgas-sources-reflection` | 3000–3010 | VERIFIED-CONDITIONAL |
| `BH-VIID-C-0097` | `p12:thm:v203-blocking-oscillation` | 3024–3045 | VERIFIED |
| `BH-VIID-C-0098` | `p12:cor:v203-summable-action-defects` | 3055–3078 | VERIFIED-CONDITIONAL |
| `BH-VIID-C-0099` | `p12:thm:v204-blocking-presentation` | 3099–3120 | VERIFIED |
| `BH-VIID-C-0100` | `p12:thm:effective-action-stability-qft4` | 3140–3167 | VERIFIED-CONDITIONAL |
| `BH-VIID-C-0101` | `p12:thm:v185-uniform-source-effective-action-stability` | 3179–3214 | VERIFIED-CONDITIONAL |
| `BH-VIID-C-0102` | `p12:cor:v236-source-owned-continuum` | 3251–3269 | REPRODUCED |
| `BH-VIID-C-0103` | `p12:cor:v236-ward-dependent` | 3271–3281 | REPRODUCED |
| `BH-VIID-C-0104` | `p12:thm:source-stable-heat-polymer-domain` | 3317–3360 | VERIFIED-CONDITIONAL |
| `BH-VIID-C-0105` | `p12:cor:polymer-defect-stability` | 3394–3412 | VERIFIED-CONDITIONAL |
| `BH-VIID-C-0106` | `p12:prop:no-one-regime-haar-polymer-continuum` | 3423–3437 | VERIFIED-CONDITIONAL |
| `BH-VIID-C-0107` | `p12:thm:g78-msrg-consequence` | 3486–3499 | UNRESOLVED |
| `BH-VIID-C-0108` | `p12:prop:v198-finite-rg-recurrence` | 3576–3595 | VERIFIED |
| `BH-VIID-C-0109` | `p12:prop:v198-stiffness-activity` | 3603–3624 | VERIFIED |
| `BH-VIID-C-0110` | `p12:prop:v198-conditional-stopping-budget` | 3637–3666 | VERIFIED-CONDITIONAL |
| `BH-VIID-C-0111` | `p12:thm:two-scale-comparison-qft4` | 3725–3728 | UNRESOLVED |
| `BH-VIID-C-0112` | `p12:lem:qft4g-projection-stability` | 3819–3834 | VERIFIED |
| `BH-VIID-C-0113` | `p12:thm:qft4hij-local-state-convergence` | 3844–3859 | VERIFIED |
| `BH-VIID-C-0114` | `p12:prop:v2211-mixed-state-refinement-bound` | 3871–3882 | VERIFIED |
| `BH-VIID-C-0115` | `p12:prop:tier2-qft4-estimates` | 3920–3933 | VERIFIED |
| `BH-VIID-C-0116` | `p12:thm:tier2-closes-qft4-bounded` | 3951–3964 | VERIFIED-CONDITIONAL |
| `BH-VIID-C-0117` | `p12:prop:tier2-quadrature` | 3970–3990 | VERIFIED |
| `BH-VIID-C-0118` | `p12:cor:v185-ym-quadrature-presentation-invariance` | 3996–4017 | VERIFIED-CONDITIONAL |
| `BH-VIID-C-0119` | `p12:lem:tier2-flat-chart-covariance` | 4027–4044 | VERIFIED-CONDITIONAL |
| `BH-VIID-C-0120` | `p12:lem:tier2-asymptotic-locality` | 4049–4066 | UNRESOLVED |
| `BH-VIID-C-0121` | `p12:prop:rg-not-new-input` | 4076–4079 | UNRESOLVED |
| `BH-VIID-C-0122` | `p12:thm:v2140-rg-boundary-response` | 4084–4117 | VERIFIED-CONDITIONAL |
| `BH-VIID-C-0123` | `p12:cor:v2140-sm-one-loop-boundary-response` | 4133–4143 | REPRODUCED |
| `BH-VIID-C-0124` | `p12:prop:v199-rgas-spectral-criterion` | 4174–4180 | VERIFIED |
| `BH-VIID-C-0125` | `p12:prop:v199-rgas-response-plateau` | 4193–4205 | VERIFIED |
| `BH-VIID-C-0126` | `p12:prop:v2158-d4-voronoi-constant-curvature` | 4337–4392 | VERIFIED-CONDITIONAL |
| `BH-VIID-C-0127` | `p12:prop:v226-refinement-coefficients` | 4512–4525 | VERIFIED |
| `BH-VIID-C-0128` | (definition) `p12:def:v236-surg` | 3242–3249 | FORMALIZED |
| `BH-VIID-C-0129` | (definition) `p12:def:heat-polymer-activity-norm` | 3297–3315 | FORMALIZED |
| `BH-VIID-C-0130` | (definition) `p12:def:g78-msrg` | 3448–3479 | FORMALIZED |
| `BH-VIID-C-0131` | (definition) `p12:def:v198-complete-action-norm-interface` | 3533–3574 | FORMALIZED |
| `BH-VIID-C-0132` | (definition) `p12:def:bh-renormalization-map` | 3696–3711 | FORMALIZED |
| `BH-VIID-C-0133` | (definition) `p12:def:two-scale-gapped-comparison` | 3714–3723 | FORMALIZED |
| `BH-VIID-C-0134` | (definition) `p12:def:local-vacuum-comparison-seminorm` | 3774–3798 | FORMALIZED |
| `BH-VIID-C-0135` | (definition) `p12:def:admissible-local-vacuum-compatibility` | 3800–3817 | FORMALIZED |
| `BH-VIID-C-0136` | (definition) `p12:def:tier2-spectral-window-class` | 3904–3918 | FORMALIZED |
| `BH-VIID-C-0137` | Action-first path groupoid ownership as a conditional auxiliary presentation | 2823–2826 | FORMALIZED |
| `BH-VIID-C-0138` | Positive Radon–Nikodym effective coarse action and vacuum-constant scope | 2953–2958 | VERIFIED-CONDITIONAL |
| `BH-VIID-C-0139` | Vacuum constant versus retained dynamical metric and finite continuum firewall | 3016–3021 | FORMALIZED |
| `BH-VIID-C-0140` | Bounded source tilts, extensive oscillation, native UV limitations | 3087–3097 | VERIFIED-CONDITIONAL |
| `BH-VIID-C-0141` | Exact finite presentation changes do not replace inter-level blocking | 3129–3136 | FORMALIZED |
| `BH-VIID-C-0142` | Semigroup and covariance consequences require same reflection-positive action owner | 3228–3238 | VERIFIED-CONDITIONAL |
| `BH-VIID-C-0143` | Strong-heat polymer regime separated from small-field UV expansion | 3287–3295 | FORMALIZED |
| `BH-VIID-C-0144` | Scale vs refinement index and full-action sup norm distinction | 3523–3531 | FORMALIZED |
| `BH-VIID-C-0145` | Claim-specific premise reduction and scope of source zero-free domain | 3675–3694 | FORMALIZED |
| `BH-VIID-C-0146` | Alternating cross-vacuum diagnostics fail; same-side transfer detects defect | 3890–3897 | VERIFIED |
| `BH-VIID-C-0147` | Tier-2 finite-symbol versus interacting cross-level defect limits | 4072–4074 | FORMALIZED |
| `BH-VIID-C-0148` | Numerical affine-F4 crossover checkpoint and complete-activity scope | 4217–4254 | VERIFIED-CONDITIONAL |
| `BH-VIID-C-0149` | U(1) valence-three coupled Fourier obstruction to one-face heat projectivity | 4264–4301 | VERIFIED |
| `BH-VIID-C-0150` | Affine F4 Coxeter incidence count and polymer growth constants | 4308–4335 | VERIFIED-CONDITIONAL |
| `BH-VIID-C-0151` | Hessian heat versus optional standard heat and strict KP margins | 4404–4484 | VERIFIED-CONDITIONAL |
| `BH-VIID-C-0152` | Fixed strong heat on shrinking position-lattice regulator is an optional diagnostic | 4488–4506 | VERIFIED-CONDITIONAL |
| `BH-VIID-C-0153` | Frozen momentum algebra does not imply uniform spatial/field estimates | 4532–4540 | FORMALIZED |


## Batch 4 — source replay, exact checks and adjudication (4547–6757)

### Finite selector algebras and classical/thermal/gauge subsystem scope (4561–5283)

The external/internal trace factorization is a finite tensor-operator identity; the proof neither assumes nor concludes a factorized physical state. The finite C* selector algebra and its commutant have the claimed Wedderburn forms, and the antitone selector relation is exact. A two-qubit matrix test independently gives commutant dimensions 8 and 4 for a nested selector pair. Finite energy/gauge sector invariance follows on the stated exact-commutator/common-Hamiltonian branch; imported Paper-IV conservation and finite KMS uniqueness are not rederived as new axioms. The direct-sum KMS central-mixture caveat and the distinction from production-state thermalization are correct. GP2 sector admissibility and finite-witness classes are *internal classification conventions*, not empirical theorems excluding external theories.

**G-0011** localizes the unquantified classical-mechanics Poisson correspondence. Its classical probability C*=C^n part is exact and independent. **G-0012** identifies missing local density, continuity equation and constitutive closure conditions for the stronger hydrodynamic equation statement. An exact conserved but nonlocal Bell projector supplies an adversarial check against conservation-alone sufficiency. Finite subsystem typing and external-interface presentations remain valid.

### Truncated CCR, finite witness criteria, and correction already present (5287–5701; 6463–6520)

The one-mode boundary identity `[a_N,a_N†]=I−(N+1)|N><N|` is exact. The tabulated N=8,32,128 tail estimates reproduce. The source correctly treats new-particle and BSM names as inadmissible without a native finite transcript, and does not infer a mass or physical population from a commutant. **G-0010** identifies the *earlier* proof wording that promotes a single expectation-level defect test to ordinary full CCR recovery. The *later* theorem at lines 6463–6492 explicitly refutes that inference with `rho_N=|N−1><N−1|`, and the sufficient trace-norm/tightness result at 6494–6520 gives a valid independent condition for regular Weyl-state convergence. These alternative routes are preserved; no false global CCR obstruction is introduced.

### QCD source domains, comparison numerics and G16/G17 transport (5705–6298)

The static-light screening theorem is a direct Rayleigh–Ritz squeeze under its *supplied trial-vector energy bound*; no native full-QCD screening is inferred. The C² even source example correctly disproves an automatic quartic remainder. Clock-index scalar divergence follows under the zero-mode/positive-pair hypotheses and is not a physical condensate. The sharp spectral-band 2×2 crossing example, finite link holonomy no-go and odd double-factorial cofinality checks are coherent, with temporal and spatial operators kept distinct. The eight E36/E40 mass-comparison values agree numerically with the displayed expressions (modulo source rounding), but are explicitly retained as non-derivational diagnostics; the nuclear transfer denominator/selector is not claimed proved.

The minimal source quotient in current Paper VII-C is **real**, so the 1D `C^{-1}` reduction of finite source contragredience is compatible with the general `C^{-†}` formula; an apparent complex-scalar conjugation allegation was rejected after reading the imported source. The matrix RGE follows by differentiation on an invertible comparison chart, and finite-normalization degeneracy is exact. The later G16 theorem distinguishes closed finite constructors from named-scheme numerical evaluations and from a physical pole. The electromagnetic Hessian naturality statement is about retaining a given source coordinate, not a free new physical matching constant; Thomson response remains a scoped continuum/readout frontier.

### Baryon, F40 and exact 96-face/Clifford/Wilson reference proofs (6310–6757)

The C3 transfer gain 1/5 gives squared 1/25 on a normalized pure quintet comparator; flavor couplings, transfer gaps and mass poles are *not* thereby identified. Independent SU(3) character orthogonality reproduces `E F=1/9`, `Var F=11/162`, and `Var(96-face average)=11/15552` under independent Haar links. Two distinct triangular faces have exclusive link variables, so pairwise covariances vanish in that reference measure; no interacting QCD variance follows. The independent-Haar 3-path baryon determinant second moment is exactly 1/27, with the 192-fan orthogonality and interaction-order comparisons quarantined.

The finite comparison Hamiltonian's full spinor/angular-momentum spectrum independently gives cumulative ranks **2, 8, 20, 28, 50, 82, 126, 184** for R=7 and gap **2κ** above selected r>=3 highest-spin levels. The symmetric-cube rank list **0,1,4,10,20**, full Spin(4) block dimensions 16+4 and positive Gram-kernel identity pass at their stated mathematical scopes. The SU(3) central-heat spin-flux response has one interior positive zero at **t*=3.2002263350685032…**. Neither this comparison Hamiltonian nor those gauge averages determine a physical nuclear QCD pole.

**G-0013** is a separate missing-evidence issue: `Proofs/Paper00-PetersenHodgePlucker-v1_11-verify.py` is present with historical output, but imports `v1_10-verify.py`, absent from all provided ZIPs. The script aborts at import and cannot replay the exact native F40 60-arrow / 21-frame certificate. The distinct `Paper00-PaperVIIRepairProofs-v1_1.py` executes and reproduces some 24-cell/CCR/face data, but does not substitute for that unavailable F40 dependency.

### New Batch-4 issue certificates

#### BH-VIID-G-0010 — moderate / TYPE_OR_DOMAIN

**First source step:** `p12:prop:executable-ccr-boundary-witness-numerics`, `Paper7D-TechnicalMaterial-v1_46.tex:5397`. **Source obligation:** Keep expectation-level CCR recovery separate from regular Weyl-state convergence, as already accomplished by the later theorem; source-level claim cross-references must not overpromote the weaker criterion.

**Finding:** The printed proof equates vanishing of the single commutator expectation defect with general ordinary CCR recovery. Its own later theorem p12:thm:v350-ccr-expectation-vs-core (6463–6492) corrects this: rho_N=|N-1><N-1| has epsilon_N=0 while mean occupation grows, so the expectation test does not establish a regular Weyl state. The numerical cutoff values themselves are correct.

**Verified ancestry/reach:** p4:prop:explicit-finite-ccr-boundary-defect -> p12:cor:ccr-regular-subsystem-condition -> p12:prop:executable-ccr-boundary-witness-numerics; p12:prop:executable-ccr-boundary-witness-numerics -> table 5376-5381 (wording requires expectation/full-state distinction).

**Valid bypass:** p12:thm:v350-ccr-expectation-vs-core; p12:prop:v350-ccr-state-tightness. **Scope guard:** No failure of the exact finite CCR identity; geometric-tail states remain regular under their own stronger bounds.

**Unresolved requirement:** Source-reconcile early v2.37 cutoff table/proof with the already-present v2.350 two-level theorem; no new theorem needed.

#### BH-VIID-G-0011 — minor / MISSING_CONDITION

**First source step:** `p12:prop:classical-subsystem`, `Paper7D-TechnicalMaterial-v1_46.tex:5088-5096`. **Source obligation:** Attach source-defined correspondence map, topology and commutator/Poisson convergence as the guard for the classical-mechanics part, rather than inferring it from commutativity alone.

**Finding:** The commutative finite subalgebra statement is exact. The stronger classical Hamiltonian equation requires a specified coherent/semi-classical correspondence family with scaled commutator-to-Poisson limit and compatible dynamics. The proof says this limit holds "when" those conditions are supplied, but the proposition does not state the map or convergence hypotheses.

**Verified ancestry/reach:** p12:def:selector-datum -> p12:prop:classical-subsystem; p12:prop:classical-subsystem -> classical-mechanics subsystem readout.

**Valid bypass:** commutative classical probability C*=C^n branch is independently valid. **Scope guard:** No claim that classical mechanics is absent from the framework; this is a quantifier/limit guard.

**Unresolved requirement:** Cite or specify the already-required controlled deformation/correspondence limit for the nontrivial classical-mechanics statement.

#### BH-VIID-G-0012 — moderate / MISSING_CONDITION

**First source step:** `p12:prop:hydrodynamics-subsystem`, `Paper7D-TechnicalMaterial-v1_46.tex:5239-5246`. **Source obligation:** Require a licensed locality/net and extensive charge density, continuity/current control, local-equilibrium/scale-separation and an actual constitutive/closure estimate for the claimed hydrodynamic equation.

**Finding:** Commutation/conservation alone does not imply that the global Q_i have a local density in the selected finite local algebra, satisfy a continuity equation, or admit a closed long-wavelength transport law. Exact counterexample: on two qubits H=0 and Q=|Phi+><Phi+| commute, but Q does not lie in the span of onsite operators q1⊗I+I⊗q2. The proof introduces a selected local-equilibrium coarse graining but does not certify the needed charge-density and hydrodynamic closure maps.

**Verified ancestry/reach:** p4:finite-conservation-theorem -> p12:prop:hydrodynamics-subsystem; p12:prop:hydrodynamics-subsystem -> claimed long-wavelength hydrodynamic closure.

**Valid bypass:** Paper IV exact finite charge conservation itself remains valid. **Scope guard:** Counterexample attacks the bare conservation ⇒ local-density implication only, not any preselected local equilibrium model that supplies these conditions.

**Unresolved requirement:** Source-match existing local-net/current/kinetic proof or retain as a genuinely conditional interface claim.

#### BH-VIID-G-0013 — moderate / MISSING_EVIDENCE

**First source step:** `p12:prop:v345-f40-execution-ledger`, `Paper7D-TechnicalMaterial-v1_46.tex:6360-6377`. **Source obligation:** Supply the required v1_10 verifier and its inputs, or an independently executable v1_11 verifier with immutable source evidence for 60-arrow mapping, 11/16/21 readout ranks, and cycle-frame polynomial.

**Finding:** The DAG ZIP includes v1_11 Python source and archived text output, but the script imports Paper00-PetersenHodgePlucker-v1_10-verify.py via runpy on line 14, and the v1_10 verifier is absent from every currently supplied ZIP. Direct replay terminates FileNotFoundError before any of the eight certificate assertions execute. The separately supplied PaperVIIRepairProofs-v1_1.py runs successfully but does not reproduce this v1_11 60-arrow/21-frame certificate.

**Verified ancestry/reach:** Proofs/Paper00-PetersenHodgePlucker-v1_10-verify.py (missing) -> v1_11-verify.py -> p12:prop:v345-f40-execution-ledger; v1_11 historical output -> p12:prop:v345-f40-execution-ledger (evidence missing, no physical realization inferred).

**Valid bypass:** separate PaperVIIRepairProofs-v1_1 exact 24-cell and CCR checks, not the F40 certificate. **Scope guard:** Missing executable evidence is not evidence that the claimed ranks/polynomial are false.

**Unresolved requirement:** Provide the exact dependency v1_10, then rerun v1_11 and compare recorded hashes/results; no physical QCD action inference.

### Batch 4 census (52 named results, 12 definitions, 31 material blocks)

The table gives exact source-located disposition on the paper's declared domain, not a claim that every item has an independent external certificate.

| Claim ID | Source result / material block | Lines | Status |
|---|---|---:|---|
| `BH-VIID-C-0154` | p12:cor:v2102-finite-internal-momentum-trace | 4561–4584 | VERIFIED |
| `BH-VIID-C-0155` | (definition) p12:def:finite-bh-carrier-algebra | 4655–4666 | FORMALIZED |
| `BH-VIID-C-0156` | (definition) p12:def:selector-datum | 4668–4686 | FORMALIZED |
| `BH-VIID-C-0157` | (definition) p12:def:accessible-commutant-algebra | 4688–4700 | FORMALIZED |
| `BH-VIID-C-0158` | p12:thm:finite-selector-commutant-subsystem | 4702–4717 | VERIFIED-CONDITIONAL |
| `BH-VIID-C-0159` | p12:thm:wedderburn-selector-form | 4727–4748 | VERIFIED-CONDITIONAL |
| `BH-VIID-C-0160` | p12:cor:hidden-dof-multiplicity | 4756–4763 | VERIFIED-CONDITIONAL |
| `BH-VIID-C-0161` | p12:thm:order-reversing-selector-lattice | 4769–4787 | VERIFIED |
| `BH-VIID-C-0162` | (definition) p12:def:energy-symmetry-selector | 4811–4828 | FORMALIZED |
| `BH-VIID-C-0163` | p12:thm:finite-energy-symmetry-sector | 4830–4854 | VERIFIED |
| `BH-VIID-C-0164` | (definition) p12:def:stabilizer-after-breaking | 4876–4885 | FORMALIZED |
| `BH-VIID-C-0165` | p12:prop:symmetry-breaking-selector-reduction | 4887–4894 | VERIFIED-CONDITIONAL |
| `BH-VIID-C-0166` | (definition) p12:def:finite-gauge-selector | 4904–4922 | FORMALIZED |
| `BH-VIID-C-0167` | p12:thm:finite-gauge-projection | 4924–4937 | VERIFIED |
| `BH-VIID-C-0168` | (definition) p12:def:subsystem-status-classes | 5007–5024 | FORMALIZED |
| `BH-VIID-C-0169` | p12:prop:gp2-filter-new-sectors | 5026–5038 | FORMALIZED |
| `BH-VIID-C-0170` | p12:thm:theory-subsystem-classification | 5047–5059 | VERIFIED-CONDITIONAL |
| `BH-VIID-C-0171` | p12:prop:classical-subsystem | 5080–5093 | UNRESOLVED |
| `BH-VIID-C-0172` | p12:cor:k16-finite-kms-target-versus-thermalization | 5113–5144 | VERIFIED |
| `BH-VIID-C-0173` | p12:prop:sr-subsystem | 5154–5170 | VERIFIED-CONDITIONAL |
| `BH-VIID-C-0174` | p12:prop:gr-subsystem | 5183–5194 | VERIFIED-CONDITIONAL |
| `BH-VIID-C-0175` | p12:prop:gauge-ym-subsystem | 5200–5203 | VERIFIED-CONDITIONAL |
| `BH-VIID-C-0176` | p12:prop:sm-qcd-subsystems | 5209–5212 | VERIFIED-CONDITIONAL |
| `BH-VIID-C-0177` | p12:prop:eft-subsystem | 5218–5227 | VERIFIED-CONDITIONAL |
| `BH-VIID-C-0178` | p12:prop:hydrodynamics-subsystem | 5233–5243 | UNRESOLVED |
| `BH-VIID-C-0179` | p12:prop:condensed-matter-subsystems | 5249–5252 | VERIFIED-CONDITIONAL |
| `BH-VIID-C-0180` | (definition) p12:def:controlled-continuum-subsystem | 5262–5269 | FORMALIZED |
| `BH-VIID-C-0181` | p12:thm:continuum-theories-subsystem-limits | 5271–5274 | VERIFIED-CONDITIONAL |
| `BH-VIID-C-0182` | p12:cor:ccr-regular-subsystem-condition | 5310–5317 | VERIFIED |
| `BH-VIID-C-0183` | p12:prop:executable-ccr-boundary-witness-numerics | 5353–5394 | UNRESOLVED |
| `BH-VIID-C-0184` | (definition) p12:def:native-new-physics-witness | 5404–5415 | FORMALIZED |
| `BH-VIID-C-0185` | p12:cor:finite-witness-transcript-closure | 5419–5422 | VERIFIED-CONDITIONAL |
| `BH-VIID-C-0186` | p12:thm:finite-witness-criterion-new-sectors | 5427–5430 | FORMALIZED |
| `BH-VIID-C-0187` | p12:cor:finite-witness-bsm-sectors | 5437–5440 | FORMALIZED |
| `BH-VIID-C-0188` | p12:cor:where-new-physics-search | 5446–5459 | FORMALIZED |
| `BH-VIID-C-0189` | (definition) p12:def:finite-discovery-algorithm | 5468–5491 | FORMALIZED |
| `BH-VIID-C-0190` | p12:thm:finite-resolution-discovery-coverage | 5493–5496 | FORMALIZED |
| `BH-VIID-C-0191` | (definition) p12:def:finite-witness-target-transcript | 5518–5544 | FORMALIZED |
| `BH-VIID-C-0192` | p12:prop:finite-witness-target-priority | 5600–5615 | VERIFIED |
| `BH-VIID-C-0193` | p12:cor:no-particle-claim-from-witness-alone | 5620–5627 | FORMALIZED |
| `BH-VIID-C-0194` | p10:prop:v2187-conditional-static-light-screening | 5716–5733 | VERIFIED |
| `BH-VIID-C-0195` | p10:prop:v2189-clock-zero-mode-scope | 5779–5792 | VERIFIED-CONDITIONAL |
| `BH-VIID-C-0196` | (definition) p12:def:v288-native-scalar-source-dual | 6086–6100 | FORMALIZED |
| `BH-VIID-C-0197` | p12:prop:v288-contragredient-mass-source-transport | 6102–6114 | VERIFIED |
| `BH-VIID-C-0198` | p12:cor:v288-mass-rge-dual-transport | 6116–6129 | VERIFIED |
| `BH-VIID-C-0199` | p12:prop:v288-finite-normalization-degeneracy | 6131–6140 | VERIFIED |
| `BH-VIID-C-0200` | p12:prop:v289-native-overlap-scalar-normalization | 6160–6170 | VERIFIED-CONDITIONAL |
| `BH-VIID-C-0201` | p12:cor:v289-tree-source-coordinate | 6172–6183 | VERIFIED-CONDITIONAL |
| `BH-VIID-C-0202` | p12:thm:v293-g16-structural-status | 6220–6244 | VERIFIED-CONDITIONAL |
| `BH-VIID-C-0203` | p12:cor:v293-native-source-evolution-bypasses-scheme | 6246–6258 | VERIFIED-CONDITIONAL |
| `BH-VIID-C-0204` | p12:cor:v2100-g17-no-free-matching | 6267–6281 | VERIFIED-CONDITIONAL |
| `BH-VIID-C-0205` | p12:cor:v2100-thomson-frontier | 6283–6298 | VERIFIED-CONDITIONAL |
| `BH-VIID-C-0206` | p12:prop:v344-baryon-character-execution-ledger | 6312–6329 | VERIFIED-CONDITIONAL |
| `BH-VIID-C-0207` | p12:prop:v345-f40-execution-ledger | 6358–6374 | UNRESOLVED |
| `BH-VIID-C-0208` | p12:prop:v350-flux-reference-witness | 6391–6413 | VERIFIED |
| `BH-VIID-C-0209` | p12:thm:v350-wedderburn-exact-scope | 6433–6453 | VERIFIED |
| `BH-VIID-C-0210` | p12:thm:v350-ccr-expectation-vs-core | 6463–6481 | VERIFIED |
| `BH-VIID-C-0211` | p12:prop:v350-ccr-state-tightness | 6494–6507 | VERIFIED |
| `BH-VIID-C-0212` | p12:thm:v357-clifford-shell-spectrum | 6540–6568 | VERIFIED |
| `BH-VIID-C-0213` | p12:prop:v357-shell-weyl-stability | 6589–6599 | VERIFIED |
| `BH-VIID-C-0214` | p12:prop:v357-degree-three-source-no-go | 6606–6627 | VERIFIED |
| `BH-VIID-C-0215` | p12:prop:v357-positive-gram-kernel | 6636–6648 | VERIFIED |
| `BH-VIID-C-0216` | p12:prop:v357-heat-spinflux-sign | 6657–6671 | VERIFIED |
| `BH-VIID-C-0217` | p12:prop:v365-haar-three-path-second-moment | 6714–6725 | VERIFIED |
| `BH-VIID-C-0218` | Ownership boundary: finite-quantum foundation is imported from Paper IV | 4552–4553 | FORMALIZED |
| `BH-VIID-C-0219` | Trace product-sector scope: no physical state or measure factorization | 4600–4607 | FORMALIZED |
| `BH-VIID-C-0220` | Selector-generated finite sectors, GP2 native-vs-supplied classification | 4638–4649 | FORMALIZED |
| `BH-VIID-C-0221` | Commutant antitonicity and Galois-type selector interpretation | 4796–4805 | VERIFIED-CONDITIONAL |
| `BH-VIID-C-0222` | Finite Noether conservation under an exact generator commutator | 4860–4874 | VERIFIED-CONDITIONAL |
| `BH-VIID-C-0223` | QCD singlet and finite gauge-sector import scope | 4944–4947 | FORMALIZED |
| `BH-VIID-C-0224` | Subsystem status and finite-witness ledger cross-reference table | 4951–5005 | FORMALIZED |
| `BH-VIID-C-0225` | Finite quantum states, instruments and channels are Paper IV imports | 5065–5078 | FORMALIZED |
| `BH-VIID-C-0226` | Finite thermal/KMS entropy and channel calculus are Paper IV imports | 5099–5111 | FORMALIZED |
| `BH-VIID-C-0227` | Continuum reconstruction cannot bypass the finite witness certificate | 5280–5283 | FORMALIZED |
| `BH-VIID-C-0228` | Finite CCR trace obstruction and truncated boundary formula are imported | 5291–5308 | REPRODUCED |
| `BH-VIID-C-0229` | CCR boundary saturation does not by itself add a boson | 5348–5351 | FORMALIZED |
| `BH-VIID-C-0230` | Executable finite witness targets and null-condition table | 5509–5598 | FORMALIZED |
| `BH-VIID-C-0231` | SR and GR retained as typed imported subtheories, not whole theory | 5638–5648 | FORMALIZED |
| `BH-VIID-C-0232` | Summary selector, gauge, energy, continuum and witness schema | 5652–5701 | FORMALIZED |
| `BH-VIID-C-0233` | C2 even source counterexample to theta4 remainder | 5750–5761 | REPRODUCED |
| `BH-VIID-C-0234` | Clock degree cannot substitute for a physical spatial mode density | 5809–5823 | VERIFIED-CONDITIONAL |
| `BH-VIID-C-0235` | Sharp spectral projection crossing and projector derivative jets | 5827–5852 | REPRODUCED |
| `BH-VIID-C-0236` | Finite retained holonomies do not determine global Dirac compression | 5856–5865 | VERIFIED-CONDITIONAL |
| `BH-VIID-C-0237` | Licensed field/dual action grammar distinguished from global Dirac geometry | 5869–5880 | FORMALIZED |
| `BH-VIID-C-0238` | Odd-clock double-factorial divisor cofinality | 5884–5890 | REPRODUCED |
| `BH-VIID-C-0239` | Exploratory E36/E40 mass arithmetic and unpromoted nuclear transfer ansatz | 5902–6045 | REPRODUCED |
| `BH-VIID-C-0240` | No new source/temperature selector and internal vs full-sector mass gap firewall | 6050–6075 | FORMALIZED |
| `BH-VIID-C-0241` | Split G16 flow, finite comparison and pole obligations | 6142–6151 | FORMALIZED |
| `BH-VIID-C-0242` | Historical G16 comparison frontier superseded by noncritical constructor | 6185–6193 | FORMALIZED |
| `BH-VIID-C-0243` | Interacting scalar response and common noncritical finite scheme constructor | 6203–6218 | VERIFIED-CONDITIONAL |
| `BH-VIID-C-0244` | Heavy baryon mass-difference comparison remains unselected diagnostic | 6342–6350 | FORMALIZED |
| `BH-VIID-C-0245` | Exact PaperVIIRepairProofs output and nonphysical-scope provenance | 6522–6532 | REPRODUCED |
| `BH-VIID-C-0246` | Clifford comparison does not identify physical nuclear gap spectrum | 6682–6693 | FORMALIZED |
| `BH-VIID-C-0247` | Determinant fan order-independence and two-root Gram whitening | 6700–6713 | REPRODUCED |
| `BH-VIID-C-0248` | Research-only Wilson fan/electric/jet measurements not action spectra | 6736–6754 | FORMALIZED |

## Audit completeness, issue ancestry and release controls

- **Source completeness:** the exhaustive formal-source extractor found and dispositioned all 64 formal environments in lines 4547–6757 (52 named results + 12 definitions), with 43 proof environments. A manual E1 census added 31 unnamed material blocks there. Together with Batches 1–3 this yields the **248** claimed dispositions across all **6,757** lines and **132** proofs.
- **No physical promotion:** explicit non-realization frontiers for F40, mass poles, nonminimal BSM sectors, strong-heat RG comparison, screening and a reconstructed continuum Ward/net limit are preserved exactly as conditional or non-witness statements. A missing script does not constitute a refutation. A finite reference spectrum is not a hadron mass spectrum.
- **Exact first-origin register:** 13 distinct IDs `BH-VIID-G-0001` through `BH-VIID-G-0013` with source origin, class, severity, consumed conditions and verified or possible downstream paths. Issues G-0001–G-0009 are inherited unchanged from Batches 1–3. The four new issues G-0010–G-0013 refer to 4 new first-step origins, not duplicated upstream conditions.
- **Per-route bypass:** issue G-0010 is bypassed by later v2.350 regular Weyl-state theorem; G-0011 does not affect classical finite probability; G-0012 does not affect finite conservation; G-0013 does not affect the independent v2.350 24-cell/Haar/CCR checker; issues G-0006/G-0007 preserve independent QFT4 proof routes. Upstream proofs G0/GP1–GP3, S1/S3, m_p=1 are not reopened.
- **Evidence independence:** the latest E3/E4 results are in `Paper7D-Batch4IndependentChecks-v1_1.py` and `Paper7D-Batch4IndependentResults-v1_1.json`. The source's reported v1_11 F40 results are retained explicitly as unexecuted until their missing dependency is supplied. No background agents, new framework derivations, PDF compilation, or edits to original paper were performed.
- **DAG integration:** the final atlas adds a namespaced linked Paper7D audit layer with source-located claim, assumption-alias, issue, evidence and typed proof-route records; canonical graph status/proof flags outside the target are not bulk-modified. Each active issue's verified paths are separate from possible/unconfirmed impacts. Version and archive integrity are certified in the ZIP release manifest.

**Final verdict:** `FULLY_AUDITED_WITH_OPEN_GAPS`. This is a complete scoped audit of the paper's printed proof chain, not a certification that all physical hypotheses or numerical spectra have been realized. All 13 issue IDs remain traceable and available for a separate repair request, which this verification protocol itself prohibits.

---

## Current-source issue-specific repair addendum — 18 November 2026 (batch 3)

**Current source:** `Paper7D-TechnicalMaterial-v1_57.tex`; **SHA256:** `e498081e1914dd1b037e22c520c8353b59776bfa50958a5909132597a7391015`. Original audit history retained above, not erased. This addendum supersedes the named defects only at the corrected theorem-statement scope, never an unconditional global E3/E4/physical statement.

### BH-VIID-G-0001 — `p10:prop:v2159-holonomy-cotangent-firewall`

- **Effective status:** `SOURCE_TYPE_DEFECT_CLOSED__NO_PHYSICAL_SOURCE_PROMOTION`.
- **Exact source:** `Paper7D-TechnicalMaterial-v1_57.tex:276`, SHA above.
- **Original defect:** A general cotangent pullback is over the fiber product A_x G^E T*G^E, not a globally defined map T*G^E -> T*A without selecting x above the basepoint. Negative conclusion about forward symplectic descent remains supported.
- **Correction:** Typed cotangent pullback over X ×_Y T*Y; gave exact connection-relative holonomy variation; kept no-forward-descent conclusion.
- **Retained owner / limit:** No full continuum symplectic descent is inferred.
- **Local evidence:** `Paper00-MathematicalRepairBatch3Verification-v1_1.json` (26 bounded checks overall). No complete replacement proof-chain audit or new global theorem certificate asserted.

### BH-VIID-G-0008 — `p12:lem:tier2-asymptotic-locality`

- **Effective status:** `SOURCE_CLAIM_CORRECTED__PHYSICAL_OWNER_OR_GLOBAL_AUDIT_PENDING`.
- **Exact source:** `Paper7D-TechnicalMaterial-v1_57.tex:4107`, SHA above.
- **Original defect:** Identify the actual finite operator/source constructors and prove a uniform bound of ||[A_L(f),B_L(g)]||_omega by the overlap of their retained support kernels, with parity/constraint and support constants; or state it as an explicit branch guard.
- **Correction:** Corrected locality to a norm inequality with explicit self-adjoint operator windows, uniform norm constants and a separate operator-overlap estimate.
- **Retained owner / limit:** Uniform overlap for action-owned constrained local operators not proved by scalar kernel pointwise decay.
- **Local evidence:** `Paper00-MathematicalRepairBatch3Verification-v1_1.json` (26 bounded checks overall). No complete replacement proof-chain audit or new global theorem certificate asserted.

### BH-VIID-G-0009 — `p12:prop:rg-not-new-input`

- **Effective status:** `SOURCE_CLAIM_CORRECTED__PHYSICAL_OWNER_OR_GLOBAL_AUDIT_PENDING`.
- **Exact source:** `Paper7D-TechnicalMaterial-v1_57.tex:4152`, SHA above.
- **Original defect:** Distinguish bookkeeping for known action coordinates from uniqueness/inference of every finite running coupling solely through the QFT4 local expectation compatibility inequalities.
- **Correction:** Corrected bookkeeping/identifiability distinction and included exact H -> H+cI Gibbs-state nonidentifiability counterexample.
- **Retained owner / limit:** No universal action-coupling identifiability theorem without an injective fixed-scheme owner map.
- **Local evidence:** `Paper00-MathematicalRepairBatch3Verification-v1_1.json` (26 bounded checks overall). No complete replacement proof-chain audit or new global theorem certificate asserted.

### BH-VIID-G-0010 — `p12:prop:executable-ccr-boundary-witness-numerics`

- **Effective status:** `SOURCE_CLAIM_CORRECTED__PHYSICAL_OWNER_OR_GLOBAL_AUDIT_PENDING`.
- **Exact source:** `Paper7D-TechnicalMaterial-v1_57.tex:5490`, SHA above.
- **Original defect:** Keep expectation-level CCR recovery separate from regular Weyl-state convergence, as already accomplished by the later theorem; source-level claim cross-references must not overpromote the weaker criterion.
- **Correction:** Corrected top-weight numerical table and proof to necessary one-commutator-expectation convergence, not sufficient full regular Weyl recovery.
- **Retained owner / limit:** Regular Weyl-state and moment/domain convergence remain separate.
- **Local evidence:** `Paper00-MathematicalRepairBatch3Verification-v1_1.json` (26 bounded checks overall). No complete replacement proof-chain audit or new global theorem certificate asserted.

### BH-VIID-G-0011 — `p12:prop:classical-subsystem`

- **Effective status:** `SOURCE_CLAIM_CORRECTED__PHYSICAL_OWNER_OR_GLOBAL_AUDIT_PENDING`.
- **Exact source:** `Paper7D-TechnicalMaterial-v1_57.tex:5174`, SHA above.
- **Original defect:** Attach source-defined correspondence map, topology and commutator/Poisson convergence as the guard for the classical-mechanics part, rather than inferring it from commutativity alone.
- **Correction:** Added quantization family, topology, ħ scaling, product/Poisson commutator and Hamiltonian evolution comparison requirements.
- **Retained owner / limit:** The actual source-defined correspondence and physical classical limit remain conditional.
- **Local evidence:** `Paper00-MathematicalRepairBatch3Verification-v1_1.json` (26 bounded checks overall). No complete replacement proof-chain audit or new global theorem certificate asserted.

**Additional implementation:** Synchronizes `\BHExternalRefs{Paper7A-QCDKernel-v1_177}` and `Macros-v2_185.tex` with the latest current-source registry; old Macros v2.180 imported stale AUX references.


---

## Current evidence-integrity addendum — 18 Nov 2026 (batch 4)

VII-D new source `Paper7D-TechnicalMaterial-v1_58.tex`, SHA256 `7ce476abc4a46cd99469462e8b97cca31e821a1f97a1d4a0b81a735a47725458`. Named original issues `BH-VIID-G-0002`, `BH-VIID-G-0003`, `BH-VIID-G-0005` were **not** fully numerically replayed. The theorem and form-factor claims are now conditional on missing exact witness arrays, checkers or incidence operator, respectively. See `Paper00-EvidenceIntegrityBatch4-v1_1.md` and issue-level v1.6 crosswalk. All earlier audit history retained.

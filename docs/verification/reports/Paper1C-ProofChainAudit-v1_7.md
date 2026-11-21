# Paper I-C — Contact and energy normalization proof repairs (audit addendum v1_7)

**Current source:** `Paper1C-M8Geometry-v1_142.tex` (Paper00-PapersMinimal-v3_021). **Prior audit:** v1_6 source-frozen v1_140; retained below. **Current resolution layer:** `DAG/AuditLayer/Paper1Resolution-v1_1/Index.json`.

**BH-IC-139-OR-0001 — RESOLVED BY CORRECT MATHEMATICAL SIGN AND PROOF.** In `p1b:thm:g17-contact`, under fibre-first orientation, residual fibre inversion sends `η→−η`, `F→−F`, `c1→−c1`, **and reverses the total-space orientation**. Hence `∫_{-T}(−η)∧(d(−η))² = ∫_T η∧(dη)²`, and `c1²` is unchanged. The previous assertion that the normalized characteristic integral changes sign under a *consistent* reorientation was incorrect. The source theorem and its proof now state the correct invariant. Holding total-space orientation fixed is a different convention and does produce sign reversal of the raw form integral.

**BH-IC-139-NM-0002 — RESOLVED BY METRIC-NORMALIZED ENERGY IDENTITY.** In `p1b:thm:v2217-nonconstant-cartan-dirac`, the dimensionless derivative is now displayed as `R²|∇^{g_R}u|²`, equivalently `|∇^{g_1}u|²`. For `h=q1²−1/4`, `R²⟨|∇^{g_R}h|²⟩=8⟨h²⟩=1/2` and the quadratic coefficient is `1/12−1/32=5/96`. This repairs the radius ambiguity and supplies the missing derivative proof; other polynomial coefficients are checked independently.

`Paper1C-ContactEnergyExactChecks-v1_1.py` supplies **109 independent exact assertions (PASS)**, including full rational `S³` coordinate moments, the energy/CS coefficients, contact criterion and all 49 integer orientation cases with `(a,b)∈{−3,…,3}²`.

**Still open:** the eleven prior inherited evidence/global topology obligations remain guarded, along with other I-D original-data and global certificates. These source corrections do not certify the unrelated Dirac perturbation coefficient, every global bundle classification, or any physical occurrence theorem. No full fresh I-C audit of CC20 is claimed.

---

## Frozen prior audit for provenance (v1_6)

# Paper I-C — Proof-chain audit v1_6 (current source v1_140)

**Current authoritative manuscript:** `Paper1C-M8Geometry-v1_140.tex` · SHA256 `b26b32973091d56b3ae87321f598245fca17850c35718c36627a70cc033143ed` (PapersMinimal v3_019).
**Protocol:** RigorousVerificationDAGWorkProtocol v2_4 and ProofChainAuditProtocol v1_1.
**Updated DAG:** Paper00-DAGAtlas-v1_156 · **Audit collection:** Paper00-ProofChainAudits-v1_69.

## Current source review and grading

**506/506 current formal source objects source-bound audited**, including all named formal statements, formal remarks and the CC14–CC18 inserted comparison sections. First 490 source statements and adjacent proof bodies match the earlier frozen audit; first 505 match v1_139 exactly. The newly added 506th tomography proposition was read and boundedly independently checked. None of these text matches is a mathematical E3 proof in itself.

Historical grades of original 490 statements retained. New 16 source objects graded at E1-only (and E3-bounded where listed), **no unconditional proof status promotion**. Current census grade counts: **{'FORMALIZED': 55, 'REPRODUCED': 163, 'VERIFIED': 214, 'VERIFIED-CONDITIONAL': 74}**. Batched E3 scoped controls: Batch1=10, Batch2=30, Batch3=250, Batch4=177, a total of **467 bounded checks**, not 467 complete independent theorem proofs. Complete source proof obligations and conditions are recorded in DAG AuditLayer `Paper1C-M8Geometry-v1_3`.

## Open issue registry (all identifiers)

- **BH-IB-EV-0001** (verification evidence only; MISSING_INDEPENDENT_PROOF_EVIDENCE): p1b:thm:g15-unstable ([1527, 1549]); p1b:thm:g20-rank2-existence ([1638, 1652]); p1b:thm:g20-rank3-existence ([1771, 1787]); p1b:thm:g20-rank3-fibre ([1800, 1833]). Reconstruct the source-specific obstruction/desuspension and fixed-rank bundle existence implications independently, including the adopted Čadek–Crabb–Vanžura and Yang hypotheses. The I-C appendices give a substantive source proof; current finite Chern and Smith tests are narrower.
- **BH-IB-EV-0002** (verification evidence only; MISSING_INDEPENDENT_PROOF_EVIDENCE): p1b:thm:g20-rank2-fibre-even ([1670, 1736]); p1b:thm:v2170-ordinary-counts ([2097, 2124]); p1b:thm:v2170-ordinary-born ([2180, 2201]). Independently reconstruct the full level-12 mapping-component group, its affine determinant-unframing action on all relative filling torsors, and every claimed orbit count. The exact finite F2 shear and zero-Chern checks confirm only specified components.
- **BH-IB-EV-0003** (verification evidence only; MISSING_INDEPENDENT_PROOF_EVIDENCE): p1b:thm:g21-born-fixed-count ([2301, 2338]); p1b:thm:g21-index-obstruction ([2363, 2387]); p1b:thm:g21-exotic-lift ([2506, 2519]); p1b:thm:g21-exotic-nogo ([2533, 2538]); p1b:thm:g21-principal-descent ([2589, 2624]). Independently verify the equivariant Hopf target representation/underlying class and the coarse symmetric-square no-go; recheck the Dirac Lefschetz fixed-point application and the full principal descent classification. Arithmetic congruence checks are not the complete equivariant proof.
- **BH-IB-EV-0004** (verification evidence only; MISSING_INDEPENDENT_PROOF_EVIDENCE): p1b:prop:v2170-mixed-gluing ([3004, 3020]); p1b:lem:v2170-w-cohomology ([3046, 3081]); p1b:thm:v2170-mixed-quotient ([3258, 3283]); p1b:thm:complete-mixed-rank-two ([4069, 4131]). Independent equivariant Thom/Cartan–Leray calculation for W; actual global determinant-one/odd-winding gauge realizations and normalized boundary restrictions; independent source-specific I-C natural joining carry and torsor/forgetful orbit proofs.
- **BH-IB-EV-0005** (verification evidence only; MISSING_INDEPENDENT_PROOF_EVIDENCE): p1b:thm:v273-triple-icosahedral-nineteen-design ([5009, 5022]); p1b:thm:v274-branch-symmetric-twin-convolution ([5086, 5128]). Exact Vandermonde signed support, F12/F20 gcd, unique real F12 root in allowed interval, conditional two-projector eigenvalues and norm constants; exact peer theorem and dense-generation proof source labels were located.
- **BH-IB-EV-0006** (verification evidence only; MISSING_INDEPENDENT_PROOF_EVIDENCE): p1b:thm:g22-global-complex ([7028, 7051]); p1b:thm:g16-model ([7219, 7247]); p1b:thm:g14-generalized ([7151, 7178]). Complex-structure parameter dimensions, two model Dolbeault Hodge polynomials and Frölicher E1→E2 ranks in an exact prime-field specialization, Bismut period normalization; both I-C controlling appendix anchors located.
- **BH-IB-EV-0007** (verification evidence only; MISSING_INDEPENDENT_PROOF_EVIDENCE): p1b:thm:v214-full-skt-locus ([7415, 7442]); p1b:cor:v214-canonical-kodaira ([7487, 7503]). The exact rank-one and rank-two ddbar algebra, positivity-condition reduction, and negative O(-2m,-2m) section count agree; complete compact holomorphic averaging and the global classification remain source-dependent.
- **BH-IB-EV-0008** (verification evidence only; MISSING_INDEPENDENT_PROOF_EVIDENCE): p1b:thm:all-level-sampling ([9083, 9118]). Paper I-C gives an explicit T_{a,b} coisometry plus Schur orthogonality and compact convex-hull argument; independent combinatorial rank, degree-frontier, graph and tensor controls pass, but a full globally implemented bundle evaluation was not rerun for arbitrary m.
- **BH-IB-EV-0009** (verification evidence only; MISSING_INDEPENDENT_PROOF_EVIDENCE): p1b:prop:g08-product ([13357, 13378]). Explicit 16-spinor Cl8 model, 112 gamma-traceless fibre, squared-symbol speeds 1 (96) and 9/16 (16), rank-35 trace-free symmetric fibre, and selected full Dirac multiplicity arithmetic.
- **BH-IB-EV-0010** (verification evidence only; MISSING_INDEPENDENT_PROOF_EVIDENCE): p1b:prop:g10-product ([14530, 14552]). Reynolds projection for a faithful finite unitary model, Riemann–Hurwitz total ramification of a degree-12 map, 144 product degree, 288 Chern square, and 2T/2O/2I branch-order consistency.
- **BH-IB-EV-0011** (minor; MISSING_EVIDENCE): None (None). Independently derive and convention-match the native midpoint covariant derivative, curvature Weitzenboeck Hessian, and positive ghost/gauge projection to the complete quotient spectral operator; preserve the actual compact gauge slice and normalization.
- **BH-IC-139-OR-0001** (minor; NORMALIZATION_OR_READOUT): p1b:thm:g17-contact (1094). State which normalized fibre orientation and integration convention changes when residual fibre orientation reverses; Chern square and compatible fibre-first contact integral stay unchanged.
- **BH-IC-139-NM-0002** (minor; NORMALIZATION_OR_READOUT): p1b:thm:v2217-nonconstant-cartan-dirac (16573). Identify the unit-sphere metric used by the proof in the displayed gradient energy on S^3_R, or insert the equivalent R² factor if expressing gradients using g_R.

The **11 inherited E3/E4 obligations** are independent-proof/evidence limits rather than confirmed mathematical refutations. **2 minor current-source ambiguities** are orientation wording and radius-gradient normalization. The new tomography statement, 720-dimensional evaluation, and the 600-chamber kernel comparisons passed bounded controls; no new mathematical counterexample was demonstrated. Physical carrier/observable identities remain typed and conditional as in source.

## Final audit classification and artifact integrity

`FULLY_AUDITED_WITH_OPEN_GAPS`: all 506 source formal statements have an identified source and evidence status, while precise global independent proof tasks remain. Canonical graph theorem/assumption identities and inherited statuses are preserved. Current Paper1C audit layer: `DAG/AuditLayer/Paper1C-M8Geometry-v1_3/Index.json`; source archive `Sources-v3_019/` unmodified; only latest Paper1C audit report is present in ProofChainAudits v1_69.

---

## Historical report v1_5, retained as embedded provenance, NOT an active v1_5 file

# Paper1C — CC18 current-source scope rebase (Paper1C-ProofChainAudit-v1_5.md)

**Latest source:** `Paper1C-M8Geometry-v1_140.tex`; SHA-256 `b26b32973091d56b3ae87321f598245fca17850c35718c36627a70cc033143ed`.  **Framework release:** `Paper00-PapersMinimal-v3_019.zip` based on v3.018.  **DAG release:** `Paper00-DAGAtlas-v1_155.zip` based on v1.154.  **Audit collection:** `Paper00-ProofChainAudits-v1_68.zip` based on v1.67.

**Scope and grade:** `SOURCE_INTEGRATED_LOCAL_MATH_CHECKS / NEW_CLAIMS_NOT_FULLY_AUDITED`.  The historical audit below remains valid only for the original source body and the exact original manuscript version it names.  The added CC18 proof statements have formal source labels, precise dependency owners and reproducible finite/exact checks, but **not a fresh exhaustive E3/E4 audit for this entire revised paper**.  No old issue, open physical obligation, or conditional status is silently closed.  No physical occurrence/observable was promoted.

New source-labelled mathematical result(s):
- `p1c:prop:cc18-720-tomography-bound` — source-integrated auxiliary comparison, no physical-owner certificate.

**Local evidence:** `DAG/SourceUpdates/DAGCrossConnections-v1_9/` contains the independent exact-cubature, exact-block, independent facet-geometry and independent nonet reconstruction scripts from supplement v1.9; the release manifest records their replay status and the exact updated source anchors.  The predecessor audit, source text before the appended CC18 block, and all predecessor issue ledgers are preserved as provenance; source hash changed and must not be mistaken for E0 equality to the old manuscript.

---

## Historical audit retained verbatim (not current-version re-certification)

# Paper I-C — Proof-chain audit and integrated independent-evidence update — v1_4

**Source currently registered:** `Paper1C-M8Geometry-v1_138.tex` · SHA-256 `d953a7b07bec0909ee4d8396e5a727de4ab6367d50a56078baec123a8f63ff33`.
**Controlling technical appendix:** `Paper1D-TechnicalMaterial-v1_66.tex` · SHA-256 `653482c0e4aa3013c015573a50d0350f136c5ef62da31bfd6c536daafcd9d020`.
**Framework archive:** `Paper00-PapersMinimal-v3_013.zip`. **DAG archive:** `Paper00-DAGAtlas-v1_138.zip`.
**Verification protocol:** `Paper00-RigorousVerificationDAGWorkProtocol-v2_4.md`; `Paper00-ProofChainAuditProtocol-v1_1.md`.

## Current disposition, 2026-11-15

The source-integrated supplement adds independent derivation evidence for the **same 490 formal statements**, not new claimed theorems. All prior theorem labels, quantified statements and original proof bodies are preserved. This is a **source/evidence rebase**, not a new 490-statement independent re-audit. The prior 490/490 statement audit from `v1_3` remains the frozen historical baseline and is reproduced below.

| Evidence status | Canonical issue roots | Count |
|---|---|---:|
| Candidate full independent certificates; adjudication pending | `BH-IB-EV-0005`, `BH-IB-EV-0007`, `BH-IB-EV-0008`, `BH-IB-EV-0011` | 4 |
| Partial independent derivations; explicit global steps remain | `BH-IB-EV-0001`, `BH-IB-EV-0002`, `BH-IB-EV-0003`, `BH-IB-EV-0004`, `BH-IB-EV-0006`, `BH-IB-EV-0009`, `BH-IB-EV-0010` | 7 |
| Established mathematical counterexamples from this update | — | 0 |

**Rechecks:** All five independently supplied verification scripts executed successfully in this update. They test exact icosahedral character moments, quotient/Morse low-spin algebra, mapping and boundary finite quotients, TT heat coefficients, and the physical gamma-traceless constant-orbital Rarita operator. They do not establish the missing global gauge or orbit classifications. Specifically, the ambient 16-dimensional projected Rarita kernel is *not* a physical 112-dimensional gamma-traceless zero mode.

**Open proof boundaries:** EV-0001 rank-two/fixed-Chern classification; EV-0002 full affine unframing; EV-0003 fixed-class/principal equivariant orbit enumeration; EV-0004 global gauge-image realization and relative spectral sequence; EV-0006 full global normal-form and twisted bracket; EV-0009 all-orbital constrained Rarita spectrum; EV-0010 correlated/nonfree stabilizer strata. The four candidate obligations remain open until a complete source-and-convention adjudication is performed.

**DAG action:** The canonical issues are source-rebased to `Paper1C-M8Geometry-v1_138.tex` and supplemented with reproducible evidence and scoped status fields. **No theorem proof status is promoted and no issue is deleted.** The historical theorem DAG and 490 existing statement hashes retain their identities. The release manifest and current audit-layer links refer to the updated archive versions.

---

## Frozen original four-batch audit record, v1_3 (provenance)

# Paper I-C — Consolidated rigorous proof-chain audit — v1_3

**Authoritative current manuscript:** `Paper1C-M8Geometry-v1_137.tex` (source archive `Paper00-PapersMinimal-v3_012.zip`)  
**Source SHA-256:** `c09f2f8b49860114e0eb840c5414528efd16ff588e2e99f6d48aa03cb529b029`  
**Current Atlas:** `Paper00-DAGAtlas-v1_137.zip`  
**Audit result:** `FULLY_AUDITED_WITH_OPEN_GAPS` — **490 / 490 formal-source objects reviewed; 11 open independent-proof E3/E4 evidence obligations; 0 established source-matched mathematical refutations**.

This replaces the migration-only `Paper1C-ProofChainAudit-v1_2.md`. Previous Paper I-B M8Geometry and Paper I-C TechnicalMaterial audit records are **historical provenance**; the current Paper I-C mathematical contents were source-rescoped in four current-source audit batches. **No modification to the TeX paper** occurred. Proof status never upgrades merely because a control script passes.

# Paper I-C — Rigorous verification, Batch 4 (final), v1_1

**Source:** `Paper1C-M8Geometry-v1_137.tex` · SHA-256 `c09f2f8b49860114e0eb840c5414528efd16ff588e2e99f6d48aa03cb529b029` · source release `Paper00-PapersMinimal-v3_012`  
**Protocol:** `Paper00-RigorousVerificationDAGWorkProtocol-v2_4` and proof-chain audit protocol.  
**Scope:** formal objects **375–490** inclusive (zero-based indices 374–489); **116 / 116** source-bound objects.  
**Classification:** `FULLY_AUDITED_WITH_OPEN_GAPS` as formal-object dispositions; **NOT** independent end-to-end proof certification for every global assertion.

## Summary and exact scope

- **109 historical** statements rebound to exact current TeX, **7 newly inserted** statements individually classified, **zero missing** objects, **101** adjacent formal proof environments for this slice; a missing adjacent proof is not automatically an error for definitions and remarks or for material proved in adjacent section text.
- **284/284 new scope-limited checks passed:** 272 restricted exact algebraic controls, six finite numerical/spectral controls, six E0 source/scope/domain checks. **36 distinct statements** directly targeted by new mathematical checks; the remaining statements were source-adjudicated and carry specifically marked earlier provenance, not newly proved from scratch.
- **2,916 / 2,916 historical checks rerun**, in three separate independent-control suites (batches 8, 9, 10 from the predecessor manuscript). These are *reruns* on earlier inputs, **not** 2,916 new source-version mathematical certifications.
- **46** previously reviewed material edges with targets in this batch rebound to current current source, of which eight are mathematically semantic rather than literal reference edges. **Five new** source-witnessed material edges for the newly inserted statements; others are not invented merely because they have cross-references.
- **69** distinct literal source reference labels resolve across the current 31-paper corpus. **One** inherited formal statement and **two** proof bodies change paper *ownership / appendix-pointer wording only*. No changed mathematical formula or quantifier was detected in those three historical matches.
- **No exact in-domain counterexample established.** Eleven previously open evidence obligations remain open; they are *not* proven false statements. No new axiom, paper edit, geometry, particle identity, or physical readout was introduced.

## New source formal claims (seven)

| Current index | Label | Source lines | Disposition | Verified boundary |
|---:|---|---|---|---|
| 448 | `p1:thm:v188-exceptional-defect-residues` | 23613–23634 | REPRODUCED | Derived-subgroup and exceptional quotient arithmetic; no new carrier states |
| 449 | `p1:cor:v188-trimer-as-2t-abelianization` | 23645–23661 | REPRODUCED | 2T/Q8 C₃ quotient / oriented trimer |
| 450 | `p1:cor:v188-square-pairs-2t-orientations` | 23670–23680 | REPRODUCED | Square operation on C₃ quotient; not a group homomorphism on 2T |
| 451 | `p1:cor:v188-unique-exceptional-sign-residue` | 23690–23703 | REPRODUCED | Real sign characters of exceptional groups; no particle identification |
| 452 | `p1:rem:v188-operation-carrier-firewall` | 23711–23719 | FORMALIZED | Operation vs carrier explicitly distinguished |
| 453 | `p1:thm:v357-normal-jet-exact` | 23723–23752 | REPRODUCED | Exact formal normal-jet sequence for declared splitting, tested on polynomial comparison models |
| 454 | `p1:rem:v357-normal-jet-scope` | 23767–23776 | FORMALIZED | Normal-jet result does not imply physical action or gauge dynamics |

### Nontrivial mathematical controls

The 120-element binary icosahedral group is generated and multiplied with exact algebraic (golden-ratio) arithmetic; derived subgroup, abelianization and unique real-sign character claims are cross-checked with independently constructed 2T and 2O. Normal-jet exactness is tested on 20 polynomial/matrix instances, explicitly separating an additive comparison of jets from multiplicative constructions. Further finite exact tests cover F₇ quotient arithmetic, weighted residues, noncommuting resolvent compressions, 81 matrix-unit coefficients, balanced finite odd heat, and Born-exchange selection.

These checks verify the **stated algebraic identities in their tested domain**. They do not prove global theorem hypotheses or select a physical measure or field dynamics. Source proof locations and their cryptographic hashes are in `Paper1C-RigorousVerificationBatch4Evidence-v1_1.json`.

## All unresolved independent-verification issue roots

No issue ID is duplicated for a new source occurrence. Eleven historical issue identities are preserved as *evidence-only* obligations at their earliest established source origins:

| Issue | Exact remaining independent-proof obligation | Current origin excerpts |
|---|---|---|
| `BH-IB-EV-0001` | Reconstruct the source-specific obstruction/desuspension and fixed-rank bundle existence implications independently, including the adopted Čadek–Crabb–Vanžura and Yang hypotheses. The I-C appendices give a substantive source proof; current finite Chern and Smith tests are narrower. | `p1b:thm:g15-unstable` L1521, `p1b:thm:g20-rank2-existence` L1632 |
| `BH-IB-EV-0002` | Independently reconstruct the full level-12 mapping-component group, its affine determinant-unframing action on all relative filling torsors, and every claimed orbit count. The exact finite F2 shear and zero-Chern checks confirm only specified components. | `p1b:thm:g20-rank2-fibre-even` L1664, `p1b:thm:v2170-ordinary-counts` L2091 |
| `BH-IB-EV-0003` | Independently verify the equivariant Hopf target representation/underlying class and the coarse symmetric-square no-go; recheck the Dirac Lefschetz fixed-point application and the full principal descent classification. Arithmetic congruence checks are not the complete equivariant proof. | `p1b:thm:g21-born-fixed-count` L2295, `p1b:thm:g21-index-obstruction` L2357 |
| `BH-IB-EV-0004` | Independent equivariant Thom/Cartan–Leray calculation for W; actual global determinant-one/odd-winding gauge realizations and normalized boundary restrictions; independent source-specific I-C natural joining carry and torsor/forgetful orbit proofs. | `p1b:prop:v2170-mixed-gluing` L2998, `p1b:lem:v2170-w-cohomology` L3040 |
| `BH-IB-EV-0005` | Reconstruct the full degree-12 and degree-20 binary-icosahedral character overlaps and exact sibling Reynolds-projector geometry directly from fixed source coordinates, independently of the polynomial identities and the imported Paper II-F calculation. Confirm spectral multiplicities and source-specific dense-generation hypothesis. | `p1b:thm:v273-triple-icosahedral-nineteen-design` L5003, `p1b:thm:v274-branch-symmetric-twin-convolution` L5080 |
| `BH-IB-EV-0006` | Independently match the full Magnin normal-form hypotheses to u(2)⊕u(2), verify the global Fourier-character Dolbeault contraction and filtered quasi-isomorphism in I-C, and reconstruct the H-twisted generalized Kähler bracket integrability with exact convention. | `p1b:thm:g22-global-complex` L7022, `p1b:thm:g16-model` L7213 |
| `BH-IB-EV-0007` | Independently verify for every global invariant-complex-structure normal form the holomorphic left/right compact action required for SKT metric averaging, and the global holomorphic relative torus-tangent frame/connected-fibre descent used in the canonical-bundle claim. | `p1b:thm:v214-full-skt-locus` L7409, `p1b:cor:v214-canonical-kodaira` L7481 |
| `BH-IB-EV-0008` | Independently reconstruct the all-m homogeneous Spin(4)/SU(2)_diag section-model isometry and its polynomial degree bound for every retained U_{a,b}, and confirm the positive quadrature transports each specified finite coefficient function without identifying untransported operators. | `p1b:thm:all-level-sampling` L9077 |
| `BH-IB-EV-0009` | Independently reproduce the full global constrained transverse-traceless and Rarita–Schwinger eigenspaces/multiplicities, their domain restrictions and resulting product heat/zeta coefficients, rather than only the gamma-projected principal symbol and finite Dirac labels. | `p1b:prop:g08-product` L13351 |
| `BH-IB-EV-0010` | Independently verify the global finite quotient kernel normalization, selected free/nonfree quotient stabilizer cases, and the source-specific degree-twelve reference pencil ramification/branch-locus geometry beyond the general Riemann–Hurwitz and Chern-class calculations. | `p1b:prop:g10-product` L14524 |
| `BH-IB-EV-0011` | Independently derive and convention-match the native midpoint covariant derivative, curvature Weitzenboeck Hessian, and positive ghost/gauge projection to the complete quotient spectral operator; preserve the actual compact gauge slice and normalization. |  |

## Registration repair and graph status

`BH-IC-DAG-0001`: The predecessor `Paper1B-M8Geometry` historical audit and `Paper1C-TechnicalMaterial` historical audit have been treated as predecessor provenance, not as the **current** Paper I-C / I-D owners. In the successor Atlas, the authoritative new `Paper1C-M8Geometry-v1_1` audit layer names `Paper1C-M8Geometry-v1_137.tex`, preserving the older layers as historical traceability. This is **RESOLVED in the final archive**, not a mathematical failure. The inherited `p1b:` labels remain canonical; they are not renamed, since labels are identities independent of the paper filename. A small set of assertions already present in Paper I-B / I-A is linked as additional occurrences rather than given duplicate foundational owners.

**Registration limitations:** The current source has seven added formal objects compared with the 483-statement historical paper, but four of the group-theoretic labels also occur at their prior source-owner; do not create duplicate graph nodes. Two truly new normal-jet labels require new global claim nodes. Source-normalized matching alone does not independently prove the global spectral assertions; the eleven issue roots remain open.

## Complete four-batch census

| Batch | Claims | New passing controls | Source-review position |
|---|---:|---:|---|
| 1 | 126 | 24 | Reciprocal topology, bundle, Born exchange and initial finite sampling |
| 2 | 124 | 84 | Finite representations, complex and spectral geometry |
| 3 | 124 | 174 | Morse, response, torsion/Dirac and singular spectral construction |
| 4 | 116 | 284 | Exceptional algebra, normal-jet, boundary response and positive sources |
| **Total** | **490** | **566** | **490/490 dispositions, 11 unresolved independent-proof roots** |

Full-source statuses comprise **214 VERIFIED, 74 VERIFIED-CONDITIONAL, 152 REPRODUCED, 50 FORMALIZED**. 483 inherited statuses are historical dispositions with explicit source reconciliation, not new certification. Of 490 statements, 419 have an immediately associated formal proof, while 420 proof environments are present; remaining definitions, remarks and section derivations receive source-specific classification rather than automated failure.

**Evidence grading:** E0 anchors/hashes/label check are administrative, E1 replay means source-same argument, E2 a bounded numerical attack, E3 exact independent calculation in a restricted domain; no E4 externally independent global proof for all open roots has been obtained. No separate parallel agents took part in this session.

## Outputs and provenance

- `Paper1C-RigorousVerificationBatch4Evidence-v1_1.json`: 116 source-linked formal objects, exact source proof texts, labels, hashes, changed wording, reviewed edge witnesses, and E0/E1/E2/E3 provenance.
- `Paper1C-IndependentControlsBatch4-v1_1.py` + `...Batch4Results-v1_1.json`: the direct reproducibility of all new restricted controls.
- `Paper1C-ProofChainAudit-v1_3.md`: current-source consolidated replacement for the formerly migration-only v1_2 report, with all 11 issue IDs and complete four-batch evidence lineage.
- Final Atlas and ProofChainAudits versions increment **once**: `Paper00-DAGAtlas-v1_137.zip` and `Paper00-ProofChainAudits-v1_53.zip`. Sources remain byte-unchanged and historical audit layers retain their own provenance.


# Source migration and repair-integration addendum — Paper3B-ProofChainAudit-v1_5.md

**Integration release:** `Paper00-PapersMinimal-v3_007.zip`, 14 November 2026.
**Current paper source:** `Paper3B-SpectralAction-v1_187.tex`.
**Status:** `SOURCE_INTEGRATED; GLOBAL_SOURCE_REAUDIT_PENDING`. An inherited historical audit is not a correctness certificate for the newer current manuscript.
**Evidence policy:** Local algebraic proofs and scoped tests do not discharge physical source/observable interfaces or automatically alter the canonical proof DAG.

---

## Historical source-bound audit: Paper3B-ProofChainAudit-v1_4.md
# Born–Hopf Geometry III-B — Final rigorous source audit (Batch 4, cumulative)

**Report:** `Paper3B-ProofChainAudit-v1_4.md`  
**Target:** `Paper3B-SpectralAction-v1_181.tex` (6,144 lines; SHA-256 `ac97a9c5aea0dc3d2716edd61a7f0058128403147cbbae08d2b9dd754ba48913`).  
**Sources:** original `Paper00-PapersMinimal-v2_370` corpus, matched exact source in `Paper00-DAGAtlas-v1_99`; bounded imported passages from Papers I-B, II-A–D, III-A, III-C, III-E, III-F, III-G.  
**Protocol:** `Paper00-RigorousVerificationDAGWorkProtocol-v2_4.md` (no repairs, no modifications of sources, no physical predictions).  
**Batch 4:** lines 4,765–6,144, **46/46** remaining formal declarations, **22/22** source proof environments, **13** independent/adversarial control groups passing within explicitly stated mathematical domains.  
**Cumulative:** **179/179** formal declarations and **81/81** proof environments reviewed; **0 unreviewed formal claims**.  
**Disposition:** `FULLY_AUDITED_WITH_OPEN_GAPS` (complete source coverage, not unconditional verification of every hypothesis/realization).  
**Source mutation:** none. PDFs not generated or recertified. Functional checks were separate passes in one execution, not independently staffed Work agents.

## Final disposition by evidence status

| Status | Claims |
|---|---:|
| VERIFIED | 40 |
| VERIFIED-CONDITIONAL | 56 |
| REPRODUCED (further independent verification needed) | 4 |
| UNRESOLVED | 5 |
| FORMALIZED/REGISTERED (definitions and qualified formal remarks) | 74 |
| **Total** | **179** |

These **claim statuses are not issue counts**. A conditional theorem may be mathematically correct; an open physical-occurrence certificate is not an algebraic counterexample. Inherited source-scope issue `BH-IIIA-G-0001` and newly located III-B issues `BH-IIIB-G-0001`, `BH-IIIB-G-0002` remain open. No new distinct issue was established in Batch 4. The counted UNRESOLVED claims are individually listed in the machine-readable ledger; not all are new root defects.

## Batch 4 source-level checks (lines 4,765–6,144)

**Clifford projection, 4781–5297.** Exact real Cl(0,3) regular left-multiplication matrices give `Tr_R(L_a)=8<a>_0`; the scalar rank-one projector `P0` has ambient real normalization `tau8(P0)=1/8`. The physical four-complex-dimensional module has normalized trace `Tr_C/4`, with one-complex-rank projector weight `1/4`. The two readouts agree on represented Clifford *scalar extraction* through the explicit pair of chiral simple ideals, not on arbitrary projectors. `CORN` physical scalar contribution is theorem-conditional on a pre-generated, G0-occurring constituent presentation and ambient non-renormalized readout. The Chevalley `SO(3)` invariant subspace is dimension two (`1`, pseudoscalar); full `O(3)` invariants are scalar only. The *unique map* is proved locally; physical terminal occurrence is a later III-C import, not a manufactured III-B event.

**Directed heat and bare metric branch, 5331–5538.** Fixed-time spectral exhaustion uses positive trace-class monotone convergence. If `t_m mu_m / |log t_m|→∞`, the omitted tail is `o(t_m^N)` for every fixed `N`; fixed finite matrices do not inherit continuum small-`t` coefficients. The physical momentum seed remains `m_p=1`. The admitted four-dimensional Euclidean Dirac branch with pure metric rank `4×48×(1/8)=24` yields exactly the stated local volume and Einstein coefficients: `24 Λg^4 − 2 Λg² R_E` in common `(16π²)^(-1)` heat units, `κ_J=Λg²/(8π²)=12U`, `V0,J/κ_J=12Λg²`. The full source, metric, clock, and Lorentz realization guards remain distinct.

**Coordinate/centre and quadratic transport, 5543–5784.** A commuting zero-order Dirac perturbation leaves `[D,f]` unchanged but changes `D²`; a central offset in a block-reducing Hamiltonian preserves even commutator dynamics and changes raw heat traces. The generated SU(2) diagonal graph projection is orientation-preserving and does not exchange the two Spin(4) simple factors. A noncentral SU(2) relative element determines a maximal-torus axis only on its occurrence-conditioned branch. The quadratic Cliffordization exact sequence has dimensions `16=9+7`, with a true trace-matched fibre product. The sentence about no mixed contractions at 5682–5687 is interpreted under the **same stage guard** as open issue G-0001; it is not a new independent defect.

**Petersen and meron, 5867–6140.** Exact dodecahedral-axis enumeration gives `M2=10|v|²/3`, `M4=2|v|⁴`, `M6(u_a)=370/243`, `H6(u_a)=160/1701`; the sextic anisotropy is nonzero harmonic. The `A5` edge representation `4+5+3+3′` has a four-real-parameter self-adjoint commutant and no physically inserted spectral operator absent separate licensing. The round relative SU(2) Born meron has `λ=1/2`, CS `1/2` modulo integers, negative homogeneous YM Hessian, and central fundamental Wilson loop `−I₂`. The fixed fundamental twist matches the round spin connection. Exact Hodge harmonic counting gives its one zero mode, paired nonzero spectrum and square heat trace. Independently differentiating the meromorphic zeta continuation reproduces `ζ_B(0)=−1`, `ζ'_B(0)=−2log r+2log2−2ζ_R(3)/π²`, and `det'(D_B²)=r² exp(2ζ_R(3)/π²)/4`. These are test-bundle identities, not observed particle masses or proven physical gauge gaps.

## Every remaining issue (earliest root IDs; no duplicated downstream issues)

### 1. `BH-IIIA-G-0001` — inherited OPEN / moderate, conditional frontier

- **Earliest recorded root:** Paper III-A introductory momentum-carrier handoff, using Paper II-B `p2:thm:momentum-host-H1` (lines 1115–1166) and `p2b:thm:momentum-carrier-rigidity` (1439–1489). Paper III-B repeats the stronger identification at lines 85–89, 248–252, 554–568, 813–836 and its conclusion at 5794–5800.
- **Exact obligation:** distinguish established `m_p=1` and the six generated momentum types from universal physical whole-endpoint `H_p ≅ H_1`, which still requires the II-B structured comparison certificate (i)–(iii).
- **Impact:** conditional III-B statements using full physical carrier and multiplicity-sensitive finite traces; the group topology, quaternion algebra and exact finite mathematical calculations have no proved failure from this qualifier. The separate `m_p=1` proof is preserved.
- **Resolution requirement:** locate a source-valid whole-structured comparison discharge or retain explicit guard at uses. This audit does not change the upstream root status.

### 2. `BH-IIIB-G-0001` — OPEN / moderate, TYPE_OR_DOMAIN and MISSING_CONDITION

- **Earliest III-B origin:** `p3:thm:sectorwise_additivity`, lines **3039–3045**, proof **3071–3080**. The imported `p3:lem:no-invariant-mixed-vector-contraction` at 3010–3035 excludes independently transforming `Spin(4)_x×Spin(4)_p` *pre-diagonal* mixed vector slots.
- **Missing transition:** the same III-B target has a generated diagonal right Cartan connection at 1644–1723, while I-B/III-G contain a mixed global reciprocal 2-form under simultaneous right transformation. To exclude *all* mixed contractions of the completed action owner requires a source-matched stage/symmetry and constructor-exhaustion certificate. The later remark 5682–5687 retains the narrower firewall and does not discharge the stronger exhaustive conclusion.
- **Verified bypass:** direct-sum finite spectral-trace additivity is an independent valid action construction, lines 3081–3094; the issue does **not** refute its algebraic trace identity.
- **Direct impact:** `BH-IIIB-C-0076` (narrow lemma, valid at its independent-covariance scope) → `BH-IIIB-C-0077` (broad exhaustion unresolved) → `BH-IIIB-C-0078` (`p3:cor:no-boundary-to-position-transfer`, proof 3114–3120). `Paper III-F p3:thm:locality_selection` and Paper VI-A boundary-position interfaces are **POSSIBLY_AFFECTED**, with no certified blocked remote proof route.
- **Resolution requirement:** source-based assertion of the precise transformation/constructor stage for the whole action, or scoped use of the existing narrow theorem; no new mixed physical action is proposed.

### 3. `BH-IIIB-G-0002` — OPEN / moderate, MISSING_EVIDENCE / constructor-origin scope

- **Earliest III-B origin:** `p3b:thm:v173-joint-heat-process-corealization`, lines **3292–3340**, particularly physical role promotion at 3333–3338.
- **Missing transition:** the spectral theorem correctly derives `e^(-tD²)` mathematically from self-adjoint `D`. It does not itself locate the frozen II-A `Orig_Σ` output license for the **complete process family and scalar closed-trace/localized-trace sort**, including prior constructor word, pre-evaluation scope and non-obstructed FRC branch.
- **Verified bypass:** the separately conditional closed-loop route `p3:thm:gp2-dcl-derivation` (2210–2262) explicitly invokes a performed G0 closed process/FSR word, and the mathematical semigroup/direct-sum finite trace identities remain valid. Neither bypass proves automatic native output co-realization.
- **Direct impact:** `BH-IIIB-C-0088` → `BH-IIIB-C-0090` and native heat-`D1` role-level language; later III-E, IV and V interfaces are **POSSIBLY_AFFECTED** only, not globally re-audited or marked invalid.
- **Resolution requirement:** find an existing source-qualified frozen complete process+readout word and its FRC nonobstruction, or continue to state physical co-realization conditionally.

**Other tracked boundary challenges, not confirmed defects:** `BH-IIIB-CH-B1-001` relative Sigma constructor-license scope; prior `CH-B1-002`, `CH-B1-003` forward proofs checked in I-B/III-G; `CH-B2-002` raw trace versus normalized Born role weight checked as distinct; no false new issue IDs created for these reviews.

## Explicit scope of completeness

The exact target `.tex` is exhausted by the 179 formal claim ledger and 81 proof environments. Supplementary unlabelled proof-relevant source scopes and cross-paper imports are catalogued to their checked interface extent, not as whole peer-paper audits. The `FORMALIZED`, `REPRODUCED`, `UNRESOLVED`, and `VERIFIED-CONDITIONAL` dispositions remain evidence-sensitive and do not imply every statement was unconditionally independently proved. E3/E4 controls verify the identical supplied target mathematics or probe its hypothesis boundaries. There are no confirmed in-domain algebraic counterexamples in Batch 4. The final global DAG must preserve all prior core records, append the linked source-bound III-B audit layer, and make the two new gap origins, inherited root and branch-specific bypasses queryable. Source TeX/PDF and historical evidence are retained unchanged, with no theory repair.

## Batch 4 claim-by-claim disposition

| Audit ID | Source theorem / formal object | Source lines | Final disposition |
|---|---|---:|---|
| `BH-IIIB-C-0134` | `p3:lem:clifford_scalar_projection` | 4781–4792 | VERIFIED |
| `BH-IIIB-C-0135` | `p3:thm:normalized-protected-octet-trace` | 4806–4842 | VERIFIED-CONDITIONAL |
| `BH-IIIB-C-0136` | `p3:def:scalar-corner-readout` | 4863–4888 | FORMALIZED |
| `BH-IIIB-C-0137` | `p3:thm:derived-scalar-corner-readout` | 4890–4916 | VERIFIED-CONDITIONAL |
| `BH-IIIB-C-0138` | `p3b:cor:protected-split-corealization` | 4938–4956 | VERIFIED-CONDITIONAL |
| `BH-IIIB-C-0139` | `p3:prop:kinematic-sector-weight` | 4970–4985 | VERIFIED-CONDITIONAL |
| `BH-IIIB-C-0140` | `p3:def:octet-scalar-projection-weight` | 4997–5012 | FORMALIZED |
| `BH-IIIB-C-0141` | `p3:thm:octet-scalar-projection-rule` | 5014–5030 | VERIFIED-CONDITIONAL |
| `BH-IIIB-C-0142` | `(unlabelled)` | 5046–5058 | FORMALIZED |
| `BH-IIIB-C-0143` | `p3:thm:regular-module-two-eights` | 5060–5115 | VERIFIED-CONDITIONAL |
| `BH-IIIB-C-0144` | `(unlabelled)` | 5144–5149 | FORMALIZED |
| `BH-IIIB-C-0145` | `p3:rem:two-eights` | 5151–5162 | FORMALIZED |
| `BH-IIIB-C-0146` | `(unlabelled)` | 5165–5170 | FORMALIZED |
| `BH-IIIB-C-0147` | `p3:lem:o3-clifford-expectation` | 5172–5191 | VERIFIED |
| `BH-IIIB-C-0148` | `p3:rem:o3-not-so3` | 5209–5235 | VERIFIED-CONDITIONAL |
| `BH-IIIB-C-0149` | `p3:prop:reeb-selection` | 5237–5261 | VERIFIED-CONDITIONAL |
| `BH-IIIB-C-0150` | `p3b:rem:infrared-derived-later` | 5279–5297 | FORMALIZED |
| `BH-IIIB-C-0151` | `(unlabelled)` | 5299–5309 | FORMALIZED |
| `BH-IIIB-C-0152` | `(unlabelled)` | 5310–5322 | FORMALIZED |
| `BH-IIIB-C-0153` | `p3:thm:directed-spectral-window-exhaustion` | 5331–5373 | VERIFIED-CONDITIONAL |
| `BH-IIIB-C-0154` | `p3:thm:hk_sectorwise` | 5409–5427 | VERIFIED-CONDITIONAL |
| `BH-IIIB-C-0155` | `(unlabelled)` | 5429–5434 | FORMALIZED |
| `BH-IIIB-C-0156` | `(unlabelled)` | 5436–5441 | FORMALIZED |
| `BH-IIIB-C-0157` | `(unlabelled)` | 5446–5450 | FORMALIZED |
| `BH-IIIB-C-0158` | `(unlabelled)` | 5452–5463 | FORMALIZED |
| `BH-IIIB-C-0159` | `(unlabelled)` | 5465–5473 | FORMALIZED |
| `BH-IIIB-C-0160` | `(unlabelled)` | 5477–5483 | FORMALIZED |
| `BH-IIIB-C-0161` | `p3b:cor:v2216-bare-vacuum-ratio` | 5493–5518 | VERIFIED-CONDITIONAL |
| `BH-IIIB-C-0162` | `p3b:prop:v226-square-scope` | 5551–5558 | VERIFIED |
| `BH-IIIB-C-0163` | `p3b:prop:v227-action-centre` | 5578–5589 | VERIFIED |
| `BH-IIIB-C-0164` | `p3b:thm:diagonal-fibre-spin-ancestry` | 5622–5634 | VERIFIED-CONDITIONAL |
| `BH-IIIB-C-0165` | `p3b:rem:independent-scalar-window-scope` | 5651–5665 | FORMALIZED |
| `BH-IIIB-C-0166` | `p3b:cor:v191-relative-occurrence-axis` | 5668–5680 | VERIFIED-CONDITIONAL |
| `BH-IIIB-C-0167` | `(unlabelled)` | 5682–5687 | FORMALIZED |
| `BH-IIIB-C-0168` | `p3b:prop:v236-protected-octet-independent` | 5695–5706 | VERIFIED-CONDITIONAL |
| `BH-IIIB-C-0169` | `p3b:cor:v236-exceptional-commutator-exports` | 5707–5718 | VERIFIED-CONDITIONAL |
| `BH-IIIB-C-0170` | `p3b:thm:v189-quadratic-sibling-exact-sequence` | 5731–5750 | VERIFIED |
| `BH-IIIB-C-0171` | `p3b:cor:v189-quadratic-fibre-product` | 5758–5771 | VERIFIED |
| `BH-IIIB-C-0172` | `p3b:thm:v319-petersen-moment-six` | 5875–5890 | VERIFIED |
| `BH-IIIB-C-0173` | `p3b:prop:v319-petersen-four-coefficients` | 5905–5925 | VERIFIED |
| `BH-IIIB-C-0174` | `p3b:thm:v346-born-meron-ym` | 5947–5968 | VERIFIED |
| `BH-IIIB-C-0175` | `p3b:cor:v346-born-meron-wilson` | 5984–5998 | VERIFIED-CONDITIONAL |
| `BH-IIIB-C-0176` | `p3b:thm:v349-meron-spin-hodge` | 6019–6038 | VERIFIED |
| `BH-IIIB-C-0177` | `p3b:cor:v349-meron-dirac-spectrum` | 6053–6073 | VERIFIED |
| `BH-IIIB-C-0178` | `p3b:thm:v349-meron-zeta-heat` | 6086–6112 | VERIFIED |
| `BH-IIIB-C-0179` | `p3b:rem:v349-meron-spectrum-physical-guard` | 6132–6140 | FORMALIZED |

## Evidence and release lineage

- **Independent Batch 4 results:** `Paper3B-Batch4-IndependentChecks-v1_4.json`, 13/13 passing scoped groups. Symbolic/matrix, rational golden-ratio axis, spectral theta and analytic zeta checks are explicitly nonphysical.
- **Complete cumulative formal ledger:** `Paper3B-Batch4-Checkpoint-v1_4.json`, all 179 source declarations with exact source locators and flags.
- **Source snapshot:** SHA-256 `ac97a9c5aea0dc3d2716edd61a7f0058128403147cbbae08d2b9dd754ba48913` matches both Paper ZIP and supplied atlas source copy; hash confirms identity only, not theorem correctness.
- **Prior batch evidence:** batches 1, 2 and 3 retained in final ledger by stable IDs; earlier issue statuses remain unchanged without new evidence to discharge them.
- **Release:** DAG `Paper00-DAGAtlas-v1_100.zip`, proof audits `Paper00-ProofChainAudits-v1_18.zip`. Release hashes, ZIP integrity and full entry readback must be checked after writing; this Markdown report itself is not a postwrite certificate.

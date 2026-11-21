# Source migration and repair-integration addendum — Paper3A-ProofChainAudit-v1_7.md

**Integration release:** `Paper00-PapersMinimal-v3_007.zip`, 14 November 2026.
**Current paper source:** `Paper3A-GeneratedDynamics-v1_176.tex`.
**Status:** `SOURCE_INTEGRATED; GLOBAL_SOURCE_REAUDIT_PENDING`. An inherited historical audit is not a correctness certificate for the newer current manuscript.
**Evidence policy:** Local algebraic proofs and scoped tests do not discharge physical source/observable interfaces or automatically alter the canonical proof DAG.

---

## Historical source-bound audit: Paper3A-ProofChainAudit-v1_6.md
# Paper3A — v2.372 source repair addendum (13 November 2026)

**Successor:** `Paper3A-ProofChainAudit-v1_6.md`.  
**Current source:** `Paper3A-GeneratedDynamics-v1_170.tex`.  
**Current SHA-256:** `d284204d07be684985d3b1c63eb561b40c0c7cafd2c131b58dd1a6f97f8519a8`.  
**Historical audit:** `Paper3A-ProofChainAudit-v1_5.md`.  
**Source repair scope:** 1 distinct issue(s); 1 textual corrections.  
**Disposition:** `SOURCE_REPAIRED_WITH_SCOPED_CHECKS; FORMAL_REAUDIT_PENDING` for only the listed IDs. Other issues and all original evidence statuses unchanged.

| Issue ID | New source line(s) | Repaired issue |
|---|---|---|
| `BH-IIIA-G-0008` | 5507 | Omitting Hessian contact breaks the actual scalar Hessian chain law but not associativity of a truncated tensor congruence. |

The historical report below refers to the previous source version and explicitly marks those same issue IDs as `OPEN` **as of that old version**. Those specific historical labels are superseded only as source-edit dispositions by the addendum above; the original audit text is retained to prevent loss of evidence or false global certification. Other issues are unchanged. Recheck the updated source theorem and its proof/use dependencies before promoting an issue to closed in the canonical DAG.

---

## Historical predecessor audit (unchanged text; former source version)

# Born–Hopf Geometry Paper III-A — completed rigorous correctness audit, Batches 1–5

**Artifact:** `Paper3A-ProofChainAudit-v1_5.md`  
**Source:** `Paper3A-GeneratedDynamics-v1_169.tex`, SHA-256 `af384df88772019a94329f4d06d86a80e8ea103b38fc03282f4e80de5127abce`  
**Corpus:** `Paper00-PapersMinimal-v2_370.zip`  
**Protocol:** `Paper00-RigorousVerificationDAGWorkProtocol-v2_4.md`  
**Atlas:** `Paper00-DAGAtlas-v1_99.zip`  
**Coverage:** 185/185 substantive source objects, 152/152 formal declarations, 84 proof environments and 304 exact displays. All substantive target content and summary aliases dispositioned; no target item remains NOT_AUDITED.  
**Classification:** FULLY_AUDITED_WITH_OPEN_GAPS.  
**Cumulative outcomes:** {"FORMALIZED": 66, "VERIFIED-CONDITIONAL": 93, "VERIFIED": 22, "UNRESOLVED": 4}.  
**Batch5 outcomes:** {"FORMALIZED": 4, "VERIFIED-CONDITIONAL": 5, "UNRESOLVED": 1, "VERIFIED": 5}.

Full audit means every claim was examined and classified; it does not mean every claim is proved or every conditional physical antecedent established. The current source census now mirrors the authoritative current ledger statuses; older extraction snapshots remain historical.

## All current findings

**BH-IIIA-G-0001 — OPEN, moderate source-scope ambiguity (inherited).** Introductory lines95–99 summarize full H_p≅H1 without the whole-endpoint comparison certificates qualified in II-B and III-A510–530/1146–1169. Existing CMP-I/II/III apply only to the full-endpoint branch. Generated support and m_p=1 remain verified. No downstream failed proof or observable consequence is certified. Clarify the summary or supply the exact stronger certificates.

**BH-IIIA-G-0002 — RESOLVED, minor DAG integrity (inherited).** Three stale active source/condition pointers were corrected in Batch1. No mathematical change.

**BH-IIIA-G-0003 — OPEN/UNRESOLVED, moderate type/domain (inherited).** C65 at2139–2141 uses the spatial scalar band m_cmp=P_x(2) as a scalar deck-even sampling window without a declared typed comparison. P_x(2) contains E1 and odd primitive Hopf charges, while the q± quotient character lattice requires n+w even. A0024 records the missing interface as INFERRED/NOT-YET-LOCATED. Parent retention remains verified. No source-defined physical countermodel or remote failed consumption is certified. Specify the intended window/map; no repair is inserted.

**BH-IIIA-G-0004 — OPEN, minor cited-route scope mismatch (inherited).** C80 at2736–2741 cites reciprocal-status-discharge, whose current III-G provider requires P_mc. Keep that guard on its full-profile route. The native CHAR/product T2 proof through C20/C24/C60 is independently valid without P_mc. Qualify the citation or cite that native route.

**BH-IIIA-G-0005 — OPEN/UNRESOLVED, moderate vector-map normalization ambiguity (inherited from Batch3).** The unnamed relative-solder paragraph at3282–3295 uses su(2)* --(tau*)^-1--> p* --Phi_v--> T_b*S_B3 but does not define tau:su(2)→p. II-C619–660 gives evaluation ev(X,-X)=2X and Phi_v=(ev*)^-1. Choosing tau=ev^-1 yields the full Maurer–Cartan form; choosing the anti-diagonal inclusion yields half that form, matching the displayed III-B relative solder on the labelled section. Both are isomorphisms, but their exact normalizations differ. A0063 records only this unlocated definition, not a new physical axiom. The scalar character (n,-n)→n is already fixed; vector/scalar rank, rank4, a^4 and the positive H^(1/4) response remain independently verified. Only C99 VECTOR_EXACT_NORMALIZATION is blocked. No source-as-printed numerical refutation, failed observable or cross-paper failed consumption is certified. Define/cite tau with its exact normalization and verify the displayed composition; no replacement map is supplied.

**BH-IIIA-G-0006 — OPEN/UNRESOLVED, moderate exact-interface verification gap (inherited from Batch4).** In the unnamed K16 source-localization paragraph4562–4571, the retained carrier for the primitive scalar source a and the exact normalized map rho16src are not specified by a located provider. The asserted rho16src(2X_(a,u))=(a omega)_A e^A is a factor-two cotangent/source identification; current II-C first-symbol pairing supplies a different precisely typed harmonic/transvection quotient, while III-C supplies Clifford block/grade calculations. Neither exact consumed composite has been located. A0103 records the unverified map/carrier/normalization certificate, not a new physical axiom. The displayed equation may define a readout convention; that does not independently verify its asserted generated source ancestry or K16 grade. No false formula, E44 contradiction, missing fermion/action constructor or physical countermodel is certified. Self-adjointness of X and source/tangent/fermion/projectability firewalls remain valid on their own domains. III-G6408ff repeats the source/tangent distinction without using this exact coefficient, so no failed remote proof or observable path is established. Locate and replay the existing precise source map, carrier and normalization; no map or repair is inserted.

**BH-IIIA-G-0007 — RESOLVED, minor DAG-only integrity defect (inherited from Batch4).** The inherited raw material index contained240 rows already excluded by the proof query:155 EVIDENCE_FOR,51 SCOPE_GUARD,1 SCOPE_REFERENT and33 other scope/candidate-named rows. They are preserved in Paper00-InheritedNonmaterialEdges-v1_1.json and in all original typed layers. Derived proof-only adjacency and reachability now apply the existing query filter consistently; core mathematical data, sources and earlier statuses are unchanged. This corrects indexing, not a source proof.

**BH-IIIA-G-0008 — OPEN/UNRESOLVED, minor source-property ambiguity (new).** C174 at 5507–5509 says dropping the Hessian contact term generally destroys the preceding coherence. Complete actual two-jet pullbacks do associate and the contact term is generally required to obtain the actual Hessian. However pure tensor congruence H→Dg*HDg also associates for every composable smooth map: T_g(T_f(H))=T_(f∘g)(H) by the ordinary first-derivative chain rule. The independent nonaffine positive-chart control gives truncated sequential=direct 3456, while actual/full 4704 at x=1; affine controls agree. Thus the literal algebraic-nonassociativity interpretation is disproved, while actual-Hessian compatibility is a valid reading. Only the final property reference remains ambiguous; C174 overall is UNRESOLVED, with its full formula, full associativity and actual-Hessian consistency branches separately verified. No new assumption can make tensor pullback nonassociative. Clarify which coherence is meant; no source edit or replacement theorem is supplied. No failed cross-paper/observable path is established.

**BH-IIIA-G-0009 — OPEN, minor cited-provider scope mismatch (new).** C185 at 5721–5725 attributes general complete Petersen action-jet/source-mark retention to C150. That provider at 4783–4834 assumes finite positive shared-interior quadratic blocks and proves Schur variance plus limited terminal consequences; it does not by itself establish arbitrary complete graded/background jet retention. C118→C145, C147 and C146 already provide the correct generic claim-complete owner/reuse/firewall route under actual licensed Petersen incidence A0128 and existing owner/physical-sum scope A0041/A0083. The generic branch remains verified conditional and acquires no positive-pivot assumption. The cited quadratic specialization is separately recorded and cannot serve as the sole generic proof. Cite/qualify the existing generic route; no repair implemented. No theorem, finite Petersen identity, no-action-insertion firewall or downstream observable is refuted.

**BH-IIIA-G-0010 — RESOLVED, minor inherited DAG boundary-ID collision (new).** Seven Batch2 IDs were each assigned to both a registrar boundary and an adversarial boundary. They are not interchangeable: B2-BND-0005 denoted both the causal envelope (2442–2474) and the deck-readout boundary (2135–2142). The seven adversarial objects now have distinct B2-E4-BND IDs; all 116 records and original evidence are retained. All 36 current E4 references and G0003’s boundary pointer are qualified. An explicit identity adjudication preserves the historical mapping. No source claim, condition, material proof edge or mathematical status changes.

Ten current issues: seven open and three resolved. No unambiguous source-wide mathematical refutation or failed physical observable is certified. The stronger C174 tensor-nonassociativity interpretation is explicitly disproved as an INTERPRETED object, not silently identified with the correct actual-jet statement. Source-scope ambiguities, missing typed interfaces, missing verification certificates, cited-route defects and resolved DAG-only defects remain distinct. Conditional hypotheses are not called mathematical errors.

## Complete source coverage

| Audit alias | Source lines | Owner | Status |
|---|---:|---|---|
| BH-IIIA-C-0001 | 124–136 | `Reciprocal configuration metric scale CAL_xp` | FORMALIZED |
| BH-IIIA-C-0002 | 141–165 | `Metric-curry scope and historical BR/IND status aliases` | FORMALIZED |
| BH-IIIA-C-0003 | 166–175 | `Scalar phase action-unit calibration CAL_hbar` | FORMALIZED |
| BH-IIIA-C-0004 | 176–187 | `Primitive scalar-turn clock calibration CAL_t` | FORMALIZED |
| BH-IIIA-C-0005 | 189–234 | `Framework-prefix definition and premise-minimal/profile separation` | FORMALIZED |
| BH-IIIA-C-0006 | 255–325 | `Paper-II import theorem-package and domain ledger` | FORMALIZED |
| BH-IIIA-C-0007 | 327–340 | `Selector-status classes and nonpromotion between sorts` | FORMALIZED |
| BH-IIIA-C-0008 | 342–362 | `Finite-role, coordinate-class and exceptional-support boundary` | FORMALIZED |
| BH-IIIA-C-0009 | 369–386 | `p3:g0-actualization` | FORMALIZED |
| BH-IIIA-C-0010 | 388–423 | `p3a:lem:generated-role-occurrence-inheritance` | VERIFIED-CONDITIONAL |
| BH-IIIA-C-0011 | 425–428 | `p3:def:constitutive-datum` | FORMALIZED |
| BH-IIIA-C-0012 | 430–436 | `p3:gp1-finiteness` | FORMALIZED |
| BH-IIIA-C-0013 | 438–445 | `p3:gp2-geometric-primacy` | FORMALIZED |
| BH-IIIA-C-0014 | 447–454 | `p3:gp3-faithful-closure` | FORMALIZED |
| BH-IIIA-C-0015 | 456–494 | `p3a:thm:v166-reciprocal-interface-summary` | VERIFIED-CONDITIONAL |
| BH-IIIA-C-0016 | 498–508 | `p3:def:constitutive-residue-main` | FORMALIZED |
| BH-IIIA-C-0017 | 510–530 | `p3:def:imported-vector-momentum-constitution` | FORMALIZED |
| BH-IIIA-C-0018 | 538–608 | `p3:lem:rank-one-lattice-dual-spectrum` | VERIFIED |
| BH-IIIA-C-0019 | 610–653 | `p3a:def:scalar-loop-character-constructor` | FORMALIZED |
| BH-IIIA-C-0020 | 655–724 | `p3a:thm:g0-derived-scalar-character-role` | VERIFIED-CONDITIONAL |
| BH-IIIA-C-0021 | 726–748 | `p3a:cor:s1-universal-corealization-bridge` | VERIFIED-CONDITIONAL |
| BH-IIIA-C-0022 | 758–780 | `p3a:rem:relation-free-readout-firewall` | VERIFIED-CONDITIONAL |
| BH-IIIA-C-0023 | 782–792 | `p3:rem:born-reciprocity-lorentzian-recovery` | FORMALIZED |
| BH-IIIA-C-0024 | 798–860 | `p3:thm:scalar_classification_import` | VERIFIED-CONDITIONAL |
| BH-IIIA-C-0025 | 865–883 | `p3:def:reciprocal-vector-bookkeeping-package` | FORMALIZED |
| BH-IIIA-C-0026 | 886–889 | `Closure theorem uniqueness/least/minimal proof convention` | FORMALIZED |
| BH-IIIA-C-0027 | 892–929 | `p3:rem:dimensionful-calibration-boundary` | FORMALIZED |
| BH-IIIA-C-0028 | 934–953 | `p3a:def:dynamical-readout-occurrences` | FORMALIZED |
| BH-IIIA-C-0029 | 955–990 | `p3a:thm:two-branch-dynamical-handoff` | VERIFIED-CONDITIONAL |
| BH-IIIA-C-0030 | 992–1001 | `p3a:cor:no-gp3-readout-profile` | VERIFIED-CONDITIONAL |
| BH-IIIA-C-0031 | 1008–1019 | `p3a:rem:scalar-evaluation-carrier-window-dictionary` | FORMALIZED |
| BH-IIIA-C-0032 | 1021–1032 | `p3a:cor:clocked-position-character-support` | VERIFIED-CONDITIONAL |
| BH-IIIA-C-0033 | 1034–1045 | `p3a:cor:clock-family-scalar-kinetic-identity` | VERIFIED-CONDITIONAL |
| BH-IIIA-C-0034 | 1131–1144 | `Reciprocal \(S^3\) notation and physical scale` | FORMALIZED |
| BH-IIIA-C-0035 | 1146–1169 | `p3:thm:momentum` | VERIFIED-CONDITIONAL |
| BH-IIIA-C-0036 | 1170–1184 | `The imported branch is already the constituted simply connected one` | FORMALIZED |
| BH-IIIA-C-0037 | 1186–1236 | `p3:thm:born-reciprocity-exhaustion` | VERIFIED-CONDITIONAL |
| BH-IIIA-C-0038 | 1238–1252 | `Typed unequal-level finite Born branch exchange` | VERIFIED-CONDITIONAL |
| BH-IIIA-C-0039 | 1258–1271 | `Dimensionless chiral and dimensionful physical operator conventions` | FORMALIZED |
| BH-IIIA-C-0040 | 1275–1301 | `p3:lem:born` | VERIFIED-CONDITIONAL |
| BH-IIIA-C-0041 | 1304–1332 | `p3:thm:position` | VERIFIED-CONDITIONAL |
| BH-IIIA-C-0042 | 1334–1342 | `p3:rem:reciprocal-scale-calibration` | FORMALIZED |
| BH-IIIA-C-0043 | 1344–1358 | `p3:rem:p2-to-p3-position` | FORMALIZED |
| BH-IIIA-C-0044 | 1360–1405 | `p3:cor:hopf-abelian-line` | VERIFIED-CONDITIONAL |
| BH-IIIA-C-0045 | 1407–1420 | `Status of the abelian slot` | FORMALIZED |
| BH-IIIA-C-0046 | 1422–1442 | `p3:lem:primitive-contact-speed-normalization` | FORMALIZED |
| BH-IIIA-C-0047 | 1445–1471 | `p3:cor:doubled-vector` | VERIFIED-CONDITIONAL |
| BH-IIIA-C-0048 | 1476–1500 | `p3:thm:vector-sector-not-symplectic` | VERIFIED |
| BH-IIIA-C-0049 | 1502–1567 | `p3:lem:no-intrinsic-vector-scalar` | VERIFIED |
| BH-IIIA-C-0050 | 1569–1585 | `p3:cor:no-intrinsic-scalar-pair` | VERIFIED |
| BH-IIIA-C-0051 | 1588–1596 | `p3:rem:provisional-scalar-labels` | FORMALIZED |
| BH-IIIA-C-0052 | 1598–1642 | `p3:thm:transported-scalar-orientation` | VERIFIED-CONDITIONAL |
| BH-IIIA-C-0053 | 1644–1693 | `p3:thm:scalar-born-residue` | VERIFIED-CONDITIONAL |
| BH-IIIA-C-0054 | 1695–1743 | `p3:thm:minimal-symplectic-completion` | VERIFIED |
| BH-IIIA-C-0055 | 1745–1805 | `p3a:thm:canonical-generator-germ-localization` | VERIFIED-CONDITIONAL |
| BH-IIIA-C-0056 | 1807–1835 | `p3a:cor:calibrated-reciprocal-position-momentum-unit` | VERIFIED-CONDITIONAL |
| BH-IIIA-C-0057 | 1837–1864 | `p3a:cor:local-cotangent-born-compatibility` | VERIFIED-CONDITIONAL |
| BH-IIIA-C-0058 | 1867–1883 | `p3:cor:missing-sector-one-pair` | VERIFIED |
| BH-IIIA-C-0059 | 1885–1941 | `p3:lem:minimal-phase-torus-quantization` | VERIFIED-CONDITIONAL |
| BH-IIIA-C-0060 | 1946–1972 | `p3:def:separable-scalar-compactification` | VERIFIED |
| BH-IIIA-C-0061 | 1974–2014 | `p3:thm:scalars` | VERIFIED-CONDITIONAL |
| BH-IIIA-C-0062 | 2017–2070 | `p3a:thm:v190-scalar-born-eigenphase-cover` | VERIFIED |
| BH-IIIA-C-0063 | 2072–2106 | `p3a:cor:v190-scalar-deck-grading` | VERIFIED |
| BH-IIIA-C-0064 | 2108–2133 | `p3a:cor:v190-scalar-mutual-moments` | VERIFIED-CONDITIONAL |
| BH-IIIA-C-0065 | 2135–2142 | `p3a:rem:v190-scalar-parent-retention` | UNRESOLVED |
| BH-IIIA-C-0066 | 2144–2250 | `p3a:def:clocked-hopf-propagation-doctrine` | FORMALIZED |
| BH-IIIA-C-0067 | 2252–2295 | `p3a:cor:clocked-hopf-corealization` | VERIFIED-CONDITIONAL |
| BH-IIIA-C-0068 | 2297–2323 | `p3a:cor:clock-half-turn-antipode` | VERIFIED-CONDITIONAL |
| BH-IIIA-C-0069 | 2327–2354 | `p3a:cor:clock-joint-orbit-monodromy` | VERIFIED-CONDITIONAL |
| BH-IIIA-C-0070 | 2367–2440 | `p3:thm:gp1-speed-calibration` | VERIFIED-CONDITIONAL |
| BH-IIIA-C-0071 | 2442–2474 | `p3:cor:gp1-round-causal-envelope` | VERIFIED-CONDITIONAL |
| BH-IIIA-C-0072 | 2476–2503 | `p3a:cor:v177-three-dimensional-causal-determinant` | VERIFIED-CONDITIONAL |
| BH-IIIA-C-0073 | 2505–2587 | `p3:thm:gp1-operation-generator-polar-dual` | VERIFIED-CONDITIONAL |
| BH-IIIA-C-0074 | 2589–2625 | `p3a:thm:causal-cone-determinant-root-isomorphism` | VERIFIED |
| BH-IIIA-C-0075 | 2627–2654 | `p3a:cor:causal-root-quadratic-half-character` | VERIFIED |
| BH-IIIA-C-0076 | 2656–2663 | `p3a:rem:determinant-root-bundle-scope` | FORMALIZED |
| BH-IIIA-C-0077 | 2665–2693 | `p3a:lem:causal-homothety` | VERIFIED-CONDITIONAL |
| BH-IIIA-C-0078 | 2695–2717 | `p3:rem:polar-dual-not-global-pair` | FORMALIZED |
| BH-IIIA-C-0079 | 2719–2731 | `Notation for \(dt\) and \(dE\) on the scalar circles` | FORMALIZED |
| BH-IIIA-C-0080 | 2733–2746 | `Why the scalar compact role space is a torus` | VERIFIED |
| BH-IIIA-C-0081 | 2749–2778 | `p3:thm:scalar-pair-no-modulus` | VERIFIED-CONDITIONAL |
| BH-IIIA-C-0082 | 2780–2806 | `p3a:cor:calibrated-scalar-m8-scale-chain` | VERIFIED-CONDITIONAL |
| BH-IIIA-C-0083 | 2808–2821 | `p3a:cor:momentum-unit-normal-form` | VERIFIED-CONDITIONAL |
| BH-IIIA-C-0084 | 2825–2879 | `p3a:thm:v245-massless-gauge-clock-lock` | VERIFIED-CONDITIONAL |
| BH-IIIA-C-0085 | 2881–2891 | `Second quantization and the vacuum-energy phase` | VERIFIED-CONDITIONAL |
| BH-IIIA-C-0086 | 2895–2911 | `p3a:def:v247-affine-spectral-defect` | FORMALIZED |
| BH-IIIA-C-0087 | 2913–2987 | `p3a:thm:v247-conformal-clock-hierarchy` | VERIFIED-CONDITIONAL |
| BH-IIIA-C-0088 | 2989–2998 | `p3a:rem:v247-conformal-matching-scope` | FORMALIZED |
| BH-IIIA-C-0089 | 3000–3027 | `p3a:cor:normalized-m8-cone-evaluation` | VERIFIED-CONDITIONAL |
| BH-IIIA-C-0090 | 3029–3140 | `p3a:thm:complete-joint-zero-defect-locus` | VERIFIED-CONDITIONAL |
| BH-IIIA-C-0091 | 3142–3163 | `p3a:cor:joint-locus-neutral-speed-extension` | VERIFIED-CONDITIONAL |
| BH-IIIA-C-0092 | 3165–3179 | `p3a:rem:hopf-character-energy-lattice` | FORMALIZED |
| BH-IIIA-C-0093 | 3181–3189 | `p3:rem:time-energy-upgrade` | FORMALIZED |
| BH-IIIA-C-0094 | 3191–3198 | `p3:rem:scalar-closure` | FORMALIZED |
| BH-IIIA-C-0095 | 3200–3220 | `p3:thm:full-compact-carrier-no-symplectic-a` | VERIFIED |
| BH-IIIA-C-0096 | 3225–3248 | `p3a:cor:primitive-scalar-unchanged-descent` | VERIFIED |
| BH-IIIA-C-0097 | 3250–3269 | `p3a:cor:faithful-clock-real-cover` | VERIFIED-CONDITIONAL |
| BH-IIIA-C-0098 | 3271–3276 | `Scalar action cell versus spatial volume and energy bounds` | FORMALIZED |
| BH-IIIA-C-0099 | 3282–3295 | `Rank-four relative-solder generator-germ localization map` | UNRESOLVED |
| BH-IIIA-C-0100 | 3297–3309 | `p3a:cor:v187-rank-four-parent-root` | VERIFIED-CONDITIONAL |
| BH-IIIA-C-0101 | 3318–3320 | `Universal continuation rule has sector-dependent carriers and laws` | FORMALIZED |
| BH-IIIA-C-0102 | 3322–3369 | `p3a:def:generated-exact-continuation-signature` | FORMALIZED |
| BH-IIIA-C-0103 | 3371–3405 | `p3a:def:exact-continuation-moduli` | FORMALIZED |
| BH-IIIA-C-0104 | 3407–3456 | `p3a:thm:universal-generated-exact-continuation` | VERIFIED-CONDITIONAL |
| BH-IIIA-C-0105 | 3460–3472 | `p3a:def:v236-dynamics-atlas-status` | FORMALIZED |
| BH-IIIA-C-0106 | 3474–3481 | `p3a:cor:v236-unresolved-common-content` | VERIFIED-CONDITIONAL |
| BH-IIIA-C-0107 | 3485–3503 | `p3a:lem:v166-continuation-certificate-transport` | VERIFIED-CONDITIONAL |
| BH-IIIA-C-0108 | 3505–3543 | `p3a:cor:rooted-dynamical-parent-cascade` | VERIFIED-CONDITIONAL |
| BH-IIIA-C-0109 | 3547–3560 | `p3a:def:v149-law-flow-history` | FORMALIZED |
| BH-IIIA-C-0110 | 3562–3610 | `p3a:thm:v149-law-flow-history-separation` | VERIFIED-CONDITIONAL |
| BH-IIIA-C-0111 | 3613–3649 | `p3a:thm:v204-action-law-transport` | VERIFIED-CONDITIONAL |
| BH-IIIA-C-0112 | 3656–3670 | `p3a:cor:v204-moving-presentation` | VERIFIED-CONDITIONAL |
| BH-IIIA-C-0113 | 3675–3685 | `p3a:rem:v149-generator-flow-families` | FORMALIZED |
| BH-IIIA-C-0114 | 3693–3705 | `p3a:def:claim-complete-action-owner` | FORMALIZED |
| BH-IIIA-C-0115 | 3707–3729 | `p3a:thm:claim-complete-action-descent` | VERIFIED-CONDITIONAL |
| BH-IIIA-C-0116 | 3731–3768 | `p3a:cor:boundary-trivial-same-action-reclosure` | VERIFIED-CONDITIONAL |
| BH-IIIA-C-0117 | 3770–3780 | `p3a:def:frozen-preaction-signature` | FORMALIZED |
| BH-IIIA-C-0118 | 3782–3818 | `p3a:thm:generated-action-constructor-closure` | VERIFIED-CONDITIONAL |
| BH-IIIA-C-0119 | 3820–3832 | `p3a:cor:preaction-no-self-witness` | VERIFIED-CONDITIONAL |
| BH-IIIA-C-0120 | 3834–3845 | `p3a:cor:bare-effective-action-firewall` | VERIFIED-CONDITIONAL |
| BH-IIIA-C-0121 | 3847–3872 | `p3a:cor:born-equivariant-constructor-descent` | VERIFIED-CONDITIONAL |
| BH-IIIA-C-0122 | 3874–3896 | `p3a:thm:variational-sort-firewall` | VERIFIED-CONDITIONAL |
| BH-IIIA-C-0123 | 3898–3925 | `p3a:thm:unique-solution-history-descent` | VERIFIED-CONDITIONAL |
| BH-IIIA-C-0124 | 3927–3947 | `p3a:cor:transverse-crossing-descendant` | VERIFIED-CONDITIONAL |
| BH-IIIA-C-0125 | 3959–3978 | `p3a:lem:regular-constraint-ideal` | VERIFIED |
| BH-IIIA-C-0126 | 3980–4100 | `p3a:thm:v149-native-noether-frontier` | VERIFIED-CONDITIONAL |
| BH-IIIA-C-0127 | 4102–4125 | `p3a:cor:v176-noether-constrained-one-ray` | VERIFIED-CONDITIONAL |
| BH-IIIA-C-0128 | 4127–4134 | `p3a:rem:v176-constraint-history-clock-firewall` | FORMALIZED |
| BH-IIIA-C-0129 | 4137–4171 | `p3a:cor:identity-survival-oriented-nonstationarity` | VERIFIED-CONDITIONAL |
| BH-IIIA-C-0130 | 4173–4199 | `p3a:cor:common-process-invariant` | VERIFIED-CONDITIONAL |
| BH-IIIA-C-0131 | 4201–4288 | `p3a:thm:finite-generator-one-ray-rigidity` | VERIFIED-CONDITIONAL |
| BH-IIIA-C-0132 | 4290–4315 | `p3a:prop:v2211-clock-affinity-certificate` | VERIFIED-CONDITIONAL |
| BH-IIIA-C-0133 | 4317–4327 | `p3a:cor:v166-finite-normal-form-certificate` | VERIFIED-CONDITIONAL |
| BH-IIIA-C-0134 | 4330–4350 | `p3a:cor:v149-finite-unitary-generator` | VERIFIED-CONDITIONAL |
| BH-IIIA-C-0135 | 4352–4360 | `p3a:rem:v149-finite-continuum-semigroup-status` | FORMALIZED |
| BH-IIIA-C-0136 | 4362–4375 | `p3a:rem:continuation-generator-boundary` | FORMALIZED |
| BH-IIIA-C-0137 | 4377–4425 | `p3a:thm:generated-process-projectability` | VERIFIED-CONDITIONAL |
| BH-IIIA-C-0138 | 4427–4459 | `p3a:cor:v166-smooth-process-descent` | VERIFIED-CONDITIONAL |
| BH-IIIA-C-0139 | 4461–4557 | `p3a:thm:threshold-event-descent` | VERIFIED-CONDITIONAL |
| BH-IIIA-C-0140 | 4562–4582 | `Balanced K16 source localization and fibre-constant scalar projection` | UNRESOLVED |
| BH-IIIA-C-0141 | 4586–4593 | `p3a:rem:v182-k16-fermion-sort-firewall` | FORMALIZED |
| BH-IIIA-C-0142 | 4602–4631 | `p3a:thm:v184-normalized-successor-residual` | VERIFIED-CONDITIONAL |
| BH-IIIA-C-0143 | 4633–4644 | `p3a:cor:v184-width-eight-cell` | VERIFIED-CONDITIONAL |
| BH-IIIA-C-0144 | 4650–4669 | `p3a:cor:v226-coordinate-continuation` | VERIFIED-CONDITIONAL |
| BH-IIIA-C-0145 | 4683–4716 | `p3a:cor:v183-action-coconsumption` | VERIFIED-CONDITIONAL |
| BH-IIIA-C-0146 | 4718–4724 | `p3a:rem:v183-action-coconsumption-firewall` | FORMALIZED |
| BH-IIIA-C-0147 | 4725–4752 | `p3a:cor:complete-parent-descendant-reuse` | VERIFIED-CONDITIONAL |
| BH-IIIA-C-0148 | 4753–4758 | `Complete-parent reuse with critical directions retained before elimination` | FORMALIZED |
| BH-IIIA-C-0149 | 4768–4781 | `Common physical action assembly and single allocation of overlap` | FORMALIZED |
| BH-IIIA-C-0150 | 4783–4834 | `p3a:thm:v2216-common-action-consumption` | VERIFIED-CONDITIONAL |
| BH-IIIA-C-0151 | 4836–4852 | `p3a:rem:v2216-multiaction-scope` | FORMALIZED |
| BH-IIIA-C-0152 | 4856–4869 | `p3a:prop:v245-common-action-two-jet-equality` | VERIFIED |
| BH-IIIA-C-0153 | 4870–4881 | `p3a:rem:v245-two-jet-owner-firewall` | FORMALIZED |
| BH-IIIA-C-0154 | 4887–4924 | `p3a:thm:v246-integrable-parent-reconstruction` | VERIFIED-CONDITIONAL |
| BH-IIIA-C-0155 | 4926–4947 | `p3a:cor:v246-sector-restriction-kernel` | VERIFIED |
| BH-IIIA-C-0156 | 4949–4965 | `p3a:rem:v246-parent-reconstruction-scope` | FORMALIZED |
| BH-IIIA-C-0157 | 4968–4986 | `p3a:par:v245-common-action-rigor-frontier` | FORMALIZED |
| BH-IIIA-C-0158 | 4992–5010 | `p3a:cor:v223-cap-consumption` | VERIFIED-CONDITIONAL |
| BH-IIIA-C-0159 | 5025–5031 | `Complete reference-cap source translation j_r` | VERIFIED-CONDITIONAL |
| BH-IIIA-C-0160 | 5033–5040 | `Off-shell collar transport and actual shared-interior incidence` | VERIFIED-CONDITIONAL |
| BH-IIIA-C-0161 | 5042–5051 | `Primitive-owner retraction and complete native-cap chronology` | VERIFIED-CONDITIONAL |
| BH-IIIA-C-0162 | 5063–5088 | `p3a:def:v188-native-claim-data` | FORMALIZED |
| BH-IIIA-C-0163 | 5090–5128 | `p3a:thm:v188-native-observable-fibre` | VERIFIED-CONDITIONAL |
| BH-IIIA-C-0164 | 5130–5166 | `p3a:cor:v188-claim-relative-completeness` | VERIFIED-CONDITIONAL |
| BH-IIIA-C-0165 | 5168–5188 | `p3a:def:v188-native-completion-certificate` | FORMALIZED |
| BH-IIIA-C-0166 | 5198–5224 | `p3a:cor:v185-projective-cone-protection` | VERIFIED-CONDITIONAL |
| BH-IIIA-C-0167 | 5226–5234 | `p3a:rem:v185-constants-speed-firewall` | FORMALIZED |
| BH-IIIA-C-0168 | 5243–5270 | `Typed local Lorentzian coframe homothety/shear/rotation descent` | VERIFIED-CONDITIONAL |
| BH-IIIA-C-0169 | 5272–5285 | `p3a:cor:v189-spatial-shear-decomposition` | VERIFIED-CONDITIONAL |
| BH-IIIA-C-0170 | 5290–5305 | `Finite complete visible-response quotient and dark-data boundary` | VERIFIED-CONDITIONAL |
| BH-IIIA-C-0171 | 5439–5445 | `Licensed finite common-action word and additional global gluing domain` | FORMALIZED |
| BH-IIIA-C-0172 | 5448–5476 | `p3a:v251:eq:full-pullback-hessian` | VERIFIED-CONDITIONAL |
| BH-IIIA-C-0173 | 5478–5493 | `Anchored coefficient Hessian integrability and radial primitive` | VERIFIED-CONDITIONAL |
| BH-IIIA-C-0174 | 5495–5509 | `Full two-jet transition pullback and triple-overlap coherence` | UNRESOLVED |
| BH-IIIA-C-0175 | 5512–5537 | `Positive shared-interior Schur response and variance defect identity` | VERIFIED-CONDITIONAL |
| BH-IIIA-C-0176 | 5539–5584 | `p3a:v251:thm:shared-second-jet` | VERIFIED |
| BH-IIIA-C-0177 | 5586–5590 | `Background response jets versus ordinary fixed-point action two-jets` | FORMALIZED |
| BH-IIIA-C-0178 | 5592–5608 | `paper3a:corollary:atlas-frame-covariance-of-the-second-jet-defect-220dfda` | VERIFIED |
| BH-IIIA-C-0179 | 5610–5628 | `paper3a:proposition:atlas-first-nonzero-higher-order-response-mismatch-4fe1b0f` | VERIFIED |
| BH-IIIA-C-0180 | 5630–5634 | `Regular positive-pivot domain and unlicensed endpoint limits` | FORMALIZED |
| BH-IIIA-C-0181 | 5637–5650 | `Two vanishing separate reductions with nonzero shared response second jet` | VERIFIED |
| BH-IIIA-C-0182 | 5653–5677 | `Raw 96-fold joint normalization versus uniformly transported Newton branch` | VERIFIED-CONDITIONAL |
| BH-IIIA-C-0183 | 5685–5691 | `Embedded 2I Petersen packet and momentum-carrier nonidentification` | FORMALIZED |
| BH-IIIA-C-0184 | 5693–5713 | `p3a:prop:v319-petersen-marked-jet` | VERIFIED |
| BH-IIIA-C-0185 | 5715–5726 | `p3a:prop:v319-petersen-action-firewall` | VERIFIED-CONDITIONAL |

## Final-batch evidence and scope

15 E1 replay records, 16 active independent mathematical certificates plus one E0 summary reconciliation, 24 adversarial attacks and source-bound boundary records cover the final 15 objects. The latest independent certificate file v1_2 includes its post-freeze C185 citation clarification and preserves the original mathematical records/lineage; superseded v1_1 certificate/notes are omitted from this release. 71 independent and 17 adversarial exact controls pass. Controls support the separately recorded general arguments and never replace them; E0 counts/schema/ZIP checks are not mathematical E3.

The independent final census reads every current source declaration/proof/display and maps 16 closing-summary blocks plus 15 other summary/scope ranges to their actual owners. Abstract 64–73 and nonmathematical preamble/bibliography boundaries are explicitly disposed. No supplementary substantive claim had to be invented, and no claim was dropped to reach completion. Existing source-qualified H1 support and m_p=1 remain checkpoints; source summaries do not become new proof edges or unqualified full-endpoint certificates.

C171 begins with a supplied licensed common action and actual incidence/once-only overlap allocation; no interaction follows from merely co-realizing sectors. C172 retains all pullback/contact/ordered odd-coefficient/source-frame terms. Admitted derivatives of S_int are an explicit inferred conditional scope, not automatic consequences of generated provenance. C173 uses arbitrary coefficient anchors for construction; pairwise existing-action equality is only a locally discharged uniqueness test. Independent physical action origin remains separate from self-reconstruction.

C175 has source-supported real and complex positive-variance cases. The real source import is only its complete-square algebra; terminal PSD/slope, physical assembly and unrelated normalizations are not silently imported. C176 real/complex proofs of each same mathematical clause are OR cases, never a demand for both carrier sorts. C2 background coefficient regularity and regular-point centre agreement are distinct predicates; neither follows from C3 action maps alone or from terminal-port compatibility. The second-jet iff/finite HS criterion does not assume the derivative equality it characterizes.

C178 frame-derivative terms vanish at compatible Delta=0; no off-compatible simplification is made. C179 retains adequate smoothness for its actual r and asserted 2r derivative, including a valid r=0 boundary; inherited C2 is not enough for every higher-order derivative. C180 excludes singular/changing-domain/closing-gap endpoints. C181 is a direct scalar polynomial diagnostic with locally checked matrix data, no native physical occurrence or physical-sum word assumed. Background jets of the retained Hessian and ordinary fixed-point action two-jets are kept distinct.

C182 preserves actual raw joint coupling and the separate stronger certified whole-action normalization branch. Gphys=Gscal/96 is allowed when the actual final action is raw; equality with Gscal requires an already certified uniform full-word map and z=1/96. Rescaling a gravity trace alone supplies no such map. A scalar coordinate is not a fermion first-order pairing, and no observed Newton datum enters this verification.

C183 imports only an already occurring embedded 2I support when used physically; C184 mathematical cancellation/complement parity uses the supplied marked finite packet. The mathematical marked-packet predicate is not merged with actual physical marking. Exact I-A coordinate and Gram identities are checked at their stated field/representation scope. Neither the 15-channel count nor a finite A5 rotation action creates H1 identification, a continuous Noether family, a new field or an action coefficient. C185 generic co-consumption uses its earlier full-owner route, with the narrow printed citation separately challenged.

16 genuinely new typed predicates A0113–A0128 are indexed once at their earliest validated source appearances, with reused predicates referenced rather than duplicated. Interaction/higher-jet regularity remains conditional; no new physical axiom, constructor, normalization projection or repair theorem is introduced. A0102 remains withdrawn and unreused. The 240-row inherited nonmaterial provenance file remains byte-identical, and no such row re-enters proof ancestry.

## Queries and completion

Run `python3 Paper00-DAGQuery-v1_99.py summary`, `issues`, `claim BH-IIIA-C-0174`, `conditions BH-IIIA-C-0174:TRIPLE_ASSOCIATIVITY`, `conditions BH-IIIA-C-0174:OMITTED_CONTACT_COHERENCE_AS_PRINTED`, `conditions BH-IIIA-C-0176:SECOND_JET_FORMULA`, `conditions BH-IIIA-C-0182:RAW_PHYSICAL_BRANCH`, `conditions BH-IIIA-C-0185:ACTUAL_OPERATOR_COCONSUMPTION`, or `impact BH-IIIA-G-0009`.

Paper3A source audit is complete, with its audited open obligations retained. No next unaudited target batch remains. Other papers are only source-checked at exact consumed interfaces; this release does not certify the whole framework.

The paired audit ZIP contains exactly seven latest Markdown reports: six byte-identical existing Paper-II audits and current III-A v1_5. The DAG has one current III-A v1_5 layer and current source tree. Distinct earlier evidence/named provenance remains history; no superseded current report/layer, PDF, nested ZIP or build/debug artifact is added. All paper/macro/bibliography sources remain unchanged.

## Independent release review

PASS: 80 pre-write integrity checks; complete final-remainder source/evidence/branch review and full-paper census/scope reconciliation; 56 independent actual CLI queries; coordinator 41 clause queries and scoped-discharge tests. All 170 earlier statuses and 32 controlling sources remain unchanged. G0008 retains only the printed coherence ambiguity, with the stronger tensor-nonassociativity interpretation separately disproved; G0009 has its earlier generic owner bypass. G0010 resolves seven inherited boundary-ID collisions, preserving all original records and all 116 distinct boundaries. G0006 remains an exact-interface evidence gap; G0007 preserves its 240 original quarantined rows byte-for-byte. No global framework verification is claimed.

## Exact post-write certificate WRT-IIIA-B5-0001

Final DAG archive: `Paper00-DAGAtlas-v1_99.zip`, SHA-256 `566727ce43b0f11900d24a41b3acad5e835f1f4f7ce56ab73d3a56493d3f7477`; 822 unique entries, 19018628 bytes. Exact written bytes were reopened: CRC, every JSON, every payload hash, 32 controlling source files, current source/condition indexes, and latest-only contents passed. This E0 result is distinct from mathematical evidence. The archive hash is stored here to avoid a self-referential hash inside that archive.

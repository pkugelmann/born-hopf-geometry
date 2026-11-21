# Paper7B — current-source repair and bounded-check addendum (18 November 2026)

**Current source:** `Paper7B-QCDReadouts-v1_164.tex`; SHA-256 `2659e5aa8a1cc87d0cd186c2efc006ce0c5b6f5f61493017fea01b534cdc8487`.
**Framework:** Paper00-PapersMinimal-v3_032.zip; **DAG:** Paper00-DAGAtlas-v1_182.zip; **Audit:** Paper00-ProofChainAudits-v1_74.zip.
**Scope:** TARGETED SOURCE REPAIR / SELECTED CLAIM LOCAL RECHECK, **not a new full-paper E3/E4 audit**. Historical text and findings below are preserved. Old open verdicts are not erased; consult the effective status ledger `Paper00-ClosedGapCrosswalk-v1_4.json`.

**Repair:** two-state transfer Ritz values, exact source-visible Schur pole test; no actual pole owner/physical QCD spectrum asserted.

**Evidence:** `Paper00-MultiDomainReverificationBatch2-v1_1.md`, source patch diff and 38/38 combined scoped checks. Physical action, state, pole, history and observational occurrence remain conditional unless independently proved from actual owners.

---

## Previous audit preserved as historical document

# Paper7B — current-source bounded verification annex, 2026-11-18

This is the latest full audit report, with the original historical audit text preserved verbatim below. Current source matches v3.031; older `OPEN` entries retain historical meaning. For the **effective current disposition**, see `Paper00-QCDReverificationBatch1-v1_1.md` and crosswalk v1.3 in the DAG. This is not a full new-paper E3/E4 audit.

**Reviewed roots:** 13 · **Local corrections verified:** 7 · **Owner-gated:** 6.

| Issue | Current source line | Effective source disposition |
|---|---:|---|
| `BH-VIIB-G-0134` | 227 | Scoped local correction verified |
| `BH-VIIB-G-0135` | 796 | Source conditional, owner unresolved |
| `BH-VIIB-G-0137` | 974 | Scoped local correction verified |
| `BH-VIIB-G-0138` | 1149 | Scoped local correction verified |
| `BH-VIIB-G-0139` | 908 | Scoped local correction verified |
| `BH-VIIB-G-0140` | 1801 | Scoped local correction verified |
| `BH-VIIB-G-0141` | 1919 | Source conditional, owner unresolved |
| `BH-VIIB-G-0142` | 2692 | Source conditional, owner unresolved |
| `BH-VIIB-G-0143` | 2987 | Scoped local correction verified |
| `BH-VIIB-G-0144` | 3591 | Scoped local correction verified |
| `BH-VIIB-G-0145` | 3794 | Source conditional, owner unresolved |
| `BH-VIIB-G-0146` | 4266 | Source conditional, owner unresolved |
| `BH-VIIB-G-0147` | 4809 | Source conditional, owner unresolved |

**New issue `BH-VIIB-G-0148`:** trial 2x2 transfer-block pole identification is false without reduction; in-domain finite counterexample recorded in batch report.

---

## Preserved historical source-era audit (original text below)

# Source migration and repair-integration addendum — Paper7B-ProofChainAudit-v1_4.md

**Integration release:** `Paper00-PapersMinimal-v3_007.zip`, 14 November 2026.
**Current paper source:** `Paper7B-QCDReadouts-v1_157.tex`.
**Status:** `SOURCE_INTEGRATED; GLOBAL_SOURCE_REAUDIT_PENDING`. An inherited historical audit is not a correctness certificate for the newer current manuscript.
**Evidence policy:** Local algebraic proofs and scoped tests do not discharge physical source/observable interfaces or automatically alter the canonical proof DAG.

---

## Historical source-bound audit: Paper7B-ProofChainAudit-v1_3.md
# Repair addendum — Paper7B, 13 November 2026

**Current source:** `Paper7B-QCDReadouts-v1_151.tex` (SHA-256 `efe40952e04b0c845e1009c94a0acf95b5260a85280eaa379f948bca6c5318e1`)  
**Inherited audit:** `Paper7B-ProofChainAudit-v1_2.md`; the complete text follows, unedited as historical evidence.  
**Disposition:** SOURCE-REPAIR EVENT, not independent full re-audit; no theorem/physical status promotion.  

| Distinct source-audit issue | Current TeX location(s) | Repair/scope | Remaining status |
|---|---|---|---|
| `BH-VIIB-G-0134` | `Paper7B-QCDReadouts-v1_151.tex:210`, `Paper7B-QCDReadouts-v1_151.tex:212` | Transfer spectrum is taken on Ran(P) instead of ambient PHP with spurious zero eigenvalues. | SOURCE_REPAIRED; REAUDIT PENDING |
| `BH-VIIB-G-0135` | `Paper7B-QCDReadouts-v1_151.tex:727`, `Paper7B-QCDReadouts-v1_151.tex:729`, `Paper7B-QCDReadouts-v1_151.tex:737` | Physical nucleon-sector spectral claim now requires a nonzero reducing projection [PN,H]=0. | SOURCE_REPAIRED; IMPORTED/PHYSICAL CONDITION OPEN |
| `BH-VIIB-G-0137` | `Paper7B-QCDReadouts-v1_151.tex:908`, `Paper7B-QCDReadouts-v1_151.tex:922`, `Paper7B-QCDReadouts-v1_151.tex:934` | Two-state Hermitian mixing eigenvalues corrected from kappa squared to absolute kappa squared. | SOURCE_REPAIRED; REAUDIT PENDING |
| `BH-VIIB-G-0138` | `Paper7B-QCDReadouts-v1_151.tex:1085`, `Paper7B-QCDReadouts-v1_151.tex:1103` | Reported two-loop QCD scale explicitly requires and states the external MZ reference and beta normalization. | SOURCE_REPAIRED; IMPORTED/PHYSICAL CONDITION OPEN |
| `BH-VIIB-G-0139` | `Paper7B-QCDReadouts-v1_151.tex:845`, `Paper7B-QCDReadouts-v1_151.tex:856` | Simple-pole residue uses holomorphic numerator at pole divided by denominator derivative; higher jets affect finite part. | SOURCE_REPAIRED; REAUDIT PENDING |
| `BH-VIIB-G-0140` | `Paper7B-QCDReadouts-v1_151.tex:1731`, `Paper7B-QCDReadouts-v1_151.tex:1740`, `Paper7B-QCDReadouts-v1_151.tex:1747` | Finite-volume Feynman–Hellmann hadron mass response subtracts the vacuum-energy derivative. | SOURCE_REPAIRED; IMPORTED/PHYSICAL CONDITION OPEN |
| `BH-VIIB-G-0141` | `Paper7B-QCDReadouts-v1_151.tex:1847`, `Paper7B-QCDReadouts-v1_151.tex:1870`, `Paper7B-QCDReadouts-v1_151.tex:1873` | Winding number alone no longer identifies Noether baryon current without action/current-matched map. | SOURCE_REPAIRED; IMPORTED/PHYSICAL CONDITION OPEN |
| `BH-VIIB-G-0142` | `Paper7B-QCDReadouts-v1_151.tex:2626`, `Paper7B-QCDReadouts-v1_151.tex:2641` | PDF normalization on [0,1] requires actual support/crossing and endpoint and zero-mode controls. | SOURCE_REPAIRED; IMPORTED/PHYSICAL CONDITION OPEN |
| `BH-VIIB-G-0143` | `Paper7B-QCDReadouts-v1_151.tex:2919`, `Paper7B-QCDReadouts-v1_151.tex:2929` | Negative-x GPD antiquark branch signs are stated separately for unpolarized and helicity sectors. | SOURCE_REPAIRED; IMPORTED/PHYSICAL CONDITION OPEN |
| `BH-VIIB-G-0144` | `Paper7B-QCDReadouts-v1_151.tex:3521`, `Paper7B-QCDReadouts-v1_151.tex:3537` | Dimensionful Hamiltonian source uses -T/V times logZ derivative, distinct from dimensionless-exponent convention. | SOURCE_REPAIRED; REAUDIT PENDING |
| `BH-VIIB-G-0145` | `Paper7B-QCDReadouts-v1_151.tex:3724`, `Paper7B-QCDReadouts-v1_151.tex:3737`, `Paper7B-QCDReadouts-v1_151.tex:3741` | Abstract geometric F_sigma is separated from Hurwitz E_sigma by a chosen, not automatic, isometric map. | SOURCE_REPAIRED; IMPORTED/PHYSICAL CONDITION OPEN |
| `BH-VIIB-G-0146` | `Paper7B-QCDReadouts-v1_151.tex:4226`, `Paper7B-QCDReadouts-v1_151.tex:4264` | Positive spectral measures are not claimed to imply analytic continuation to a second resonance sheet. | SOURCE_REPAIRED; IMPORTED/PHYSICAL CONDITION OPEN |
| `BH-VIIB-G-0147` | `Paper7B-QCDReadouts-v1_151.tex:4713`, `Paper7B-QCDReadouts-v1_151.tex:4715` | Pure-glue member is a typed restriction of QCD data with its own vacuum energy, not literal tuple inclusion. | SOURCE_REPAIRED; IMPORTED/PHYSICAL CONDITION OPEN |

See `Paper00-AuditRepairBatch-v1_2.md` and the 24/24 scoped math controls in the active DAG atlas for checks and counterexamples. Historical source-hash and line locations below apply **only** to the previous paper version. Do not reinterpret their original `OPEN`, `REFUTED`, or `VERIFIED` labels as new-version global adjudications.

---

## Historical audit baseline (unaltered text)

> **Merge-only identifier reconciliation (Atlas v1.120).** This is the complete unchanged mathematical Paper VII-B v1.1 audit, reissued as v1.2 solely to prevent independent issue-ID collisions. The 14 source-local `BH-G-000134`–`BH-G-000147` references are globally `BH-VIIB-G-0134`–`BH-VIIB-G-0147`. Paper VII-A retains the bare `BH-G-...` identities. See `DAG/IssueIDReconciliation-v1_120.json` for the crosswalk. This merge is not a new mathematical verification or a gap closure.

# Born–Hopf Geometry — Paper VII-B rigorous mathematical proof-chain audit

**Artifact:** `Paper7B-ProofChainAudit-v1_2.md`
**Audit unit:** current `Paper7B-QCDReadouts-v1_150.tex`, framework v2.371 source archive
**Protocol:** `Paper00-RigorousVerificationDAGWorkProtocol-v2_4.md` with proof-chain provenance v1.1
**Scope:** all 195 named mathematical statements and material unnamed step/observable interfaces in the target Paper VII-B source only.
**Classification:** `FULLY_AUDITED_WITH_OPEN_GAPS` in the source-statement disposition sense; 1 printed result refuted and 13 open issues, not a globally verified or physically complete QCD theory.
**Reviewer:** one executor performing E1 replay, independent E3 checks and E4 adversarial tests sequentially; **no multi-agent independent agreement claimed**.
**Frozen source SHA-256:** `d23f9643784f1963e50d51a45fcdecb3f37508414154d855008bfd5cdb7bc2c0`.

## Cumulative verdicts

| Disposition | Count |
|---|---:|
| `VERIFIED` | 59 |
| `VERIFIED-CONDITIONAL` | 67 |
| `REPRODUCED` | 18 |
| `FORMALIZED` | 40 |
| `UNRESOLVED` | 10 |
| `REFUTED` | 1 |
| **Total** | **195** |

The 195-statement count is the named-environment census, not an assertion that only named formulae were read. The audit also inspected essential unnamed equations, source assumptions, physical readout typing, imported theorem instances and explicit exclusions. Conditional statuses retain the actual domain guards and are not promoted to physical occurrence.

## Batch summary

| Batch | Claim records | Source span | Number of independently executed tests | New issue IDs |
|---|---:|---|---:|---|
| 1 | 31 | 109–832 | 0 | BH-VIIB-G-0134, BH-VIIB-G-0135, BH-VIIB-G-0136 |
| 2 | 31 | 833–1681 | 15 | BH-VIIB-G-0137, BH-VIIB-G-0138, BH-VIIB-G-0139 |
| 3 | 36 | 1682–2633 | 24 | BH-VIIB-G-0140, BH-VIIB-G-0141, BH-VIIB-G-0142 |
| 4 | 44 | 2637–3881 | 50 | BH-VIIB-G-0143, BH-VIIB-G-0144, BH-VIIB-G-0145 |
| 5 | 53 | 3887–5695 | 77 | BH-VIIB-G-0146, BH-VIIB-G-0147 |

## All source-bound named result dispositions

| # | Label | Source line | Class | Adjudicated scope/step |
|---:|---|---:|---|---|
| 1 | `p11:def:imported-paper-x-core-datum` | 109–124 | `FORMALIZED` | imported exact tuple; no mathematical occurrence promotion |
| 2 | `p11:cor:v147-generated-readout-descendants` | 126–141 | `REPRODUCED` | generated structural readout scope via imported Paper7A/Paper2A; upstream source matched, independent physical grammar proof not re-executed |
| 3 | `p11:cor:v2187-spectrum-before-population` | 154–174 | `VERIFIED` | finite functional calculus and preparation-independent spectrum |
| 4 | `p11:rem:conditional-strong-interface-scope` | 186–201 | `FORMALIZED` | scope limitation and numeric ancestry reminder |
| 5 | `UNLABELED:Paper7B:definition:209` | 209–221 | `FORMALIZED` | readout definitions; spectrum-of-compression domain notation under review |
| 6 | `p11:cor:v154-km-selector-retired` | 228–236 | `FORMALIZED` | conditional spurion uniqueness claim; actual G16 transport retained |
| 7 | `p11:thm:singlet-support-classification` | 329–345 | `REPRODUCED` | SU3 invariant contractions, exhaustive primitive types checked to first tensor degrees; no full independent FFT audit |
| 8 | `p11:thm:hadronic-fermion-parity` | 351–360 | `VERIFIED` | triality + parity mod 2 |
| 9 | `p11:cor:minimal-baryon-exchange-symmetry` | 369–372 | `VERIFIED` | antisymmetric determinant and fermion exchange |
| 10 | `p11:thm:color-casimir-attraction-channels` | 384–402 | `VERIFIED-CONDITIONAL` | all 5 Casimir factors checked independently; sign-as-attraction only on leading one-gluon-exchange branch; current V-C import is p7v2:prop:color-channels (renamed title) |
| 11 | `p11:thm:primitive-channel-loss-hierarchy` | 415–431 | `VERIFIED-CONDITIONAL` | color Casimir not dynamic amplitude; spectral gap on ran(P) only |
| 12 | `p11:cor:numerical-primitive-channel-floors` | 437–442 | `VERIFIED-CONDITIONAL` | family H=E0I+cP and restricted gap; depends on ran(P) typing |
| 13 | `p11:thm:v323-petersen-k-core-spectrum` | 460–477 | `VERIFIED` | exact characteristic polys for k=0,...,5 plus all 32 subset numerical checks independent from 7D proof |
| 14 | `p11:cor:v323-2-3-contrast` | 490–501 | `VERIFIED` | norm of k2 vs k3 eigenvalues and J map separation |
| 15 | `p11:prop:v323-actual-hadron-spectrum-criterion` | 508–521 | `REPRODUCED` | source-owned physical embedding necessary; excludes geometry-only pole mapping |
| 16 | `p11:prop:v327-meson-gram-support` | 540–566 | `VERIFIED` | Gram eigen decomposition/PSD condition |
| 17 | `p11:def:v327-meson-squared-gap-observable` | 573–590 | `FORMALIZED` | conditional source-owned squared mass gap test |
| 18 | `p11:rem:v327-meson-matched-spectrum-benchmark` | 592–618 | `FORMALIZED` | PDG benchmark orientation; no theorem, approximate only |
| 19 | `p11:prop:v327-no-automatic-meson-spectrum` | 620–631 | `VERIFIED` | parameter-varying conditional Hamiltonian vs fixed projector |
| 20 | `p11:def:hadronic-eigenvalue-problem` | 658–667 | `FORMALIZED` | actual invariant sector definition, refinement guard |
| 21 | `p11:thm:native-spectral-correlator-mass-bridge` | 670–685 | `VERIFIED` | positive spectral Laplace and log derivative on nonzero overlap branch |
| 22 | `p11:rem:v2217-temporal-source-clock` | 692–706 | `VERIFIED` | 2x explicit cubic clock sign tests C0<C1 |
| 23 | `p11:prop:dimensional-hadron-mass-form` | 709–718 | `VERIFIED` | reference-unit dimensional identity |
| 24 | `p11:thm:native-nucleon-mass-eigenvalue` | 724–734 | `UNRESOLVED` | isospin-labelled physical projector not shown to reduce actual H on general unequal-mass branch |
| 25 | `p11:def:finite-baryon-flux-junction-support` | 741–751 | `FORMALIZED` | epsilon-singlet flux-leg representation |
| 26 | `p11:lem:no-incoherent-baryon-junction-branch` | 753–758 | `REPRODUCED` | finite Wedderburn commutant criterion imported from VII-A; no branch occurrence asserted |
| 27 | `p11:thm:baryon-flux-junction-contraction` | 764–773 | `VERIFIED` | 3C_F+2pair=0 gives -2 |
| 28 | `p11:thm:positive-native-nucleon-mass-floor` | 779–788 | `VERIFIED-CONDITIONAL` | positive uniform floor iff inf_L gap>0, provided exact P_N sector |
| 29 | `p11:cor:dimensionless-baryon-anchor-floor` | 794–799 | `VERIFIED` | reference-gap ratio dimensionless and nonuniversal |
| 30 | `p11:thm:finite-hadron-spectrum-closure` | 805–808 | `REPRODUCED` | finite spectral decomposition on all *conserved* blocks; no numeric spectrum computed |
| 31 | `p11:rem:m8-batch-qcd-readout-inputs` | 814–826 | `FORMALIZED` | readout scope remark |
| 32 | `p11:lem:v153-scheme-invariant-isolated-pole` | 836–848 | `VERIFIED-CONDITIONAL` | Determinant zero divisor preserved on common analytic invertible chart; residue covariance requires simple-pole or full Laurent-jet interpretation (issue BH-VIIB-G-0139) |
| 33 | `p11:def:same-channel-finite-transfer-block` | 858–873 | `FORMALIZED` | Finite source Gram normalization and transfer approximant are definitions; positive contraction follows on vacuum-offset positive H |
| 34 | `p11:thm:no-parameter-same-channel-mixing` | 875–880 | `VERIFIED` | Nested-trial min-max on compressed e^{-tA}, not on e^{-t compressed A}; transfer-energy Ritz monotonicity independently checked |
| 35 | `p11:thm:no-additional-shell-normalizer-qcd` | 886–892 | `VERIFIED-CONDITIONAL` | No extra fit normalizer on already supplied Hamiltonian/clock; not a derivation of absolute QCD scale |
| 36 | `p11:cor:first-two-support-pole-extraction` | 898–928 | `REFUTED` | Displayed real-symmetric 2x2 matrix and kappa^2 discriminant fail for arbitrary complex Gram-orthonormal source states; exact admissible 2x2 counterexample (BH-VIIB-G-0137) |
| 37 | `p11:thm:inclusive-color-counting-export` | 951–979 | `VERIFIED-CONDITIONAL` | Color sums 2,10/3,11/3 independently reconstructed; observable R(s) uses explicitly imported SMAT/IR and massless leading-power assumptions |
| 38 | `p11:thm:qcd-validation-hierarchy` | 1016–1022 | `FORMALIZED` | Acyclic validation pipeline is a source policy; unfinished observed quantities explicitly remain targets, not computed predictions |
| 39 | `p11:cor:derived-perturbative-comparison-package` | 1072–1087 | `UNRESOLVED` | Running and nf=3 fixed fractions checked, but 206.9499404 MeV needs 91.1876 GeV comparison scale and Lambda convention not specified/source-owned (BH-VIIB-G-0138) |
| 40 | `p11:cor:primitive-support-and-baryon-matrix-elements` | 1094–1104 | `VERIFIED` | Wigner-Eckart and Feynman-Hellmann separate group factors from dynamical matrix elements; no count-based gA prediction |
| 41 | `p11:thm:orthogonal-hurwitz-adjoint-winding-variance` | 1110–1122 | `VERIFIED` | Quadratic covariance w^T C w and PSD counterfamily independently verified |
| 42 | `p11:cor:hard-exclusive-da-moments-and-kernels` | 1128–1141 | `VERIFIED-CONDITIONAL` | Asymptotic DA beta integrals algebraic; absolute amplitudes require physical Fpi/source matrix and process-scoped factorization certificate |
| 43 | `p11:cor:thermal-bqs-susceptibility-endpoint` | 1151–1185 | `VERIFIED` | Independently derived all BQS 3x3 susceptibility entries and all diagonal fourth-to-second ratios from free Dirac pressure |
| 44 | `p11:cor:native-pseudoscalar-gas-fingerprint` | 1191–1201 | `VERIFIED-CONDITIONAL` | Free Bose gas formulas exact within stated ideal-gas/mass-input domain; not numerical crossover or interacting QCD |
| 45 | `p11:thm:leading-transverse-contact-support-selection` | 1222–1228 | `VERIFIED` | Same JPC/flavor source sector may support varying interaction strengths and eigenvalues; count energies not fixed |
| 46 | `p11:thm:native-leading-vector-nonet` | 1234–1242 | `REPRODUCED` | SU3 octet plus singlet and reduced matrix-element independence; physical vector poles conditional on actual currents, source matrices |
| 47 | `p11:cor:native-vector-current-constants` | 1248–1255 | `VERIFIED` | Conserved-charge Ward fixes F(0), does not fix Fprime(0), residues or VMD uniqueness |
| 48 | `p11:thm:native-axial-pole-L10` | 1261–1274 | `VERIFIED` | Arbitrary c>0 solves first two Weinberg narrow-resonance sum rules; nonunique axial mass and L10 |
| 49 | `p11:thm:native-scalar-L5-L8` | 1280–1288 | `VERIFIED` | Chiral source-response coefficient definitions plus positive parameter counterfamily establish nonuniqueness of scalar saturation values |
| 50 | `p11:thm:native-L1-L2-L3` | 1294–1299 | `REPRODUCED` | L1-3 as renormalized p4 generating functional coefficients; source matching structure repeated but physical correlator execution not independently evaluated |
| 51 | `p11:thm:native-L7-anomalous` | 1305–1310 | `VERIFIED-CONDITIONAL` | Quadratic heavy-singlet tree elimination yields negative exchange low-energy coefficient, conditional on positive singlet mass/source normalization |
| 52 | `p11:cor:native-leading-p7-constants-summary` | 1316–1321 | `VERIFIED` | L4,L6 not forced zero by absent carrier labels; chiral invariants allow independent couplings |
| 53 | `p11:thm:block-b-finite-pole-dressing` | 1337–1367 | `VERIFIED` | Direct complex 3x3 block inverse independently reproduces finite Feshbach projected resolvent; poles real before open-channel limit |
| 54 | `p11:cor:schur-positive-gap-weight` | 1380–1407 | `VERIFIED` | 1D complement calculation checks residue/lowering; general degenerate Loewner bounds source-matched to Paper1B theorem |
| 55 | `p11:thm:response-visible-inverse` | 1421–1440 | `VERIFIED` | Independent two-pole complete matrix response yields rank-sum minimal environment and invisible dark subspace; imported I-B theorem exact |
| 56 | `p11:cor:block-b-leading-vector-complex-poles` | 1455–1463 | `VERIFIED-CONDITIONAL` | Only after open-channel limiting boundary/continuation; finite self-adjoint block does not by itself yield complex resonances |
| 57 | `p11:thm:block-c-topology-pseudoscalar-separation` | 1472–1479 | `REPRODUCED` | Z(theta) cumulants and anomaly current separation from source; actual chiYM and coupled correlator are unexecuted |
| 58 | `p11:thm:block-d-finite-distribution-spectral-measures` | 1485–1497 | `REPRODUCED` | Physical PDF owner imported with distinct optional exact LFRep branch; named later claims located, not upgraded before their batches |
| 59 | `p11:thm:block-e-thermal-finite-trace` | 1508–1513 | `VERIFIED` | Finite-dimensional thermal trace is real analytic for T>0 with finite charge/chemical sources; critical transition requires limit |
| 60 | `p11:thm:block-f-nuclear-transfer-cumulants` | 1519–1524 | `REPRODUCED` | Möbius cumulant algebra well defined given partition-indexed cluster amplitudes; sector energies/contacts require actual QCD source calculations |
| 61 | `p11:thm:v2210-lit-gevp-frame-gap` | 1542–1584 | `VERIFIED` | Finite source isometry/GEVP, minmax upper energies, complete frame lower-gap bound and Weyl error bounds independently checked |
| 62 | `p11:prop:v2210-lit-semigroup-leakage` | 1603–1613 | `VERIFIED` | Duhamel double off-block insertion bounds nonreducing compression-return by tau^2 delta^2/2; positive Hermitian numeric examples |
| 63 | `p11:thm:nucleon-trace-anomaly-bridge` | 1692–1711 | `VERIFIED-CONDITIONAL` | Trace Ward identity gives M_N only on matched relativistic normalization with finite scale residual proved absent/absorbed; source explicitly retains R_scale otherwise. |
| 64 | `p11:thm:native-scalar-response-bridge` | 1716–1726 | `UNRESOLVED` | M_h is a vacuum-subtracted gap, but FH proof uses raw hadron eigenvalue derivative; connected/vacuum-subtracted scalar operator must be specified. Exact E4 example BH-VIIB-G-0140. |
| 65 | `p11:thm:rg-invariant-scalar-bridge` | 1732–1749 | `VERIFIED-CONDITIONAL` | Opposite anomalous dimensions imply RG invariance of m_q times scalar density in the declared scheme. Sigma as derivative is safe after mass-source/vacuum normalization. |
| 66 | `p11:thm:native-goldberger-treiman-bridge` | 1754–1762 | `VERIFIED-CONDITIONAL` | PCAC, isolated physical nucleon/pion poles and controlled chiral limit are explicit; GT residue relation standard within those conditions; no numerical g_A inferred. |
| 67 | `p11:thm:leading-native-nucleon-axial-charge` | 1768–1778 | `VERIFIED-CONDITIONAL` | Independent normalized SU6 spin-flavor state reproduces Delta u=4/3, Delta d=-1/3, g_A=5/3; source expressly does not assert physical ground-state realization. |
| 68 | `p11:thm:native-one-pion-exchange-nuclear-boundary` | 1784–1809 | `VERIFIED-CONDITIONAL` | Derivative pion-pole vertices generate quoted OPE momentum structure on SMAT/LSZ chiral branch; contacts consume actual pole-subtracted matching prescription, not finite support counts. |
| 69 | `p11:thm:microscopic-topological-baryon-matching` | 1828–1852 | `UNRESOLVED` | Determinant color singlet and pi3(SU3)=Z are each valid; identification of normalized microscopic U1_B current with chiral winding needs action-derived matching, not proved from uniqueness of conservation alone (BH-VIIB-G-0141). |
| 70 | `p11:thm:wzw-baryon-multiplet-quantization` | 1857–1872 | `VERIFIED-CONDITIONAL` | Imported VII-A WZW coefficient N_c=3 plus actual winding-B chiral soliton and SU3 hedgehog collective quantization gives Y_R=Nc B/3, allowed octet/decuplet; no state occurrence asserted. |
| 71 | `p11:cor:leading-baryon-mass-relations` | 1877–1894 | `VERIFIED` | Exact symbolic substitution confirms octet GMO and linear decuplet equal spacing in the stated first-order isospin-limit spurion form; no absolute mass derived. |
| 72 | `p11:thm:nc3-large-color-scaling` | 1899–1904 | `VERIFIED` | Asymptotic big-O with free coefficient does not supply equality or normalization at Nc=3. |
| 73 | `p11:thm:native-chiral-running` | 1942–1953 | `VERIFIED-CONDITIONAL` | Integrated chiral L_i running and log cancellation independently checked, given scheme Gamma_i; matching scale arbitrary within EFT window. |
| 74 | `p11:cor:native-one-loop-FK-Fpi` | 1959–1965 | `REPRODUCED` | Conditional one-loop formula described but full explicit function is not printed here; provenance is chiral generating functional with free matched L5, F0, masses; no decimal. |
| 75 | `p11:cor:native-one-loop-mass-logs` | 1971–1976 | `REPRODUCED` | Renormalized p4 chiral mass expansion necessarily includes analytic L_i counterterms and logs; source gives no explicit numerical mass to verify. |
| 76 | `p11:cor:native-vector-strong-widths` | 1982–1998 | `VERIFIED-CONDITIONAL` | Two-body open-channel vector width follows phase space only with on-shell source 3pt vertex and SMAT1–3,5,7 (SMAT4 for LSZ); no KSRF prediction. |
| 77 | `p11:rem:vector-vertex-reclosure-targets` | 2008–2016 | `FORMALIZED` | Explicit limitation: flavor-dependent vector 3pt amplitudes remain uncomputed; no extrinsic strange-leg coefficient inserted. |
| 78 | `p11:lem:minimal-transverse-spin-glue-sheet` | 2025–2030 | `VERIFIED` | Scaling the physical Hamiltonian insertion leaves a normalized geometric second moment unchanged, independently showing 8/3 not a dynamical energy weight. |
| 79 | `p11:lem:dressed-determinant-current-projections` | 2036–2041 | `VERIFIED` | Wigner–Eckart reduced matrix elements independent across vector/axial/tensor/magnetic operators; conserved vector Ward controls charge only. |
| 80 | `p11:thm:native-baryon-spin-gluon-ladder` | 2047–2062 | `UNRESOLVED` | Block spectrum identity holds for invariant spin/flavor sector, but physical pole assertion inherits prior BH-VIIB-G-0135 projector-commutation certificate, especially unequal mass branch; do not duplicate root. |
| 81 | `p11:rem:baryon-recoupling-status` | 2068–2071 | `FORMALIZED` | Explicit recoupling coefficients are finite reference block values; not physical baryon masses absent full Hamiltonian diagonalization. |
| 82 | `p11:thm:native-dressed-baryon-residues` | 2073–2085 | `VERIFIED-CONDITIONAL` | Different source residues are distinct current matrix elements; scalar Feynman–Hellmann as mass-gap derivative inherits vacuum-subtraction guard BH-VIIB-G-0140. |
| 83 | `p11:thm:finite-em-current-radius-reclosure` | 2091–2103 | `VERIFIED` | Independent analytic form-factor family F(q²)=Q+cq² shows Ward charge does not determine radius or magnetic slope. |
| 84 | `p11:cor:native-octet-axial-current-block` | 2110–2118 | `VERIFIED` | Two octet reduced axial couplings from SU3 8⊗8 containing two octets; no numerical F/D ratio from color determinant. |
| 85 | `p11:prop:v2220-physical-baryon-readout` | 2142–2168 | `VERIFIED-CONDITIONAL` | Finite positive spectral expansion and large-T log-ratio exact for two visible isolated stable spin levels; not resonance pole identification. |
| 86 | `p11:prop:v2220-flux-source-test` | 2178–2202 | `VERIFIED-CONDITIONAL` | FH derivative for isolated simple level and spin-invariant multiplet trace independently checked; geometric source is bookkeeping, not mass parameter. |
| 87 | `p11:thm:v235-signed-face-source-compression` | 2214–2231 | `REPRODUCED` | Exact Haar conditional covariance and 3 of 96 fan-face overlap give 85/768 and difference 1/2304; source upstream Haar orthogonality used, off-diagonal proof not separately exhaustively recomputed. |
| 88 | `p11:cor:v235-signed-adjoint-selection` | 2255–2278 | `REPRODUCED` | Adjoint character projection coefficient 3/(96*8)=1/256 independently checked; mode-overlap cancellation inherits preceding Haar support. |
| 89 | `p11:cor:v235-hurwitz-edge-source-ward` | 2290–2305 | `VERIFIED` | Independent 24-cell simplicial incidence reconstructed: 24 vertices, 96 edges, 96 faces, boundary ranks 23 and 73; all vertex-gradient directions annihilate face-generated source. |
| 90 | `p11:rem:v235-source-vs-poles` | 2315–2341 | `VERIFIED-CONDITIONAL` | Pure-electric comparison is explicitly noninvariant, nonphysical baryon gap; cubic affine determinant derivative -2Tr A³ directly verified; physical fermionic insertion remains conditional. |
| 91 | `p11:rem:v230-all-link-flux-readout` | 2345–2357 | `FORMALIZED` | Source expressly forbids identifying finite comparison x with interacting Euclidean time or baryon hyperfine poles. |
| 92 | `p11:def:hadronic-distribution-package` | 2390–2469 | `FORMALIZED` | LF-A through LF-D source packages typed separately: physical plus owner/state and claim-local limit, optional stronger exact LFRep. No automatic hadron occurrence. |
| 93 | `p11:thm:v134-fixed-plus-sector-preservation` | 2471–2490 | `VERIFIED` | Finite spectral functional calculus gives [H,E_p]=0 from [H,Pphys+]=0 on preserved singlet subspace; no need for R3. |
| 94 | `p11:def:claim-local-lf-limit-package` | 2501–2528 | `FORMALIZED` | L1–L5 are optional claim-indexed limit hypotheses; L2–L4 not provided merely by geometry; L5 only for TMD. |
| 95 | `p11:rem:v186-exact-asymptotic-lfrep-split` | 2531–2547 | `FORMALIZED` | Exact finite LFRep and asymptotically controlled local-flat representation are distinct certificates; no exact conclusion from vanishing limit defect. |
| 96 | `p11:rem:v252-physical-fock-plus-distinction` | 2549–2563 | `FORMALIZED` | R3 equality PF+=Pphys+ is not entailed by R1-R2; explicit commuting diagonal model demonstrates independence. |
| 97 | `p11:thm:lf-wilson-line-identification` | 2565–2589 | `VERIFIED-CONDITIONAL` | Gauge-link bilocal endpoint covariance and covariant Taylor on geodesic Hopf null ray check; continuum collinear PDF identification explicitly consumes L2–L4, no finite exact Fock positivity/support inferred. |
| 98 | `p11:thm:native-pdf-sum-rules` | 2601–2623 | `UNRESOLVED` | Source’s immediately prior theorem expressly does not prove [0,1] PDF support; Ward full moments alone do not imply [0,1] integrals. Additional support/crossing/zero-mode certificate needed (BH-VIIB-G-0142). |
| 99 | `p11:rem:v264-optional-finite-positive-measure-branch` | 2637–2647 | `FORMALIZED` | Optional exact finite positive fractions are explicitly distinguished from renormalized physical PDF; no positivity transfer without matching. |
| 100 | `p11:thm:native-dglap-scale-evolution` | 2649–2677 | `VERIFIED-CONDITIONAL` | V-C DGLAP/ERBL/threshold generators imported with scheme and boundary; exact SU3 factors check; preservation of physical [0,1] moments inherits BH-VIIB-G-0142. |
| 101 | `p11:thm:native-qcd-factorization-bridge` | 2685–2701 | `VERIFIED-CONDITIONAL` | Process-dependent factorization and SMAT/IR hypotheses are explicitly required; no generated scattering amplitudes inferred from light-ray definitions. |
| 102 | `p11:thm:native-distribution-amplitude-export` | 2714–2737 | `VERIFIED-CONDITIONAL` | Axial-current limit fixes DA integral when normalized supported light-ray pion matrix element and required LF/ERBL realization exist; 6x(1-x) is conditional UV fixed mode. |
| 103 | `p11:thm:isospin-symmetric-pion-da-parity` | 2748–2770 | `VERIFIED-CONDITIONAL` | Isospin/charge-conjugation exchange gives DA parity under the stated equal-mass symmetry and Wilson-line domain; Gegenbauer odd coefficients vanish. |
| 104 | `p11:cor:closed-pion-da-first-moments` | 2784–2797 | `VERIFIED` | Symmetric normalized pion DA forces mean x=1/2 and vanishing first xi moment, independent of its even shape. |
| 105 | `p11:cor:asymptotic-pion-da-moments` | 2804–2839 | `VERIFIED` | Exact SymPy integration reproduces every printed x^n and xi^(2m) closed formula in general and samples; fixed ERBL mode is separately imported. |
| 106 | `p11:thm:asymptotic-determinant-baryon-da` | 2877–2889 | `VERIFIED-CONDITIONAL` | 3-quark asymptotic ERBL lowest mode 120 x1 x2 x3 integrates exactly to one on simplex; no finite-scale nucleon DA derived. |
| 107 | `p11:thm:native-gpd-unification-bridge` | 2896–2907 | `UNRESOLVED` | GPD forward equation H_q(x,0,0)=q(x) lacks domain: native q is [0,1] quark PDF, whereas GPD x ranges [-1,1]. For x<0 the C-conjugate antiquark branch is generally -qbar(-x), unless q is explicitly signed-extended (BH-VIIB-G-0143). Other local-current/Ji limits remain conditional identities. |
| 108 | `p11:thm:native-bjorken-sum-rule-bridge` | 2912–2931 | `VERIFIED-CONDITIONAL` | Bjorken first moment and 1-alpha_s/pi nonsinglet coefficient standard on actual polarized DIS, OPE, SMAT and PDF-support domain; no native numeric g_A computed. |
| 109 | `p11:thm:asymptotic-quark-gluon-momentum-partition` | 2937–2960 | `VERIFIED-CONDITIONAL` | 2x2 LO DGLAP moment matrix has exact zero eigenvector (3nf,16), reproducing Q/G; physical PDF integrals require inherited support BH-VIIB-G-0142. |
| 110 | `p11:cor:qcd-remnant-envelope-25-support` | 2971–2976 | `VERIFIED` | 25=9+16 is arithmetic, not an operator projection. Source explicitly refuses physical remnant inference. |
| 111 | `p11:cor:asymptotic-quark-gluon-angular-momentum-partition` | 2983–3024 | `VERIFIED-CONDITIONAL` | Ji total angular-momentum operator shares spin-two singlet anomalous-dimension matrix; printed 9/50 and 8/25 check. Requires native GPD EMT matching and inherited GPD domain qualification BH-VIIB-G-0143. |
| 112 | `p11:prop:fragmentation-as-singlet-outcome` | 3045–3050 | `FORMALIZED` | Defines required CPTP hadronization channel and states lack of constructed Kraus map. Finite singlet projection alone does not supply out-state probabilities. |
| 113 | `p11:thm:native-fragmentation-hadronization-export` | 3057–3074 | `VERIFIED-CONDITIONAL` | Inclusive charge/momentum conservation is algebraic under CPTP charge/four-momentum-preserving channel; SM1-3,6 and IR separately guard asymptotic hadrons. |
| 114 | `p11:def:distribution-computation-targets` | 3090–3104 | `FORMALIZED` | Prioritizes moments, g_A, sigma_piN and matrix elements as computation targets; sigma term inherits BH-VIIB-G-0140. |
| 115 | `p11:thm:v2210-lit-spacelike-source-jets` | 3109–3141 | `VERIFIED-CONDITIONAL` | Finite path-ordered Wilson transporter yields exactly covariant source jets and Taylor remainder under N+1 differentiability; no exact LFRep or Fock projector assumed. |
| 116 | `p11:cor:v2210-lit-ioffe-ratio-test` | 3158–3173 | `VERIFIED-CONDITIONAL` | Common nonzero state-independent scalar Z cancels in normalized Ioffe ratio; mixing/additive contacts and physical PDF matching explicitly excluded. |
| 117 | `p11:def:native-thermal-partition-function` | 3228–3250 | `FORMALIZED` | Grand canonical finite Haar-singlet strong trace defined on actual finite H_L and conserved charges; no continuum thermodynamic phase assumed. |
| 118 | `p11:thm:finite-thermal-export-exists` | 3252–3255 | `VERIFIED` | Trace of finite self-adjoint H with real chemical sources exists and is strictly positive; external data absent. |
| 119 | `p11:thm:native-thermodynamic-response-bridge` | 3261–3300 | `VERIFIED` | Duhamel derivative of logZ, epsilon=Ts-varpi+mu n, p_mech=T d_V W tested for finite volume-dependent H; p_mech != varpi absent extensivity. |
| 120 | `p11:thm:thermal-trace-anomaly-operator-closure` | 3312–3348 | `VERIFIED-CONDITIONAL` | Complete finite scale insertion identity and conditional Euler law reproduced. Continuum QCD anomaly insertion retains uncomputed R_scale rather than setting it to zero. |
| 121 | `p11:thm:native-qcd-stefan-boltzmann-limit` | 3360–3380 | `VERIFIED-CONDITIONAL` | SB coefficients 16 gluon and 12 quark dof per flavor reproduce pi²(8/45+7Nf/60) only on explicitly certified near-continuum free-gas window. |
| 122 | `p11:prop:v2211-fixed-ceiling-thermal-remainder` | 3387–3411 | `VERIFIED` | Numerical quadratures at multiple r verify printed Bose/Fermi pressure/energy cutoff-tail bounds, occupation truncation formula; does not prove interacting limit. |
| 123 | `p11:rem:v245-gluon-count-singlet-thermal-firewall` | 3424–3437 | `FORMALIZED` | Distinguishes local free gluon helicity factor g=16 from finite exact Haar-singlet thermal trace; no inconsistent product factorization. |
| 124 | `p11:thm:native-low-temperature-pion-gas` | 3440–3458 | `VERIFIED-CONDITIONAL` | Three massless continuum Goldstones give p/T4=pi²/30 and epsilon=3p; source conditions on spontaneously broken phase. Fixed finite L does not yield this endpoint without thermodynamic/local-flat size window. |
| 125 | `p11:def:thermal-export-object` | 3466–3491 | `FORMALIZED` | Finite thermal export tuple and pressure/extensivity branch unambiguously defined; not an external EOS. |
| 126 | `p11:def:native-scalar-shell-thermal-activation-scale` | 3494–3497 | `FORMALIZED` | Log temperature reference coordinate carries no physical Tc or shell scaling; source rejects count-to-temperature identification. |
| 127 | `p11:def:native-thermal-crossover-readout` | 3499–3513 | `FORMALIZED` | Finite response and maximizer mathematically defined. If h is dimensionful H-source, Sigma=V^-1 d_h logZ is not conventional condensate <O>/V: differs by factor 1/T; physical crossover identification needs source convention (BH-VIIB-G-0144). |
| 128 | `p11:prop:thermal-activation-shell-amplitude` | 3515–3524 | `VERIFIED` | A dimensionless shell coefficient alone cannot set a temperature without dimensionful H or source; no physical number derived. |
| 129 | `p11:prop:native-transition-scaling` | 3530–3541 | `VERIFIED` | Finite analytic positive partition forbids fixed-L nonanalytic phase transitions; Gaussian countermodel shows u↦-u does not select crossover. |
| 130 | `p11:prop:hadronic-rates-native-thermal-averages` | 3547–3564 | `VERIFIED-CONDITIONAL` | Rate average is a typed construction from actual QCD masses, matrix elements and SMAT/IR-qualified cross sections; no computed thermal rates or BBN fits supplied. |
| 131 | `p11:thm:cosmological-export-boundary` | 3576–3579 | `FORMALIZED` | One-way QCD to VI-B cosmological export boundary; not a numerical cosmology prediction. |
| 132 | `p11:def:selected-finite-shell-readout-support` | 3598–3609 | `FORMALIZED` | Definition B_r=Sym^r(C4) at fixed selected carrier; readout r not changed momentum truncation m. |
| 133 | `p11:lem:raw-selected-cell-shell-count` | 3611–3625 | `VERIFIED` | Stars-and-bars dimension binom(r+3,3) and sequence 1,4,10,20,35,56,84 exact for raw symmetric powers. |
| 134 | `p11:rem:first-three-terms-selected` | 3634–3651 | `REPRODUCED` | Source I-A H1 shell 1,4,10 matches raw B0,B1,B2 only in dimensions; no equivariant isomorphism asserted or assumed. |
| 135 | `p11:lem:first-forbidden-coordinate-exclusion-boundary` | 3653–3689 | `VERIFIED` | SU2 x SU2 Clebsch–Gordan returns two chiral 2D and excludes two 6D weight-3/2 sectors; not automatic physical nuclear deletion. |
| 136 | `p11:def:oriented-coordinate-boundary-face` | 3697–3718 | `UNRESOLVED` | P1A defines a chosen X=C eta + F_sigma and only optionally attaches Hurwitz E_sigma after explicit isomorphism. VII-B substitutes trimer E_sigma without source-specified embedding F_sigma to E_sigma. Quotient ranks valid but identity of physical face and actual Gram kernel depends on that map (BH-VIIB-G-0145). |
| 137 | `p11:lem:triangular-rank-coordinate-boundary` | 3720–3737 | `VERIFIED-CONDITIONAL` | For chosen degree-three-onset face eta Sym^(r-1)(F) rank binom(r+1,2) exact; upstream onset r<3=0 is expressly a convention, not geometric inevitability. |
| 138 | `p11:thm:v2211-nuclear-gram-kernel-certificate` | 3746–3762 | `VERIFIED-CONDITIONAL` | Given actual S L=0 and complementary positive Gram floor, ker S=L by linear algebra; physical realized operator must execute the test. |
| 139 | `p11:prop:no-insertion-status-coordinate-boundary` | 3772–3791 | `VERIFIED-CONDITIONAL` | No new physical projector conditional on previously chosen oriented face and actual Gram-kernel test; inherits unresolved E-to-F embedding BH-VIIB-G-0145, and no proof of unique physical selector. |
| 140 | `p11:def:boundary-reduced-finite-shell-support` | 3805–3817 | `FORMALIZED` | Degreewise quotient B_r/L_r at r>=3; not a quotient algebra, as I-A explicitly warns. Distinct orientation signs are alternatives. |
| 141 | `p11:thm:native-boundary-reduced-shell-count` | 3819–3852 | `VERIFIED-CONDITIONAL` | Geometric ranks 1,4,10,14,25,41,63 and twofold CAR capacities 2,8,20,28,50,82,126 reproduce; actual physical nuclear shell ordering not computed; inherits BH-VIIB-G-0145. |
| 142 | `p11:rem:boundary-reduced-shell-count-status` | 3868–3881 | `FORMALIZED` | Explicit mathematical-vs-physical nuclear capacity firewall; no binding energies or isotope stability concluded. |
| 143 | `p11:thm:v2210-lit-complete-duhamel-contacts` | 3887–3903 | `VERIFIED` | Finite matrix Duhamel differentiation includes -beta E(H_ab) contact and positive logarithmic-mean covariance; explicit nonlinear central source has negative Hessian. |
| 144 | `p11:thm:standard-method-import-boundary` | 3968–4002 | `VERIFIED-CONDITIONAL` | Standard external extraction toolbox only processes supplied native finite data under its own theorem hypotheses; the theorem expressly does not compute QCD coefficients. |
| 145 | `p11:prop:hypothesis-audit-standard-imports` | 4019–4052 | `VERIFIED-CONDITIONAL` | Source enumerates specific native-input checks for Feshbach, chiral, anomaly, scattering, LF and thermal methods; all are guard conditions, not discharged physical results. |
| 146 | `p11:thm:exact-scalar-hodge-schur-ledger` | 4057–4063 | `VERIFIED` | Dimensionless incidence/Hodge spectra are independent of physical Yang–Mills form; generalized physical eigenvalues vary under rescaling the latter. |
| 147 | `p11:thm:native-scalar-curvature-krylov-block` | 4069–4080 | `VERIFIED-CONDITIONAL` | Lanczos/Ritz variational property holds for fixed finite selfadjoint Hodge matrix; physical energy identification requires separately supplied positive Yang–Mills/metric pair. |
| 148 | `p11:thm:compact-scalar-glue-singlet-mixing` | 4086–4104 | `VERIFIED-CONDITIONAL` | Flavor multiplicities fix normalized singlet amplitudes sqrt(2/3),sqrt(1/3); displayed real 3x3 matrix is a declared leading compact ansatz, not a computed full scalar spectrum. |
| 149 | `p11:cor:compact-scalar-cubic` | 4110–4137 | `VERIFIED` | 3x3 determinant, Schur fractions, analytic even nondegenerate perturbative glue-root shift and its conditional sign exactly reproduce. |
| 150 | `p11:thm:scalar-two-goldstone-trace-row` | 4147–4160 | `VERIFIED-CONDITIONAL` | Two-Goldstone discontinuity/dispersion is explicitly conditional on computed couplings and a certified positive spectral cut or process unitarity; reduced chiral constants remain free native responses. |
| 151 | `p11:thm:schur-real-part-sheets-residues` | 4170–4234 | `UNRESOLVED` | Dispersion tail integral and simple matrix-pole residue formula check, but real-cut Gamma(s) is not guaranteed holomorphically continuable; sheet formula at complex s needs analytic continuation domain and sheet conventions (BH-VIIB-G-0146). |
| 152 | `p11:thm:isolated-resonance-pole-residue-limit` | 4247–4281 | `VERIFIED-CONDITIONAL` | Rouché argument and matrix residue convergence hold assuming holomorphic continued D_L,D and locally uniform convergence; physical S-matrix pole needs separate SMAT package. Does not discharge BH-VIIB-G-0146 in preceding theorem. |
| 153 | `p11:thm:tensor-pseudoscalar-glue-closures` | 4298–4304 | `REPRODUCED` | Tensor and singlet-anomaly block algebra is valid when source topological cumulants and matching projectors are actually supplied; no numerical topology mass extracted. |
| 154 | `p11:cor:transport-endpoint-closures` | 4310–4315 | `VERIFIED` | Explicit distinct valence measures 2delta_a and delta_(1-2a) obey identical counts/momentum but varying splits; exact transport endpoints remain conditional on their owner packages. |
| 155 | `p11:prop:finite-qcd-benchmark-package` | 4378–4384 | `FORMALIZED` | Proof-status partitions are mutually scoped: finite geometric numbers vs executed nonperturbative matrix readouts and continuum obligations; no native QCD numbers supplied. |
| 156 | `p11:thm:post-gap-finite-carrier-control` | 4422–4428 | `VERIFIED-CONDITIONAL` | Positive uniform gap controls imaginary-time semigroup; exponential spatial clustering requires declared locality/RP and continuum hypotheses; norm-resolvent stability of isolated spectral islands is valid. |
| 157 | `p11:cor:native-pure-glue-comparison-control-derived` | 4434–4443 | `VERIFIED` | Example kappa_L=1/L confirms strictly positive finite gaps need not give uniform infimum; antecedent not falsely marked proved. |
| 158 | `p11:thm:admissible-refinement-stability-finite-readouts` | 4450–4504 | `VERIFIED-CONDITIONAL` | Riesz projection norms/ranks, finite island eigenvalues, source residues, and simple scalar pole/nonzero-overlap criterion follow under stated norm-resolvent hypotheses. |
| 159 | `p11:cor:source-selected-fixed-momentum-state` | 4527–4556 | `VERIFIED-CONDITIONAL` | For actual gauge-singlet physical fixed-plus island, commuting spectral projectors and nonzero source overlap construct a normalized state; convergence requires nonzero limiting overlap and projector/operator norm limits. |
| 160 | `p11:thm:paper-xi-finite-qcd-completion-certificate` | 4595–4614 | `REPRODUCED` | Completion is explicitly limited to a typed finite readout grammar and conditional operator/limit interfaces; state, chiral, uniform gap, area, spectrum and scattering calculations not claimed. |
| 161 | `p11:thm:two-layer-paper-xi-export-paper-xii` | 4654–4660 | `VERIFIED-CONDITIONAL` | Finite operator sequence versus continuum targets are cleanly separated, with quantified limit/RP/gap/area certificates reserved downstream. |
| 162 | `p11:def:pure-g-wilson-continuum-datum` | 4671–4681 | `FORMALIZED` | Finite QCD export defined by existing H, transfer, operators, sources and traces with unexecuted limits and occurrence left conditional. |
| 163 | `p11:def:pure-glue-wilson-curvature-subdatum-paper-xii` | 4683–4697 | `UNRESOLVED` | Pure-glue member can be constructed as a deletion/restriction and vacuum recalculation, but the literal set inclusion D_YM subset D_QCD is not type-correct for the displayed tuples (BH-VIIB-G-0147). |
| 164 | `p11:cor:paper-x-xii-circularity-audit` | 4728–4733 | `VERIFIED` | One-way VII-A to VII-B to VII-C proof-use chronology is sound; backward calibration would violate supplied independent source selection. |
| 165 | `p11:rem:printed-qcd-numerics-source-branch` | 4739–4741 | `FORMALIZED` | Explicitly excludes unconditional nonperturbative decimals; perturbative comparison numbers consume supplied running/mass/scale. |
| 166 | `p11:thm:v164-vacuum-gap-readouts` | 4819–4834 | `VERIFIED-CONDITIONAL` | Symmetric finite ground projector/zero-temperature Gibbs state and transfer-gap logarithm are correct for a positive actual transfer with stated time unit; physical gap beyond carrier remains conditional. |
| 167 | `p11:thm:v164-string-tension-readout` | 4836–4853 | `VERIFIED-CONDITIONAL` | Wilson area readout is stated for generated chart, fixed-loop limit and transfer/RP hypotheses; strictly positive tension requires separate same-action area certificate, not inferred from shape. |
| 168 | `p11:thm:v165-native-carrier-gap-qcd-boundary` | 4855–4869 | `VERIFIED-CONDITIONAL` | Native carrier-support spectral gap distinct from QCD transfer and continuum YM gap; imported carrier gap not re-proven, no physical mass inferred. |
| 169 | `p11:cor:v226-hadron-coefficients` | 4916–4924 | `VERIFIED-CONDITIONAL` | Complete finite momentum response inverse may reconstruct admitted same-source coefficients once an actual complete hadron frame is supplied; native 137 count not full hadron dimension. |
| 170 | `p11:cor:v227-hadron-response` | 4945–4954 | `VERIFIED-CONDITIONAL` | Equality of complete finite meromorphic source responses determines admitted pole/residue comparisons, not all physical eigenvalues outside source-visible sector. |
| 171 | `p11:prop:v338-formal-source-residues` | 4984–5003 | `VERIFIED` | Secular determinant factors linear in t give normalized source numerator, residue slopes and [0,1] bounds of a projector deformation; no physical hadron interpretation. |
| 172 | `p11:prop:v338-native-meson-no-mass-prediction` | 5013–5029 | `VERIFIED` | Independent source coefficients change physical poles with unchanged Hodge/Pfaffian data; contact projector rank does not determine pion/kaon masses. |
| 173 | `UNLABELED:Paper7B:remark:5042` | 5042–5050 | `FORMALIZED` | Optional finite source-owned transfer need not assume RG masses as axioms, but still requires same-action Hamiltonian and source before claiming physical meson spectrum. |
| 174 | `p11:prop:v344-same-action-curvature-extraction` | 5070–5085 | `VERIFIED` | Large-time Euclidean correlators isolate unique lowest source-visible selected masses; log-ratio produces three-channel second difference and cancels constant source scales. |
| 175 | `p11:cor:v344-character-no-hadron-mass` | 5095–5105 | `REPRODUCED` | Petersen three-face eligibility and 1/25 geometric transfer do not determine baryon same-action mass curvature or sign; arbitrary compatible flavor couplings vary curvature. |
| 176 | `UNLABELED:Paper7B:remark:5116` | 5116–5122 | `FORMALIZED` | Real stable ground-state asymptotic is not a complex resonance pole; additional coupled-channel continuation is required. |
| 177 | `p11:prop:v345-f40-no-mass-inference` | 5130–5149 | `VERIFIED-CONDITIONAL` | F40 representation frame reconstruction and mirror-source eligibility are geometric; physical pole requires same-action embedding, source residue and leakage block. |
| 178 | `p11:prop:v349-f40-unique-packet-no-pole` | 5162–5181 | `VERIFIED-CONDITIONAL` | F40 44-coordinate reconstruction and 23 compatibility conditions are imported from P1A and do not imply full-H energy poles; distinct operator sorts kept separate. |
| 179 | `p11:prop:v350-nuclear-cumulative-obstruction` | 5203–5219 | `VERIFIED` | Degreewise 2d ranks differ from cumulative occupancy 2 sum d; exact cumulative sequence 2,10,30,58,108,190,316 reproduced. |
| 180 | `p11:thm:v350-nuclear-physical-spectral-count` | 5229–5249 | `VERIFIED-CONDITIONAL` | Nested genuine nuclear-H spectral projectors of ranks d yield 2d cumulative capacities only with physical intertwiner and twofold spin degeneracy; rank increments check. |
| 181 | `p11:prop:v350-light-ray-owner-qualification` | 5261–5278 | `VERIFIED-CONDITIONAL` | Physical null generator commutes with H under inherited longitudinal commutation; physical light-ray PDF sum rules additionally consume current/EMT Mellin and support/limit certificates, inheriting BH-VIIB-G-0142. |
| 182 | `p11:thm:v350-dglap-fixed-nf-correction` | 5288–5311 | `VERIFIED` | Fixed-n_f DGLAP singlet matrix has zero column sums and stationary eigenvector (3nf,16), giving 9/25,16/25 for nf3 and 9/17 for nf6. |
| 183 | `p11:prop:v356-hadron-effective-mass-error` | 5329–5346 | `VERIFIED` | Finite positive spectral source correlator yields nonincreasing effective mass and explicit exponential residue/visible-gap error bound. |
| 184 | `p11:thm:v356-octa-heat-wilson` | 5357–5378 | `VERIFIED-CONDITIONAL` | Isolated uniform SU(3) heat-face octahedron Z and Wilson fusion series reproduce cited numerical W1,W2, conditional heat-model action not native physical Wilson tension. |
| 185 | `p11:prop:v356-full-hurwitz-character-leading` | 5390–5401 | `VERIFIED-CONDITIONAL` | 24 eight-face octahedral cycles and two fundamental/antifundamental labels yield 24*2*9=432 leading coefficient at heat Casimir exponent 16/3, on uniform 96-face conditional gauge model. |
| 186 | `p11:rem:v356-closed-shell-status` | 5420–5436 | `FORMALIZED` | Printed isolated and Monte Carlo comparators are not same-action or rigorous confidence claims; no physical string tension or QCD mass inferred. |
| 187 | `p11:thm:v357-pair-transfer-shell-gap` | 5444–5477 | `VERIFIED-CONDITIONAL` | Finite destination ground-state nonzero pair-source overlaps isolate E_N+2-E_N; correlator ratio gives energy curvature and finite-time exponential error bound. |
| 188 | `p11:prop:v357-shell-gap-curvature-source` | 5489–5510 | `VERIFIED` | Second difference of a spin-paired one-body reference yields 2(e_K+1-e_K) plus residual curvature; quark-source derivative commutes with finite difference on differentiable branches. |
| 189 | `p11:rem:v357-nuclear-pair-scope` | 5518–5529 | `FORMALIZED` | Explicitly leaves physical pair-overlap, nuclear spectra, and Gram/physical cumulative shell certificates conditional. |
| 190 | `p11:def:v365-hadron-pole-channel` | 5542–5559 | `FORMALIZED` | Defines same-action visible pole and complete channel hyperedge as source/full-resolvent object; requires detector, outgoing states and actual charge/flavor/kinematic projectors. |
| 191 | `p11:prop:v365-pole-leakage-test` | 5561–5570 | `VERIFIED` | 2x2 Feshbach counterexample shows compressed root differs from full pole when leakage B nonzero; reducing subspace B=0 and nonzero overlap suffices to preserve visible pole. |
| 192 | `p11:rem:v365-observable-decay-frontier` | 5581–5594 | `FORMALIZED` | Geometric count/weight comparisons are not exhaustive physical hadron/decay tables and cannot alone imply irreversible widths; physical source/SMAT criteria enumerated. |
| 193 | `p11:prop:v366-prepared-hurwitz-angular-law` | 5606–5629 | `VERIFIED-CONDITIONAL` | Independent CG and spherical-harmonic calculation reproduces prepared J3/2 isotropic and J5/2 quartic distribution and 9/4 axis ratio; physical rotation/source, pure Qchi and partial-wave assumptions explicit. |
| 194 | `p11:prop:v366-hurwitz-decay-residue-gate` | 5644–5663 | `VERIFIED-CONDITIONAL` | Actual pole-to-decay-channel residue and action-owned intertwiner are required; pentagonal rank-3 selection annihilator is geometric, not a physical branching fraction. |
| 195 | `p11:rem:v366-decay-physical-frontier` | 5676–5687 | `FORMALIZED` | Explicitly declines identifying named observed resonances, new widths or physical masses from unprojected finite representation decompositions. |

## Complete canonical issue register (every distinct root, including resolved issue)

Status taxonomy: errors/refutation, missing source certificates, valid conditional physical readout frontiers, or source/evidence typing. No new physical mechanism or theorem was inserted.

### BH-VIIB-G-0134 — MINOR — TYPE_OR_DOMAIN — OPEN

**Earliest matched source location:** `UNLABELED:Paper7B:definition:209`, `Paper7B-QCDReadouts-v1_150.tex:210-214`.

**Exact problem / remaining obligation:** The spectrum of P H P must be understood as the restriction to ran(P), not its full carrier extension with zero complement.

**Direct/negative evidence:** VII-B-B01-E3-DOMAIN-001.

**Effect:** Read literally on the whole space, projection compression introduces spurious zero levels and invalidates positive gap assertions; prose repeatedly indicates intended restricted-block reading.

**Verified material descendants:** None beyond source origin recorded.

**Possible/unconfirmed remote effects:** p11:thm:primitive-channel-loss-hierarchy; p11:cor:numerical-primitive-channel-floors; p11:thm:native-nucleon-mass-eigenvalue; p11:thm:positive-native-nucleon-mass-floor

**Scope firewall:** No claim of failed finite QCD physics if restricted block semantics is understood.

### BH-VIIB-G-0135 — MODERATE — MISSING_CONDITION — OPEN

**Earliest matched source location:** `p11:thm:native-nucleon-mass-eigenvalue`, `Paper7B-QCDReadouts-v1_150.tex:724-738`.

**Exact problem / remaining obligation:** Show that the specified spin/isospin nucleon projector reduces actual H_L, [H_L,P_N,L]=0, on the claimed physical mass-source branch; alternatively identify the exact conserved-charge or source-visible spectral projector being used.

**Direct/negative evidence:** VII-B-B01-E3-REDUCING-001.

**Effect:** A nonreducing isospin projector can have compression eigenvalues different from the poles of actual H. Unequal running quark masses make exact isospin a claim-specific condition, not universal full-QCD conservation.

**Verified material descendants:** None beyond source origin recorded.

**Possible/unconfirmed remote effects:** p11:thm:positive-native-nucleon-mass-floor; p11:cor:dimensionless-baryon-anchor-floor; p11:thm:nucleon-trace-anomaly-bridge

**Scope firewall:** Abstract 3x3 Hermitian witness is a logical boundary test, not an in-grammar full-QCD countermodel; result remains UNRESOLVED, not REFUTED.

### BH-VIIB-G-0136 — MINOR — DAG_COVERAGE — RESOLVED

**Earliest matched source location:** `p11:thm:color-casimir-attraction-channels`, `Paper7B-QCDReadouts-v1_150.tex:384-411`.

**Exact problem / remaining obligation:** Resolve the current imported V-C source theorem by ID, not stale title.

**Direct/negative evidence:** VII-B-B01-E3-CASIMIR-001.

**Effect:** V-C current source calls the cited exact result Short-distance color channels; the numbers are consistent but the quoted title cannot be resolved literally.

**Verified material descendants:** p7v2:prop:color-channels -> p11:thm:color-casimir-attraction-channels -> p11:thm:primitive-channel-loss-hierarchy

**Possible/unconfirmed remote effects:** None recorded.

**Scope firewall:** Locator-only issue, not a claim of false color factors or wrong QCD attraction sign.

### BH-VIIB-G-0137 — MODERATE — INCORRECT_STEP — OPEN

**Earliest matched source location:** `p11:cor:first-two-support-pole-extraction`, `Paper7B-QCDReadouts-v1_150.tex:898-937`.

**Exact problem / remaining obligation:** In an arbitrary complex Gram-orthonormal trial basis the transfer block must be Hermitian; the printed symmetric matrix and eigenvalues with kappa_AB^2 require a real relative-phase convention not contained in the stated hypotheses.

**Direct/negative evidence:** P7B-B02-E3-TRANSFER-001.

**Effect:** A valid positive transfer has real positive eigenvalues but the printed square-root discriminant can be negative if the off-diagonal source overlap is imaginary. Independent general-Hermitian Ritz statements survive.

**Verified material descendants:** None beyond source origin recorded.

**Possible/unconfirmed remote effects:** p11:thm:native-leading-vector-nonet; p11:thm:block-b-finite-pole-dressing

**Scope firewall:** Exact counterexample is a legal 2-dimensional positive finite transfer, not a counterexample to the physical H_L compiler or to Ritz monotonicity.

### BH-VIIB-G-0138 — MODERATE — NORMALIZATION_OR_READOUT — OPEN

**Earliest matched source location:** `p11:cor:derived-perturbative-comparison-package`, `Paper7B-QCDReadouts-v1_150.tex:1072-1092`.

**Exact problem / remaining obligation:** Identify the dimensionful input M_Z^{BH} and precise conventional two-loop Lambda integration definition used to convert the legitimate dimensionless running factor into the printed 206.9499404 MeV; distinguish external measured comparison from native output.

**Direct/negative evidence:** P7B-B02-E3-RUNNING-001.

**Effect:** Without a dimensionful comparison-scale certificate the decimal MeV result is not derivable from alpha_s=1/sqrt72 and universal beta coefficients. Exact independent recalculation reproduces that decimal when mu=91.1876 GeV is supplied.

**Verified material descendants:** None beyond source origin recorded.

**Possible/unconfirmed remote effects:** p11:thm:native-dglap-scale-evolution; p11:thm:asymptotic-quark-gluon-momentum-partition

**Scope firewall:** Two-loop running arithmetic is correct within the asymptotic integration convention; this is provenance of a comparison number, not a refutation of the beta function or a claim that QCD mass scale cannot exist.

### BH-VIIB-G-0139 — MINOR — MISSING_CONDITION — OPEN

**Earliest matched source location:** `p11:lem:v153-scheme-invariant-isolated-pole`, `Paper7B-QCDReadouts-v1_150.tex:836-856`.

**Exact problem / remaining obligation:** Distinguish invariance of determinant-zero multiplicity from pointwise covariance of Laurent residue coefficients; a simple pole or constant regular maps suffice for latter, whereas higher-order principal parts mix with derivatives of analytic maps.

**Direct/negative evidence:** P7B-B02-E3-SCHEME-001.

**Effect:** An analytic nonzero frame factor preserves zero multiplicity but a p-dependent frame can mix double-pole Laurent coefficients; individual residues do not always transform by value-at-pole channel matrices.

**Verified material descendants:** None beyond source origin recorded.

**Possible/unconfirmed remote effects:** p11:cor:native-vector-current-constants; p11:cor:block-b-leading-vector-complex-poles

**Scope firewall:** Algebraic analytic-chart counterexample is at a double pole, not a challenge to stable physical simple pole residues.

### BH-VIIB-G-0140 — MODERATE — MISSING_CONDITION — OPEN

**Earliest matched source location:** `p11:thm:native-scalar-response-bridge`, `Paper7B-QCDReadouts-v1_150.tex:1716-1729`.

**Exact problem / remaining obligation:** For native hadron mass M_h=E_h-E_0, show the scalar insertion used is connected/vacuum-subtracted so its expectation is <h|dH/dm|h>-<0|dH/dm|0>, or establish dE0/dm=0; specify compatible 1/(2M_h) relativistic normalization.

**Direct/negative evidence:** B03-E3-FH-002.

**Effect:** Differentiating vacuum-subtracted physical mass is not the same as differentiating the excited eigenvalue when vacuum energy depends on m_q. Relativistic normalization does not by itself subtract the vacuum.

**Verified material descendants:** p11:thm:native-scalar-response-bridge -> p11:thm:native-dressed-baryon-residues (scalar source branch only)

**Possible/unconfirmed remote effects:** p11:thm:rg-invariant-scalar-bridge; p11:thm:nucleon-trace-anomaly-bridge

**Scope firewall:** Simple finite Hamiltonian counterexample disproves unqualified eigenvalue-to-gap FH inference, not renormalized continuum QCD sigma relations.

### BH-VIIB-G-0141 — MODERATE — MISSING_CONDITION — OPEN

**Earliest matched source location:** `p11:thm:microscopic-topological-baryon-matching`, `Paper7B-QCDReadouts-v1_150.tex:1828-1855`.

**Exact problem / remaining obligation:** Establish an action/current-matched map from the microscopic quark baryon charge to the normalized chiral winding current on the chiral soliton branch; independent conservation and pi3(SU3)=Z do not identify their charges.

**Direct/negative evidence:** B03-E3-WZW-006.

**Effect:** A microscopic determinant singlet has baryon charge 1, but constant U:S3->SU3 has winding 0; deriving their equality requires a physical EFT matching map, not just a shared U1 label. The constant map is a logical independence witness, not a claimed realized baryon.

**Verified material descendants:** None beyond source origin recorded.

**Possible/unconfirmed remote effects:** p11:thm:wzw-baryon-multiplet-quantization; p11:cor:leading-baryon-mass-relations

**Scope firewall:** Does not refute pi3(SU3), winding integrality, WZW hypercharge formula or physical skyrmion descriptions.

### BH-VIIB-G-0142 — MODERATE — MISSING_CONDITION — OPEN

**Earliest matched source location:** `p11:thm:native-pdf-sum-rules`, `Paper7B-QCDReadouts-v1_150.tex:2601-2633`.

**Exact problem / remaining obligation:** In the physical collinear PDF construction without exact R3, establish support/crossing/zero-mode conditions that identify the full local-current and stress-tensor Mellin moments with integrals over 0<=x<=1 for q, antiquark and gluon.

**Direct/negative evidence:** B03-E3-FIXPLUS-018.

**Effect:** VII-B:2565-2595 explicitly denies that physical bilocal theorem proves [0,1] support, yet VII-B:2601-2623 writes 0..1 integrals. Ward identities fix whole Mellin moments, not restricted integrals without the support/crossing bridge.

**Verified material descendants:** None beyond source origin recorded.

**Possible/unconfirmed remote effects:** p11:thm:native-dglap-scale-evolution; p11:thm:native-qcd-factorization-bridge

**Scope firewall:** The toy off-support density is a logical nonimplication witness, not a realized QCD state; physical PDF sum rules are not thereby experimentally refuted.

### BH-VIIB-G-0143 — MINOR — TYPE_OR_DOMAIN — OPEN

**Earliest matched source location:** `p11:thm:native-gpd-unification-bridge`, `Paper7B-QCDReadouts-v1_150.tex:2896-2907`.

**Exact problem / remaining obligation:** Declare x>0 on quark forward H=q branch and the negative-x antiquark continuation H^q(x,0,0)=-qbar(-x), or explicitly define one signed extended q(x) on [-1,1], consistent with earlier 0..1 q and qbar.

**Direct/negative evidence:** B04-E4-GPD-NEG-011.

**Effect:** Same source writes GPD moments on [-1,1] but earlier quark PDFs q_f, qbar_f separately on [0,1]. The all-x forward equality is ill-typed or false without charge-conjugation continuation.

**Verified material descendants:** p11:thm:native-gpd-unification-bridge -> p11:cor:asymptotic-quark-gluon-angular-momentum-partition (Ji operator bridge; not fixed fractions alone)

**Possible/unconfirmed remote effects:** p11:thm:native-qcd-factorization-bridge

**Scope firewall:** No claim that the usual full GPD moments, form factors or Ji sum rule fail with the proper convention.

### BH-VIIB-G-0144 — MINOR — NORMALIZATION_OR_READOUT — OPEN

**Earliest matched source location:** `p11:def:native-thermal-crossover-readout`, `Paper7B-QCDReadouts-v1_150.tex:3499-3513`.

**Exact problem / remaining obligation:** Clarify whether h is a dimensionless source in exponent (then Sigma is intentionally defined as printed) or a dimensionful chiral Hamiltonian mass source h*O (then the physical condensate density is T/V*d_h logZ). Specify whether Tc,L is merely a conventionally chosen response or physical chiral condensate crossover.

**Direct/negative evidence:** B04-E4-CHI-SOURCE-031.

**Effect:** If h enters H as an energy source, d_h logZ carries 1/T. Multiplication by T changes the selected response and potentially its maximizer; source leaves that physical identification unstated.

**Verified material descendants:** None beyond source origin recorded.

**Possible/unconfirmed remote effects:** p11:def:thermal-export-object (T_c,L tuple component); p11:thm:cosmological-export-boundary

**Scope firewall:** Not a counterexample to the definition; no claim that a measured QCD transition temperature is incorrectly calculated because none is printed.

### BH-VIIB-G-0145 — MODERATE — MISSING_CONDITION — OPEN

**Earliest matched source location:** `p11:def:oriented-coordinate-boundary-face`, `Paper7B-QCDReadouts-v1_150.tex:3697-3718; Paper1A-Geometry-v5_168.tex:9208-9234`.

**Exact problem / remaining obligation:** Produce the explicit selected orientation-compatible isomorphism F_sigma≈E_sigma within X≈N_sigma⊕F_sigma, or an established proof that actual Gram-kernel and physical source-map conditions are invariant over allowed identifications. I-A explicitly calls E identification optional, while VII-B substitutes E as an embedded face without its map.

**Direct/negative evidence:** B04-E4-HURWITZ-IDENT-042, B04-E3-SHELL-FACE-037.

**Effect:** Abstract F_sigma and Hurwitz E_sigma are both 3-dimensional, so quotient rank arithmetic is right, but they are not the same embedded subspace until a specific map is declared. Changing complementary embedding changes L3, so an actual S_r can annihilate one but not another.

**Verified material descendants:** p11:def:oriented-coordinate-boundary-face -> p11:thm:v2211-nuclear-gram-kernel-certificate -> p11:thm:native-boundary-reduced-shell-count (physical-capacity route only)

**Possible/unconfirmed remote effects:** p11:prop:no-insertion-status-coordinate-boundary

**Scope firewall:** Does not refute the binomial, triangular, quotient ranks, CAR capacities or conditional Gram-kernel proof. Degree-three onset is a source-stated upstream convention, not here falsely refuted.

### BH-VIIB-G-0146 — MODERATE — MISSING_CONDITION — OPEN

**Earliest matched source location:** `p11:thm:schur-real-part-sheets-residues`, `Paper7B-QCDReadouts-v1_150.tex:4170-4234, especially 4199-4207`.

**Exact problem / remaining obligation:** Establish a channel-local holomorphic continuation of the real-cut discontinuity Gamma^(alpha)(s) to the claimed complex resonance sheet, including cut/end-point domain and sign conventions, or explicitly condition sheet formula on this continuation. Positivity plus the stated tail condition alone do not give such an extension.

**Direct/negative evidence:** B05-E4-CUSP-DENSITY, B05-E3-TAIL-DISPERSION, B05-E3-RESIDUE-MATRIX.

**Effect:** A positive compactly supported cut density with a nonanalytic cusp inside the open cut satisfies the integral and tail hypotheses, but cannot be evaluated as a holomorphic Gamma(s) through that point. A sheet-indexed complex zero needs this additional analytic input.

**Verified material descendants:** None beyond source origin recorded.

**Possible/unconfirmed remote effects:** p11:thm:paper-xi-finite-qcd-completion-certificate (continued resonance route); Paper VII-C SMAT identification only if source continuation route used

**Scope firewall:** No error in algebraic matrix simple-zero residue formula or conditional holomorphic Rouché limit.

### BH-VIIB-G-0147 — MINOR — TYPE_OR_DOMAIN — OPEN

**Earliest matched source location:** `p11:def:pure-glue-wilson-curvature-subdatum-paper-xii`, `Paper7B-QCDReadouts-v1_150.tex:4683-4697`.

**Exact problem / remaining obligation:** Specify a well-typed projection/restriction map from the full finite compiler to the pure-glue Hamiltonian/operator datum and how its vacuum Omega_YM is selected. The displayed YM and full-QCD sets consist of different operators/states on different carriers, so the literal subset inclusion does not hold as written.

**Direct/negative evidence:** B05-E4-PURE-GLUE-TUPLE-TYPE.

**Effect:** Literal set inclusion would equate projected YM operators and vacuum with full-QCD datum entries despite different carrier/ground-state definitions. The intended submodel/functor semantics remain available but need typing.

**Verified material descendants:** p11:def:pure-glue-wilson-curvature-subdatum-paper-xii -> p11:cor:paper-x-xii-circularity-audit (export typing only)

**Possible/unconfirmed remote effects:** Paper VII-C pure-glue continuum/OS export interface

**Scope firewall:** Does not refute construction of a pure-glue finite model or any of the paper’s conditional continuum boundaries.

## Final Batch 5 important replay results

The Duhamel Hessian includes its nonlinear Hamiltonian contact term. Compact scalar 3×3 cubic and the nondegenerate glue root shift agree algebraically, but no scalar mass follows without native source entries. The real-cut spectral tail estimate is valid; a complex continuation additionally needs analytic data `BH-VIIB-G-0146` beyond positivity of the cut density. Rouché and Riesz projector/residue convergence are verified **on their stated holomorphic/norm-resolvent hypotheses**, not as proved QCD occurrence.

The separate pure-glue datum exists as a construction interface only with an actual typed restriction/deletion map and its own vacuum. Literal `D_{YM} ⊂ D_{QCD}` is ill-typed for the displayed lists of distinct operators; see `BH-VIIB-G-0147`. No physical Yang–Mills gap is imported.

At fixed active `n_f=3`, LO singlet momentum fractions are `(9/25,16/25)` and Ji fractions `(9/50,8/25)`, whereas formal `n_f=6` has quark fraction `9/17`. These are not matched native boundary PDFs. Source-visible effective masses and neutron pair transfer formulas produce exact same-action gap/curvature identities only with nonzero overlaps. Degreewise nuclear ranks are not cumulative capacities: independent consecutive quotient shells would yield `(2,10,30,58,108,190,316)`; physical cumulative `(2,8,20,28,50,82,126)` is a **separate conditional nested spectral threshold test**.

Independent `SU(3)` character sums reproduce the isolated uniform octahedron heat weights `W1/W2` and the 24-cell octahedral eight-face count gives the conditional full-shell coefficient `432`. The isotropic `J=3/2` and prepared `J=5/2` quartic angular intensities and the `9/4` axis/diagonal ratio have been independently reconstructed using Clebsch–Gordan and spherical harmonics. They are **not** identified with any observed resonance or decay rate.

## Mathematical integrity and continuation rules

- The target source and all imported paper files remain **byte-for-byte unchanged**. The full G0/GP1–GP3 chain, upstream constitutional checkpoints and their known certificates are not reopened without matched contrary evidence.
- Existing physical/QCD conditions are **reused by reference**. Pending canonical aliases are not silently promoted to unique new foundational assumptions.
- The audit identifies 14 issue roots (13 open and 1 resolved). The single source `REFUTED` statement concerns an unrestricted complex off-diagonal mixing formula (`BH-VIIB-G-0137`); 10 claim dispositions remain `UNRESOLVED` (some because they inherit old issues). The other 11 open issues do not individually refute theorems unless a validated counterexample exists.
- The conditional statements about continuum limits, nuclear realization, decay hyperedges, scattering/SMAT, light-front PDF support and chiral occurrence remain conditional **exactly as scoped by their source**.
- Executed independent E3/E4 tests are evidence for the individual finite formulas, not proof that a native QCD action/continuum phase has been constructed.
- The atlas contains a registered linked VII-B layer with 195 claim records, proof routes, 14 exact gap records, condition usages, source-frozen evidence and typed dependency edges. The combined graph exposes reviewed material paths without promoting citations or guessed cross-paper impacts.

## Audit release and archive hygiene

**New Atlas:** `Paper00-DAGAtlas-v1_118.zip`, derived from supplied Atlas v1_117 and preserving its previous valid paper layers/controlling sources. Its proof/route updates are in `DAG/AuditLayer/Paper7B-v1_1/` and the versioned combined query indices.

**New proof-chain audits:** `Paper00-ProofChainAudits-v1_35.zip`, all previously latest audits plus this one full Paper VII-B report; no duplicate older version of a paper-level audit in the audit ZIP.

**Release validation:** recorded in `DAG/AuditLayer/Paper7B-v1_1/CoverageAndValidation.json` and `DAG/AtlasReleaseValidation-v1_118.json`.


# Paper I-B — Exact Petersen/Desargues/Reye proof completion (audit addendum v1_5)

**Current source:** `Paper1B-ExceptionalGeometry-v1_13.tex` (Paper00-PapersMinimal-v3_021). **Prior audit:** v1_4 including historical v1_10 full census; retained below. **Current resolution layer:** `DAG/AuditLayer/Paper1Resolution-v1_1/Index.json`.

**BH-IBX-EV-0009 — FINITE MATHEMATICAL CLAIMS DISCHARGED BY NEW INDEPENDENT E3 CERTIFICATES.** Four independent, self-contained scripts reconstruct the mathematical groups, graph, incidence and matrix systems rather than importing the audited implementation: `Paper1B-PetersenSL4ExactProof-v1_1.py` (5,555 exact assertions), `Paper1B-ReyeExactProof-v1_1.py` (45), `Paper1B-DesarguesWalkExactProof-v1_1.py` (2,719), and `Paper1B-ThreeCycleExactProof-v1_1.py` (469). **All 8,788 exact assertions pass.** They test 120 signed S5 actions; all 60×60 A5 group-element-pair projector identities; every 200 cyclic C3 coset type; 36×70 and 36×80 Reye incidence ranks; explicit dodecahedral distance-two isomorphism; 120 relabelings of Desargues faces; complete three-cycle matrix and class-frame identities; Lie closure of all 120 triples; fivefold contrast `K_W=-15D5`. The source now records the finite identities in a dedicated proof-certificate paragraph.

**Exactly eleven source claim labels covered:**
  - `p1:thm:v339-petersen-sl4-isometry`
  - `p1:cor:v339-petersen-matrix-symmetric-pair`
  - `p1:thm:v339-petersen-projector-strata`
  - `p1:cor:v340-reye-dodeca-second-neighbour`
  - `p1:thm:v341-desargues-rp2-parity`
  - `p1:prop:v341-walk-kernel-no-petersen-isomorphism`
  - `p1:thm:v342-three-cycle-petersen-overlap`
  - `p1:thm:v342-triangle-petersen-cycle-isometry`
  - `p1:thm:v342-class-frame-three-cycle-tomography`
  - `p1:thm:v342-minimal-path-lie-generators`
  - `p1:prop:v343-fivefold-signed-contrast`

**Scope:** Each new certificate is a reproducible exact proof of the stated **finite mathematical** relationship within the source-supplied marked A5/2I graph/permutation packet. It independently closes the earlier E3 evidentiary deficit for these eleven finite source claims, including the full finite intertwiner. The scripts do **not** prove that the packet occurs physically, that it is selected by GP3 from all possible realizations, or that an unmentioned universal geometric uniqueness theorem holds. Those stronger claims are not certified or silently relabeled as verified.

**BH-IBX-EV-0012 — OPEN.** The historical 43 `REPRODUCED` and 7 `VERIFIED-CONDITIONAL` statements (v1_10) keep their specific non-E3/imported or conditional guards. The subsequent CC18/CC20 mathematical additions to v1_13 are source-integrated but not fully re-audited by this targeted repair. No general Paper I-B formal-claim grade or physical status is promoted. The frozen prior report remains below as history.

---

## Frozen prior audit for provenance (v1_4)

# Paper1B — CC18 current-source scope rebase (Paper1B-ExceptionalGeometryProofChainAudit-v1_4.md)

**Latest source:** `Paper1B-ExceptionalGeometry-v1_11.tex`; SHA-256 `9fedbf89e465b56ff384848ebd732a8e7b678d20e7a1d4beba5b2059afe16ec5`.  **Framework release:** `Paper00-PapersMinimal-v3_019.zip` based on v3.018.  **DAG release:** `Paper00-DAGAtlas-v1_155.zip` based on v1.154.  **Audit collection:** `Paper00-ProofChainAudits-v1_68.zip` based on v1.67.

**Scope and grade:** `SOURCE_INTEGRATED_LOCAL_MATH_CHECKS / NEW_CLAIMS_NOT_FULLY_AUDITED`.  The historical audit below remains valid only for the original source body and the exact original manuscript version it names.  The added CC18 proof statements have formal source labels, precise dependency owners and reproducible finite/exact checks, but **not a fresh exhaustive E3/E4 audit for this entire revised paper**.  No old issue, open physical obligation, or conditional status is silently closed.  No physical occurrence/observable was promoted.

New source-labelled mathematical result(s):
- `p1b:thm:cc18-hopf-150-rule` — source-integrated auxiliary comparison, no physical-owner certificate.
- `p1b:thm:cc18-angular-selection` — source-integrated auxiliary comparison, no physical-owner certificate.
- `p1b:cor:cc18-angular-memory` — source-integrated auxiliary comparison, no physical-owner certificate.
- `p1b:thm:cc18-degree-six-sector-split` — source-integrated auxiliary comparison, no physical-owner certificate.

**Local evidence:** `DAG/SourceUpdates/DAGCrossConnections-v1_9/` contains the independent exact-cubature, exact-block, independent facet-geometry and independent nonet reconstruction scripts from supplement v1.9; the release manifest records their replay status and the exact updated source anchors.  The predecessor audit, source text before the appended CC18 block, and all predecessor issue ledgers are preserved as provenance; source hash changed and must not be mistaken for E0 equality to the old manuscript.

---

## Historical audit retained verbatim (not current-version re-certification)

# Born–Hopf Geometry I-B — Final Rigorous Proof-Chain Audit (current v1.10)

**Audit file:** `Paper1B-ExceptionalGeometryProofChainAudit-v1_3.md`  
**Target manuscript:** `Paper1B-ExceptionalGeometry-v1_10.tex`  
**SHA-256:** `e02e868b02dc3e22bbfae8b4563d7586646f2dc0f215145674dff5fea10854d5`  
**Current supplied papers:** `Paper00-PapersMinimal-v3_018.zip`  
**Current paired outputs:** `Paper00-DAGAtlas-v1_154.zip`; `Paper00-ProofChainAudits-v1_67.zip`  
**Protocol:** `Paper00-RigorousVerificationDAGWorkProtocol-v2_4.md` plus ProofChain Audit Protocol v1.1.

## Bounded scope and completeness

One manuscript, 506/506 formal current statements. 483 inherited claims source-normalized with their earlier theorem and proof blocks, and 23 new v1.10 formal claims freshly audited. Other papers checked only as specific imported prerequisites or reference owners; no other manuscript claimed re-audited. Source is unchanged and the audits integrate mathematical certificates only.

| Final claim status | Count | What it means |
|---|---:|---|
| VERIFIED | 341 | Matched previous or fresh verification under the exact finite mathematical statement scope |
| VERIFIED-CONDITIONAL | 7 | Verification is restricted by explicitly documented hypotheses, including 600-chamber register source assumptions |
| REPRODUCED | 43 | Source argument/computation replays but full independent/global imported-scope evidence is not established |
| FORMALIZED | 115 | Definitions and formal scope/owner statements |
| **TOTAL** | **506** | **Full source disposition; not universal physical completion** |

### Six-batch coverage

| Audit batch | Claimed ordinal range | Statements | Outcome |
|---|---|---:|---|
| 1 | 484–506 (v1.10 new) | 23 | 12 verified, 5 verified-conditional, 6 formalized |
| 2 | 1–100 | 100 | 83 verified (six newly supplied evidence certificates), 17 formalized |
| 3 | 101–200 | 100 | 73 verified, 27 formalized |
| 4 | 201–300 | 100 | 75 verified, 25 formalized |
| 5 | 301–400 | 100 | 62 verified, 17 reproduced, 21 formalized |
| 6 | 401–483 | 83 | 36 verified, 26 reproduced, 19 formalized, 2 verified-conditional |

**Historical source lineage:** `Paper1B-ExceptionalGeometry-v1_9.tex` (483 formal claims) from previous audit v1.2, with older proof certificates retained and checked for source continuity. The older `Paper1B-M8Geometry` audit has a distinct manuscript identity and is not a second active Exceptional Geometry audit.

## Mathematical verification highlights and falsification boundaries

- Exact Petersen and \(\mathfrak{sl}_4\) finite projectors: previous `EV-0009` evidence gap materially narrowed by 2,370 new passing finite tests in Batch 5, but the stronger geometric uniqueness/intertwiner remains an open issue.
- Six previously lost portable certificates `BH-IBX-EV-0001`–`0006` are now rebuilt as self-contained source-matched arithmetic scripts with 66 passing checks in Batch 2; they are marked resolved for this **finite evidence portability obligation**, not as new physical mechanisms.
- New v1.10 results: coherent nonet Gram rank, non-Markovian 25-register exact memory, 41-dimensional *linear* realization, low-band harmonic sampling, 720-point positive cubature. Results remain marked by their existing finite carrier and do not create extra GP3-selected particle states.
- Batch 6: **2145/2145 new non-tautological exact checks** over 21 exact source claims; 19,687 historical controls were earlier replayed and matched to this batch. Tested 24-cell/Fourier incidence, cross-core five-cycles, ADE/Seifert/McKay counts, eta values, quantum-double modular phases, conditional register resistances and Born-even symmetry.
- Two external mathematical references in Batch 6 have confirmed owners in latest sources: `p1:thm:general-left-invariant-hodge-dirac-compiler` in Paper I-A v5.177 and `p1c:prop:v370-e8-finite-certificate` in Paper I-D v1.67. This checks referential ownership, **not independent proof of their full results**.
- Historical v1.9 five-cycle sign erratum is preserved: the incorrect sign was refuted and source corrected; no fresh refutation of current source in this run.

## Issue ledger (19 persistent / registered identifiers)

| Issue ID | Outcome | Exact scope / remaining work |
|---|---|---|
| `BH-IBX-DAG-0001` | **RESOLVED** | RESOLVED_WITH_SCOPED_EVIDENCE |
| `BH-IBX-DAG-0002` | **RESOLVED** | RESOLVED_WITH_SCOPED_EVIDENCE |
| `BH-IBX-EV-0001` | **RESOLVED** | Self-contained source-matched finite E3 verifier and exact controls added in Batch 2; original mathematical scope and provenance retained. |
| `BH-IBX-EV-0002` | **RESOLVED** | Self-contained source-matched finite E3 verifier and exact controls added in Batch 2; original mathematical scope and provenance retained. |
| `BH-IBX-EV-0003` | **RESOLVED** | Self-contained source-matched finite E3 verifier and exact controls added in Batch 2; original mathematical scope and provenance retained. |
| `BH-IBX-EV-0004` | **RESOLVED** | Self-contained source-matched finite E3 verifier and exact controls added in Batch 2; original mathematical scope and provenance retained. |
| `BH-IBX-EV-0005` | **RESOLVED** | Self-contained source-matched finite E3 verifier and exact controls added in Batch 2; original mathematical scope and provenance retained. |
| `BH-IBX-EV-0006` | **RESOLVED** | Self-contained source-matched finite E3 verifier and exact controls added in Batch 2; original mathematical scope and provenance retained. |
| `BH-IBX-EV-0007` | **RESOLVED** | RESOLVED_WITH_SCOPED_EVIDENCE |
| `BH-IBX-EV-0008` | **RESOLVED** | RESOLVED_WITH_SCOPED_EVIDENCE |
| `BH-IBX-EV-0009` | **OPEN** | Claim-matched Petersen finite controls for all 11 named claims added in Batch 5, but full geometric uniqueness / intertwiner remains unverified. |
| `BH-IBX-EV-0010` | **RESOLVED** | RESOLVED_WITH_SCOPED_EVIDENCE |
| `BH-IBX-EV-0011` | **RESOLVED** | RESOLVED_WITH_SCOPED_EVIDENCE |
| `BH-IBX-SRC-0001` | **RESOLVED** | RESOLVED_WITH_SCOPED_EVIDENCE |
| `BH-IBX-MATH-0001` | **RESOLVED** | RESOLVED_WITH_SCOPED_EVIDENCE |
| `BH-IBX-META-0001` | **RESOLVED** | RESOLVED_WITH_SCOPED_EVIDENCE |
| `BH-IBX-DAG-0003` | **RESOLVED** | Current 23 new claims, material edges and exact-check references integrated in current 506-node audit layer and global graph. |
| `BH-IBX-DAG-0004` | **RESOLVED** | 600-chamber legacy completion records reconciled with dependent conditional/reproduced statuses: only specifically evidenced finite identities are discharged. |
| `BH-IBX-EV-0012` | **OPEN** | 43 remaining REPRODUCED and 7 VERIFIED-CONDITIONAL current claims retain exact, claim-specific imported theorem / complete E3/E4 or conditional realization obligations; see AuditClaimLedger status/evidence fields; not a mathematical refutation. |


**Current open issues:** 2 — `BH-IBX-EV-0009` (broader uniqueness/intertwiner), `BH-IBX-EV-0012` (43 reproduced and 7 verified-conditional claim scopes). **Resolved/reconciled:** 17, with all historical records retained. `DAG-0003` is closed by 23-source-node integration; `DAG-0004` is closed as a provenance/status reconciliation **without promoting any 600-chamber dependent claim**.

## Dependency and assumption control

Each current claim maps to one canonical `BH-IBX-EXG::` ID with explicit source location, proof route and status. The original reviewed source-material proof edges remain as E1 links, while the 23 new v1.10 statements add only the independently inspected 30 material edges recorded in Batch 1; no reference-only or citation-only link is promoted automatically. Existing marked geometric assumptions/conditions reuse canonical origins; no second GP3 axiom or physical-source hypothesis introduced.

The two `VERIFIED-CONDITIONAL` inherited chamber statements and five new conditional memory statements retain the chamber/source hypothesis, normalization, linear versus positive realization distinction, and nonphysicality boundary. An exact closed finite 600-chamber transfer does **not** imply physical transition rates or hadronic decay widths.

## Audit method and limitations

E0 source/ZIP hashes and label-owner checks are integrity, **not mathematics**. E1 is line/definition/quantifier replay of current source, E3 consists of exactly scoped independent scripts or genuinely different calculations, and E4 records normalization/domain/selection attacks. The historical evidence scripts replayed in later batches are not counted as fresh independent proof. External ADE, McKay, topology, representation and spectral theorems remain imports where not fully proved afresh; a finite check of their consequence does not certify their global applicability. This audit ran in a single execution with separately recorded evidence functions; **multiple genuinely independent agents are not claimed**.

## Archive release contract

The updated DAG Atlas v1.154 contains the complete source-matched 506-claim layer at `DAG/AuditLayer/Paper1B-ExceptionalGeometry-v1_3/` and registration in the canonical graph. It replaces the superseded active Exceptional Geometry layer, retains the historical distinct M8 audit under its separate namespace, and preserves all other current paper audit data. The accompanying ProofChain Audits v1.67 retains one latest audit per current paper and uses I-B v1.3. Readback validation and manifests are in the DAG release.

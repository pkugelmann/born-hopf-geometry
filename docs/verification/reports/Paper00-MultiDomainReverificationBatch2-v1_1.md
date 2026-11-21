# Multi-domain mathematical source repair and gap reconciliation — Batch 2 (18 Nov 2026)

**Source basis:** `Paper00-PapersMinimal-v3_031.zip` → `Paper00-PapersMinimal-v3_032.zip`.
**DAG:** `Paper00-DAGAtlas-v1_181.zip` → `Paper00-DAGAtlas-v1_182.zip`.
**Audits:** `Paper00-ProofChainAudits-v1_73.zip` → `Paper00-ProofChainAudits-v1_74.zip`.
**Declared scope:** Selected proof obligations, exact current source anchors, local independent mathematical checks and counterexamples. **Not a full-framework proof**, no new unconditional physical occurrence or observed spectrum claimed. Old gap registries and historical proof edges retained.

## Authoritative changed papers

- `Paper7B-QCDReadouts-v1_164.tex` — retain original complex Hermitian `|kappa|^2` mixing; distinguish Ritz transfer energy from actual source-visible full-resolvent pole; add source-residue Schur test (`p11:prop:two-support-full-resolvent-pole-certificate`). Existing `BH-VIIB-G-0148` is source-repaired but its physical-hadron-pole owner is still unresolved.
- `Paper6B-CosmologyReadouts-v1_210.tex` — remove obsolete `J(2)` **active** lineage in favor of the final-octet K48 separator established by VI-A on active j4. Preserve historical n2|n7 jet comparison at its actual scope. Fix `-17g_1/12` to `-17g_1^2/20` in GUT-normalized top Yukawa RGE, clarify reference-subtracted BBN N_eff, guard BBN history existence, portal denominators, adiabatic matter response, zero-energy sound speed and retarded-kernel domains, and correct source-owner attribution to VI-C.
- `Paper6A-GravityCosmology-v2_263.tex` — replace two nonexistent radial-Schur theorem references with the existing conditional full-curvature Schur criterion, repair an overstrong cap-versus-terminal statement into its sourced same-chart coefficient comparison, import exact III-G technical appendix anchors. No new Newton/stress realization is asserted.

## Independent bounded checks

- Cross-domain IV-C / III-C / III-D / VI-C / VII-C and VII-B Schur/mixing checks: **23/23 PASS**, `Proofs/Paper00-MultiDomainReverificationBatch2-v1_1-crossdomain-results.json`.
- Cross-paper cosmological domain, interpolation, branch, RGE, BBN, current and source-anchor checks: **15/15 PASS**, `Proofs/Paper00-MultiDomainReverificationBatch2-v1_1-cosmo-results.json`.
- Thus **38/38 bounded checks** pass. Source hashes and LaTeX build results are tracked separately from mathematical evidence; computational checks do not establish global physical claims.
- Source-locator triage on all 95 originally unreconciled IDs: **58 exact claim labels, 7 distinctive excerpts, 30 without either**, and 6 original source imports moved. This **E0 locator scan is not mathematical closure**.

## Current effective issue statuses (250 distinct issue IDs)

| Status | Count |
|---|---:|
| Prior scoped mathematical/source closures | 28 |
| Reverified local corrections from earlier and current batches | 41 |
| Prior repaired issues retaining explicit owner conditions | 8 |
| Source-repaired awaiting current recheck | 42 |
| DAG-only bookkeeping corrections | 6 |
| Historical resolutions not independently rechecked | 40 |
| Not yet adjudicated on latest source | 83 |
| VI-B cross-paper source pointer corrected, proof/owner not promoted | 1 |
| VII-B trial-pole source defect repaired, physical pole owner pending | 1 |
| **Total** | **250** |

The **41** local corrections are 13 prior plus 17 cross-domain rechecks plus 11 VI-B scope/domain rechecks. The 11 VI-B issue IDs are `BH-G-000118`, `000121`, `000122`, `000123`, `000124`, `000126`, `000128`, `000129`, `000130`, `000131`, `000132`. VI-B `BH-G-000120` is a source attribution/pointer repair only. The 17 other locally rechecked IDs appear in the machine-readable disposition ledger. `BH-VIIB-G-0148` stays in the ledger as a source-repaired, **not physically closed**, issue.

## Essential retained conditions

1. **Constitutional:** GP3 whole-candidate comparison and actual source-role occurrence distinct from established `H_1` and `m_p=1`.
2. **Cosmology:** K48 geometric response is neither an n6 native particle nor proof of the physically observed H/RAR stress and expansion history; actual same-action stress, source/history and calibration must be provided.
3. **Hadron spectroscopy:** Full finite QCD Hamiltonian and source-visible spectral projection are required before an actual hadron pole/mass; a trial block is insufficient. Continuum/locality holds on separate declared assumptions.
4. **Thermal/radiation:** BBN ΔN_eff has an explicitly chosen matched radiation baseline; reactions and initial state require actual native sources.
5. **No history rewriting:** The audit and DAG graph's old OPEN verdicts are historical evidence, not silently overwritten. Effective statuses are an additive layer.

## Reproduction

Use the scripts `Proofs/Paper00-MultiDomainReverificationBatch2-v1_1-crossdomain-verify.py` and `Proofs/Paper00-MultiDomainReverificationBatch2-v1_1-cosmo-verify.py` against the current paper source files. The three current PDFs were rebuilt from TeX with bibliography and complete cross-reference resolution (local checked compilation); the **other 28 PDFs are unmodified**. `Paper00-PapersMinimal-v3_032.zip` contains one latest TeX/PDF pair per each of 31 papers; old AUX versions are retained only for legacy crossrefs.

# Born–Hopf Geometry — QCD current-source issue verification, batch 1 (v1.1)
**Run:** 2026-11-18 · **Current papers:** Paper VII-A `v1_177`, VII-B `v1_163` from PapersMinimal v3.031 · **Parents:** DAG Atlas v1.180 / ProofChainAudits v1.72.

## Scope and meaning
Replayed all 21 previously source-repaired roots of VII-A (8) and VII-B (13) in the current TeX and compared them against their original audit obligations and v1.2 repair-batch reports. **Thirteen specific local formula/typing corrections are reverified**, while **eight still require the explicitly identified real-source or physical-owner premise**. This does not mean 13 complete physical theorems have been derived, nor that the entire two papers passed full E3/E4. The unchanged historical `OPEN` verdicts remain intact; the effective overlay is authoritative only for the issue and exact scope.

**Independent replay:** 36/36 bounded checks passed: 21 source-label/hash anchors plus 15 independent numerical/exact algebra or adversarial checks. The latter are tests of local equations and counterexamples, not a global source-to-foundation E3/E4 certification.

## Issue-by-issue source comparison
| Issue ID | Current TeX label / line | Disposition at original defect scope | What is checked or remains |
|---|---|---|---|
| `BH-G-000134` | `p10:eq:qrg-quark-mass-operator-needed` / 314 | **GUARD RETAINED** | Source import to actual nonzero G0 quark member and running/pole identification not independently discharged |
| `BH-G-000135` | `p10:prop:d4-a2-reading-of-qcd-color-support` / 449 | **LOCAL CHECK VERIFIED** | A2 root sum 2+6=8 in sl3(C); compact real su3 has real dimension 8 |
| `BH-G-000136` | `p10:thm:primitive-scalar-shell-coefficient-fixed` / 1220 | **LOCAL CHECK VERIFIED** | Rayleigh infimum exists for nonzero orthogonal P_sh, finite H=H* |
| `BH-G-000137` | `p10:thm:primitive-scalar-shell-coefficient-fixed` / 1220 | **LOCAL CHECK VERIFIED** | Equality of Rayleigh and semigroup losses requires [P_sh,H_L]=0 |
| `BH-G-000138` | `p10:def:finite-colour-singlet-projector` / 1338 | **GUARD RETAINED** | Representation/truncation invariant under local SU3^V, commutator [P_Gauss,H]=0 and local physical realization remain conditional |
| `BH-G-000139` | `p10:def:native-qcd-generating-functional` / 1562 | **LOCAL CHECK VERIFIED** | for K=e^{-tH}, -(1/t) d log K=dH; d log Tr K=-t <dH> |
| `BH-G-000140` | `p10:eq:finite-susceptibility-readout` / 1721 | **LOCAL CHECK VERIFIED** | nondegenerate ground E0 Hessian includes -<O_AB> contact term |
| `BH-G-000141` | `p10:eq:finite-susceptibility-readout` / 1721 | **LOCAL CHECK VERIFIED** | ground spectral denominator derived for simple isolated E0 and positive spectral gap |
| `BH-VIIB-G-0134` | `UNLABELED:FiniteReadoutGrammar` / 227 | **LOCAL CHECK VERIFIED** | spec(PHP)/RanP removes spurious zero complement |
| `BH-VIIB-G-0135` | `p11:thm:native-nucleon-mass-eigenvalue` / 796 | **GUARD RETAINED** | Actual nonzero P_N with isospin-preserving branch and controlled refinement not constructed by conditional statement |
| `BH-VIIB-G-0137` | `p11:cor:first-two-support-pole-extraction` / 974 | **LOCAL CHECK VERIFIED** | 2×2 Hermitian trial block has /kappa/² not kappa² in eigenvalues |
| `BH-VIIB-G-0138` | `p11:cor:derived-perturbative-comparison-package` / 1149 | **LOCAL CHECK VERIFIED** | computed 2-loop conventional scale is 206.9499404 MeV given M_Z=91.1876 GeV and alpha=1/sqrt72 |
| `BH-VIIB-G-0139` | `p11:lem:v153-scheme-invariant-isolated-pole` / 908 | **LOCAL CHECK VERIFIED** | simple inverse-propagator pole residue conjugates by value-at-pole analytic maps; higher Laurent orders mix derivatives |
| `BH-VIIB-G-0140` | `p11:thm:native-scalar-response-bridge` / 1801 | **LOCAL CHECK VERIFIED** | d(Eh-E0)/dm=<h/Hprime/h>-<0/Hprime/0>, covariant normalization guarded |
| `BH-VIIB-G-0141` | `p11:thm:microscopic-topological-baryon-matching` / 1919 | **GUARD RETAINED** | No actual source-owned current map from microscopic baryon number to winding has been verified |
| `BH-VIIB-G-0142` | `p11:thm:native-pdf-sum-rules` / 2692 | **GUARD RETAINED** | Physical light-ray support/crossing/zero-mode/contact bounds not discharged |
| `BH-VIIB-G-0143` | `p11:thm:native-gpd-unification-bridge` / 2987 | **LOCAL CHECK VERIFIED** | signed-x vector H=-antiquark and axial Htilde=+polarized antiquark reproduce correct first-moment sums |
| `BH-VIIB-G-0144` | `p11:def:native-thermal-crossover-readout` / 3591 | **LOCAL CHECK VERIFIED** | dimensionful H(h)=H+hQ gives Sigma=-T/V d_h logZ=<Q>/V |
| `BH-VIIB-G-0145` | `p11:def:oriented-coordinate-boundary-face` / 3794 | **GUARD RETAINED** | Specific physical source map and isometry-natural nuclear kernel are not inferred from abstract choice |
| `BH-VIIB-G-0146` | `p11:thm:schur-real-part-sheets-residues` / 4266 | **GUARD RETAINED** | Actual channel continuation, boundary-jump convention and resonance pole localization need independent certificate |
| `BH-VIIB-G-0147` | `p11:def:pure-glue-wilson-curvature-subdatum-paper-xii` / 4809 | **GUARD RETAINED** | Actual gauge-compatible deletion/reduction map and YM vacuum/OS/refinement ownership not supplied by conditional definition |

### Targeted mathematical checks and their exact limits
- **VII-A A₂/octets:** `su(3)` has real dimension eight; its complexification `sl₃(C)` has complex dimension eight decomposed into two Cartan plus six root directions. This fixes the original sort/dimension defect; it does not itself establish a physical local gauge sector.
- **VII-A scalar shell:** the nonzero spectral projection makes the Rayleigh infimum well-defined. The finite `H=diag(0,2)` with `P` on `(1,1)/√2` has `γ=1`, Rayleigh loss `1−e⁻¹≈0.63212`, actual transfer loss `1−(1+e⁻²)/2≈0.43233`. Equality needs a reducing projector, as the current source now says.
- **VII-A log sources:** for strictly positive `K=e⁻ᵗᴴ`, `−t⁻¹∂ log K=∂H` and `∂log Tr K=−t〈∂H〉`. A noncommuting two-source Hessian agrees with the Duhamel and source-contact formula. For a simple isolated ground state, `−E₀ʺ` equals the positive spectral response minus `〈Hʺ〉`.
- **VII-B restricted energies:** ambient `PHP` can have artificial zero modes. A rank-one sector of `H=diag(4,9)` has restricted energy 9 despite `PHP` on the full carrier containing a spurious 0. For `P` not commuting with `H`, a Ritz value can be absent from the true spectrum.
- **VII-B mixing:** the Hermitian `[[0.8,0.2i],[-0.2i,0.5]]` has eigenvalues `0.4,0.9`, agreeing with the repaired `|κ|²`. This proves the local algebra, not the exact hadron-pole identification.
- **VII-B perturbative comparison:** substituting the declared external `M_Z=91.1876 GeV` and `α=1/√72` in the printed two-loop convention reproduces `206.9499404 MeV`; it remains external-scale conditional.
- **VII-B scalar response, GPD and thermal:** separate finite demonstrations verify vacuum subtraction in `d(Eₕ−E₀)/dm`, negative-x vector/axial antiquark signs, and `−T/V∂log Z=〈∂H〉/V` on a dimensionful Hamiltonian-source branch. These are not proofs of the sourced physical limit.

## Newly established independent issue — BH-VIIB-G-0148
**Target:** Paper VII-B, `p11:cor:first-two-support-pole-extraction`, current TeX lines 973–1012. The 2×2 compressed transfer formula (978–994) is correct, but lines 986–999 call the resulting values “pole eigenvalues” and “pole masses”, and the proof (1010–1011) applies a pole-mass bridge without requiring the trial span to reduce the full `H_L`.

**Exact admissible counterexample:** Choose a finite self-adjoint full Hamiltonian
\[ H=\operatorname{diag}(0,1,2,4),\qquad t=1,\quad |A\rangle=(e_1+e_3)/\sqrt2,\quad |B\rangle=e_2. \]
The trial supports are non-null, Gram orthonormal, and can lie in the same conserved channel. In this trial span, the transfer block is diagonal with
\[ \lambda_A=(e^{-1}+e^{-4})/2\approx0.19309754,\qquad \lambda_B=e^{-2}. \]
\[ -\log\lambda_A\approx1.64455983,\qquad -\log\lambda_B=2. \]
But the full nonvacuum Hamiltonian spectral poles are exactly `{1,2,4}`; **1.64455983 is not one of them**. The operator has actual spectral poles at 1 and 4 in the correlator of `A`. This is not an attack on the mixing eigenvalue formula and does not introduce a new dynamical assumption. It is an in-domain demonstration that trial compressed transfer eigenvalues need not be actual physical poles.

**Missing edge:** a proof that the trial span reduces the full physical Hamiltonian, or a separate source-visible spectral/pole identification and controlled refinement theorem. **Bounded repair:** keep the outputs as **variational transfer-energy approximants**, consistently with the definition at VII-B lines 933–947 and theorem lines 950–959; identify full poles only with the separately certified spectral projection/limit. This is a proposed source correction, not implemented in the papers.

## Remaining physical-owner cutsets (not silently reopened as local math defects)
The verified local formulas do **not** derive a physical quark-mass source/scale, local vertexwise Gauss block, actual nonzero reducing nucleon sector, matched baryon winding current, full light-ray support/crossing, action-compatible nuclear face map, channel-local resonance continuation, or pure-YM deletion map. The source itself treats these as distinct guarded endpoints, and this batch has not supplied their proof certificates.

## Release rules
No current TeX, PDF, canonical theorem DAG nodes or historical audit gap files are changed. New effective issue dispositions and the new issue live in a linked namespaced reconciliation overlay, with exact current-source hashes. All arithmetic tests are reproducible from `Proofs/Paper00-QCDReverificationBatch1-v1_1-verify.py` in the new atlas (requires NumPy/SciPy).

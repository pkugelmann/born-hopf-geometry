# Born–Hopf Geometry — Planck-curvature consistency and framework source integration v1.5

**Date:** 18 November 2026  
**Source release:** `Paper00-PapersMinimal-v3_036.zip`  
**Graph release:** `Paper00-DAGAtlas-v1_186.zip`  
**Audit release:** `Paper00-ProofChainAudits-v1_77.zip`  
**Supersedes focused report:** `Paper00-PlanckCurvatureConsistency-v1_4.md` (its original frozen-source references remain historical in the preserved text below).  
**Status:** `SOURCE-INTEGRATED; SCOPED-MATH-CHECKED; COMPLETE PHYSICAL NEWTON MATCH STILL OPEN`.

## Effective current-source changes

- `Paper3F-CompleteDynamics-v1_269.tex`: new exact invariance of canonical quadratic source exchange and bounded regular-gapped Schur-residue result; these do not prove full physical matching.
- `Paper5A-FiniteMatterGeometry-v3_214.tex`: positive trace-two weak-gauge bound, including exact primitive 1/96 comparison; no physical gauge compensator generated.
- `Paper6A-GravityCosmology-v2_264.tex`: scalar Einstein variation explicitly identified as a representative; physical common-action source realization kept conditional on the inherited complete metric/source/gauge/boundary comparison.
- `Paper6B-CosmologyReadouts-v1_211.tex`: downstream late-density and static source owner caveat, terminal affine Lambda coefficient distinguished from actual nearby active metric-f(R) root.
- `Macros-v2_187.tex`: active cross-paper version links for all 31 manuscripts; xref aux for changed manuscripts updated.

**Numerical result:** the primitive `U=1/(2 pi ell_scal^2)`, scalar comparison coefficient `hbar c U/8`, native ordinary-trace coefficient `12 hbar c U`, and tested downstream arithmetic remain unchanged. `Paper00-PlanckCurvatureConsistencyChecks-v1_4.py` rerun produced **91/91** scoped passing checks. All four new PDFs compiled and the affected pages were rendered and inspected. This is not an independent global E3/E4 paper audit.

**Earliest still-open dependency:** actual physical projection of the native joint action to the primitive canonically sourced massless tensor exchange while retaining native absolute gauge/matter response and boundary/measure jets. It is registered once at the pre-existing `p3f:prop:v2211-newton-owner-matching` interface, not as a new G0/GP axiom. Neither the pure-metric marked trace nor the conditional numerical readouts certify this source-normalized physical identification. No gap status is changed to CLOSED.

---

## Previous mathematical report v1.4 (preserved as historical derivation)

# Born–Hopf Geometry — primitive-owner Newton projection derivation and obstruction audit v1.4

**Artifact:** `Paper00-PlanckCurvatureConsistency-v1_4.md`  
**Date:** 18 November 2026  
**Supersedes:** `Paper00-PlanckCurvatureConsistency-v1_3.md`  
**Frozen source:** `Paper00-PapersMinimal-v3_034.zip`; exact source `.tex` extracted from that ZIP.  
**Scope:** targeted mathematical *development* and independent counterchecks of the physical source/metric Newton-normalization bridge; not a formal release-wide single-paper DAG audit.  
**Code:** `Paper00-PlanckCurvatureConsistencyChecks-v1_4.py` (91/91 scoped checks; 69 previous preserved, 22 new).  
**Original framework ZIPs:** unchanged; no unproved physical action projection is promoted to certified status.

## Executive result

An **already generated geometric scalar-owner retraction** produces the desired gravitational coefficient exactly, without fitting:

\[
\mathcal H=\mathbb S\otimes F,\quad \dim\mathbb S=4,\;\dim F=48,
\quad \Gamma=\gamma_x\otimes\Gamma_W,\quad
P_+=(I+\Gamma)/2,\quad Z_{\rm rp}=P_+/48.
\]

Then \(\operatorname{Tr}Z_{\rm rp}=2\) and

\[
\boxed{\forall Q_g\in\operatorname{End}(\mathbb S),\qquad
\operatorname{Tr}[Z_{\rm rp}(Q_g\otimes I_F)]
=\frac1{96}\operatorname{Tr}[Q_g\otimes I_F].}
\]

Thus, **as a pure-metric coefficient readout**, \(\kappa_{\rm rp}=\kappa_J/96=U/8\), whence **if the physical action and canonical source actually realize this marked readout**,

\[
G_{\mu\nu}=\frac4{\hbar cU}T_{\mu\nu}^{\rm can},\qquad
G_N=\frac{c^3}{2\pi\hbar U}.
\]

**Physical-closure verdict: NOT YET DERIVED.** Source papers explicitly state that the native common action uses an ordinary additive trace and raw coefficient \(\kappa_J=12U\). The primitive marked readout is mathematically generated, but its **complete physical adoption**, especially gauge/canonical fermion/mixed source and boundary transport, is not established. New no-go results below show why a uniform projected trace, an invertible field reparametrization, or a gapped analytic Schur complement do not by themselves close the physical Newton observable.

The user's primitive \(U=R_p=1/(2\pi\ell_{\rm scal}^2)\) remains unchanged. The 96 is a distinct represented-action multiplicity.

## 1. Actual source chain

| Source | Exact source location in 18 Nov release | Result / role |
|---|---|---|
| Paper I-C | `Paper1C-M8Geometry-v1_142.tex:17873–17948`, `p1b:thm:v130-canonical-owner-retraction` | \(\epsilon_F=\operatorname{Tr}_F/48\) uniquely unital under full internal-unitary conjugation, with amplification-invariant *scalar owner*; theorem does not select a spectral action |
| Paper I-C | `Paper1C-M8Geometry-v1_142.tex:19492–19523`, `p1b:prop:v224-retained-primitive` | \(P_+/48\) trace two; exact 1/96 pure-metric trace; **graded correction** survives on interactions/boundaries; physical adoption still an action comparison |
| Paper V-A | `Paper5A-FiniteMatterGeometry-v3_213.tex:8012–8115`, `p5:thm:least-self-adjoint-heat-carrier`, `p5:thm:g24-raw-eh-transport` | Native common heat 192, ordinary raw \(U_J^{\rm raw}=96U\) |
| Paper V-A | `Paper5A-FiniteMatterGeometry-v3_213.tex:8129–8211`, `p5:prop:v2211-raw-newton-coupled-rescaling` and `p5:cor:common-heat-absolute-gauge-normalization` | Ordinary native gauge \(\operatorname{Tr}_F(T_i^aT_i^b)=3k_i\delta^{ab}\), \(k_2=2\), \(g_2^2=2\pi^2\); uniform action scaling changes canonical gauge couplings |
| Paper III-F | `Paper3F-CompleteDynamics-v1_268.tex:6349–6427`, `p3:thm:common-position-spectral-origin` | One generated common position action; full pure-metric and nonmetric/fermion role weights; native Dirac-EH is the physical local action **on its stated scope**, not identical to scalar heat coefficient |
| Paper III-F | `Paper3F-CompleteDynamics-v1_268.tex:5142–5184`, `p3f:prop:v2211-newton-owner-matching` | Scalar coefficient is necessary for scalar Newton identification, but the physical full-action/source projection is outstanding |
| Paper III-F | `Paper3F-CompleteDynamics-v1_268.tex:12659–12788`, `p3f:prop:v224-native-tensor` and `p3f:prop:v224-normalization-transport` | Raw tensor terms, primitive metric normalization dictionary; whole-action marked trace is not a free gravity-only choice |
| Paper III-F | `Paper3F-CompleteDynamics-v1_268.tex:12971–13026`, mixed-boundary weighting test | Fixed boundary trace-two insertion's canonical Einstein/GHY ratio and nonlinear Dirichlet response select incompatible Neumann populations in that restricted mixed collar model |
| Paper III-E | `Paper3E-GravityAction-v1_200.tex:6524–6675`, `p3e:prop:v356-whole-action-jet-criterion` and `p3e:prop:v358-finite-reduction-covariance` | Matching EH coefficient does not match all jets; finite quantum Gaussian reduction has determinant/source-measure correction |
| Paper VI-A | `Paper6A-GravityCosmology-v2_263.tex:828–927`, `p8:thm:reciprocal-position-source-normalization` | Consumer inserts \(\hbar cU/8\) into Einstein variation; physical origin is conditional on previous action projection |

## 2. Rigorous coefficient extraction from existing primitive geometry

Assume only the source's fixed dimensions, involutive relative grading, and trace neutrality \(\operatorname{Tr}_F\Gamma_W=0\). The projector \(P_+=(I+\Gamma)/2\) has rank 96, so its normalized insertion \(Z_{\rm rp}=P_+/48\) has trace 2. For any pure metric endomorphism \(Q_g\otimes I_F\),

\[
\begin{aligned}
\operatorname{Tr}_{\mathbb S\otimes F}\left[\frac{P_+}{48}(Q_g\otimes I_F)\right]
&=\frac1{96}\bigl[\operatorname{Tr}_{\mathbb S}Q_g\operatorname{Tr}_F I_F
+\operatorname{Tr}_{\mathbb S}(\gamma_x Q_g)\operatorname{Tr}_F\Gamma_W\bigr]\\
&=\frac12\operatorname{Tr}_{\mathbb S}Q_g
=\frac1{96}\operatorname{Tr}_{\mathbb S\otimes F}(Q_g\otimes I_F).
\end{aligned}
\]

The source-native EH coefficient is \(\kappa_J=12U\). By linearity of the pure metric heat coefficient in the trace:

\[
\boxed{\kappa_{\rm rp}=\frac1{96}(12U)=\frac U8.}
\]

On a chart where \(S_{g,\rm phys}=(\hbar cU/8)\int\sqrt{-g}R\) and the same actual action has the canonical Hilbert source \(\delta S_{m,\rm phys}=-\tfrac12\int\sqrt{-g}\,T_{\mu\nu}^{\rm can}\delta g^{\mu\nu}\), stationarity gives \(G_{\mu\nu}=4T_{\mu\nu}^{\rm can}/(\hbar cU)\). Thus \(G_N=c^3/(2\pi\hbar U)\) in the source's SI normalization. **This final implication has the explicit physical-action antecedent; it is not proof that the actual native ordinary-trace action has that metric/source owner.**

### Important: the complete marked word is not a constant scaling

The primitive readout in Paper I-C is exactly

\[
\boxed{\mathcal I_{\rm rp}=\frac1{96}(\mathcal I_{\rm raw}+\mathcal I_{\rm graded}),\qquad
\mathcal I_{\rm graded}=\operatorname{Tr}(\Gamma_{\rm rel} L e^{-D^2/\Lambda_g^2}).}
\]

The graded term is generally nonzero for interacting and boundary words. A physical projection must also differentiate its moving insertion: for source/metric parameters \(q^a,q^b\),

\[
\begin{aligned}
\partial_{ab}\operatorname{Tr}[Z(q)H(q)]
=\operatorname{Tr}[&Z H_{,ab}+ Z_{,a}H_{,b}+ Z_{,b}H_{,a}+Z_{,ab}H],
\end{aligned}
\]

plus the source-dependent measure and moving domain/boundary terms when present. Equality of the zeroth-order \(R\) coefficient alone is not equality of the physical Hessian, source vertex, or quantum response.

## 3. New no-go: positive trace-two retraction cannot preserve native weak gauge normalization

**Scope:** a single *positive fixed insertion* on the existing 192-dimensional heat carrier, acting on the same Euclidean parity-even generator quadratic as the original ordinary heat action; unchanged weak generators and cutoff, without additional independently generated terms. This is not a no-go for every conceivable nonlocal or sector-selective physical projection.

Let \(T=T_2^a\) be a conventional normalized \(SU(2)_L\) fundamental generator on the source's already generated weak doublets, zero on weak singlets. Then \(\|T^2\|=1/4\). Paper V-A gives the exact index \(\operatorname{Tr}_F(T^2)=3k_2=6\), hence

\[
Q_2=I_{\mathbb S}\otimes T^2\succeq0,\quad
\|Q_2\|=\tfrac14,\quad
\operatorname{Tr}_{\mathcal H}Q_2=4\cdot6=24.
\]

For any positive \(Z\succeq0\) with \(\operatorname{Tr}Z=2\), the operator inequality \(0\le Q_2\le\tfrac14I\) yields

\[
0\le\operatorname{Tr}(ZQ_2)\le\frac14\operatorname{Tr}Z=\frac12.
\]

Therefore

\[
\boxed{\frac{\operatorname{Tr}(ZQ_2)}{\operatorname{Tr}Q_2}\le\frac1{48}<1.}
\]

In particular, the actual primitive insertion \(Z_{\rm rp}=P_+/48\) gives

\[
\boxed{\operatorname{Tr}(Z_{\rm rp}Q_2)=\tfrac14,\quad
\frac{\operatorname{Tr}(Z_{\rm rp}Q_2)}{\operatorname{Tr}Q_2}=\tfrac1{96}.}
\]

For the ordinary parity-even vector heat coefficient, the spin chirality insertion instead contracts the antisymmetric \(\epsilon_{\mu\nu\rho\sigma}F^{\mu\nu}F^{\rho\sigma}\) tensor (a separate parity-odd/graded packet) and cannot replenish the parity-even \(F_{\mu\nu}F^{\mu\nu}\) coefficient. Thus a simple marked heat substitution would change the canonical parity-even gauge coupling squares to \(g_{i,\rm rp}^2=96g_{i,\rm heat}^2\). The parity-odd contact and boundary term must still be accounted for, not erased.

This is a **strictly stronger test than a common constant rescaling**: any positive trace-two insertion fails to preserve even the native weak generator quadratic under the stated unchanged-generator assumptions. A physical projection preserving the native gauge coupling therefore needs either a separately generated compensating gauge sector or a nonuniform/sector-aware reduction that is not equivalent to simply inserting \(Z_{\rm rp}\) in every heat term.

The required **parity-even gauge restoration target** under the simple retained-heat comparison, at fixed native source/gauge generators, is \(\Delta S_{\rm YM,even}=(95/96) S_{\rm YM,raw,even}\), plus the appropriate marked contact/boundary terms. This is a *necessary target equation*, **not** an assertion that such a compensator exists or can be inserted.

## 4. New no-go: invertible metric coordinate change cannot change the physical Newton exchange

Fix a regular quadratic graviton/source subspace with \(S^{(2)}=\tfrac12 h^TKh-h^TJ\). For any invertible \(A\), put \(h'=Ah\). The **same action** becomes

\[
K'=A^{-T}KA^{-1},\qquad J'=A^{-T}J.
\]

Thus the normalized source-to-source exchange is **exactly invariant**:

\[
\boxed{J'^T(K')^{-1}J'=J^TK^{-1}J.}
\]

As a one-component example, take the raw kinetic coefficient \(K=12U\) and \(h'=\sqrt{96}\,h\). Then \(K'=U/8\), but \(J'=J/\sqrt{96}\), so \(J'^2/K'=J^2/(12U)\). A metric-variable redefinition can make the coefficient *look* correct without changing a canonically measured force. A complete metric-and-source map must be judged on the exchange amplitude, not the graviton coefficient in isolation.

## 5. New bounded Schur test: regular gapped elimination cannot change the leading massless pole residue

For a local weak-field transverse-tensor sector with momentum \(k\), consider a source-native Hessian with \(K_{hh}=\kappa_J k^2+O(k^4)\), an eliminated block \(C(k)=C_0+O(k^2)\) invertible at \(k=0\), and a metric-to-interior mixing \(B(k)=O(k^2)\). These are explicit assumptions (typical of derivative/curvature mixing with a gapped internal sector), not a general property asserted of every Born–Hopf boundary or nonlocal operator. The exact Schur reduction is

\[
K_{\rm eff}=K_{hh}-BC^{-1}B^\dagger
=\kappa_J k^2+O(k^4).
\]

Therefore it does **not** replace \(\kappa_J\) by \(\kappa_J/96\) in the massless spin-two \(1/k^2\) residue. More singular mixing, an extra massless carrier, a nonanalytic boundary kernel, a nontrivial metric/source-incidence map, or a genuinely marked physical action are separate candidates requiring their **actual** native construction and source jets. This result does not exclude them.

For the source's ordinary local metric-f(R) scalaron, the already established conditional weaker bound (v1.3) also prevents a factor-96 Newton rescue from its at-most-4/3 Yukawa enhancement.

## 6. Precise remaining physical bridge, now narrowed

**TARGET:** physical Newton response measured by one canonical generated test body on the source's common clocked low-curvature chart; Paper VI-A `p8:thm:reciprocal-position-source-normalization` as the affected consumer.

**EXACT EXISTING INPUTS:**

1. Native additive common-heat action \(S_J\), with \(\kappa_J=12U\), native YM indices/canonical couplings and canonically normalized matter source.
2. Natural primitive-owner retraction \(Z_{\rm rp}=P_+/48\), yielding \(\kappa_{\rm rp}=U/8\) on pure-metric words.
3. Valid same-action Schur rules, source/metric mixed-jet and quantum-measure criteria; they **do not select the physical application** of that retraction by themselves.

**MISSING EDGE:** a *generated, claim-complete physical action/observable map* from the native ordinary joint action to one actual physical metric, source, gauge and boundary response that simultaneously realizes

\[
\begin{gathered}
\lim_{k^2\to0}\left[k^2\,\Pi_{\rm TT}\,K_{\rm phys}^{-1}(k)J_{B,\rm phys}(k)\right]
\quad\text{with precisely the scalar-owned canonical Newton residue }G_{\rm scal},\\
\text{the native canonical gauge current/kinetic residues},\qquad
\text{and the same canonical test-body rest energy/clock}.
\end{gathered}
\]

Here the actual physical projection must transport the **complete** action/metric/source/boundary/measure jets, not merely produce a matching number in \(\kappa_{\rm rp}\). For a regular stationary reduction, the physical quadratic data are

\[
K_{\rm phys}=K_{hh}-K_{h\xi}K_{\xi\xi}^{-1}K_{\xi h},\qquad
J_{B,\rm phys}=J_{hB}-K_{h\xi}K_{\xi\xi}^{-1}J_{\xi B},
\]

with gauge quotients, zero modes, determinant/contact terms and source normalization included on their actual domains. For a nontrivial marked readout, source derivatives of \(P_+\) and the graded term must also be kept.

**WHY STILL OPEN:** Paper I-C:19521–19523 explicitly says physical adoption is an action comparison; Paper III-F:12783–12788 and Paper V-A:8138–8163 explicitly preserve the gauge/source/firewall; Paper III-E:6554–6563 and 6666–6674 explicitly preserve the physical first/mixed-jet and quantum-measure bridge. No source-derived selector for a *sector-aware complete physical action* meeting all these constraints was established in this run. Thus we cannot infer physical \(G_{\rm scal}\) unconditionally from the current raw action.

**HOW TO CLOSE IT WITHOUT NEW FUNDAMENTAL PRINCIPLES:** identify the **already generated** actual source-cyclic/projected observable in the source-native joint packet whose complete response has the primitive EH residue and native gauge/matter residues. Compute its full spectral metric/source/gauge two-jet—including graded pieces and boundary/measure terms—and compare physical source-to-source exchange; if a derived boundary or stationary Schur operator provides an additional 95/96 gauge-even contribution or altered metric incidence, calculate it explicitly instead of postulating it. This is one missing action-equality/observable-owner certificate, not a request for a new GP axiom.

### Status table

| Statement | Finding |
|---|---|
| 1/96 primitive metric coefficient | **EXACT, SOURCE-DERIVED** (replayed) |
| 2π primitive curvature \(U\) | **PRESERVED** |
| Native gauge absolute couplings unchanged under uniform marked heat replacement | **FALSE in that comparison**, and ruled out by new positive trace-two upper bound |
| Invertible metric reparametrization can change canonical Newton exchange | **FALSE** (exact exchange invariance) |
| Regular gapped analytic Schur sector can reduce massless EH pole by 96 | **FALSE under stated k² mixing/gap hypotheses** |
| A generated nonuniform physical action map exists with required scalar EH plus native gauge/matter | **NOT ESTABLISHED** (not refuted globally) |
| Paper VI-A scalar Einstein variation | **ALGEBRAICALLY VALID, PHYSICALLY CONDITIONAL** pending owner equality |
| Inflation/late-cosmology physical absolute scale | **CONDITIONAL** on same action/observable matching; dimensionless ratios may cancel normalization |

## 7. Verification and provenance

`Paper00-PlanckCurvatureConsistencyChecks-v1_4.py` independently builds a \(192\times192\) relative-graded projector and explicit 12-doublet weak-generator quadratic with \(\operatorname{Tr}_F T^2=6\), checks the 1/96 exact trace and 1/48 upper bound, source-preserving field reparametrization, gapped-Schur residue, and preserves 69 prior numerical/scoped checks. All 91 checks pass. These finite checks verify the displayed algebra in their declared scope; they do not construct a physical Born–Hopf projection or certify quantum gravity.

**Do not update the canonical DAG owner status to CLOSED from this report.** The proposal is a focused source-linked result for a subsequent targeted proof-chain repair or physical projection construction.

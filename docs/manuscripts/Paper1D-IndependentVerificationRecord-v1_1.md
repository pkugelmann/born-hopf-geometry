# Paper I-D — preserved independent-verification evidence and status record

**Source snapshot:** `Paper1D-TechnicalMaterial-v1_68.tex` from PapersMinimal v3.056.
**Record edition:** v1_1, exported during editorial revision to `Paper1D-TechnicalMaterial-v1_69.tex`.

This is the **original source text of the eleven-issue independent-verification supplement**, retained verbatim in TeX form below. Its four candidate and seven partial labels are **historical audit status**, not a present independent promotion or claim of closure. All mathematical calculations were retained in the edited I-D manuscript under subject headings. Later source-specific propositions remain part of the manuscript; their domains do not turn an audit candidate into a closed claim.

The authoritative DAG and proof-chain auditing archives have **not** been changed here.

## Original independent-verification supplement (verbatim TeX)

```tex
\section*{Independent verification supplement: eleven Paper~I-C proof obligations}
\noindent
This supplement is an independently rederived evidence layer for the
pre-existing source theorems. It preserves the canonical historical issue
identities \texttt{BH-IB-EV-0001}--\texttt{BH-IB-EV-0011}. The four
\emph{candidate certificates} are still subject to final claim-matched
adjudication; the other seven are \emph{partial certificates}. Assertions
not discharged below are explicitly left open. The source statements and
their original proof order remain authoritative.

\paragraph{EV-0001: stable desuspension and fixed-rank scope (partial).}
In the established stable Chern lattice, write
$\Delta=BC-AD$, $c_3=2m\,u_xu_p$ and
$c_4=(\Delta+2nm-6s)\mathcal O$.
If $6\mid(\Delta+2nm)$ choose
$s=(\Delta+2nm)/6$ to obtain the stable rank-four representative with
$c_4=0$. The only obstruction to a nowhere-zero section of an oriented
rank-four complex bundle over an eight-complex is its Euler/top Chern class:
the sphere fiber $S^7$ is $6$-connected and the primary obstruction lies
in $H^8(-;\mathbb Z)$. Splitting the resulting trivial line gives a
rank-three bundle with the required $c_1,c_2,c_3$. Necessity follows from
$c_4(E_3\oplus\underline{\mathbb C})=0$ and the same stable lattice. Thus
\[
 E_3\ \text{exists}\quad\Longleftrightarrow\quad
 6\mid(\Delta+2nm),
\]
\emph{provided} the asserted stable representative exists in the original
stable classification. The independent $\mathbb Z/2$ unstable $SU(2)$ class
on $S^3\times S^3$ is separately detected by
$[S^3\times S^3,BSU(2)]\simeq\pi_6(S^4)\simeq\mathbb Z/2$.
This route does not certify the rank-two existence criterion or exact
fixed-Chern rank-three fiber sizes.

\paragraph{EV-0002: affine mapping and determinant forgetting (partial).}
For the prescribed two-sphere-factor mapping component model, composition
has central coordinates
\[
 (a,b;z)(a',b';z')=(a+a',b+b';z+z'+ab'),
 \qquad z\in\mathbb Z/12.
\]
The secondary $(\mathbb Z/2)^3$ module transforms by
$(r,s,e)\mapsto(r,s,e+br+as)$ in the stated model. At zero Chern data
this yields five secondary orbits: two with $(r,s)=(0,0)$ and one for
each nonzero $(r,s)$. The $12^2$ primary choices give $720$
determinant-preserving classes per specified restriction sector.
The independent finite-minor quotient script agrees on 2,401 tested
integer matrices. Determinant forgetting need not preserve this count:
for $Y=S^1_a\times S^1_b\times S^3_u$ and $c_2=a u$, winding
$h=b$ changes the secondary class by
$\bar h\,\bar c_2=\bar b\,\bar a\,\bar u\ne0$.
The complete eight-dimensional affine action and all ordinary/Born orbit
counts are not certified by these restricted checks.

\paragraph{EV-0003: coherent exchange lifts (partial).}
The involutive smash sphere is $S^3\wedge S^3\simeq S^{3+3\sigma}$.
Suspending the conjugation-equivariant Hopf map yields
$S^{3+3\sigma}\to S^{3+2\sigma}\simeq S(\mathbb C^3)$,
with target involution $\mathrm{diag}(1,1,-1)$.
Pulling back the orthogonal-complement bundle supplies a coherent
\emph{complex} exchange lift of the nontrivial unstable class.
At the fixed locus the two eigenlines have signs $+1$ and $-1$, so the
equivariant determinant is nontrivial; this lift is not principal
$SU(2)$. For a determinant-preserving principal lift the fixed
isotropy must be $\pm I$, with the trivialized case subject to descent
to the symmetric-square quotient. In the stated index convention,
\[
 m_\pm={B^2-A^2\over12}\pm{A+B\over4},\qquad
 24\mid B^2-A^2+3(A+B)
\]
is the stronger principal-$SU(2)$ necessary arithmetic condition.
Exhaustive fixed-class enumeration and equivariant gauge orbit fibers
continue to depend on EV-0002.

\paragraph{EV-0004: relative mixed gluing (partial).}
For the declared mixed $(1,1)$ fixed eigenranks, the diagonal restriction
has $c_1=0$ and
$c_2=A(a_t-a_E)(u_x-u_p)$. Removing a tubular neighborhood of the
fixed locus produces $W$ with boundary; by Poincar\'e--Lefschetz
duality, $H^8(W;G)=0$ for the relevant coefficient systems.
In the adopted \emph{conditional} boundary-coordinate chart,
$T=\mathbb Z/6\oplus(\mathbb Z/2)^2$, $|T|=24$,
with integer image $2\mathbb Z$. Quotient arithmetic gives sizes
$24,12,48,12$ for the four respectively even/trivial,
even/exotic, odd/trivial and odd/exotic cases, and totals $72$ and
$120$ when the two compatible free-region classes are included.
These counts remain conditional on the \emph{actual global} gauge
extensions and the lower-degree equivariant Thom/Cartan--Leray data.
Vanishing top absolute obstruction cannot replace those proofs.

\paragraph{EV-0005: exact icosahedral character overlaps (candidate).}
Fix the source's two $2I$ embeddings related by
$g_\theta=\cos\theta+\mathbf i\sin\theta$ and let
$w=\cos^2\theta\sin^2\theta$. Direct averaging of the finite
binary-icosahedral quaternion-coordinate character moments gives
\[
 F_{12}(w)=1-28w+196w^2-420w^3,
\]
\[
 \begin{aligned}
 F_{20}(w)={}&1-\frac{220}{3}w+\frac{4532}{3}w^2
 -\frac{36212}{3}w^3\\
 &+\frac{119680}{3}w^4-44880w^5.
 \end{aligned}
\]
The only positive-degree invariant lines through degree twenty occur
in degrees twelve and twenty, with multiplicity one. Since
$F_{12}(0)=1$, $F_{12}(1/4)=-5/16$ and
$\gcd_{\mathbb Q[w]}(F_{12},F_{20})=1$, the selected zero of $F_{12}$
annihilates Fourier modes through degree nineteen but not degree
twenty. In the twin $2T$-core completion model the overlap is
$-5/16$ and the independent projector eigenvalues are
\[
 a={275\over8192},\qquad b={525\over8192},\qquad
 \|\mathrm{err}_{19}(n)\|=\sqrt{13(a^{2n}+b^{2n})}.
\]
The group-generated density condition gives convergence to Haar on
continuous scalar tests and strong $L^2$ convergence of averaging
operators, not any physical measure selection. Full adjudication
must explicitly recheck the source embedding conventions.

\paragraph{EV-0006: global complex structures (partial).}
For a nonzero vertical Fourier character $m\in\mathbb Z^4$, the
Dolbeault differential has vertical symbol $\lambda(m)$; the map
$m\mapsto\lambda(m)$ is injective and bounded below by $c|m|$.
The homotopy
\[
 h_m={\sum_j\overline{\lambda_j(m)}\iota_{\bar Z_j}
 \over\sum_j|\lambda_j(m)|^2},\qquad
 \bar\partial h_m+h_m\bar\partial=1
\]
contracts each nonzero vertical Fourier component and preserves smooth
Fourier convergence. Only the torus-invariant complex survives.
The independent global normal-form route specializes the known
compact-Lie-group classification to
$\mathfrak{su}(2)^2\oplus\mathfrak u(1)^2$, with two root signs and a
complex structure on the real four-dimensional Cartan--central plane.
This does not by itself reprove the external classification or finish
the source's full $H$-twisted generalized-K\"ahler bracket check.

\paragraph{EV-0007: pluriclosed averaging and canonical descent (candidate).}
The right four-torus acts holomorphically throughout the stated
normal-form family: it rotates the two roots and fixes the vertical
complex plane. Averaging an arbitrary pluriclosed Hermitian form under
left translations and this compact right torus preserves both
positivity and $\partial\bar\partial\omega=0$. In rank two,
$\mathrm du_1=x$, $\mathrm du_2=y$ gives
$\partial\bar\partial\omega=i\operatorname{Re}(h_{1\bar2})xy$;
positive diagonal $H$ provides a solution. In rank one,
$\mathrm du=x+\tau y$, $\mathrm dv=0$, $\operatorname{Im}\tau\ne0$,
\[
 \partial\bar\partial\omega
 =i h_{1\bar1}\operatorname{Re}\tau\,xy,
\]
so positivity implies the sharp condition $\operatorname{Re}\tau=0$.
The two holomorphic vertical translation fields globally trivialize
$T^{1,0}_{M_8/\mathbb P^1\times\mathbb P^1}$, and the relative tangent
sequence yields
\[
 K_{M_8}\cong\pi^*\mathcal O(-2,-2),\qquad
 H^0(M_8,K_{M_8}^{\otimes m})=0\quad(m\ge1)
\]
by connected compact-fiber descent. This does not promote the
holomorphic model to an independently selected physical background.

\paragraph{EV-0008: homogeneous realization and positive sampling (candidate).}
Put $G=SU(2)_L\times SU(2)_R$ and
$K=SU(2)_{\mathrm{diag}}$. Each $G$-type
$U_{a,b}=V_{a/2}\otimes V_{b/2}$ has a unique top $K$-type
$V_s$, $s=(a+b)/2$. For normalized equivariant coisometry
$T_{a,b}:U_{a,b}\to V_s$ define
\[
 F_v(g)=\sqrt{\frac{(a+1)(b+1)}{a+b+1}}\,
 T_{a,b}\pi_{a,b}(g^{-1})v.
\]
This is a well-defined section of $G\times_KV_s$, and Schur
orthogonality gives
\[
 \int_G\pi(g)T^*T\pi(g)^*\,dg
 ={a+b+1\over(a+1)(b+1)}\,I,
 \qquad \|F_v\|_{L^2(G/K)}=\|v\|.
\]
For the declared family $H_m=\bigoplus_{a+b\le2m}U_{a,b}$,
sections in the global chart $(q,1)$ have coordinate degree at most
$2m$; their pairings have degree at most $4m$. Positive spherical
cubature of strength $t\ge4m$ gives isometric evaluation, and an
$r$-linear coefficient expression of degree $d$ is exact when
$t\ge2rm+d$. More generally, if the specified real coefficient
test space (including constants) has dimension $D$, the integration
functional has a positive atomic representation with at most $D$
points by the finite-dimensional convex-hull argument. Only
operators \emph{included in that coefficient test space} are thereby
transported; no claim about untransported pointwise calculus follows.

\paragraph{EV-0009: TT and Rarita--Schwinger operators (partial).}
The trace-free symmetric-two-tensor fiber rank is $35$; the eight
independent divergence constraints, adjusted by the conformal-Killing
kernel, reproduce the Clebsch--Gordan TT multiplicities. The confirmed
product TT heat coefficients include
\[
 A_0^{TT}=27V,\qquad A_2^{TT}=-27V(a+b),\qquad
 A_4^{TT}=V\bigl[\tfrac{129}{2}(a^2+b^2)-45ab\bigr].
\]
On a separate explicit constant-orbital Dirac calculation,
the ambient tangent-spinor block has dimension $128$ and its
$\gamma$-traceless physical subspace has dimension $112$. On that
subspace the matrix identity
\[
 Q^2+\tfrac12PP^*=\Pi_\gamma D_T^2\Pi_\gamma
\]
holds in the tested convention. The apparent ambient $16$-dimensional
$Q$ kernel is entirely the \emph{excluded gamma-trace complement}:
there are \emph{no genuine $Q$ zeros in this tested constant-orbital
block}. This is not an all-orbital constrained RS spectral proof;
transversality and the full product zeta/heat family remain open.

\paragraph{EV-0010: finite quotients and degree-twelve branching (partial).}
For a free isometric finite action the quotient heat kernel relative
to Riemannian volume is the image sum; for probability-normalized
measures it is the corresponding finite average. For
$q\mapsto aqb^{-1}$ a fixed point requires conjugate $a,b\in SU(2)$,
equivalently $\operatorname{Re}a=\operatorname{Re}b$; a simultaneous
affine torus action requires solving its own congruences.
The independent degree-twelve rational pencil has
\[
 f_6=z(z^4-1),\quad f_8=z^8+14z^4+1,\quad
 g_{12}=z^{12}-33z^8-33z^4+1,\quad u_{12}=f_6^2,
\]
with homogeneous lifts implicit. Symbolic identities
\[
 f_8^3=g_{12}^2+108u_{12}^2,\qquad
 u_{12}'g_{12}-u_{12}g_{12}'=-2f_6f_8^2
\]
give a basepoint-free degree-twelve pencil with six index-two and
eight index-three ramification points. Riemann--Hurwitz gives
$6+16=22=2(12)-2$; the product degree is $144$, ramification
class $22(h_x+h_p)$ and squared pulled-back anticanonical class
$288$. Exhaustive nonfree/correlated stabilizer strata, and their
orbifold kernels, remain a distinct independent-proof obligation.

\paragraph{EV-0011: midpoint Yang--Mills Hessian and gauge quotient (candidate).}
Use $[e_a,e_b]=(2/R)\epsilon_{abc}e_c$,
$[I_a,I_b]=\epsilon_{abc}I_c$ and
$A_B(e_a)=I_a/R$. The midpoint curvature is
$F_B(e_a,e_b)=-\epsilon_{abc}I_c/R^2$ in the stated convention.
The gauge-fixed Weitzenb\"ock Hessian and ghost are
\[
 \begin{aligned}
 R^2H_{\rm gf}&=(2L+S+T)^2+2+2S\cdot T
 =2J(J+1)+2j(j+1)-2,\\
 R^2\Delta_{\rm gh}&=(2L+T)^2
 =2k(k+1)+2j(j+1)-2.
 \end{aligned}
\]
Independent $j=0,\tfrac12,1$ spin matrices reproduce the printed
vector and ghost eigenvalues. At a Yang--Mills critical point the
unfixed Hessian annihilates infinitesimal gauge directions; thus
the gauge-fixed Hessian restricted to their image agrees with
the positive scalar ghost, so it is legitimate to remove these
summands. The $j=0$ quotient retains the unique negative singlet
$-2/R^2$ and positive quintet $10/R^2$; one $j=\tfrac12$ copy
survives at $R^{-2}$; and for $j\ge1$,
$R^2\lambda\ge2j(j+1)-2\ge2$. Hence the classical spatial
Morse index is one, there is no quotient zero mode, and the least
positive eigenvalue is $R^{-2}$. This does not imply a
Lorentzian transition or a populated decay history.

\paragraph{Outstanding adjudication boundary.}
At this supplement's release, the four candidate issue records
\texttt{EV-0005}, \texttt{EV-0007}, \texttt{EV-0008} and
\texttt{EV-0011} are \emph{not} administratively closed; their
independent convention/source-matching certificates require final
review. The other seven remain \emph{open with partial evidence}.
All restricted numerical and exact-arithmetic scripts and their
checksums belong to the separately versioned Paper~I-C gap-closure
evidence archive and the current DAG verification evidence layer.

```

## Original status remark (verbatim TeX)

```tex
\begin{remark}[Reconciled issue status and nonpromotion guards]
The source-specific independent evidence closes the \emph{mathematical
scope} of the marked $2I$ character/cubature calculation (EV-0005),
the stated Hermitian-family pluriclosed and canonical calculation
(EV-0007), the declared finite coefficient-space homogeneous sampling
(EV-0008), and the classical \emph{spatial} midpoint Yang--Mills
Hessian/gauge quotient (EV-0011).  Each retains its source-level
normalizations and selection boundaries.  EV-0001 is discharged only
for rank-three existence; EV-0003 retains the principal $SU(2)$
exchange-lift no-go.  EV-0004 is narrowed by the compatible seeds,
actual low-gauge construction, unpointed lens evaluation, and the
specified natural gauge comparison, but is \emph{not} closed as an
all-components global classification.  EV-0002 remains open for the
complete eight-dimensional secondary affine determinant action.
EV-0006, EV-0009, and EV-0010 remain open outside their verified
restricted scopes.  The numerical NZ.4 directed-rounding certificate
and the finite 490-simplex, F40/Hurwitz/$E_8$ executable artifacts
remain independent reproducibility obligations; the small-cap
inverse-function argument supplies the specified topological
homotopy, \emph{not} those numerical certificates.  No new physical
constructor, occurrence, particle mass or decay rate is asserted.
\end{remark}
```

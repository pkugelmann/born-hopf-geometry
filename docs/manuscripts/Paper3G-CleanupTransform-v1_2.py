#!/usr/bin/env python3
"""Preservation-first editorial transformation of the designated Paper III-G source.
Input: exact Paper3G-TechnicalMaterial-v1_57.tex SHA256 b816daa5...
Outputs: revised .tex, reversible standalone-source annotations CSV, text-edit CSV,
         object/proof/math and cross-reference conservation evidence JSON.
Only source attribution and editorial presentation is changed; inherited labels
and all mathematical expressions and theorem/proof bodies are retained.
"""
from pathlib import Path
import re,csv,json,hashlib,difflib,collections
base=Path(__file__).resolve().parent
src=base/'Paper3G-TechnicalMaterial-v1_57.tex'
assert hashlib.sha256(src.read_bytes()).hexdigest()=='b816daa50d8d88a48ee934f89b3f6e466cb5942e82ec460534b983c499d0e340'
old=src.read_text()
lines=old.splitlines(keepends=True)
original=lines.copy()
edits=[]
# Strict original-line-based substitutions; assert text at each site.
def repl(n, before, after, kind):
    s=lines[n-1]
    if before not in s:raise AssertionError((n,repr(before),repr(s[:200])))
    if s.count(before)!=1:raise AssertionError((n,'nonunique text',before))
    lines[n-1]=s.replace(before,after)
    edits.append({'line':n,'category':kind,'before':s.rstrip('\n'),'after':lines[n-1].rstrip('\n')})

# Current metadata, current macro registry and scope-accurate title date.
repl(63,'Macros-v2_188.tex','Macros-v2_202.tex','cross-reference registry')
repl(73,'Version 1.057 --- 19 November 2026','Version 1.058 --- 20 November 2026','edition metadata')
repl(73,'Framework v3.053','Framework v3.076','current release integration')
repl(78,
    'Paper III-G is the technical owner of auxiliary and optional proof chains transferred from Papers III-A--III-F. Mathematical theorem and proof bodies are preserved with inherited labels and hypotheses; this paper does not add new physical occurrences, fixed sources, calibrated profiles, or cosmological histories. Physical source/action statements remain in their owning main papers.',
    'This technical companion establishes reciprocal-continuation and phase-cell tests, finite spectral and Hopf--Clifford certificates, valuation and Laurent comparisons, conditional gravity-action junctions, and local Schur, heat, and source-response bounds. Exact computations and countermodels distinguish generated geometry from optional selectors, benchmark actions, and calibrated inputs. Finite identities by themselves do not constitute physical source occurrences, observed couplings, or cosmological histories.',
    'abstract publication synopsis')


# Mathematical subject headings, no removal of theorem or proof text.
HEADINGS={
  772:'Dynamical theorem scopes and representation status',
  992:'Conditional finite-carrier and fixed-action selector tests',
  1786:'Conditional lower-ideal momentum-support comparisons',
  2277:'Auxiliary transverse harmonic-window rank tests',
  4426:'Conditional depth-two scalar/tensor K16 comparisons',
  4576:'Smooth hierarchy parameterization and scope',
  4922:'Conditional depth-two least-support comparison',
  6487:'Local versus terminal response ownership',
  8413:'Independent benchmarks, normalizations, and exact certificates',
  8706:'Shell--frame return and a conditional \\(1/96\\) source weight',
}
for n,new in HEADINGS.items():
 oldline=lines[n-1]
 m=re.match(r'(\\(?:subsection|subsubsection|section)\{)(.+)(\}\s*)$',oldline)
 if not m: raise AssertionError(('heading',n,oldline))
 repl(n,m.group(2),new,'section title')

repl(8415,r'\paragraph{Verification index.} The exact original theorem labels',
    r'\paragraph{Verification scope.} The mathematical hypotheses and conclusions', 'verification structure')
repl(8416,
    r'of the auxiliary calculations in Sections~\ref{p3g:sec:constitution}--\ref{p3g:sec:sources} provide the primary verification index.',
    r'in Sections~\ref{p3g:sec:constitution}--\ref{p3g:sec:sources} delimit the exact comparisons below.',
    'verification structure')

# Neutral, mathematical descriptions for separately assumed comparison domains.
CAPTIONS={
 1009:('Legacy finite-carrier selector diagnostic and fixed-action level-one alternative','Finite-carrier selector diagnostic and fixed-action level-one alternative'),
 1806:('Former spectral-lower-ideal finite-role domain','Conditional spectral-lower-ideal finite-role domain'),
 1842:('Historical sharpness of the former finite-role domain','Sharpness of the conditional finite-role domain'),
 1874:('Historical fixed-action alternative inside the former level-one window','Fixed-action alternative inside an assumed level-one window'),
 1981:('Former factor-local momentum support and lower bound','Conditional factor-local momentum support and lower bound'),
 2039:('Former factor-local momentum level, conditional','Factor-local momentum level under an explicit ceiling'),
 2105:('Former finite typed-role realization under explicit shape and level conditions','Finite typed-role realization under explicit shape and level conditions'),
 2149:('Historical compact-cell value and trace stability','Conditional compact-cell value and trace stability'),
 2181:('Historical cell-constitution scope','Conditional cell-constitution scope'),
 2196:('Historical level-one realization and Paper-I-A handoff','Conditional level-one realization and Paper-I-A comparison'),
 2286:('Legacy transverse harmonic-window normalization','Auxiliary transverse harmonic-window normalization'),
 2320:('Legacy two-cutoff auxiliary transverse count','Two-cutoff auxiliary transverse count'),
 2362:('Legacy status of the saturated transverse-count check','Conditional saturated transverse-count check'),
 5036:('Historical depth-two dressed positive-response comparison','Conditional depth-two dressed positive-response comparison'),
 5109:('Historical depth-two coefficient freeze and reflected label','Depth-two coefficient freeze and reflected label'),
 5235:('Historical depth-two K16 third-jet freeze (comparison only)','Depth-two K16 third-jet comparison'),
}
for n,(a,b) in CAPTIONS.items():repl(n,a,b,'formal caption (scope retained)')

# Bring the late six standalone mathematical sections under one self-consistent
# verification chapter, while leaving every section label as-is.
for n in [8421,8484,8706,8858,8905,9020]:
 repl(n,'\\section{','\\subsection{','section hierarchy')
for n in [8907,8959,8979,9003]:
 repl(n,'\\subsection{','\\subsubsection{','section hierarchy')
repl(9098,'\\subsubsection{','\\subsection{','section hierarchy: Maxwell sibling')

# Historical reference ownership corrections verified against active 31-paper
# source labels; original label IDs and the mathematical statements are unchanged.
for n in [1819,1869,2070]:repl(n,'Paper~II-B','Paper~II-F','source owner II-F')
for n in [2074,2256,2780,3366,3466,3486,3492]:repl(n,'Paper~I-A','Paper~I-B','source owner I-B')
for n in [5888,5949,6301,6316,6339,7819,8041,8057]:repl(n,'Paper~I-C','Paper~I-D','source owner I-D')
old_b={
 1375:'I-C',1421:'I-C',3084:'I-C',3098:'I-C',3127:'I-C',3155:'I-C',3172:'I-C',3222:'I-C',3249:'I-C',
 4862:'I-D',4940:'I-D',5021:'I-C',5143:'I-D',5186:'I-D'
}
for n,own in old_b.items():repl(n,'Paper~1B',f'Paper~{own}','source owner '+own)
# Bibliography keys: current source uses deprecated hybrid I-B key; choose
# the exact paper owning the nearest cited theorem, as validated by label map.
ci={982:'I-C',3261:'I-C',4940:'I-D',5022:'I-C',5143:'I-D',5188:'I-D',5892:'I-D',5951:'I-D',6160:'I-C',6218:'I-C',6302:'I-D',6317:'I-D',6340:'I-D',7619:'I-C',7656:'I-C',7704:'I-C',7741:'I-C',7778:'I-C',7820:'I-D',7854:'I-C',7897:'I-C',8042:'I-D'}
for n,own in ci.items():repl(n,'Kugelmann2026Paper1B','Kugelmann2026Paper1'+own[-1],'bibliography paper owner '+own)

# Remove revision-stage prose, not conditional premises or calculations.
# Treat all mathematical displays as immutable, including those in optional
# comparison branches; replace only statements of provenance/development history.
prose={
 606:('The earlier stage remains historically unresolved and is not rewritten as','The smaller-domain conclusion is not retrospectively strengthened as'),
 1086:('That contrast motivated the later revision.  It is historical only: current','The independent current'),
 1897:('Historically this provided an alternative consistency check to the former','This supplies a conditional consistency check to the separately assumed'),
 2188:('This appendix preserves that calculation only as a historical diagnostic.','This calculation is a conditional comparison and does not enter the active seed proof.'),
 2279:('This appendix is retained for provenance of the former auxiliary counting','This subsection studies a separate auxiliary harmonic-counting'),
 2397:('The old THC/SAT branch is retained only as a historical auxiliary diagnostic.','The THC/SAT branch is only an auxiliary rank comparison.'),
 6496:('The historical v1.114 G15 primitive source statement was the v1.113 gate','The separately scoped directed-source identity is'),
 6501:('retained as release provenance only and is superseded by Release v1.117.','not a premise for the terminal deep response.'),
  585:('The superseded \\(\\mathsf P_{\\rm sli}\\) package is retained','The optional \\(\\mathsf P_{\\rm sli}\\) package is used'),
  586:('only as historical selector bookkeeping.  By contrast,','only as a conditional comparison.  By contrast,'),
}
for n,(a,b) in prose.items():repl(n,a,b,'historical prose reframing')
# Remove remaining development narration while retaining each branch's precise
# status as a separately hypothesized mathematical comparison.  Only prose
# changes; all mathematical expressions and inherited references remain in place.
secondary={
  222:('The legacy symbols','The auxiliary symbols'),
  623:('former \\(\\mathsf P_{\\rm sli}\\) route is historical only.','the optional \\(\\mathsf P_{\\rm sli}\\) route is not a premise of this result.'),
  724:('the historical','the auxiliary'),
  994:('The following material records the former tower/fixed-action routes to a','The following comparison tests level-one selection under separately'),
  995:('level-one carrier.  It is retained as a sharp diagnostic of the weaker former','imposed tower and fixed-action premises. It identifies the conclusions'),
  996:('signature only.  The current constitutional route imports','dependent on those premises. The constitutional route independently imports'),
  1047:('This proposition records the former fixed-action alternative.  It is not used by the current constitutional route, because Paper~II-B now derives the momentum carrier directly from the revised GP2 host closure.',
        'This fixed-action alternative is conditional on the supplied level-one window; the independent Paper~II-B momentum-host proof does not consume it.'),
  1086:('In the former selector architecture the vector finite-level problem was treated differently: once the coordinate sector was required, lower-ideal candidates formed a nested family with mathematical lower bound \\(s\\ge1\\), but the old framework did not derive the endpoint \\(s=1\\).  The independent current Paper~II-B derives \\(\\mathcal H_p\\cong\\mathcal H_1\\) directly and reads off \\(m_p=1\\) afterward.',
        'The optional lower-ideal comparison admits nested candidate supports with \\(s\\ge1\\), once the coordinate sector is required, but does not select the terminal member \\(s=1\\). The independent Paper~II-B host theorem establishes \\(\\mathcal H_p\\cong\\mathcal H_1\\) and \\(m_p=1\\).'),
  1788:('The statements in this appendix preserve the former lower-ideal/level-ceiling','The following statements study a separately postulated lower-ideal/level-ceiling'),
  1789:('analysis as a diagnostic of the weaker pre-revision signature.  They are not','domain and its exact consequences. They are not'),
  1791:("Paper~II-B.  Whenever the older prose below says that a level is ``selected'',","Paper~II-B. Any selection statement below is restricted"),
  1792:('it is to be read only inside the explicitly displayed former conditional','to its explicitly displayed conditional'),
  1793:('domain.  In the current chronology,','domain. The independent constitutional result is'),
  1802:('Using any of those later or superseded structures to reselect the momentum','None of these separately conditioned structures may select the momentum'),
  1803:('carrier would be an invalid backward selector.  Their correctly typed','carrier backwards from downstream data. They instead supply'),
  1804:('conditional mathematics may nevertheless remain as historical diagnostics.','conditional mathematical comparisons on their stated domains.'),
  1844:('In the former weaker momentum signature, before canonical-image host closure was adopted, omitting \\(\\mathsf P_{\\rm sli}\\) left the generated scalar and coordinate roles insufficient to force \\(\\mathcal H_1\\).  On one reciprocal factor, the proper',
        'Without the auxiliary lower-ideal premise \\(\\mathsf P_{\\rm sli}\\), the scalar and coordinate constraints alone do not entail \\(\\mathcal H_1\\). On one reciprocal factor, the proper'),
  1865:('In that former signature they were excluded precisely by the complete spectral-lower-ideal rule.  Under the revised GP2 host closure they are already excluded by exact/faithful no-omission of the generated momentum-host content.',
        'They are excluded by the optional complete spectral-lower-ideal rule, or independently by GP2 exact/faithful no-omission of the constituted momentum-host content.'),
  2144:('In that former signature,','Under those auxiliary premises,'),
  2183:('In the former selector architecture,','On the conditional lower-ideal/ceiling domain,'),
  2192:('this former selector','the optional selector'),
  2214:('used to select the level.  Within this former branch, representation-theoretic conclusions depending only on \\(\\mathcal H_1\\) followed by modus ponens; current uses instead import \\(\\mathcal H_p\\cong\\mathcal H_1\\) from Paper~II-B.  The normalized Paper-I-A',
        'used to select the level. Within this conditional comparison, representation-theoretic conclusions depending only on \\(\\mathcal H_1\\) follow from the stipulated endpoint; the independent \\(\\mathcal H_p\\cong\\mathcal H_1\\) result is imported from Paper~II-B. The normalized Paper-I-B'),
  2252:('The historical tag','The notation'),
  2256:('The historical tag','The auxiliary tag'),
  2258:('It is now \\emph{superseded on the reciprocal-position side}:','It does not control the physical reciprocal-position side: '),
  2314:('If one nevertheless retains the historical auxiliary assumptions','Under the separately supplied auxiliary assumptions'),
  2459:('Clifford response.  At the historical III-B stage the maximally mixed','Clifford response. The generic comparison does not determine the maximally mixed'),
  2460:('ultraviolet normalization and the interpolation profile are not derived and','ultraviolet normalization or the interpolation profile; they'),
  2461:('therefore remain explicit forward data in this generic appendix.  This status','remain explicit forward data in this generic comparison. Their status'),
  2462:('is not retroactively changed by later specialization.','is unchanged by an independently constituted specialization.'),
  3941:('The legacy','The auxiliary'),
  4876:('current release Paper~III-F extends it through the generated depth-two','Paper~III-F also establishes the generated depth-two'),
  4877:('coefficient character and thereby replaces the former copied-response action','coefficient character and its distinct inverse-Euler action'),
  4878:('placement by the unique inverse-Euler primitive.  The exact structural','primitive. The exact structural'),
  5033:('used in earlier releases is therefore retained only as an appendix diagnostic,','is a separately conditional comparison,'),
  6276:('the historical local-\\(L\\)/G26-GLOBAL route','a conditional local-\\(L\\)/G26-GLOBAL comparison'),
  6490:('the older','the distinct'),
}
for n,(a,b) in secondary.items():
 if a not in lines[n-1]:
  options=[k for k,line in enumerate(lines,1) if a in line]
  if not options:raise AssertionError(('unlocatable',n,a))
  n=min(options,key=lambda k:abs(k-n))
 repl(n,a,b,'scientific scope prose')
# These old appendix inclusions now form the subsections of a technical paper.
# Preserve all labels and cross-paper references, but do not call subsections appendices.
for i,ln in enumerate(lines,1):
 for a,b in [('This appendix','This subsection'),('this appendix','this subsection'),('In this appendix','In this subsection')]:
  if a in ln:
   repl(i,a,b,'technical-companion terminology')
   ln=lines[i-1]
# For references to III-G subsections, use an honest section-level locator.
for n in [812,2703,8350,8390]:
 if 'Appendix~\\ref' not in lines[n-1]:
  raise AssertionError(('Appendix locator missing',n,repr(lines[n-1])))
 repl(n,'Appendix~\\ref','Section~\\ref','internal subsection locator')

# Reproducible mathematical status without embedding an internal development
# script path in the published theorem (the exact code remains in DAG Atlas).
repl(9080,'heat expansion; finite numerical checks in','heat expansion. Finite checks of its initial coefficients','publication terminology')
repl(9081,'\\texttt{Proofs/Paper00-MultiGapClosures-v1\\_1-verify.py}','','publication terminology')
repl(9082,'validate the first terms, while the analytic theta identity','provide independent corroboration; the analytic theta identity','publication terminology')
repl(9083,'proves all terms.','proves the expansion to all orders.','publication terminology')
repl(6500,'This paragraph is','This identity is','publication terminology')
# The original claimed verifier was never in the supplied current release. Keep the algebra;
# identify the separately supplied moment-only exact replay without asserting missing matrix checks.
repl(8897, 'The standalone exact script is', 'An exact polynomial verification of the axis moments is supplied as', 'reproducibility correction')
repl(8898, r'\texttt{Paper3G-PetersenDynamics-v1\_1-verify.py}', r'\texttt{Paper3G-PetersenMoments-v1\_1-verify.py}', 'reproducibility correction')
repl(8898, 'in the cumulative', 'in the', 'reproducibility correction')
repl(8899, 'update bundle.  No physical Hessian', 'technical supplement. The separate two-core matrix checks require their declared operators and are not a consequence of the moment script alone. No physical Hessian', 'reproducibility guard')
# Preserve historical inline annotations in the same ledger as standalone comments.

# Avoid publication's dependence on a private directory filename; the analytic
# theta identity is already stated and proved and no numerical check is deleted.
repl(9092,'finite numerical checks in','independent finite checks can') if False else None

# Archive only comments that are pure source annotations.  They are not used
# by TeX, but are preserved verbatim in a machine-readable reversible ledger.
comments=[]
for i,s in enumerate(lines,1):
 if s.lstrip().startswith('%'):
  comments.append({'original_line':i,'source':original[i-1].rstrip('\n')})
  lines[i-1]=''
 elif '% stable atlas label; provenance v2_277' in s:
  comments.append({'original_line':i,'source':original[i-1].rstrip('\n')})
  assert s.count('% stable atlas label; provenance v2_277')==1
  lines[i-1]=s.replace('% stable atlas label; provenance v2_277','')

# Preserve formulae while making PDF bookmarks text-safe (heading typography only).
for n,expr,short in [(2798,r'\(E_7\)','E7'),(3388,r'\(E_7\)','E7'),(8706,r'\(1/96\)','1/96'),(9098,r'$S^3$','S3')]:
 repl(n, expr, r'\texorpdfstring{'+expr+'}{'+short+'}', 'pdf bookmark text-safety')
# One final scientific synthesis after the last technical Maxwell result and before bibliography.
conclusion = r'''\subsection{Conclusions and mathematical scope}
The exact certificates collected here are mathematical results on their stated
representation, geometric, spectral, and source/action domains. Conditional
lower-ideal selectors, finite comparison matrices, scalar normalization factors,
and optional interpolation families do not by themselves select physical events,
whole-action couplings, decay processes, or detector outcomes. Actual occurrence
and quantitative observable claims require the corresponding constituted source,
common marked action, and measurement interface in the owning paper. The
negative results, countermodels, and regularity qualifications above are part
of the scope of the results and are not discarded by this technical compilation.
'''
assert lines[-2].strip()==r'\printbibliography' and lines[-1].strip()==r'\end{document}'
lines.insert(len(lines)-2,'\n'+conclusion+'\n')
new=''.join(lines)
# Source-only edits must NOT remove any math displays/inline math. Compare the
# literal math tokens in their original occurrence order (two delimiters, +$).
def maths(s):
 pat=re.compile(r'(?<!\\)\$\$[\s\S]*?(?<!\\)\$\$|(?<!\\)\\\[[\s\S]*?(?<!\\)\\\]|(?<!\\)\\\([\s\S]*?(?<!\\)\\\)|(?<!\\)\$(?:\\.|[^$])*?(?<!\\)\$',re.M)
 return [re.sub(r'\s+',' ',m.group()) for m in pat.finditer(s)]
def objs(s):
 return collections.Counter(re.findall(r'\\begin\{(theorem|proposition|corollary|lemma|definition|remark|proof)\}',s))
def labels(s):return re.findall(r'\\label\{([^}]+)\}',s)
def refs(s):return re.findall(r'\\(?:ref|eqref|Cref|cref|autoref)\{([^}]+)\}',s)
math_before=maths(old);math_after=maths(new)

if math_before!=math_after:
 for j,(m1,m2) in enumerate(zip(math_before,math_after)):
  if m1!=m2:
   print('FIRST MATH DIFF',j,repr(m1[:180]),repr(m2[:180]));break
 assert False, f'Math spans changed old:{len(math_before)} new:{len(math_after)}'
assert objs(old)==objs(new)
assert labels(old)==labels(new)
assert refs(old)==refs(new)
assert new.count('\\printbibliography')==1 and new.rstrip().endswith('\\end{document}')
assert new.count('Kugelmann2026Paper1B')==0
out=base/'Paper3G-TechnicalMaterial-v1_58.tex';out.write_text(new)
with (base/'Paper3G-RemovedSourceAnnotations-v1_1.csv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=['original_line','source']);w.writeheader();w.writerows(comments)
with (base/'Paper3G-EditorialTextChanges-v1_1.csv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=['line','category','before','after']);w.writeheader();w.writerows(edits)
# Proof block changes expose the only body differences; mathematical consistency
# remains a source/audit question, not automatically proved by the edit diff.
proofpattern=re.compile(r'\\begin\{proof\}([\s\S]*?)\\end\{proof\}')
po=proofpattern.findall(old);pn=proofpattern.findall(new)
assert len(po)==len(pn)
proof_diff=[]
for i,(a,b) in enumerate(zip(po,pn),1):
 if a!=b:
  proof_diff.append({'ordinal':i,'before':a.strip(),'after':b.strip()})
(base/'Paper3G-ProofTextChanges-v1_1.json').write_text(json.dumps(proof_diff,indent=2))
# Formal text changes not part of a proof.
for e in edits:
 if e['category'].startswith('formal caption') and e['after'].split(']')[-1]!=e['before'].split(']')[-1]:
  raise AssertionError(e)
evidence={
 'baseline_file':src.name,'baseline_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),
 'output_file':out.name,'output_sha256':hashlib.sha256(out.read_bytes()).hexdigest(),
 'source_line_count_original':len(original),'source_line_count_revised':len(new.splitlines()),
 'comments_archived':len(comments),'editorial_changes':len(edits),
 'formal_objects_original':objs(old),'formal_objects_revised':objs(new),
 'proofs_identical':len(po)-len(proof_diff),'proofs_source_owner_edits':len(proof_diff),
 'labels_original':len(labels(old)),'labels_preserved':labels(old)==labels(new),
 'math_spans_preserved':len(math_before),'math_spans_identical':math_before==math_after,
 'references_original':len(refs(old)),'references_unchanged':refs(old)==refs(new),
 'editorial_change_categories':dict(collections.Counter(e['category'] for e in edits)),
 'standalone_comments_remaining':sum(l.lstrip().startswith('%') for l in new.splitlines())
}
(base/'Paper3G-SourcePreservation-v1_1.json').write_text(json.dumps(evidence,indent=2,default=dict))
print(json.dumps({k:v for k,v in evidence.items() if k not in ('formal_objects_original','formal_objects_revised')},indent=2))

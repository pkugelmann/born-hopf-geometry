#!/usr/bin/env python3
"""Produce a provenance-transparent 2T / 2O / 2I support illustration.

The vertices are the exact quaternionic sets displayed in Paper I-B:
- 2T: 8 quaternion units + 16 half-units;
- 2O: 2T plus 24 pair-coordinate unit quaternions;
- 2I: 2T plus 96 golden-ratio vertices, the 600-cell.
The 2I edge set is the exact nearest-neighbour 600-cell graph (720 edges).
The artwork is a 2D projection only; no group inclusion 2O -> 2I is implied.
"""
import itertools,math
from pathlib import Path
from xml.sax.saxutils import escape
import numpy as np

phi=(1+math.sqrt(5))/2
ptsT=[]
for k in range(4):
 for s in (-1.,1.):
  v=[0.]*4;v[k]=s;ptsT.append(tuple(v))
for signs in itertools.product((-1.,1.),repeat=4):ptsT.append(tuple(a/2 for a in signs))
assert len(ptsT)==24
ptsO=list(ptsT)
for a,b in itertools.combinations(range(4),2):
 for s,t in itertools.product((-1.,1.),repeat=2):
  v=[0.]*4;v[a]=s/math.sqrt(2);v[b]=t/math.sqrt(2);ptsO.append(tuple(v))
assert len(ptsO)==48
ptsI=list(ptsT)
for perm in itertools.permutations(range(4)):
 inv=sum(perm[i]>perm[j] for i in range(4) for j in range(i+1,4))
 if inv%2:continue
 for signs in itertools.product((-1.,1.),repeat=3):
  source=[0.,signs[0]*0.5,signs[1]*phi/2,signs[2]/(2*phi)]
  v=[0.]*4
  for i,pos in enumerate(perm):v[pos]=source[i]
  ptsI.append(tuple(v))
assert len(ptsI)==120 and len(set(ptsI))==120
T=np.array(ptsT);O=np.array(ptsO);I=np.array(ptsI)
assert np.max(abs(np.linalg.norm(I,axis=1)-1))<1.e-12
edgesI=[(a,b) for a in range(120) for b in range(a+1,120) if abs(np.dot(I[a],I[b])-phi/2)<1.e-10]
assert len(edgesI)==720,(len(edgesI),'expected 720')
# Use the shortest angular edge distance among the 48 F4 support points.
dots=np.array([np.dot(O[a],O[b]) for a in range(48) for b in range(a+1,48)])
dist=min((1-x for x in dots if x<1-1.e-12))
edgesO=[(a,b) for a in range(48) for b in range(a+1,48) if abs((1-np.dot(O[a],O[b]))-dist)<1.e-10]
# Rotate four-dimensional points by orthogonal QR; then project into two dimensions.
seed=np.array([[.4, .6,-.5,.3],[.8,-.1,.2,.55],[-.25,.3,.75,.5],[.3,-.6,.4,-.25]])
Q,_=np.linalg.qr(seed)
def project(pts,cx,cy,scale):
 v=pts@Q
 # 4D perspective followed by weak 3D camera shear, an informative projection,
 # not a planar embedding of the 4D edge graph.
 denom=1-0.16*v[:,3]
 return np.c_[cx+scale*(v[:,0]+.27*v[:,2])/denom,cy+scale*(v[:,1]-.23*v[:,2])/denom],v[:,3]
Oxy,Oz=project(O,282,358,145)
Ixy,Iz=project(I,856,358,145)
parts=['''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1150 760" role="img" aria-labelledby="t d">
<title id="t">2O and 2I: two distinct exceptional completions of the 24-element Hurwitz core 2T</title>
<desc id="d">Left: a two-dimensional projection of the 48 quaternionic elements of binary octahedral 2O, with 24 shared Hurwitz elements in gold and 24 complementary elements in mint. Right: a projection of 120 unit quaternions of binary icosahedral 2I, the vertices of the 600-cell, with its 720 exact nearest-neighbour edges. The common Hurwitz core has 24 vertices. The fork does not embed 2O inside 2I.</desc>
<defs>
<linearGradient id="bg" x1="0" x2="1" y1="0" y2="1"><stop stop-color="#102a36"/><stop offset="1" stop-color="#081924"/></linearGradient>
<filter id="glow"><feGaussianBlur stdDeviation="3"/></filter>
</defs>
<rect width="1150" height="760" fill="url(#bg)"/>
<rect x="32" y="115" width="514" height="464" rx="18" fill="#102c36" stroke="#355660"/>
<rect x="603" y="115" width="514" height="464" rx="18" fill="#102c36" stroke="#355660"/>
<text x="44" y="57" font-family="system-ui, sans-serif" fill="#edf7f2" font-size="35" font-weight="700">One Hurwitz core, two exceptional extensions</text>
<text x="45" y="90" font-family="system-ui, sans-serif" fill="#a5bfc5" font-size="17">Unit quaternions on S³ · exact support counts · projected four-dimensional structures</text>
<text x="62" y="152" font-family="system-ui, sans-serif" fill="#eaf8ed" font-size="27" font-weight="700">2O · 48 points</text>
<text x="63" y="180" font-family="system-ui, sans-serif" fill="#a6c8c7" font-size="17">binary octahedral · two 24-cell cosets</text>
<text x="636" y="152" font-family="system-ui, sans-serif" fill="#eaf8ed" font-size="27" font-weight="700">2I · 120 points</text>
<text x="637" y="180" font-family="system-ui, sans-serif" fill="#a6c8c7" font-size="17">binary icosahedral · 600-cell vertices</text>
''']
def paths(pos, depths, edges,accent):
 for a,b in sorted(edges,key=lambda v:float(depths[v[0]]+depths[v[1]])):
  d=(float(depths[a])+float(depths[b]))/2
  op=.11+.15*((d+2)/4)
  # make shared 2T internal edges visible, other links delicate
  iscore=a<24 and b<24
  col='#d8b36c' if iscore else accent
  if iscore:op+=.12
  parts.append(f'<line x1="{pos[a,0]:.1f}" y1="{pos[a,1]:.1f}" x2="{pos[b,0]:.1f}" y2="{pos[b,1]:.1f}" stroke="{col}" stroke-width="{1.0 if iscore else .72}" opacity="{min(.5,op):.3f}"/>')
 # Draw deeper vertices first
 for k in sorted(range(len(pos)),key=lambda k:float(depths[k])):
  core=k<24;col='#f0c775' if core else accent
  r=(3.3 if core else 2.6)*(1+.16*float(depths[k]))
  parts.append(f'<circle cx="{pos[k,0]:.2f}" cy="{pos[k,1]:.2f}" r="{r:.2f}" fill="{col}" opacity="{.85 if core else .76}"/>')
paths(Oxy,Oz,edgesO,'#86dbc6')
paths(Ixy,Iz,edgesI,'#8dc9df')
parts.extend(['''<text x="63" y="535" font-family="system-ui, sans-serif" fill="#d4e4e4" font-size="16">24 in 2T + 24 in the other coset</text>
<text x="638" y="535" font-family="system-ui, sans-serif" fill="#d4e4e4" font-size="16">24 in 2T + 96 golden-ratio vertices</text>
<line x1="575" y1="128" x2="575" y2="579" stroke="#42616e" stroke-dasharray="5 9"/>
<rect x="43" y="612" width="1062" height="106" rx="16" fill="#0b2330" stroke="#466e71"/>
<circle cx="79" cy="647" r="7" fill="#f0c775"/><text x="98" y="653" font-family="system-ui,sans-serif" fill="#eef3e8" font-size="17">2T · 24 common Hurwitz units</text>
<circle cx="439" cy="647" r="7" fill="#86dbc6"/><text x="457" y="653" font-family="system-ui,sans-serif" fill="#eef3e8" font-size="17">2O complement · 24</text>
<circle cx="752" cy="647" r="7" fill="#8dc9df"/><text x="770" y="653" font-family="system-ui,sans-serif" fill="#eef3e8" font-size="17">2I complement · 96</text>
<text x="78" y="688" font-family="system-ui,sans-serif" fill="#9ed7ce" font-size="17" font-weight="650">2T inside 2O</text><text x="326" y="688" font-family="system-ui,sans-serif" fill="#9ed7ce" font-size="17" font-weight="650">2T inside 2I</text>
<text x="630" y="688" font-family="system-ui,sans-serif" fill="#f0c775" font-size="17" font-weight="650">2O not inside 2I · distinct branches</text>
<text x="44" y="748" font-family="system-ui,sans-serif" fill="#839da8" font-size="12">Geometric illustration using exact Paper I-B quaternion coordinates; the 2D view is a projection, not a literal embedding of the four-dimensional cells.</text>
</svg>'''])
output=Path(__file__).resolve().parents[1]/'docs'/'figures'/'exceptional-fork-2o-2i.svg'
output.parent.mkdir(parents=True,exist_ok=True)
output.write_text('\n'.join(parts),encoding='utf8')
print(f'{output.name}: 2T=24, 2O=48 (nearest edges {len(edgesO)}), 2I=120 (600-cell edges {len(edgesI)})')

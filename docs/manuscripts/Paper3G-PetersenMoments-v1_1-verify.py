#!/usr/bin/env python3
"""Exact symbolic replay of the ten-axis A5 second, fourth and sixth moments.

Scope: independently checks the *axis-moment* part of III-G v1.58's
Petersen technical section. It does NOT replay the separate T/B two-core
matrix identities, 15-edge projectors, E36 congruences or physical assertions.
No external empirical input. Requires SymPy.
"""
import hashlib
import json
import sympy as s
from pathlib import Path

x,y,z=s.symbols('x y z')
p=(1+s.sqrt(5))/2
q=1/p
v=s.Matrix([x,y,z]); r2=x*x+y*y+z*z
axes=([s.Matrix((1,1,sg))/s.sqrt(3) for sg in (-1,1)]
    + [s.Matrix((1,-1,sg))/s.sqrt(3) for sg in (-1,1)]
    + [s.Matrix((q,sg*p,0))/s.sqrt(3) for sg in (-1,1)]
    + [s.Matrix((p,0,sg*q))/s.sqrt(3) for sg in (-1,1)]
    + [s.Matrix((0,q,sg*p))/s.sqrt(3) for sg in (-1,1)])
assert len(axes)==10
for a in axes:assert s.simplify(a.dot(a)-1)==0
m2=s.expand(sum(a.dot(v)**2 for a in axes))
m4=s.expand(sum(a.dot(v)**4 for a in axes))
h6=s.expand(sum(a.dot(v)**6 for a in axes)-s.Rational(10,7)*r2**3)
assert s.simplify(m2 - s.Rational(10,3)*r2)==0
assert s.simplify(m4 - 2*r2**2)==0
assert s.simplify(sum(s.diff(h6,w,2) for w in (x,y,z)))==0
h6values=[s.simplify(h6.subs(dict(zip((x,y,z),a)))) for a in axes]
assert all(t==s.Rational(160,1701) for t in h6values)
print(json.dumps({
  'scope':'axis moments only; not two-core action/operator replay',
  'num_axes':len(axes),
  'axis_norms':'10/10 exactly one',
  'second_moment':'10 r^2/3',
  'fourth_moment':'2 r^4',
  'sixth_harmonic_laplacian':'0',
  'sixth_harmonic_at_all_axes':'160/1701',
  'pass':True,
},indent=2))

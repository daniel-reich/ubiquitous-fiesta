
import itertools
def is_vampire(n):
  ns = str(n)
  l = len(ns)
  if l<3: return "Normal Number"
  
  case = lambda p: any(int("".join(p[:v]))*int("".join(p[v:]))==n for v in [l//2,l%2+l//2])
  
  vamp = any(case(p) for p in list(itertools.permutations(ns)))
  
  if not vamp: return "Normal Number"
  if len(ns)%2: return "Pseudovampire"
  return "True Vampire"


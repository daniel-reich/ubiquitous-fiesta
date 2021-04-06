
from itertools import groupby
def can_patch(bridge, planks):
  hole=[i for i in [len(list(g)) for v,g in groupby(bridge) if not v] if i>1]
  hole.sort(reverse=True)
  planks.sort(reverse=True)
  return all([b-a>=-1 for a,b in zip(hole,planks)]) and len(hole)<=len(planks)


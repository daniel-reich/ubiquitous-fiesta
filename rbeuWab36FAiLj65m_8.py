
from collections import defaultdict as dd
def grouping(w):
  d = dd(list)
  for k,v in ((len([y for y in x if y.isupper()]), x) for x in sorted(w,key=str.casefold)):
    d[k].append(v)
  return dict(sorted(d.items()))



from collections import defaultdict
def stem_plot(lst):
  d = defaultdict(list)
  nl = ((str(x//10), str(x%10)) for x in lst)
  for k,v in nl:
    d[k].append(v)
  
  e = {k: " ".join(sorted(v)) for k,v in d.items()}
  return [k + " | " + v for k,v in sorted(e.items(),key=lambda z: int(z[0]))]


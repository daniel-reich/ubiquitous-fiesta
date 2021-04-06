
from collections import defaultdict as dd
​
def map_letters(w):
​
  w = [ (w[i], i) for i in range(len(w)) ]
  w_dict = dd(list)
  
  for k, v in w:
    w_dict[k].append(v)
    
  return dict(w_dict)


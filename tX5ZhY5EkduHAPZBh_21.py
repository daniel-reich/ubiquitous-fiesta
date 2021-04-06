
import numpy as np
def nearest_element(n, lst):
  m = np.min(abs(np.array(lst)-n))
  el = []
  for i in range(0,len(lst)):
    if abs(n-lst[i]) <= m:
      el.append(lst[i])
  return lst.index(np.max(el))


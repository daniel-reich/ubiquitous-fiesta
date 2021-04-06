
def major_sum(lst):
  ps,ns,zc = 0,0,0
  for x in lst:
    if x > 0: ps += x
    elif x < 0: ns += x
    else: zc += 1
  
  result = max(ps,abs(ns),zc)
  if result == abs(ns): return ns
  else: return result


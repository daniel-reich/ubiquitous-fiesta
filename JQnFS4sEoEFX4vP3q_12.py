
import itertools
def product_pair(lst, k):
  if len(lst)<k:
    return None
  l=[]
  for x in list(itertools.combinations(lst,k)):
    a=1
    for y in x:
      if type(y)==int:
        a*=y
    l.append(a)
  return (min(l),max(l))


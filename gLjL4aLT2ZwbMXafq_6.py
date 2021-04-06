
def fair_swap(l1, l2):
  out=set()
  diff=sum(l1)-sum(l2)
  for a in set(l1):
    for b in set(l2):
      if diff==-b+a+a-b:
        out.add((a,b))
  return out



def fair_swap(l1, l2):
  S1 = sum(l1)
  S2 = sum(l2)
  l2 = set(l2)
  
  if (S1-S2)%2:
    return set()
  
  delta = (S2-S1)//2
  return {(x,x+delta) for x in l1 if x+delta in l2}



def simple_comp(lst1, lst2):
  if lst1 == [] and lst2 == []: return True
  if not lst1 or not lst2: return False
  if len(lst1)!=len(lst2): return False
  a = sorted([eval(str(abs(i))) for i in lst1])
  b = sorted([eval(str(abs(i))) for i in lst2])
  return all(j**2==b[i] for i, j in enumerate(a))==True


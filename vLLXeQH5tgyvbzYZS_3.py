
def count_factors(a, b, c):
  af = []
  bf = []
  cf = []
  common = []
  for f in range(2, a+1):
    if a%f == 0:
      af.append(f)
  for f in range(2, b+1):
    if b%f == 0:
      bf.append(f)
  for f in range(2, c+1):
    if c%f == 0:
      cf.append(f)
  for n in af + bf + cf:
    if (af+bf+cf).count(n) == 3 and common.count(n) == 0:
      common.append(n)
  return len(common)
  
​
def is_prim_pyth_triple(lst):
  abc = sorted(lst)
  if count_factors(abc[0], abc[1], abc[2]) != 0:
    return False
  if abc[0]**2 + abc[1]**2 == abc[2]**2:
    return True
  return False


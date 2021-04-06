
def major_sum(lst):
  p = sum([i for i in lst if i>=0])
  n = sum([i for i in lst if i<0])
  z = lst.count(0)
  
  if p > abs(n) and p>z:
    return p
  elif abs(n) > p and abs(n) > z:
    return n
  else:
    return z



def min_swaps(st):
  l = len(st)
  t1, t2 = '01', '10'
  s = sum(st[x]!= t1[x%2] for x in range(l))
  s2 = sum(st[x]!= t2[x%2] for x in range(l))
  return min(s,s2)


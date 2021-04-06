
def covered_integers(lst):
  m = min(i[0] for i in lst)
  M = max(i[1] for i in lst)
  return sum(any(i[0]<=x<=i[1] for i in lst) for x in range(m,M+1) )


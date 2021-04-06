
def iqr(lst):
  lst.sort()
  i = len(lst)//2
  Q1, Q3 = (median(q) for q in (lst[:i], lst[-i:]))
  return Q3-Q1
  
def median(lst):
  n = len(lst)
  i = (n-1)//2
  m = lst[i:-i] if n>2 else lst
  return sum(m)/len(m)


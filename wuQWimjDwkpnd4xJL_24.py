
def balanced(lst):
  f=lst[:len(lst)//2]
  l=lst[-len(lst)//2:]
  if sum(f)==sum(l): return lst
  if sum(f)>sum(l): return f+f
  return l+l


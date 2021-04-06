
def nespers(lst):
  inner_nespers = [nespers(l) if type(l)==list else 1 for l in lst]
  return prod(range(1,len(lst)+1)) * prod(inner_nespers)
​
def prod(lst):
  p=1
  for i in lst: p*=i
  return p


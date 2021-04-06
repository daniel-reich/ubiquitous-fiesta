
def adjacent_product(lst):
  l=[]
  for a,b in zip(lst,lst[1:]):
    l.append(a*b)
  return max(l)



def difference_two(lst):
  l=[]
  for x in sorted(lst):
    if x+2 in lst:
      l+=[[x,x+2]]
  return l



def largest_gap(l):
  l=sorted(l)
  return max(y-x for x,y in zip(l,l[1:]))


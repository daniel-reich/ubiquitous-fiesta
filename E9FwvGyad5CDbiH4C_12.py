
def block(lst):
  return sum(l.count(2)*(len(lst)-i-1) for i,l in enumerate(lst))


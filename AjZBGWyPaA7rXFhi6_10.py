
def min_swaps(s1, s2):
  return ([x==y for x,y in zip(s1,s2)].count(False))/2


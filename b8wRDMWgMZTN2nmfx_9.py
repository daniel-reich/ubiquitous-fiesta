
def equal(a, b, c): 
  s = set([a, b, c])
  return sum((a, b, c).count(i) for i in s if (a, b, c).count(i) > 1)


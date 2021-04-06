
def min_swaps(string):
  a = '01'*len(string)
  b = '10'*len(string)
  c = sum([1 for i, j in zip(string, a) if i!=j])
  d = sum([1 for i, j in zip(string, b) if i!=j])
  return min(c,d)



def min_swaps(string):
  res = sum(int(c) == i%2 for i,c in enumerate(string))
  return min(res, len(string)-res)


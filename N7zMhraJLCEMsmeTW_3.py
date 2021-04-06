
def min_swaps(s):
  n = sum(a%2!=int(b) for a,b in enumerate(s))
  return min(n,len(s)-n)


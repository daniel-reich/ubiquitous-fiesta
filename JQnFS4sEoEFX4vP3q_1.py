
from numpy import prod
​
def product_pair(lst, k):
  if len(lst) < k:
    return None
  lst.sort()
​
  mn, mx = sorted([prod(lst[:k]), prod(lst[-k:])])
  for i in range(k >> 1):
    mn = min(mn, prod(lst[:i*2 + 1] + lst[len(lst) - (k - (i*2 + 1)):]))
    mx = max(mx, prod(lst[:i*2 + 2] + lst[len(lst) - (k - (i*2 + 2)):]))
​
  return mn, mx


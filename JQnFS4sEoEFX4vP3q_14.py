
from itertools import combinations as c
def product_pair(lst, k):
  if len(lst) < k: return
  prod = lambda lst: eval("*".join(map(str,lst)))
  ans = sorted(prod(i) for i in c(lst,k))
  return (ans[0],ans[-1])



from re import findall
​
def is_ascending(s, k=None):
  k = 1 if k is None else k
  if k > (len(s) + 0.1) // 2: return False
  n = list(map(int, findall(r'.{1,'+str(k)+'}', s)))
  return True if all(a+1 == b for a, b in zip(n, n[1:])) \
    else is_ascending(s, k + 1)


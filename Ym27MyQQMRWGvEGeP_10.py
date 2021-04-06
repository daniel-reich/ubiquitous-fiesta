
from re import findall
​
def is_consecutive(s, k=None):
  k = 1 if k is None else k
  if k > (len(s)+0.1)//2: return False
  n = list(map(int, findall(r'.{1,'+str(k)+'}', s)))
  return True if all(b-a == 1 for a, b in zip(n, n[1:])) \
    or all(b-a == -1 for a, b in zip(n, n[1:])) else \
    is_consecutive(s, k+1)


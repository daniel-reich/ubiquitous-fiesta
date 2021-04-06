
from collections import Counter
​
def sock_merchant(lst):
  C = Counter(lst)
  return sum([k // 2 for k in C.values()])


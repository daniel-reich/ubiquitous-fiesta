
from collections import Counter
def sock_merchant(lst):
  return sum(v//2 for v in Counter(lst).values())


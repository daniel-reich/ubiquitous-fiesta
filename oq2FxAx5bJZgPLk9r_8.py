
from collections import Counter
def sock_merchant(lst):
  return sum(c//2 for c in Counter(lst).values())


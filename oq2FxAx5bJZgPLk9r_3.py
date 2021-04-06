
from collections import Counter
def sock_merchant(lst):
  counter = Counter(lst)
  return sum(list(map(lambda x: x//2,list(counter.values()))))


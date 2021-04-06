
from collections import Counter
def missing(lst):
  lst.sort()
  key = [lst[i+1]-lst[i] for i in range(len(lst)-1)]
  ck = Counter(key).most_common(1)[0][0]
  for i in range(len(lst)-1):
    if lst[i+1]-lst[i] != ck:
      return lst[i]+ck


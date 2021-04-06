
from collections import Counter 
def most_frequent_char(lst):
  d = Counter("".join(lst))
  maxVal = max(Counter("".join(lst)).values())
  l =[]
  for key, val in d.items():
    if val == maxVal:
      l.append(key)
  return sorted(l)


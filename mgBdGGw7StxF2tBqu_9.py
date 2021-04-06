
from collections import Counter
​
​
def duplicates(txt):
  c = Counter(txt) 
  return len(txt) - len(c)


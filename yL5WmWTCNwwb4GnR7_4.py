
from collections import Counter
​
def return_unique(lst):
  c = Counter(lst)
  lst = [n for n in lst if c[n] == 1]
  return lst


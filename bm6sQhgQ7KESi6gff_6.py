
from collections import Counter
​
def find_the_difference(s, t):
  return list(Counter(t) - Counter(s))[0]


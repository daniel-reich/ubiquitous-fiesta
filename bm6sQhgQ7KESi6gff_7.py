
from collections import Counter
def find_the_difference(s, t):
  return [k for k in Counter(t)-Counter(s)][0]


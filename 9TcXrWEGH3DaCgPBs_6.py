
from collections import Counter
def find_odd(lst):
  return [k for k, v in Counter(lst).items() if v%2==1][0]


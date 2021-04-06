
from collections import Counter
def multiplicity(lst):
  return sorted([list(i) for i in Counter(lst).most_common()], key = lambda x: lst.index(x[0]))


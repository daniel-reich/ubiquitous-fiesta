
from collections import defaultdict
def map_letters(word):
  d = defaultdict(list)
  for i, w in enumerate(word):
    d[w].append(i)
  return d


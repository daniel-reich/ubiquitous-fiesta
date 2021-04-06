
from collections import Counter
def can_build(s1, s2):
  return all(v <= Counter(s1)[k] for k,v in Counter(s2).items())


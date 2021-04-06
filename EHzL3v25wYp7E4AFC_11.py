
from collections import Counter
def can_build(s1, s2):
  return not Counter(s2) - Counter(s1)


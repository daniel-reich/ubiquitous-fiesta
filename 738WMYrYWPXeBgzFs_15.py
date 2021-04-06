
from collections import Counter
def is_valid(txt):
  keys = {True:'YES',False:'NO'}
  counter = Counter(txt)
  if len(set(counter.values())) == 1:
    return 'YES'
  if len(set(counter.values())) == 2:
    if list(counter.values()).count(max(counter.values())) == 1:
      return keys[max(counter.values()) - min(counter.values()) == 1]
  return 'NO'


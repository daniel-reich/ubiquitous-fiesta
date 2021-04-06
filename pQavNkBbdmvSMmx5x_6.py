
from collections import Counter
def majority_vote(lst):
  if len(lst) == 0:
    return None
  votovi = Counter(lst)
  if len(list(votovi.keys())) == 1:
    return max(votovi, key=votovi.get)
  values = list(votovi.values())
  return max(votovi, key=votovi.get) if sum(values) / len(values) != values[0] else None


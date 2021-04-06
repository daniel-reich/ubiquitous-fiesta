
from collections import Counter
def max_occur(text):
  ct = Counter(text)
  m = max(ct.values())
  if m == 1:
    return "No Repetition"
  return [k for k,v in ct.items() if v == m]


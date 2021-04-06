
from collections import Counter as C
def max_occur(text):
  d=dict(C(text))
  m=max(d.values())
  res=[x for x in d if d[x]==m]
  return sorted(res) if m!=1 else "No Repetition"


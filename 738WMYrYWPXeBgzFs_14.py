
from collections import Counter as C
def is_valid(txt):
  d=dict(C(txt))
  if len(set(d.values()))==1:
    return 'YES'
  elif len(set(d.values()))==2:
    if list(d.values()).count(max(d.values()))==1 and max(d.values())-min(d.values())==1:
      return 'YES'
    else:
      return 'NO'
  else:
    return 'NO'


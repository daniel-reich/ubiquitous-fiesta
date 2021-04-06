
from collections import Counter
def single_occurrence(txt):
  if txt:
    d=Counter(txt.upper())
    k={x:y for y,x in d.items()}
    return k[min(d.values())]
  else:return ''


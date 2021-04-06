
from collections import Counter as C
def make_anagram(a, b):
  d,e=C(a), C(b)
  A=[x for x in d if x in e]
  c=sum([min(d[x],e[x]) for x in A])
  return len(a)+len(b)-2*c


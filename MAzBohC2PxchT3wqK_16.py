
from itertools import zip_longest
​
def shadow_sentence(a, b):
  return all((len(i) == len(j)) and not any(k in i for k in j) for i, j in zip_longest(a.split(), b.split(), fillvalue= ''))


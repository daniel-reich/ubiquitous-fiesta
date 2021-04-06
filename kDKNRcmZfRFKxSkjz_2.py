
from itertools import zip_longest
​
def unmix(txt):
  return ''.join(a+b for a, b in zip_longest(txt[1::2], txt[::2], fillvalue=''))


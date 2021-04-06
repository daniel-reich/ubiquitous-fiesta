
from itertools import groupby
​
def is_icecream_sandwich(txt):
  return txt == txt[::-1] and len(list(groupby(txt))) == 3


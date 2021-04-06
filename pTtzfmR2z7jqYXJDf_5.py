
from itertools import groupby
def possible_palindrome(txt):
  lst = [k for k, g in groupby(sorted(txt)) if len(list(g)) % 2 == 1]
  return len(lst) <= 1


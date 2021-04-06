
from itertools import groupby
def remove_repeats(s):
  return ''.join(k for k,g in groupby(s))


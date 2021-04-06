
from math import ceil, log
​
def million_in_month(a, r):
  return ceil(log(((1e6 * (r - 1)) / a) + 1, r))



from math import ceil, log
​
def million_in_month(f, m):
  return ceil(log(1e6 * (m - 1) / f + 1) / log(m))


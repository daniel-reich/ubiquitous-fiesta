
from math import ceil
​
def cal(d):
  return ceil(d / 5) if d <= 150 else 40 + cal(d - 120)


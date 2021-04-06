
from math import ceil
​
def num_of_days(cost, savings, start):
  i, c = 0, 0
  while savings + i * (i + start * 2 - 1) / 2 - 21 * (c - 1) * c + 6 * (c - 1) * (7 - (i % 7 or 7)) < cost:
    i += 1
    c = ceil(i / 7)
  return i


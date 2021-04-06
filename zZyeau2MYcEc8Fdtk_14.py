
from math import ceil
​
def round_number(num : int, n : int) -> int:
  closest_multiply = num / n
  return n * (ceil(closest_multiply) if closest_multiply % 1 >= 0.5 else round(closest_multiply))


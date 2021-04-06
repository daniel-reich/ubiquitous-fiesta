
import math
def series_resistance(lst):
  if sum(lst) > 1:
    return str(sum(lst)) + " ohms"
  else:
    return str(sum(lst)) + " ohm"



import re
from collections import defaultdict
​
pattern = re.compile(r'(-?\d+), *(-?\d+)')
​
def is_rectangle(coordinates):
  x_entries = defaultdict(int)
  y_entries = defaultdict(int)
  for coord_pair_str in coordinates:
    match = pattern.search(coord_pair_str)
    if match is not None:
      x_entries[match.group(1)] += 1
      y_entries[match.group(2)] += 1
  
  for k in x_entries.keys():
    if x_entries[k] != 2:
      return False
  for k in y_entries.keys():
    if y_entries[k] != 2:
      return False
  return True


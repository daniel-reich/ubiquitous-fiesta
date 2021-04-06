
from itertools import groupby
​
def color_pattern_times(cols):
  if len(cols) > 0:
    pencils = [col[0] for col in groupby(cols)]
    coloring = 2 * len(cols)
    switching = 1 * (len(pencils) - 1)
    return coloring + switching
  else:
    return 0


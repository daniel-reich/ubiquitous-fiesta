
import re
​
def swap_xy(txt):
  x1, x2, y1, y2 = re.findall(r'-?\d+', txt)
  return '({}, {}), ({}, {})'.format(x2, x1, y2, y1)


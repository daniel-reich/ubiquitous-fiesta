
import re
​
def swap_xy(txt):
  pairs = re.findall(r'(-?\d+), (-?\d+)', txt)
  return ', '.join(['({}, {})'.format(*pair[::-1]) for pair in pairs])


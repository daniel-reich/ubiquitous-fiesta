
import re
​
def swap_xy(txt):
  return re.sub(r'([\d-]*), ([\d-]*)', r'\2, \1', txt)


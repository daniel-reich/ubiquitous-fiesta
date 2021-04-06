
import re
def make_happy(txt):
  return re.sub('(?<=[:8x;])\(',')',txt)


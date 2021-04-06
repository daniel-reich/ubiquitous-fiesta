
import re
def is_central(txt):
  spcs = re.findall(r'\s+', txt)
  return len(txt) == 1 or (len(spcs) == 2 and len(spcs[0]) == len(spcs[1]))



import re
​
def count_same_ends(txt):
  return len(re.findall(r'\b(\w)\w*\1\b', txt.lower()))


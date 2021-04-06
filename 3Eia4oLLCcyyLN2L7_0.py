
import re
def remove_repeats(s):
  return re.sub(r'(\w)\1+',r'\1', s)


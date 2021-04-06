
import re
def find_longest(s):
  return max(re.findall(r'\b\w+\b', s.lower()), key=len)



import re
​
def longest_zero(s):
  return sorted(re.findall("0+", s))[-1:][0] if '0' in s else ''


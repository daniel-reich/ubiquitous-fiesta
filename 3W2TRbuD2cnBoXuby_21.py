
import re
​
def collect(s, n):
  return sorted(re.findall('.{{{}}}'.format(n), s))


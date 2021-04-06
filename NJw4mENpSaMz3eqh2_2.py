
import re
​
def is_undulating(n):
  s = str(n)
  return re.match(r'(.)(.)(\1\2)*\1\2?$', s) and s[0] != s[1] or 0


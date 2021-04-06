
import re
​
def increment_string(t):
  n = ''.join(re.findall(r'\d*\Z', t)) or '0'
  x = str(int(n)+1)
  r = '0'*(len(n)-len(x)) + x
  return t.replace(n, r) if int(n) else t+'1'


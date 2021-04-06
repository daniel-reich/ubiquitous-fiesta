
import re
​
def remove_leading_trailing(n):
  if float(n) == 0:
    return '0'
  n = re.sub(r'^0*','',n)
  if re.search(r'\.',n):
    n = re.sub(r'0*$','',n)
  n = re.sub(r'\.$','',n)
  n = re.sub(r'^\.','0.',n)
  return n


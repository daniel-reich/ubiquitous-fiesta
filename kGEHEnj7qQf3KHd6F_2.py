
import re
​
def alphanumeric_restriction(s):
  if re.fullmatch(r"[0-9]+", s):
    res = True
  elif re.fullmatch(r"[a-zA-Z]+",s):
    res = True
  else:
    res = False
​
  return res


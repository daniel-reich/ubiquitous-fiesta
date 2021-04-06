
import re
def score_it(s):
  if not "(":
    return 0
  elif bool(re.search(r'\d+',s)) == False:
    return 0
  else:
    total = 0
    n = 0
    chars = re.findall(r'\(+|\)+|\d+',s)
    print(chars)
    for char in chars:
      if char[0] == "(":
        n += len(char)
      elif char[0] == ")":
        n -= len(char)
      else:
        total += n * int(char)
    return total


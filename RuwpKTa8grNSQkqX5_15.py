
import re
​
def fractions(decimal):
  regex_match = re.match("(\d*)\.(\d*)\((\d*)\)", decimal)
  groups = regex_match.groups()
  denom = 1
  tail = (groups[2]*10)[:15]
  original = float(groups[0] + '.' + groups[1] + tail)
  num = original
  while abs(round(num) - num) > 0.000001:
    num += original
    denom += 1
  return str(int(round(num))) + '/' + str(denom)


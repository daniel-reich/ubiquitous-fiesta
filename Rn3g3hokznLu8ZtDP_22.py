
import re
​
def increment_string(txt):
  match = re.match(r"([a-z]+)([0-9]+)", txt)
  if match:
    items = match.groups()
    l = len(items[1])
    a = (int(items[1]) + 1)
    return items[0] + (str(a).rjust(l, '0'))
  else:
    return txt + '1'


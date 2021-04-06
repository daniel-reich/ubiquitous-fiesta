
import re
​
def first_repeat(s):
  try:
    return re.findall(r'(\w)\w*\1', s)[0]
  except IndexError:
    return '-1'


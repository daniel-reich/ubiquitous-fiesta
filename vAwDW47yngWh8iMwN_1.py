
import re
​
def capLast(txt):
  return re.sub(r'(\w)(\s|\Z)', lambda x: x.group(0).upper(), txt)


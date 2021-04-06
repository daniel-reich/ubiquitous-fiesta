
import re
​
def camelCasing(txt):
  return re.sub(r'([^a-z])(\w)', lambda x: x.group(2).upper(), txt.lower())


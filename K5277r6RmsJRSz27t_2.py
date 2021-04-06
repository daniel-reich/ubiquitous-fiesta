
import re
​
def emphasise(txt):
  return re.sub(r'\b(\w)', lambda x: x.group(1).upper(), txt.lower())


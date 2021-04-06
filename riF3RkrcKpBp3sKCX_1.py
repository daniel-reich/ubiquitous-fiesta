
import re
​
def cap_space(txt):
  return re.sub('([A-Z])', r' \1', txt).lower()


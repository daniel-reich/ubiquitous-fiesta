
import re
​
def dashed(txt):
  return re.sub('([aeiouAEIOU])', r'-\1-', txt)


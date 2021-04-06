
import re
def dashed(txt):
  return re.sub(r'([aeiouAEIOU])',r'-\1-',txt)


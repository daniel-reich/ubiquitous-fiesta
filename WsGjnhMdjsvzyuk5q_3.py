
import re
def dashed(txt):
  return re.sub(r'[aeiou]', lambda v: '-'+v.group(0)+'-', txt, flags=re.I)


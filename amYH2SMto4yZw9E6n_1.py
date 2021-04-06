
import re
def validate(s):
  m = None
  if '  ' not in s:
    m = re.match(r'^(?:\+?(1))?[-. (/]*(\d{3})[-. )/]*(\d{3})[-. /]*(\d{4})(?: *x(\d+))?$',s)
  return True if m else False


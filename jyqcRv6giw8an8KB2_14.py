
import re
def invert(s):
  return "".join([c.lower() if re.match("[A-Z]", c) else c.upper() for c in s[::-1]])


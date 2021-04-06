
import re
def has_digit(txt):
  x = bool(re.findall("\d", txt))
  return x


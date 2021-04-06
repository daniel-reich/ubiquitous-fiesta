
import re
def has_digit(txt):
  if re.findall("[0-9]", txt):
    return True
  else:
    return False


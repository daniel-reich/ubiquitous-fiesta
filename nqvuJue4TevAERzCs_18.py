
import re
def has_digit(txt):
  x = re.findall("[0-9]",txt)
  if len(x)==0:
    return False
  else:
    return True


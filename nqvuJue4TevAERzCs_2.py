
import re
def has_digit(txt):
  x = re.search('\d', txt)
  if x:
        return True
  else:
        return False


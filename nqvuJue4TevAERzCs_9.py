
import re
def has_digit(txt):
  match = re.search('\d+', txt)
  if match:
    return True
  else:
    return False


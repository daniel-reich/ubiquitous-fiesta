
import re
def validate_email(txt):
  if re.match("^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", txt) != None:
    return True
  return False



import re
def validate_email(txt):
  if re.match(r'[a-zA-Z\.]+@[a-zA-Z.]+\.[a-zA-Z]+', txt):
    return True
  return False


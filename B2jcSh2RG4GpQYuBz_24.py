
import re
def is_valid_phone_number(txt):
  if re.match("^\(\d{3}\)\s\d{3}-\d{4}$", txt):
    return True
  return False


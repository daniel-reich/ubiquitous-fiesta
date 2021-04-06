
import re
def is_valid_phone_number(txt):
  return bool(re.search("^\(\d{3}\)\s\d{3}-\d{4}$",txt))


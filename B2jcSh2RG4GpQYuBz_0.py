
import re
def is_valid_phone_number(txt):
  return bool(re.match('^\(\d{3}\) \d{3}-\d{4}$', txt))


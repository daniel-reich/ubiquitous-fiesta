
import re
def is_valid_phone_number(txt):
  return re.match(r'^\(\d{3}\) \d{3}-\d{4}$', txt) is not None


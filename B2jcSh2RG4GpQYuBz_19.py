
import re
​
def is_valid_phone_number(txt):
  pattern = '^\(\d{3}\) \d{3}-\d{4}$'
  return True if re.match(pattern, txt) else False


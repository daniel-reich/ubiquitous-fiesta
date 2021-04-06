
import re
def is_valid_phone_number(txt):
  return bool(re.search('\(\d{3}\) \d{3}-\d{4}',txt)) and len(txt)==14



def is_valid_phone_number(txt):
  import re
  return bool(re.search(r'^\(\d{3}\)\s\d{3}-\d{4}$', txt))


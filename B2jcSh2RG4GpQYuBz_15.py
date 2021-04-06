
import re
def is_valid_phone_number(txt):
  obj = re.search(r'^\(\d{3}\)\ \d{3}-\d{4}$', txt)
  print(txt, obj)
  return obj and True or False


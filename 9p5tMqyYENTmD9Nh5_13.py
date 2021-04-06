
def is_valid_hex_code(txt):
  import re
  return True if re.search('^#([0-9a-fA-F]){6}$',txt) else False


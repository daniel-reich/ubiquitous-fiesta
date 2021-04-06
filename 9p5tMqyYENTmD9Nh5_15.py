
import re
def is_valid_hex_code(txt):
  if re.match(r'^#[a-fA-F0-9]{6}$',txt):
    return True
  else:
    return False



from re import match
def is_valid_hex_code(txt):
  if len(txt)!=7: return False
  return bool(match(r'^#[\dA-Fa-f]+$', txt))


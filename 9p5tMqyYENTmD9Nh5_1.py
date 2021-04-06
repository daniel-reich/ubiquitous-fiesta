
import re
def is_valid_hex_code(txt):
  return bool(re.match(r'^\#[0-9a-f]{6}$', txt, re.I))


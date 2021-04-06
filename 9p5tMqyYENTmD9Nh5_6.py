
import re
def is_valid_hex_code(txt):
  return bool(re.match(r'\A#[a-fA-F0-9]{6}\Z', txt))


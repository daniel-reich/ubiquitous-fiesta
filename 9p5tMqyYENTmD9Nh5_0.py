
import re
​
def is_valid_hex_code(txt):
  return bool(re.match(r'#[A-Fa-f0-9]{6}$', txt))


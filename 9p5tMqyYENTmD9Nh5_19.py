
import re
def is_valid_hex_code(txt):
  return re.match(r'^#[a-f0-9]{6}$',txt,re.I) != None



import re
def is_valid_PIN(pin):
  return bool(re.fullmatch(r'\d{4}|\d{6}',pin))


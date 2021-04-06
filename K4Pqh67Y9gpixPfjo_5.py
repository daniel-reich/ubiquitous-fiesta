
import re
def is_valid_PIN(pin):
  return bool(re.match('^(?:\d{4}|\d{6})$', pin))


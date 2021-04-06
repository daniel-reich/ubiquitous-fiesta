
import re
def is_valid_phone_number(txt):
  return re.match('^\([0-9]{3}\) [0-9]{3}-[0-9]{4}$', txt) is not None


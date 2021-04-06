
import re
def validate_email(txt):
  return re.match(r'^.+@.+\.com$', txt) is not None


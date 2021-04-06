
import re
def letters_only(s):
  return bool(re.match(r'^[a-z ]+$', s))


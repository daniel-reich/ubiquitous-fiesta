
import re
def validate(s):
  rexp = r'^(?:[+]?1[ ]?)?(?:\d{3}|\(\d{3}\))[ ]?\d{3}[ ]?\d{4}$'
  return bool(re.match(rexp, re.sub(r'[.\-/]', ' ', s)))


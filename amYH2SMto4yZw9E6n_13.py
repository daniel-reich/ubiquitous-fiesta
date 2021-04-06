
import re
def validate(s):
  return bool(re.match(r'\+?\d?[-. /]?(\()?\d{3}(\))?[-. /]?\d{3}[-. /]?\d{4}',s))


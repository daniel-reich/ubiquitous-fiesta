
import re
def assignment(date):
  return bool(re.match(r'^\d{4}\/\d{2}\/\d{2}$', date))


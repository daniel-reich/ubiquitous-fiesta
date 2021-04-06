
import re
​
def assignment(date):
  if re.match(r'\d{4}/\d{2}/\d{2}', date):
    return True
  else:
    return False



import re
​
def assignment(date):
  return bool(re.fullmatch("\d{4}(/\d\d){2}", date))


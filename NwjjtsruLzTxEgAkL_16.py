
from re import match
def assignment(date):
  return bool(match("\d{4}/\d{2}/\d{2}", date))


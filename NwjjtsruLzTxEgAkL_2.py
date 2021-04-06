
from re import search
def assignment(date):
  return bool(search(r'\A\d{4}(\/\d{2}){2}\Z', date))


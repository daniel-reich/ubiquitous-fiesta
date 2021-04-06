
from re import search
def assignment(date):
  return bool(search(r"\b\d\d\d\d\/\d\d\/\d\d\b", date))


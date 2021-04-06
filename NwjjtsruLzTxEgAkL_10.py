
from re import search
def assignment(date):
  return bool(search(r"\b\d{4}\/\d{2}\/\d{2}\b",date))


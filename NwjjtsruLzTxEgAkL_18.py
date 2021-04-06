
from re import search
​
​
def assignment(date):
  return bool(search(r"^(\d{4})([-/])(\d{2})\2\d{2}$", date))


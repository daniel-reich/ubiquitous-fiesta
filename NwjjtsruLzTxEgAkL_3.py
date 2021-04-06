
from re import search
def assignment(date):
  return search(r"^(\d{4})([-/])(\d{2})([-/])(\d{2})", date)!=None


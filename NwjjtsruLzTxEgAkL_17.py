
import re
def assignment(date):
  match = re.match(r"(\d{4})([-/])(\d{2})\2(\d{2})", date)
  return True if match else False


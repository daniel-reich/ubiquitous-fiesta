
from re import search
def assignment(date):
  try:
    return bool(search(r"(?<![a-z])(\d{4}/\d{2}/\d{2})(?![a-z])", date).group(0))
  except AttributeError:
    return False


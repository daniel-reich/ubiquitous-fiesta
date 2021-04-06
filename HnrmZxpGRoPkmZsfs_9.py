
import datetime
def is_valid_date(x, y, z):
  isValidDate = True
  try:
    datetime.datetime(int(z),int(y),int(x))
  except ValueError :
    isValidDate = False
  return isValidDate


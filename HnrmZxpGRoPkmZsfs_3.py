
import datetime
def is_valid_date(d, m, y):
  isValidDate = True
  try:
    datetime.datetime(y,m,d) 
  except:
    isValidDate = False
  return isValidDate



import datetime
def has_friday_13(month, year):
  day=13
  x=datetime.datetime(year,month,day)
  y=x.strftime("%A")
  if y=='Friday':
    return True
  else: 
    return False


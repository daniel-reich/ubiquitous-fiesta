
import datetime
def first_tuesday_of_the_month(year, month):
  for i in range(1,8):
    x=datetime.datetime(year,month,i)
    if x.strftime("%A")=='Tuesday':
      return str(x)[:10]


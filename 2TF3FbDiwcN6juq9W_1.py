
from datetime import datetime
​
def days_until_2021(date):
  a = datetime.strptime(date, "%m/%d/%Y")
  b = datetime.strptime('1/1/2021', "%m/%d/%Y")
  return "{} day{}".format((b-a).days, 's' if (b-a).days>1 else '')



from datetime import datetime
def first_tuesday_of_the_month(year, month, day=1):
  a = datetime(year, month, day).strftime("%A")
  b = {"Monday":2, "Tuesday":1, "Wednesday":7, "Thursday":6,
       "Friday":5, "Saturday":4, "Sunday":3}
  c = "0"+str(month) if month<10 else month
  return "{}-{}-0{}".format(year, c, b[a])


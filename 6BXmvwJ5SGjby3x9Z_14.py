
from datetime import datetime
def hours_passed(time1, time2):
  t1=datetime.strptime(time1, '%I:%M %p')
  t2=datetime.strptime(time2, '%I:%M %p')
  dt=(t2-t1).seconds//3600
  if dt:
    return "{} hours".format(dt)
  else:
    return "no time passed"


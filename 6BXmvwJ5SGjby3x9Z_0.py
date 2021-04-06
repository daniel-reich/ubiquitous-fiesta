
import datetime
def hours_passed(time1, time2):
  if time1 == time2:
    return "no time passed"
  else :
    dt1 = datetime.datetime.strptime(time1, '%I:%M %p')
    dt2 = datetime.datetime.strptime(time2, '%I:%M %p')
    return "{} hours".format(str(dt2-dt1).split(':')[0])


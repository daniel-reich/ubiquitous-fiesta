
import datetime
def get_day(day):
  daylist = day.split('/')
  x = datetime.datetime(int(daylist[2]), int(daylist[0]), int(daylist[1]))
  return (x.strftime("%A").capitalize())


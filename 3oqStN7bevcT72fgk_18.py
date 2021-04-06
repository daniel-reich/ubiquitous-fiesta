
import datetime
def get_day(day):
  week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
  d = datetime.date(int(day[-4:]), int(day[:2]), int(day[3:5]))
  return week[d.weekday()]


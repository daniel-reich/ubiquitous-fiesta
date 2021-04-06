
import datetime
def week_after(d):
  day, mon, year =[int(x) for x in d.split('/')]
  dd=datetime.timedelta(days=7)
  nw=datetime.date(year, mon, day)+dd
  return '{0:02d}/{1:02d}/{2}'.format(nw.day, nw.month, nw.year)


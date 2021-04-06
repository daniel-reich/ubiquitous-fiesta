
import calendar
def first_tuesday_of_the_month(year, month):
  m=calendar.monthrange(year, month)[0]
  d={0:2,1:1,2:7,3:6,4:5,5:4,6:3}
  return '{}-{:02d}-{:02d}'.format(year, month,d[m])



import datetime
​
def days_until_2021(date):
  d1 = datetime.datetime(2021,1,1)
  date = datetime.datetime(int(date.split('/')[2]),int(date.split('/')[0]),int(date.split('/')[1]))
  if (d1-date).days == 1:
    return '1 day'
  else:
    return '{} days'.format((d1 - date).days)


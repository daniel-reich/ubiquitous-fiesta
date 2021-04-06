
import datetime
def week_after(date):
  d,m,y=date.split('/')
  date=datetime.date(int(y),int(m),int(d))+datetime.timedelta(days=7)
  return date.strftime('%d/%m/%Y')


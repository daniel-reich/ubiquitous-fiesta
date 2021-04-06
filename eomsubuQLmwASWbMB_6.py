
import datetime
import calendar
days = {0:'zon',1:'maan',2:'dins',3:'woens',4:'donder',5:'vrij',6:'zater'}
def weekday_dutch(date):
  day = datetime.datetime.strptime(date, '%d %m %Y').weekday()
  return days[(day+1)%7] + 'dag'


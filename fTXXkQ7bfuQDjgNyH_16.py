
from datetime import datetime,timedelta
def day_of_year(date):
  d1 = datetime.strptime(date,'%m/%d/%Y')
  d2 = datetime.strptime('1/1/'+date.split('/')[-1],'%m/%d/%Y')
  return 1+(d1-d2).days


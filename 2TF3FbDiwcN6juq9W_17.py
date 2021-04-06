
from datetime import datetime
​
def days_until_2021(date):
  date = datetime.strptime(date,'%m/%d/%Y')
  ret = (datetime.strptime('01/01/2021','%m/%d/%Y')-date).days
  return str(ret)+' days' if ret>1 else '1 day'


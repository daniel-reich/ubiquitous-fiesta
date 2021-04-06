
import datetime
​
def days_until_2021(date):
  date = datetime.datetime.strptime(date, "%m/%d/%Y")
  base = datetime.datetime.strptime('1/1/2021', "%m/%d/%Y")
  
  ans = (base-date).days
  return '{} day{}'.format(ans, '' if ans==1 else 's')


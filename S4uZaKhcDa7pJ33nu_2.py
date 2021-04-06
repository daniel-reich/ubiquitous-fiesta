
from datetime import datetime, timedelta
​
def week_after(d):
  dt = datetime.strptime(d, '%d/%m/%Y') + timedelta(days=7)
  return dt.strftime('%d/%m/%Y')


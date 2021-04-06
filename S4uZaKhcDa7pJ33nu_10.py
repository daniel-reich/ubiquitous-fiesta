
from datetime import datetime, timedelta
def week_after(d):
  time = datetime.strptime(d,'%d/%m/%Y')
  time+=timedelta(weeks=1)
  return time.strftime('%d/%m/%Y')


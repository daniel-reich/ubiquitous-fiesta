
from datetime import datetime, timedelta
def week_after(d):
  date = datetime.strptime(d,'%d/%m/%Y') + timedelta(days=7)
  return date.strftime('%d/%m/%Y')



from datetime import datetime,timedelta
def week_after(d):
  return (datetime.strptime(d,'%d/%m/%Y')+timedelta(days=7)).strftime('%d/%m/%Y')


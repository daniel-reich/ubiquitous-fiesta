
from datetime import datetime as dt, timedelta as td
def week_after(d):
  return (dt.strptime(d, '%d/%m/%Y') + td(days=7)).strftime('%d/%m/%Y')


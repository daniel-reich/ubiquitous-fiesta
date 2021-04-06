
from datetime import date
def day_of_year(d):
  month, day, year = d.split("/")
  date_val = date(int(year),int(month),int(day))
  dayNum = date_val.strftime('%j')
  return int(dayNum)


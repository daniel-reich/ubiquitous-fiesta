
import datetime
def first_tuesday_of_the_month(year, month): 
  d=datetime.datetime(year,month,1)
  offset=1-d.weekday()
  if offset<0:
    offset+=7
  return (d+datetime.timedelta(offset)).strftime("%Y-%m-%d")



import datetime
def first_tuesday_of_the_month(year, month): 
  d = datetime.datetime(year, month, 1)
  offset = 1-d.weekday()
  if offset < 0:
    offset+=7
  result = d+datetime.timedelta(offset)
  return "{}-{:0>2}-{:0>2}".format(result.year, result.month, result.day)


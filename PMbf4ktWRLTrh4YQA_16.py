
def add_n_days_to_a_date(date, days):
  def date_formulater(date):
    days = int(date[:2])
    month = int(date[2:4])
    year = int(date[4:])
​
    return [days, month, year]
  from datetime import datetime as dt
  
  day_timestamp = 86400
  df = date_formulater(date)
​
  date = dt(df[2], df[1], df[0])
​
  datetimestamp = date.timestamp()
​
  newtimestamp = datetimestamp + (days * day_timestamp)
​
  newdate = dt.fromtimestamp(newtimestamp)
​
  newyear = newdate.strftime('%Y')
  newmonth = newdate.strftime('%m')
  newday = newdate.strftime('%d')
​
  return ''.join([newday, newmonth, newyear])


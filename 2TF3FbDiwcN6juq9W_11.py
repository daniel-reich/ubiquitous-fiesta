
import datetime
​
def days_until_2021(date):
  end_date=datetime.datetime(2021,1,1)
  date=datetime.datetime.strptime(date,"%m/%d/%Y")
  diff=end_date-date
  return str(diff.days)+(" day{}".format("s" if diff.days>1 else "" ))


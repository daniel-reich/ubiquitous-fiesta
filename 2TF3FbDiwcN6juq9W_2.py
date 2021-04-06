
import datetime
​
def days_until_2021(date):
  m,d,y=map(int,date.split("/"))
  return str(datetime.datetime(2021,1,1)-datetime.datetime(y,m,d)).split(",")[0]


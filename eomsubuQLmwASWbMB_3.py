
import datetime
​
NAME = ["maandag", "dinsdag", "woensdag", "donderdag", "vrijdag", "zaterdag", "zondag"]
​
def weekday_dutch(date):
  return NAME[datetime.datetime.strptime(date, "%d %m %Y").weekday()]


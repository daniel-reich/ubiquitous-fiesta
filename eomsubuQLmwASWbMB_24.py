
from datetime import datetime
​
def weekday_dutch(date):
  days = ['maandag','dinsdag','woensdag','donderdag',
          'vrijdag','zaterdag','zondag']
  date = [int(i) for i in date.split(" ")]
  weekday = datetime(date[2], date[1], date[0]).weekday()
  return days[weekday]


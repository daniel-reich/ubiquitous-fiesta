
import datetime
def weekday_dutch(date):
  d = datetime.datetime.strptime(date, '%d %m %Y').weekday()
  D=['maandag', 'dinsdag', 'woensdag', 'donderdag', 'vrijdag', 'zaterdag', 'zondag']
  return D[d]


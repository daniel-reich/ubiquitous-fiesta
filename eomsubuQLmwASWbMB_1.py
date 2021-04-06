
from datetime import date
​
dow = ['maandag', 'dinsdag', 'woensdag', 'donderdag', 'vrijdag', 'zaterdag', 'zondag']
def weekday_dutch(dd):
  d, m, y = map(int, dd.split())
  return dow[date(y, m, d).weekday()]


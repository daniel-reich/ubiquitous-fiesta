
from datetime import datetime as date
def day_of_year(dt):
  m, d, y = map(int, dt.split('/'))
  return int(date(y, m, d).timestamp() -
    date(y, 1, 1).timestamp()) // 86400 + 1



from datetime import datetime, timedelta
def bed_time(*t):
  diff = []
  for (a, b), (c, d) in [[k.split(':') for k in x] for x in t]:
    y, k = a+':'+b+':00', timedelta(hours=int(c), minutes=int(d), seconds=0)
    diff += [(datetime.strptime(y, '%X') - k).strftime('%X')[:-3]]
  return diff


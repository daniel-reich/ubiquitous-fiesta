
from datetime import datetime
​
def months_interval(s, e):
  if s > e:
    s, e = e, s
  out = []
  x = s
  y, m, d = x.year, x.month, x.day
  while x <= e:
    if x.strftime('%B') not in out:
      out.append(x.strftime('%B'))
    m += 1
    if m > 12:
      y += 1
      m -= 12
    x = datetime.date(y, m, d)
  return sorted(out, key = lambda x: datetime.datetime.strptime(x, '%B'))


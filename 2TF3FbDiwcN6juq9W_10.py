
from datetime import date
def days_until_2021(d):
  a = d.split('/')
  d1 = int(a[2])
  d2 = int(a[0])
  d3 = int(a[1])
  dd1 = date(d1, d2, d3)
  dd2 = date(2021, 1, 1)
  b = (dd2-dd1).days
  if b == 1:
    return '1 day'
  return '{} days'.format(b)


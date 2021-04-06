
from datetime import date as dt
def days_until_2021(date):
  st = [int(a) for a in date.split('/')]
  end = dt(2021, 1, 1)
  days = (end - dt(st[2], st[0],st[1])).days 
  return str(days)+ (' days' if days>1 else ' day')


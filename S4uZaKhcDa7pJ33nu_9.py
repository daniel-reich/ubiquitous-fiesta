
from datetime import date, timedelta
def week_after(d):
  j,m,a=map(int,d.split('/'))
  return '/'.join(str(date(a,m,j)+timedelta(7)).split('-')[::-1])


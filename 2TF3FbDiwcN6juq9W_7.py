
import datetime
def days_until_2021(date):
  a, b, c = date.split("/")
  d = datetime.datetime(int(c), int(a), int(b)).timestamp()
  e = datetime.datetime(2021, 1, 1).timestamp()
  f = int((e - d)//86400)
  return '{} day{}'.format(f ,"s" if f>1 else "")


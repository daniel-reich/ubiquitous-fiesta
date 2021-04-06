
import datetime
from time import strptime
def week_after(d):
  x = datetime.datetime.strptime(d, '%d/%m/%Y') + datetime.timedelta(7)
  return "{:02d}/{:02d}/{}".format(x.day, x.month, x.year)


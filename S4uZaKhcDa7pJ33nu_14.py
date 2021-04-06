
import datetime
​
def week_after(d):
  lst = d.split("/")
  lst = [int(x) for x in lst]
  t = datetime.datetime(lst[2], lst[1], lst[0])
  n = t + datetime.timedelta(days=7)
  return n.strftime("%d/%m/%Y")


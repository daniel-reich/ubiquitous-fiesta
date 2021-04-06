
def palindromic_date(date):
  from datetime import datetime
  d1 = "".join(date.split("/"))
  d = datetime.strptime(d1, "%d%m%Y")
  d2 = d.strftime("%m%d%Y")
  return d1 == d1[::-1] and d2 == d2[::-1]


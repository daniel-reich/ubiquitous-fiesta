
def week_after(d):
  from datetime import date, timedelta
  day, month , year = d.split('/')
  d = date(int(year), int(month), int(day)) + timedelta(7)
  return d.strftime("%d/%m/%Y")


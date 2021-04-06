
import datetime
def week_after(d):
  date = datetime.datetime.strptime(d, "%d/%m/%Y") + datetime.timedelta(days=7)
  return datetime.datetime.strftime(date, "%d/%m/%Y")


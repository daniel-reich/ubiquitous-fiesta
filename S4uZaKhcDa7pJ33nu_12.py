
import datetime
​
def week_after(d):
  return (datetime.datetime.strptime(d,"%d/%m/%Y") + datetime.timedelta(weeks=1)).strftime("%d/%m/%Y")


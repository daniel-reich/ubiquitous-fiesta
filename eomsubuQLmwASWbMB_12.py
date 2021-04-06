
import datetime
def weekday_dutch(date):
  a = {"Monday":"maandag","Tuesday":"dinsdag","Wednesday":"woensdag",
   "Thursday":"donderdag","Friday":"vrijdag","Saturday":"zaterdag",
     "Sunday": "zondag"}
  b ,c, d = date.split()
  return a[datetime.date(int(d), int(c), int(b)).strftime("%A")]


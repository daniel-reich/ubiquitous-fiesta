
from datetime import datetime as dt, timedelta
def current_streak(today, lst):
  dates = [dt.strptime(d['date'], "%Y-%m-%d") for d in lst]
  today = dt.strptime(today, "%Y-%m-%d")
  if today not in dates:
    return 0
  ans = 0
  while today in dates:
    ans += 1
    today -= timedelta(days=1)
  return ans


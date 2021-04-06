
import datetime
def dayNum(date):
  return datetime.datetime.strptime(date, "%Y-%m-%d").date().toordinal()
def current_streak(today, lst):
  dates = set([dayNum(d["date"]) for d in lst])
  day = dayNum(today)
  count = 0
  while day in dates:
    count += 1
    day -= 1
  return count


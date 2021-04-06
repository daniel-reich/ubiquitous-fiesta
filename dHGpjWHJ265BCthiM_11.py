
from datetime import datetime, timedelta
def current_streak(today, lst):
  if len(lst) == 0 or lst[-1]['date'] != today:
    return 0
  lst=lst[::-1]
  streak = 1
  for i, j in zip(lst, lst[1:]):
    t1 = datetime.strptime(i['date'],'%Y-%m-%d')
    t2 = datetime.strptime(j['date'],'%Y-%m-%d')
    if t1-t2 == timedelta(1):
      streak += 1
    else:
      return streak
  return streak


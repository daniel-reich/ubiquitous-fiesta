
from datetime import datetime,timedelta
def current_streak(today, lst):
  streak = 0
  today = datetime.strptime(today,'%Y-%m-%d')
  lst = [datetime.strptime(i['date'],'%Y-%m-%d') for i in lst]
  while today in lst:
    today-=timedelta(days=1)
    streak += 1
  return streak


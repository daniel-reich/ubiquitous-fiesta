
def dailyStreak(lst):
  cur_daily, daily = 0, 0
  for i,x in enumerate(lst):
    if x == True:
      if i == 0:
        cur_daily = 1
        daily = 1
      elif lst[i-1] == False:
        cur_daily += 1
      elif lst[i-1] == True:
        cur_daily += 1
        if cur_daily > daily:
          daily = cur_daily
    else:
      cur_daily = 0
  return daily



def current_streak(today, lst):
  if lst == []: return 0
  if today != lst[-1]["date"]: return 0
  con = 1
  lst.reverse()
  for i in range(len(lst)- 1):
    if int(lst[i]["date"][-2:]) -1 == int(lst[i+1]["date"][-2:]):
      con += 1
    else:
      break
  return con


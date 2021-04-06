
def current_streak(today, lst):
  if lst == [] or lst[-1]["date"][-2:] != today[-2:]: return 0
  lst, today = [i["date"][-2:] for i in lst], int(today[-2:])
  while today - int(lst[0]) != len(lst) - 1: lst.pop(0)
  return len(lst)


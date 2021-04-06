
def over_time(lst):
  if lst[0]<17 and lst[1] >= 17:
    workingHours = 17 - lst[0]
    overtime = lst[1] - 17
  elif lst[0] >= 17:
    overtime = lst[1] - lst[0]
    workingHours = 0
  else:
    workingHours = lst[1] - lst[0]
    overtime = 0
  money = str(format((workingHours * lst[2]) + (overtime * lst[3] * lst[2]) + 0.001, '.2f'))
  return("$"+ money)


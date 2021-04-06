
def weekly_salary(hours):
  salary = 0
  for idx, hours_day in enumerate(hours):
    if idx in [5,6]:
      if hours_day > 8:
        salary += (8*10+(hours_day-8)*15)*2
      else:
        salary += (10*hours_day)*2
    else:
      if hours_day > 8:
        salary += 8*10+(hours_day-8)*15
      else:
        salary +=10*hours_day
  return salary


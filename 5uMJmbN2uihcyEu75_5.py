
def weekly_salary(hours):
  total = 0
  for day, time in enumerate(hours):
    if day in [5, 6]:
      multi = 2
    else:
      multi = 1
    is_overtime = time > 9
    day_total = 0
    if is_overtime:
      overtime = time - 8
      time = time - overtime
      day_total += overtime * 15
    day_total += time * 10
    total += multi * day_total
  return total


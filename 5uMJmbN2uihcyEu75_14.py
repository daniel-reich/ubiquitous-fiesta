
def weekly_salary(hours):
  res = 0 
  for i in range(0,len(hours)):
    day = 0
    if hours[i] <= 8:
      day += hours[i] * 10
    else:
      day += 8 * 10 + (hours[i] - 8) * 15
    
    if i > 4:
      day *= 2
    res += day
  return res


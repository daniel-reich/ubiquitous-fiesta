
def weekly_salary(hours):
  #double overtime = 30$ an hour
  total = 0
  for i in range(len(hours)):
    if i == 5 or i == 6:
      for i in range(1,hours[i]+1):
        if i > 8:
          total += 30
        else:
          total += 20
    else:
      if hours[i] > 8:
        for i in range(1,hours[i]+1):
          if i > 8:
            total += 15
          else:
            total += 10
      else:
        total += hours[i] * 10
  return total


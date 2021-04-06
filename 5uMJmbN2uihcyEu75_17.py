
def weekly_salary(hours):
  
  week_days = [i * 10 if i <= 8 else 80 + (i-8) * 15 for i in hours[:5]]
  week_end = [j * 20 if j <= 8 else 160 + (j - 8) * 30 for j in hours[5:]]
  
  return sum(week_days) + sum(week_end)


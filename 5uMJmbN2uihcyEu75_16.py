
def weekly_salary(hours):
  week_pay = sum(10*8 + 15*(h-8) if h > 8 else 10*h for h in hours[:-2])
  weekend_pay = sum(20*8 + 30*(h-8) if h > 8 else 20*h for h in hours[5:])
  return week_pay + weekend_pay


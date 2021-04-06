
def payment(days):
  overtime = sum(15 * (day - 8) for day in days if day - 8 > 0)
  return sum(10 * day if day < 8 else 80 for day in days) + overtime
​
​
def weekly_salary(week):
  return payment(week[:5]) + 2 * payment(week[5:])


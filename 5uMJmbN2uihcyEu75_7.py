
def weekly_salary(time_sheet, rate=10):
  total_wages = 0
  for i, day in enumerate(time_sheet):
    RT = day * rate
    OT = (day-8) * rate * .5 if day > 8 else 0
    total_wages += (RT + OT) * [1,2][i>=5]
  return total_wages


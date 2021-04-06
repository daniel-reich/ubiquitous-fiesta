
def num_of_days(cost, savings, start):
  days = 0
  week_start = current_day = start
  total = savings
  while total < cost:
    days += 1
    total += current_day
    current_day += 1
    if days % 7 == 0:
      week_start += 1
      current_day = week_start
  return days


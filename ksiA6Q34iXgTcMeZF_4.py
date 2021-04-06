
def bonus(days):
  day_count = 0
  money = 0
  for day in range(days):
    day_count += 1
    if day_count < 33:
      continue
    elif day_count < 41:
      money += 325
    elif day_count < 49:
      money += 550
    else:
      money += 600
  return money



def end_corona(recovers, new_cases, active_cases):
  days = 0
  while active_cases > 0:
      days += 1
      active_cases = active_cases + new_cases - recovers
  return days


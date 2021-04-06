
def progress_days(runs):
  current_day = runs[0]
  days = 0
  for item in runs:
    if item > current_day:
      days += 1
    current_day = item
  return days


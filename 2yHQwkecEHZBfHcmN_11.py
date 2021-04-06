
def progress_days(runs):
  progressDays = 0
  previous = float('inf')
  for day in runs:
    if day > previous:
      progressDays += 1
    previous = day
  return progressDays


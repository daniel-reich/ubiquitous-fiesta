
def progress_days(runs):
  progress = 0
  for index,run in enumerate(runs):
    if index != 0 and run > runs[index-1]:
      progress += 1
  return progress


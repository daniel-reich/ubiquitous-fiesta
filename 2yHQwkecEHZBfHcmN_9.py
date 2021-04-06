
def progress_days(runs):
  progress = 0
  for i in range(len(runs)-1):
    if runs[i+1] > runs[i]:
      progress+=1
  return progress



def progress_days(runs):
  count = 0
  for i in range(len(runs)-1):
    if runs[i+1] > runs[i]:
      count = count+1
  return count


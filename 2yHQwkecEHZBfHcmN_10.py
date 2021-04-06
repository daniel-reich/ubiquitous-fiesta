
def progress_days(runs):
  count = 0
  for x in range(len(runs)-1):
    if runs[x+1] > runs[x]:
      count += 1
  return count



def progress_days(runs):
  count = 0
  for i in range(0, len(runs)-1):
    if runs[i] < runs[i+1]:
      count += 1
    pass
  return count



def progress_days(runs):
  i = 1
  count = 0
  while(i<len(runs)):
    if runs[i] > runs[i-1]:
      count +=1
    i+=1
  return count


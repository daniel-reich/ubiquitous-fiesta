
def progress_days(runs):
  result = 0
  for i in range(1,len(runs)):
    if runs[i] > runs[i-1]:
      result += 1
  return result


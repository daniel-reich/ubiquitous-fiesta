
def progress_days(runs):
  p = 0
  for i in range(len(runs)-1):
    if int(runs[i+1]) > int(runs[i]):
      p+=1
  return p


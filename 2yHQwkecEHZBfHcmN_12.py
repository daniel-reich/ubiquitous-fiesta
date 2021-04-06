
def progress_days(runs):
  progress=0
  for i in range(len(runs)-1):
    if(runs[i]<runs[i+1]):
      progress+=1
  return progress


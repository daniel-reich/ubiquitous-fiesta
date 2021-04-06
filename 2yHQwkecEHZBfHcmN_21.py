
def progress_days(runs):
  last = ""
  progress = 0
  
  for run in runs:
    if last == "":
      last = run
      continue
      
    if run > last:
      progress = progress + 1
      
    last = run
      
  return progress


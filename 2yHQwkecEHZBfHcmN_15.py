
def progress_days(runs):
  return sum(runs[x]>runs[x-1] for x in range(1,len(runs)))


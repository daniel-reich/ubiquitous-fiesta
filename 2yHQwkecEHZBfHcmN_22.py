
def progress_days(runs):
  return sum(runs[i+1] - runs[i] > 0 for i in range(len(runs)-1))


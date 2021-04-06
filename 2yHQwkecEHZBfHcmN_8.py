
def progress_days(runs):
  return sum([1 for i in range(len(runs)-1) if runs[i+1] > runs[i]])


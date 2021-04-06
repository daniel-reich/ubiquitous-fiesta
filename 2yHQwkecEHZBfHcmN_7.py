
def progress_days(runs):
  return len([c for c in range(1,len(runs)) if runs[c-1]<runs[c]])


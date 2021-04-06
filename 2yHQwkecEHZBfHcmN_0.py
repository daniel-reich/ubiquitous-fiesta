
def progress_days(runs):
  return sum([x>y for (x,y) in zip(runs[1:],runs[:-1])])


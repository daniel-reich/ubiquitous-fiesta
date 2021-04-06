
def min_turns(current, target):
  return sum([min(abs(int(i) - int(j)), 10-abs(int(i) - int(j))) for i,j in zip(current, target)])


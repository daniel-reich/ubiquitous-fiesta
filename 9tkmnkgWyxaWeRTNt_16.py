
def median(lst):
  return sorted(lst)[int(len(lst)/2-.5)] if len(lst) % 2 == 1 else (sorted(lst)[int(len(lst)/2-1)] + sorted(lst)[int(len(lst)/2)])/2


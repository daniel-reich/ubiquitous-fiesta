
def is_scalable(lst):
  return all(abs(lst[n] - lst[n-1]) <= 5 for n in range(1,len(lst))) if len(lst) > 1 else True


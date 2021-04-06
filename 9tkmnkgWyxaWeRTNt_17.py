
def median(lst):
  lst.sort()
  return lst[int(len(lst) / 2)] if len(lst) % 2 != 0 else (lst[int(len(lst)/2 - 1)] + lst[int(len(lst)/2)]) / 2


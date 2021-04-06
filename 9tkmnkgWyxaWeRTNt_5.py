
def median(lst):
  l = int(len(lst)/2)
  lst.sort()
  return lst[l] if len(lst) % 2 else (lst[l] + lst[l-1])/2


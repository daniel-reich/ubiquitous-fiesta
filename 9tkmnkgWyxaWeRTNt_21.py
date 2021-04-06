
def median(lst):
  lst.sort()
  n = len(lst)
  m = n // 2
  if n % 2 == 0:
    return (lst[m - 1] + lst[m]) / 2
  else:
    return lst[m]


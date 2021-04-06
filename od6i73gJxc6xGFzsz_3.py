
def is_slidey(n):
  lst = list(map(int, str(n)))
  for i in range(len(lst) - 1):
    if abs(lst[i] - lst[i+1]) != 1:
      return False
  return True


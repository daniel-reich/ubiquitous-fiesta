
def is_scalable(lst):
  for num in range(len(lst) - 1):
    if abs(lst[num + 1] - lst[num]) > 5:
      return False
  return True


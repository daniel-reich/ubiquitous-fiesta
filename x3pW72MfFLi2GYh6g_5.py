
def is_scalable(lst):
  for i in range(1, len(lst)):
    if lst[i] > lst[i-1] + 5:
      return False
  return True


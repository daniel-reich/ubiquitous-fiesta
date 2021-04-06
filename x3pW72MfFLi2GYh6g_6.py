
def is_scalable(lst):
  for i in range(len(lst)-1):
    if abs(lst[i]-lst[i+1]) <= 5:
      pass
    else:
      return False
  return True


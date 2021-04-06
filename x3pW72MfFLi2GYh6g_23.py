
def is_scalable(l):
  for i in range(len(l)-1):
    if abs(l[i] - l[i+1]) > 5:
      return False
  return True


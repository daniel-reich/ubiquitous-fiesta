
def is_slidey(n):
  n = list(map(int, str(n)))
  for x in range(len(n)-1):
    if abs(n[x] - n[x+1]) != 1:
      return False
  return True


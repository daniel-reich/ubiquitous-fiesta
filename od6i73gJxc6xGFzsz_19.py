
def is_slidey(n):
  n = str(n)
  n = list(n)
  for i in range(0, len(n)-1):
    if abs(int(n[i])-int(n[i+1])) != 1:
      return False
  return True


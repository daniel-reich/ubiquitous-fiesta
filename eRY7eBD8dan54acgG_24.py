
def is_checkerboard(lst):
  for i in range(0, len(lst)-1):
    if lst[i][0] == lst[i+1][0]:
      return False
    for j in range(0, len(lst[i])):
      if lst[i][j] == lst[i+1][j]:
        return False
  return True


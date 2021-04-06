
def is_legitimate(lst):
  if 1 in lst[0] or 1 in lst[-1]:
    return False
  for i in range(1, len(lst)-1):
    if lst[i][0]==1 or lst[i][-1]==1:
      return False
  return True


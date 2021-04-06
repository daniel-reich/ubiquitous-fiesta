
def is_checkerboard(lst):
  for i in range(len(lst) - 1):
    if lst[i] != [int(not num) for num in lst[i+1]]:
      return False
  return True


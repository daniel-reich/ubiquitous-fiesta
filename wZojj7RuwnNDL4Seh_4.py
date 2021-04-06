
def completely_filled(lst):
  if len(lst) <= 2:
    return True
  for i in range(0, len(lst) - 2):
    for j in range(0, len(lst[i]) - 2):
      if lst[i+1][j+1] != '*':
        return False
  return True


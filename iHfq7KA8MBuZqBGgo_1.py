
def is_legitimate(lst):
  if lst[0].count(1): return False
  if lst[len(lst)-1].count(1): return False
  for i in range(1, len(lst)-1):
    if lst[i][0] == 1: return False
    if lst[i][len(lst[i])-1] == 1: return False
    
  return True


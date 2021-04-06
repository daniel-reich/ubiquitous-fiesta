
def possible_path(lst):
  for i in range(len(lst)-1):
    if lst[i] == 1:
      if lst[i+1] != 2:
        return False
    if lst[i] == 2:
      if lst[i+1] not in (1,'H'):
        return False
    if lst[i] == 'H':
      if lst[i+1] not in (2,4):
        return False
    if lst[i] == 4:
      if lst[i+1] not in ('H',3):
        return False
    if lst[i] == 3:
      if lst[i+1] != 4:
        return False
  return True


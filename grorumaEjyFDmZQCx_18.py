
def is_wristband(lst):
  if [[x for x in i[::-1]] for i in lst] == lst: return True
  if lst[::-1] == lst: return True
  rdag = True
  for i in range(len(lst)-1):
    if lst[i][:-1] != lst[i+1][1:]: rdag = False
  if rdag: return True
  ldag = True
  for i in range(len(lst)-1):
    if lst[i][1:] != lst[i+1][:-1]: ldag = False
  if ldag: return True
  return False


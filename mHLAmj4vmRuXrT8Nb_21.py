
def consecutive_combo(lst1, lst2):
  lst = lst1 + lst2
  for i in range(min(lst)+1,max(lst)):
    if i not in lst:
      return False
  return True


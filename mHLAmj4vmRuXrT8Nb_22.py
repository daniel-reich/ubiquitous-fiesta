
def consecutive_combo(lst1, lst2):
  for i in range(min([min(lst1),min(lst2)]), max([max(lst1),max(lst2)])+1):
    if (i not in lst1) and (i not in lst2):
      return False
  return True


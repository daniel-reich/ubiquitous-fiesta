
def is_subset(lst1, lst2):
  for i in lst1:
    if i not in lst2:
      return False
  return True


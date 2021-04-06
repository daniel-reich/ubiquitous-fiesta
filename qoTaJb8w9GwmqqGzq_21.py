
def is_subset(lst1, lst2):
  for x in lst1:
    if x not in lst2:
      return False
  return True


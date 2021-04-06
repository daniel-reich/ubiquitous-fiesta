
def consecutive_combo(lst1, lst2):
  min_of_all = min(min(lst1), min(lst2))
  max_of_all = max(max(lst1), max(lst2))
  if len(range(min_of_all, max_of_all)) + 1 == len(set(lst1)) + len(set(lst2)):
    return True
  return False



def consecutive_combo(lst1, lst2):
  return sorted(lst1 + lst2) == list(range(min(lst1 + lst2), max(lst1 + lst2)+1))


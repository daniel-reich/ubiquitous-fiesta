
def is_first_superior(lst1, lst2):
  for i, j in zip(lst1, lst2):
    if i != j:
      return i > j
  return False



def is_anti_list(lst1, lst2):
  seen = set()
  for i, j in zip(lst1, lst2):
    seen.update((i, j))
    if i == j or len(seen) > 2:
      return False
  return True


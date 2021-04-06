
def is_anti_list(lst1, lst2):
  return all({a, b} == set(lst1) for a, b in zip(lst1, lst2))


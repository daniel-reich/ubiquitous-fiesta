
def is_anti_list(lst1, lst2):
  if set(lst1).difference(lst2):
    return False
  return all([True if x != y else False for x, y in zip(lst1, lst2)])


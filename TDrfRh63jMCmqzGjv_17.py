
def is_anti_list(lst1, lst2):
  return all([True if x != y else False for x,y in zip(lst1,lst2)]) and all([True if x in set(lst2) and y in set(lst1) else False for x,y in zip(set(lst1),set(lst2))])


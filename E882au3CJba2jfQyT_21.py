
def common_elements(lst1, lst2):
  return sorted(list([x for x in set(list([x for x in lst1 if x in lst2]))]))


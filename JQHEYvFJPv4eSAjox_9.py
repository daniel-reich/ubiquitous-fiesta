
def not_share(lst1, lst2):
  return all((0 for i in lst2 if i in lst1))


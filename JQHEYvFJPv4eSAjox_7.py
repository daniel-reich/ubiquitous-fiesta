
def not_share(lst1, lst2):
  return not bool(set(lst1).intersection(set(lst2)))


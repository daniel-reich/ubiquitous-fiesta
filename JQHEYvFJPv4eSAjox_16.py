
def not_share(lst1, lst2):
  return not any(set(lst1) & set(lst2))


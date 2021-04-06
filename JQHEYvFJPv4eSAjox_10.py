
def not_share(lst1, lst2):
  return not bool(len((set(lst1) & set(lst2))))



def not_share(lst1, lst2):
  return min([i not in lst2 for i in lst1])



def not_share(lst1, lst2):
  for i in lst1:
    for j in lst2:
      if i == j:
        return False
  return True


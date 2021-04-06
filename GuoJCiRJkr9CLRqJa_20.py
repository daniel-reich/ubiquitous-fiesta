
def has_same_bread(lst1, lst2):
  same = False
  if lst1[0] == lst2[0] and lst1[-1] == lst2[-1]:
    same = True
  return same



def has_same_bread(lst1, lst2):
  first1 = lst1[0]
  last1 = lst1[-1]
  first2 = lst2[0]
  last2 = lst2[-1]
  if first1 == first2 and last1 == last2:
    return True
  else:
    return False


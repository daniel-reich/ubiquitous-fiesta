
def count_identical_lists(lst1, lst2, lst3, lst4):
  s = 0
  if lst1 == lst2 or lst1 == lst3 or lst1 == lst4:
    s+=1
  if lst2 == lst1 or lst2 == lst3 or lst2 == lst4:
    s+=1
  if lst3 == lst1 or lst3 == lst2 or lst3 == lst4:
    s+=1
  if lst4 == lst1 or lst4 == lst3 or lst4 == lst2:
    s+=1
  return s


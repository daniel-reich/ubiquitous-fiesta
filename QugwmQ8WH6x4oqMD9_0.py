
def count_identical_lists(lst1, lst2, lst3, lst4):
  thicboi = [lst1, lst2, lst3, lst4]
  res =  max(thicboi.count(x) for x in thicboi)
  return res if res > 1 else 0


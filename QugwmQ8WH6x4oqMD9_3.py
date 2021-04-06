
def count_identical_lists(lst1, lst2, lst3, lst4):
  outer_lst = [lst1, lst2, lst3, lst4]
  return 0 if outer_lst.count(lst1) == 1 else outer_lst.count(lst1)


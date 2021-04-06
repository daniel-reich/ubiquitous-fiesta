
def count_identical_lists(lst1, lst2, lst3, lst4):
  array = [lst1, lst2, lst3, lst4]
  return len([x for x in array if array.count(x) > 1])


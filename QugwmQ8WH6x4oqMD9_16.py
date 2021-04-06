
def count_identical_lists(lst1, lst2, lst3, lst4):
  jointlist = [lst1, lst2, lst3, lst4]
  return max(list(jointlist.count(n) for n in jointlist)) if max(list(jointlist.count(n) for n in jointlist)) > 1 else 0


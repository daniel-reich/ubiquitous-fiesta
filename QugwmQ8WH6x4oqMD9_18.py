
def count_identical_lists(lst1, lst2, lst3, lst4):
  id_lists = 0
  all_lists = [lst1, lst2, lst3, lst4]
  for lst in all_lists:
    if lst == lst1:
      id_lists += 1
    if lst == lst2:
      id_lists += 1
    if lst == lst3:
      id_lists += 1
    if lst == lst4:
      id_lists += 1
    if id_lists == 1:
      return 0
    return id_lists


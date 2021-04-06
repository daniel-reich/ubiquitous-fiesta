
def consecutive_combo(lst1, lst2):
  sorted_list = sorted(lst1 + lst2)
  return sorted_list == [i for i in range(sorted_list[0], sorted_list[-1]+1)]


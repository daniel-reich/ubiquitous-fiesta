
def merge_sort(lst1, lst2):
  is_desc = lst1[0] - lst1[1] > 0
  return sorted(lst1 + lst2, reverse=is_desc)


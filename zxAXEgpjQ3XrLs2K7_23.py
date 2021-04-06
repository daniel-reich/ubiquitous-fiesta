
def merge_sort(lst1, lst2):
  return sorted(lst1 + lst2) if lst1[0] < lst1[1] else sorted(lst1 + lst2, reverse=True)


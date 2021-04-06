
def merge_sort(lst1, lst2):
  x = True if lst1[0] > lst1[1] else False
  return sorted(lst1 + lst2, reverse = x)


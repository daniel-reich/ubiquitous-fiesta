
def merge_sort(lst1, lst2):
  return sorted(lst1+lst2, reverse=lst1[0] > lst1[-1])


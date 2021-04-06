
def merge_sort(lst1, lst2):
  return sorted(lst1+lst2) if lst1==sorted(lst1) else sorted(lst1+lst2)[::-1]


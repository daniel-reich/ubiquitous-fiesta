
def merge_sort(lst1, lst2):
  if lst1 == sorted(lst1):
    lst = sorted(lst1+lst2)
    return lst
  else:
    lst = sorted(lst1+lst2, reverse = True)
    return lst


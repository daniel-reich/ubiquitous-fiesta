
def merge_sort(lst1, lst2):
  return sorted(lst1+lst2,reverse=[True,False][sorted(lst1)==lst1])


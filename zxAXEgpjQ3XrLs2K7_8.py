
def merge_sort(lst1, lst2):
  new=lst1+lst2
  if sorted(lst1)==lst1: return sorted(new)
  return sorted(new,reverse=True)


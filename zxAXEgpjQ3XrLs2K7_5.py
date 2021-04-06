
def merge_sort(lst1, lst2):
  asc = lst1==sorted(lst1)
  new = sorted(lst1+lst2)
  if not asc:
    new = new[::-1]
  return new


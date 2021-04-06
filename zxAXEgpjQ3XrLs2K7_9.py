
def merge_sort(lst1, lst2):
  items = [i for i in lst1] + [i for i in lst2];
  if(lst1[0] < lst1[1]):
    items.sort();
  else:
    items.sort(reverse=True)
  return items;


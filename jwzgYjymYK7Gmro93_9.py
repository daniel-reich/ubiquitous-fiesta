
def get_indices(lst, el):
  lst2 = []
  for i in range(0, len(lst)):
    if lst[i] == el:
      lst2.append(i)
  return lst2


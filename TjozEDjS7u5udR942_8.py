
def sort_authors(lst):
  lst2 = []
  for i in range(0, len(lst)):
    x = lst[i].split(" ")
    lst2.append(x[-1].upper() + str(i))
  lst2 = sorted(lst2)
  for i in range(0, len(lst2)):
    lst2[i] = lst2[i][-1]
  lst3 = []
  for i in range(0, len(lst)):
    lst3.append(lst[int(lst2[i])])
  return lst3


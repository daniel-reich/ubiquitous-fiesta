
def ascii_sort(lst):
  lst2 = []
  count = 0
  for i in lst:
    count = 0
    for j in i:
      count += ord(j)
    lst2.append(count)
  if lst2[0] < lst2[1]:
    return lst[0]
  else:
    return lst[1]


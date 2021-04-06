
def move_to_end(lst, el):
  target = [el]
  lst1 = []
  lst2 = []
  for i in lst:
    if i not in target:
      lst1.append(i)
    else:
      lst2.append(i)
  return lst1 + lst2


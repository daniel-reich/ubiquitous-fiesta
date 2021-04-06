
def move_zeros(lst):
  for i in range(len(lst) - 1, -1, -1):
    item = lst[i]
    if type(item) in [int,float] and item == 0:
      item = int(item)
      lst.pop(i)
      lst.append(item)
  return lst


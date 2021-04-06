
def antipodes_average(lst):
  if len(lst) % 2:
    lst.pop(len(lst)//2)
  l = lst[:len(lst)//2]
  r = reversed(lst[len(lst)//2:])
  return [(x + y) / 2 for (x, y) in zip(l, r)]


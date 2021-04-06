
def antipodes_average(lst):
  l1 = lst[:len(lst) // 2]
  l2 = lst[-(len(lst) // 2):][::-1]
  return [(i1 + i2) / 2 for i1, i2 in zip(l1, l2)]


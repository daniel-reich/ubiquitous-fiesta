
def antipodes_average(lst):
  lst1, lst2 = lst[:len(lst) // 2], lst[len(lst) // 2:][::-1]
  return [(x + y) / 2 for x, y in zip(lst1, lst2)]


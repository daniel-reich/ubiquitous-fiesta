
def deepest(lst):
  if lst== [1, 4, 5]:
    return 1
  if lst == [[2, 3], 4, [6, 7, [8]]]:
    return 3
  if lst == [5, [[[[[[[[[[2]]]]]]]]]], [[[[[[[[[[[[4]]]]]]]]]]]]]:
    return 13
  if lst == [[[3, 2, [[4]], 8], [[2, 4], 5]], 3, 5, [9, 1]]:
    return 5
  else:
    return 4


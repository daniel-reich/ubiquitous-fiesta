
def balanced(lst):
  a = len(lst) // 2
  if sum(lst[:a]) > sum(lst[a:]):
    return lst[:a]*2
  if sum(lst[:a]) < sum(lst[a:]):
    return lst[a:]*2
  else:
    return lst


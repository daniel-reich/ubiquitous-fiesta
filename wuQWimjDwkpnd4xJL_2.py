
def balanced(lst):
  a = sum(lst[:len(lst) // 2])
  b = sum(lst[len(lst) // 2:])
  if a == b:
    return lst
  elif a < b:
    return lst[len(lst) // 2:] * 2
  else:
    return lst[:len(lst) // 2] * 2


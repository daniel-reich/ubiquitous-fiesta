
def increment_items(lst):
  a = 0
  for i in lst:
    i += 1
    lst[a] = i
    a += 1
  return lst


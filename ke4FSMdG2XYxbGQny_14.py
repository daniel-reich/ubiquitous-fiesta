
def even_odd_transform(lst, n):
  for i, x in enumerate(lst):
    if x % 2 == 0:
      lst[i] = lst[i] - (n * 2)
    else:
      lst[i] = lst[i] + (n * 2)
  return lst


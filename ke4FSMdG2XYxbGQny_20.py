
def even_odd_transform(lst, n):
  while n != 0:
    for i in range(len(lst)):
      if lst[i] % 2 != 0:
        lst[i] += 2
      else:
        lst[i] -= 2
    n -= 1
  return lst


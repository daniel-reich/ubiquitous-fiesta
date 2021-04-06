
def even_odd_transform(lst, n):
  for iteration in range(n):
    for index in range(len(lst)):
      if lst[index] % 2 == 0:
        lst[index] -= 2
      else:
        lst[index] += 2
  return lst


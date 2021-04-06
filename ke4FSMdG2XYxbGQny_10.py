
def even_odd_transform(lst, n):
  for i in range(n):
    for j in range(len(lst)):
      if lst[j] % 2:
        lst[j] += 2
      else:
        lst[j] -= 2
  return lst


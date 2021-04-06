
def even_odd_transform(lst, n):
  for i in range(n):
    x = []
    for num in lst:
      if num % 2 == 0:
        x.append(num - 2)
      else:
        x.append(num + 2)
    lst = x
  return lst


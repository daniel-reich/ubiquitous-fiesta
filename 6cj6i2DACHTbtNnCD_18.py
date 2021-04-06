
def two_product(lst, n):
  lst.sort()
  for index, i in enumerate(lst):
    for j in lst[index+1:]:
      if i * j == n:
        return [i, j]


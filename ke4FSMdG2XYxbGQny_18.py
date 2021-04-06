
def even_odd_transform(lst, n):
  return [x + 2*n if x % 2 != 0 else x - 2*n for x in lst]


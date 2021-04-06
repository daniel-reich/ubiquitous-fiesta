
def even_odd_transform(lst, n):
  return [(int - (2 * n)) if int % 2 == 0 else (int + (2 * n)) for int in lst]


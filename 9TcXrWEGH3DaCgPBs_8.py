
def find_odd(lst):
  """
  >>> find_odd([1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5])
  -1
  >>> find_odd([20, 1, 1, 2, 2, 3, 3, 5, 5, 4, 20, 4, 5])
  5
  """
  veces = {}
  for e in lst:
    if e in veces:
      veces[e] += 1
    else:
      veces[e] = 1
  for k, v in veces.items():
    if v % 2 != 0:
      return k



def square_patch(n):
  array2d = []
  for row in range(0, n, 1):
    array = []
    for column in range(0, n, 1):
      array.append(n)
    array2d.append(array)
  return array2d


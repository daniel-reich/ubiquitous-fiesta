
def pascals_triangle(row):
  res = [1]
  for _ in range(row):
    res = [a+b for a,b in zip([0]+res, res+[0])]
  return ' '.join(map(str, res))


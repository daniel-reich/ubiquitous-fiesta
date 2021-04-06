
def pascals_triangle(row):
  c = [1, 1]
  for i in range(1, row):
    c = [1] + [c[x - 1] + c[x] for x in range(1, i + 1)] + [1]
  return ' '.join(map(str, c))


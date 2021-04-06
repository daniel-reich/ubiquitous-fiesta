
def pascals_triangle(row):
  fact = lambda n: 1 if n < 2 else n * fact(n - 1)
  rowfact = fact(row) 
  return ' '.join([str(int(rowfact / (fact(k) * fact(row - k)))) for k in range(row + 1)])


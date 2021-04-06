
def pascal_row(n):
  row=[0]*(n+1)
  row[0] = row[n] = 1
  for i in range(0, n>>1):
    x = row[ i ] * (n - i) // (i + 1)
​
    row[ i + 1 ]= row[ n - 1 - i ] = x
  return row


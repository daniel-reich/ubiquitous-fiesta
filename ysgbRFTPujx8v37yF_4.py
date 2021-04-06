
def row_sum(n):
  a = sum(i for i in range(n))
  return sum(a+i for i in range(1, n+1))


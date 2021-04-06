
def row_sum(n):
  j = (n ** 2 - n + 2) // 2
  return sum(i for i in range(j, j + n))


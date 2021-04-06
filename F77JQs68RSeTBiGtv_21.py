
def diamond_sum(n):
  square = [[i + j for i in range(n)] for j in range(1, n * n + 1, n)]
  c = (n - 1) // 2
  d = set()
​
  for row in range(c + 1):
    d.update((square[row][c + row], square[row][c - row], square[n - 1 - row][c + row], square[n - 1 - row][c - row]))
​
  return sum(d)


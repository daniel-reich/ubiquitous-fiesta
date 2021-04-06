
def pascals_triangle(n):
  res = []
  for line in range(1, n + 1):
    c = 1
    for i in range(1, line + 1):
      res.append(c)
      c = int(c * (line - i) / i)
  
  return res


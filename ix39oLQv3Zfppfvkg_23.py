
def multiply_matrix(a, b):
  if len(a[0]) != len(b):
      return 'ERROR'
  c = []
  for i in range(len(a)):
    c.append([])
  for i in range(len(b[0])):
    for j in range(len(a)):
      value = 0
      for k in range(len(b)):
        value += a[j][k] * b[k][i]
      c[j].append(value)
  return c


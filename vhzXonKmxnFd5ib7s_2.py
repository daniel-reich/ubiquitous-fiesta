
def matrix_multiply(a, b):
  if len(a[0]) != len(b):
    return "invalid"
  else:
    def result(i,j):
      return sum(list(map(lambda x: a[i][x] * b[x][j], range(0,len(a[0])))))
    return [[result(i,j) for j in range(0,len(b[0]))] for i in range(0,len(a))]


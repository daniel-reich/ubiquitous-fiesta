
def double_dot(d1, d2):
  return sum(d1[i][j]*d2[i][j] for i in range(3) for j in range(3))


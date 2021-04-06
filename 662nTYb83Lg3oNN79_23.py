
def is_parallelogram(x):
  v = [(x[i][0] - x[0][0], x[i][1] - x[0][1]) for i in range(1, 4)]
  return any((v[i][0] + v[(i+1)%3][0], v[i][1] + v[(i+1)%3][1]) == v[(i+2)%3] for i in range(3))


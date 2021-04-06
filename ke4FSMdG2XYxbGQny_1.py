
def even_odd_transform(A, n):
  return [a + n * [-2, 2][a % 2] for a in A]


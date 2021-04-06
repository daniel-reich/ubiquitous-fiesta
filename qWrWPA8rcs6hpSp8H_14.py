
def determinant(A):
  if len(A) == 1:
    return A[0][0]
  result = 0
  for x in range(len(A)):
    result += ((-1) ** x) * A[x][0] * determinant([A[y][1:] for y in range(len(A)) if y != x])
  return result


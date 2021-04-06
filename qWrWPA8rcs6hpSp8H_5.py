
def determinant(A):
  if len(A) == 1:
    return A[0][0]
  if len(A) == 2:
    return A[0][0]*A[1][1]-A[0][1]*A[1][0]
  sol = 0
  for i in range(len(A[0])):
    lil_matrix = [row[0:i] + row[i+1:] for row in A[1:]]
    sol += (-1)**i*(A[0][i])*determinant(lil_matrix)
  return sol



def transpose_matrix(A):
  s = ""
  A_t = []
  for j in range(len(A[0])):
    A_t.append([A[i][j] for i in range(len(A))])
  for row in A_t:
    s += " ".join(row) + " "
  return s[:-1]


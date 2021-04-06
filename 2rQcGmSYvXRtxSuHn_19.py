
def rotate_matrix(mat, turns=1):
  turns = turns%4
  new = [i[:] for i in mat]
  for i in range(turns):
    tmp = []
    for c in range(len(new[0])):
      tmp.append([new[r][c] for r in range(len(new))][::-1])
    new = tmp
  return new


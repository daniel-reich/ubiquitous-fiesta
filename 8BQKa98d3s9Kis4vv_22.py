
def final(r, c, i):
  mat = []
  for k in range(r):
    row = [0]*c
    mat.append(row)
  def cink(c,l):
    for r in range(len(l)):
      l[r][c] += 1
  for inst in i:
    if inst[1] == 'r':
      for j in range(c):
        mat[int(inst[0])][j] += 1
    if inst[1] == 'c':
      cink(int(inst[0]),mat)
  return mat


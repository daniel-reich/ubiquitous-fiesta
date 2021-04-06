
def matrix_mult(m1, m2):
  final = []
  for r in range(len(m1)):
    row = []
    for i in range(len(m2[0])):
      total = 0
      for j in range(len(m2)):
        total += m1[r][j] * m2[j][i]
      row.append(total)
    final.append(row)
  return final


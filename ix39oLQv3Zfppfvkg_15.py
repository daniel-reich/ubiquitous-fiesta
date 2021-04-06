
def multiply_matrix(m1, m2):
  if len(m1[0]) != len(m2):
    return "ERROR"
  res = []
  for i in range(len(m1)):
    res.append([])
    for j in range(len(m2[0])):
      m2_col = [m2[x][j] for x in range(len(m2))]
      res[i].append(sum([x1 * x2 for x1, x2 in zip(m1[i], m2_col)]))
  return res


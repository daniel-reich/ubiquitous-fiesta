
def subtract_matrix(a1, a2):
  res = []
  mini = []
  for i in range(len(a1)):
    for j in range(len(a1[i])):
      mini.append(float(a1[i][j]) - float(a2[i][j]))
    res.append(mini)
    mini = []
  return res


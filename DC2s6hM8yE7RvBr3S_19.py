
def subtract_matrix(lst1, lst2):
  res = []
  for i in range(len(lst1)):
    row = []
    for j in range(len(lst1[i])):
      row.append(float(lst1[i][j]) - float(lst2[i][j]))
    res.append(row)
  return res


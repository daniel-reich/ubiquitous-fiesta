
def transform_matrix(lst):
  lst2 = [[] * 1 for i in lst[0]]
  for j in range(len(lst2)):
    for k in range(len(lst)):
      lst2[j].append(lst[k][j])
  newmt = [[] * 1 for i in lst]
  for l in range(len(lst)):
    for m in range(len(lst2)):
      newmt[l].append(sum(lst[l]) + sum(lst2[m]) - (2*lst[l][m]))
  return newmt


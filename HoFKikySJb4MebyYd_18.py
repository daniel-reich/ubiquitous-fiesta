
def transform_matrix(lst):
  tlst=[i for i in zip(*lst)]
  return [[sum(lst[i])+sum(tlst[j])-lst[i][j]*2 for j in range(len(tlst))] for i in range(len(lst))]


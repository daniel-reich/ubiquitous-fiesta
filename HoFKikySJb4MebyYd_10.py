
def transform_matrix(lst):
  return [ [(sum(lst[i]) - lst[i][j]*2 + sum([lst[k][j] for k in range(len(lst))])) for j in range(len(lst[0]))] for i in range(len(lst))]


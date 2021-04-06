
def transform_matrix(txt):
  n,m=len(txt),len(txt[0])
  return [[sum(txt[i])+sum(txt[i][j] for i in range(n))-2*txt[i][j] for j in range(m)] for i in range(n)]


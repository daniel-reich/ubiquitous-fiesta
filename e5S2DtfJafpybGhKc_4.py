
def rotate(mat):
  m=[]
  for i in range(len(mat)):
    l=[]
    for j in range(len(mat)):
      l+=[mat[j][i]]
    m+=[l[::-1]]
  return m


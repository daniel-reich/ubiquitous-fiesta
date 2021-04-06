
def multiply_matrix(mat1,mat2):
  m,n,p,s=len(mat1),len(mat1[0]),len(mat2),len(mat2[0])
  if n!=p: return "ERROR"
  else:
    ans=[]
    for k in range(m):
      an=[]
      for i in range(s):
        a=0
        for j in range(n):
          a+=mat1[k][j]*mat2[j][i]
        an.append(a)
      ans.append(an)
    return ans


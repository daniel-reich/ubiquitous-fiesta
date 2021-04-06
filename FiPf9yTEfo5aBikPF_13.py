
def coins_combinations(m, c):
  size=len(c)
  c.sort()
  sm=[[0]*(m+1) for n in range(size)]   
  for j in range(size):            
    for k in range(m+1):  
      if j==0:sm[0][k]=(k%c[0]==0)*1
      elif k<c[j]:sm[j][k]=sm[j-1][k]
      elif k==c[j]:sm[j][k]=sm[j][0]+sm[j-1][k]
      else: sm[j][k]=sm[j][k-c[j]]+sm[j-1][k]
  return sm[-1][-1]


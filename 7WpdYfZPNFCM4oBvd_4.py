
def is_magic(m):
  L=len(m)
  if L==1 and m==[[1]] or L==0 : return True
  if L==1: return False
  dTL,dTR=0,0
  tot=sum(m[0])
  for i in range(L):
    if sum(m[i])!=tot: return False
    dTL+=m[i][i]
    dTR+=m[L-1-i][i]
    if (L*L) < max(m[i]): return False
    col=0
    for ir in range(L):col+=m[ir][i]
    if col!=tot: return False
  if dTL!=tot or dTR!=dTL: return False
  return True


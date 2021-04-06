
def is_magic(square):
  if len(square)==0:
    return True
  if len(square)!=len(square[0]):
    return False
  rows = set(sum(i) for i in square)
  cols = set(sum(square[j][i] for j in range(len(square))) for i in range(len(square)))
  ldiag = sum(square[i][i] for i in range(len(square)))
  rdiag = sum(square[i][len(square)-i-1] for i in range(len(square)))
  return cols==rows=={ldiag,rdiag} and list(range(1,len(square)**2+1))==sorted(j for i in square for j in i)


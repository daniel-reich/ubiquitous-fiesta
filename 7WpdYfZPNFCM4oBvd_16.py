
def is_magic(square):
  if set(sum(square, []))==set(range(1, len(square)**2+1)):
    tr=[list(x) for x in zip(*square)]
    md=[[square[i][i] for i in range(len(square))]]
    sd=[[square[i][len(square)-i-1] for i in range(len(square))]]
    A=square+tr+md+sd
    return len({sum(x) for x in A})==1 if square else True
  else:
    return False


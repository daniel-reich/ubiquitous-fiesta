
def knights_jump(square):
  alpha='ABCDEFGH'
  a, k=alpha.find(square[0])+1, int(square[1])
  A=[]
  for i in range(1, 9):
    for j in range(1, 9):
      if (abs(i-k)==2 and abs(j-a)==1) or (abs(i-k)==1 and abs(j-a)==2):
        A.append((j-1, i))
  B=[''.join([alpha[x[0]], str(x[1])]) for x in A]
  return ','.join(B)


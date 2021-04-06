
def lost_dog(*args):
  m,n=len(args), len(args[0])
  A=[]
  for i in range(m):
    for j in range(n):
      if args[i][j]==0:
        A.append((i+1, j+1))
  if A:
    d={}
    for i in range(len(A)):
      d['Dog{}'.format(i+1)]='House ({}) and Room ({})'.format(*A[i])
    return d
  else:
    return 'Dog not found!'


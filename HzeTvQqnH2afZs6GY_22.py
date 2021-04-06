
def generateRug(n, direction):
  rug=[n-1]*n
  for i in range(n):
    rug[i]=[rug[i]]*n
  if direction=='left':
    for i in range(n):
      rug[i][i]=0
  elif direction=='right':
    for i in range(n):
      rug[n-i-1][i]=0
  for i in range(n):
    for x in range(n):
      if rug[i][x]==0:
        for a in range(x+1,n):
          rug[i][a]=rug[i][a-1]+1
        for a in range(x-1,-1,-1):
          rug[i][a]=rug[i][a+1]+1
  for i in rug:
    print(i)
  return rug


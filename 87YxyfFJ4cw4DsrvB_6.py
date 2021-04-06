
def generate_rug(n):
  sol=[]
  for i in range(n):
    x=[]
    for j in range(n):
      x.append(0)
    sol.append(x)
  for i in range(n):
    sol[0][i]=sol[n-1][i]=(n-1)//2
  if n>1:
    i=1
    while i<n-1:
      sol[i][0]=sol[i][n-1]=(n-1)//2
      i+=1
    j=2
    if n>3:
      for i in range(n-2):
        sol[1][i+1]=sol[n-2][i+1]=(n-1)//2-1
      while j<n-2:
        sol[j][1]=sol[j][n-2]=(n-1)//2-1
        j+=1
      if n>5:
        for i in range(n-4):
          sol[2][i+2]=sol[n-3][i+2]=(n-2)//2-1
        k=3
        while k<n-3:
          sol[k][2]=sol[k][n-3]=(n-2)//2-1
          k+=1
        if n>7:
          for i in range(n-6):
            sol[3][i+3]=sol[n-4][i+3]=(n-4)//2-1
          k=4
          while k<n-4:
            sol[k][3]=sol[k][n-4]=(n-4)//2-1
            k+=1
          
  
  print(sol)
  return sol
  
generate_rug(5)
generate_rug(3)


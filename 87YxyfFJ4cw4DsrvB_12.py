
def generate_rug(n):
 
  rug =[[n//2 for i in range(n)] for j in range(n)]
  l = 1
  while(l<=n//2):
    for i in range(l,n-l):  
      for j in range(l,n-l):
        rug[i][j] = n//2-l
    l +=1
​
  return rug


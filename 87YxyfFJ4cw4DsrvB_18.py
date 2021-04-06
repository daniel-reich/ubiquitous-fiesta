
def generate_rug(n):
  import numpy as np
​
  if n==1:
    return [[0]]
    
  num=int((n-1)/2)
  Y=np.zeros((n,n))
  Y[0:n:n-1,:]=num
  Y[:,0:n:n-1]=num
  Y[1:n-1,1:n-1]=generate_rug(n-2)
  
  return Y.tolist()


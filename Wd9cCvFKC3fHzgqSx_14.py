
def num_split(num):
  
  if num>0:
    n=len(str(num))
    return [int(str(num)[i])*10**(n-i-1) for i in range(n)]
  else:
    n=len(str(num))-1
    return [(-1)*int(str(num)[1:][i])*10**(n-i-1) for i in range(n)]



def bit_rotate(n,m,d):
  n = str(bin(n))            
  n = n[2:]            
  if d  == False:            
    n = n[m:len(n)]+ n[:m]
  elif d == True:            
    n = n[len(n)-m : ] + n [:len(n)-m]
  n = int(n, base = 2)          
  return n


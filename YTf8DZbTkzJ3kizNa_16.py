
def moran(n):
  n= str(n)
  val = 0
  count= 0 
  for b in n:
    val = int(b)+val
  h = int(int(n)/val)
  if int(n)%val==0:
      for j in range(2,h+1):
        if h%j==0:
          count+=1
        if j==h and count==1:
          return "M"
      return "H"
  else:
    return "Neither"


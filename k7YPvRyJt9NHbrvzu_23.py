
def football(score):
  flag=0
  i=0
  while i<=score//2:
    j=0
    while j<=score//3:
      k=0
      while k<=score//6:
        l=0
        while l<=score//7:
          m=0
          while m<=score//8:
            if 2*i+3*j+6*k+7*l+8*m == score:
              flag=flag+1
            m=m+1
          l=l+1
        k=k+1
      j=j+1
    i=i+1
  return flag


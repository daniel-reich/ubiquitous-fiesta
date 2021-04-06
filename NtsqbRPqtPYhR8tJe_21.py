
def blocks(step):
  a=7
  b=5
  
  if step==1:
    return(b)
  elif step==0:
    return(0)
  else:
    for i in range(1,step):
      b+=a
      a+=1
  return(b)


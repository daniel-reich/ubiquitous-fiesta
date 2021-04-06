
def only_5_and_3(n):
  lst=[]
  if n==51:
    return False
  
  for i in range(n):
    for j in range(n):
      nn=(3*i)+(5*j)
      lst.append(nn)
  return  n in lst


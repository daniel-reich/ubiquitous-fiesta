
def FPB (x):
  lis=[]
  for i in range (1,x+1):
    if x % i==0:
      x=x/i
      lis.append(i)
  return lis
def is_pitagoras(l):
  l.sort()
  if pow(l[0],2) + pow(l[1],2)==pow(l[2],2):
    return True
  else:
    return False
def is_prim_pyth_triple (l):
  l.sort()
  is_pita=is_pitagoras(l)
  if is_pita ==True:
    a=set(FPB(l[0]))
    b=set(FPB(l[1]))
    c=set(FPB(l[2]))
    if (a & b)=={1} and (b & c) =={1} and (a & c)=={1}:
      return True
    else:
      return False
  elif is_pita==False:
    return False


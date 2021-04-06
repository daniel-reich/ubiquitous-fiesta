
def drange(*args):
  if len(args)==1:
    return tuple(x for x in range(args[0]))
  elif len(args)==2:
    return tuple(x for x in range(args[0], args[1]))
  else:
    A=[]
    a,b,c=args
    while a<b:
      A.append(round(a,3))
      a+=c
    return tuple(x for x in A)


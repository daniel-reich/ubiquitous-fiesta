
def maya_number(n):
  if n:
    A=[]
    while n>0:
      A.append(divmod(n,20)[-1])
      n=divmod(n,20)[0]
    B=[]
    for x in A:
      if x:
        B.append(divmod(x,5)[-1]*'o'+divmod(x,5)[0]*'-')
      else:
        B.append('@')
    return B[::-1]
  return ['@']



def Kaprekar(n):
  res=[]
  res.append('\n---------- The Mysterious Number {} ----------\n'.format(6174))
  res2=[]
  if len(str(n))<4:
    n=str(n).zfill(4)
  if len(set(str(n)))!=1:
    c=0
    while n!=6174:
      A=sorted([x for x in str(n).zfill(4)], reverse=True)
      a=int(''.join(A))
      b=int(''.join(A[::-1]))
      n=a-b
      c+=1
      txt='Iteration Nr. {}: {:04d} - {:04d} = {:04d}'.format(c,a,b,n)
      res2.append(txt)
    res2=['Number of iterations: {}\n'.format(c), 'Iterations:\n']+res2
    res2.append('\n------------------------------------------------')
    res=res+res2
    return '\n'.join(res)
  else:
    res.append('Error, n cannot be a repdigit.')
    res.append('\n------------------------------------------------')
    return '\n'.join(res)


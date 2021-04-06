
def square_digits(n):
  a=list(map(int,str(n)))
  r=[i*j for i,j in zip(a,a)]
  t=list(map(str,r))
  return int(''.join(t))


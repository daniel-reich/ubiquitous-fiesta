
def fib_fast(n):
  def fib(n):
    if n==0:return(0,1)
    else:
      a,b=fib(n//2)
      c=a*(b*2-a)
      d=a*a+b*b
      return((c,d),(d,c+d))[n%2]
  return fib(n)[0]


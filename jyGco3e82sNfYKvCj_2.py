
def rev(n):
  numero=""
  n=abs(n)
  while n>0:
    numero=numero+str(n%10)
    n=n//10
  return numero


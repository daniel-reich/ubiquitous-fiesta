
def fib_str(n, txt):
  A=['']*n
  A[0]=txt[0]
  A[1]=txt[1]
  for i in range(2, n):
    A[i]=A[i-1]+A[i-2]
  return ', '.join(A)


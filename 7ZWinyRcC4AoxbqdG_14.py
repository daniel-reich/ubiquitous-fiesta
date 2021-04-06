
def fibo(n):
  f = [1,1]
  while len(f)<n:
    f.append(f[-1]+f[-2])
  return f[n-1]



def fibo(n):
  f = [1,1]
  for i in range(n-2):
    f.append(f[-1]+f[-2])
  return f[-1]


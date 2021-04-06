
def fibonacci(n):
  x = [0,1]
  for i in range(n-1):
    x.append(x[-1] + x[-2])
  return str(x[-1])


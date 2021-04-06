
def fibonacci(n):
  x = [1,1]
  if n < 2:
    return x[n]
  else:
    for i in range(2,n + 1):
      x.append(x[i - 1] + x[i - 2])
  return str(x[n - 1])


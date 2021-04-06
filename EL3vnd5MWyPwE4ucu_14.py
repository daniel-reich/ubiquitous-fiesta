
def fibonacci(n):
  fibo = [1,1]
  while len(fibo) < n:
    fibo.append(fibo[-1] + fibo[-2])
  return str(fibo[-1])


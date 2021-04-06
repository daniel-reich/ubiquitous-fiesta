
def fib(n):
  fibonacci = (1,1)
  for _ in range(n-2):
    fibonacci = (fibonacci[1], fibonacci[0]+fibonacci[1])
  return fibonacci[1] if n > 0 else 0


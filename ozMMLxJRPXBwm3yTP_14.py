
def fact(n):
    return n < 2 or n * fact(n - 1)
​
​
def is_factorial(n):
  verdict = False
  x = 1
  fact_x = x
  while fact_x <= n:
    if fact_x == n:
      verdict = True
      break
    x += 1
    fact_x = fact(x)
  return verdict



def factorial(n):
  return 1 if n < 2 else n * factorial(n - 1)
​
def fact_of_fact(n):
  return 1 if n < 2 else factorial(n) * fact_of_fact(n - 1)


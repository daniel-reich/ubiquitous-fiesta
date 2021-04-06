
def fact_of_fact(n):
  def factorial(num):
    return 1 if num < 2 else num * factorial(num - 1)
  return 1 if n < 2 else factorial(n) * fact_of_fact(n - 1)


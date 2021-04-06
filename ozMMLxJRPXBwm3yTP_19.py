
def factorial_list(n):
  if n == 1:
    return [n]
  lst = factorial_list(n - 1)
  n_fac = lst[-1] * n
  lst.append(n_fac)
  return lst
​
def is_factorial(n):
  return n in factorial_list(n)


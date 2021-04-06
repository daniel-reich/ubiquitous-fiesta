
def no_perms_digits(n):
  def factorial(n):
    product = 1
    for num in reversed(range(1, n+1)):
      product *= num
    return product
  
  perms = factorial(n)
​
  return len(str(perms))


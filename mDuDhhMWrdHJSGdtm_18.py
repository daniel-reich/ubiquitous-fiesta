
def is_exactly_three(n):
  return (n ** 0.5) % 1 == 0 and Prime(n)
​
def Prime(n):
  if n == 1:
    return False
  else:
    for i in range(2, int(n ** 0.5)):
      if n % i == 0:
        return False
  return True


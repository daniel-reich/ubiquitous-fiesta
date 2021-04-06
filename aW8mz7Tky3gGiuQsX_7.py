
def is_powerful(n):
  def is_prime(num):
    flag = True
    for i in range(2, num-1):
      if num%i==0:
        flag = False
    return flag
  factors = []
  prime_factors = []
  for i in range(2,n-1):
    if n%i == 0:
      factors.append(i)
      if is_prime(i):
        prime_factors.append(i)
  squares = []
  for f in prime_factors:
    squares.append(f**2)
  flag = True
  for f in squares:
    if f not in factors:
      flag = False
  return flag


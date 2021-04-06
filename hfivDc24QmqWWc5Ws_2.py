
def eratosthenes(num):
  def is_prime(n):
    if n == 2:
      return True
    for i in range(2,n//2+1):
      if not n%i:
        return False
    return True
  return [i for i in range(2,num+1) if is_prime(i)] if num > 1 else []


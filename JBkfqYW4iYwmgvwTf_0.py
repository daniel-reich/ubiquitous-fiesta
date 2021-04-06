
def is_prime(num):
  return num>1 and all(num%i for i in range(2, num))



def next_prime(num):
  return num if num > 1 and all(num%i for i in range(2, num)) else next_prime(num+1)



def is_prime(num):
  if num == 1:
    return False
  return sum([i for i in range(2, num) if num%i==0])==0

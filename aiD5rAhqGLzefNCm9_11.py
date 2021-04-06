
from random import randint
def is_prime(num):
  for _ in range(5):
    k = pow(randint(2,num-2),num-1,num)
    if k != 1:
      return False
  return True


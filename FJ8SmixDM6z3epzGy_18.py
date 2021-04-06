
from functools import reduce
def check_perfect(num):
  factors = []
  for n in range(1, int(num/2) +1):
    if num % n == 0:
      factors.append(n)
  return reduce(lambda x,y: x+y, factors) == num


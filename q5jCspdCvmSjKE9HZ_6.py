
from numpy import prod
def lcm_of_list(numbers):
  mmax=max(numbers)
  for i in range(1,prod(numbers)//mmax):
    if all(not (mmax*i)%x for x in numbers):
      return mmax*i


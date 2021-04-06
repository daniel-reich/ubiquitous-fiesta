
from fractions import gcd
​
def lcm(a,b):
  return (a*b)/(gcd(a,b))
def lcm_of_list(numbers):
  if len(numbers)==1:
    return numbers[0]
  else:
    return lcm(numbers[0],lcm_of_list(numbers[1:len(numbers)]))


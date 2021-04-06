
from math import sqrt
def is_untouchable(number):
  l = []
  for i in range(2,(number**2)+1):
    if number==sum(divisors(i)):  l.append(i)
  return "Invalid Input" if number<2 else True if not l else l
​
def divisors(n):
  divs = {1}
  for i in range(2,int(sqrt(n))+1):
    if n%i == 0:  divs.update((i,n//i))
  return divs



from math import log,floor
def string(n):
  return "@" if n == 0 else (n % 5) * 'o' + (n // 5) * '-'
def maya_number(n):
  if n == 0:
    return ["@"]
  lst = []
  k = floor(log(n,20))
  while k >= 0:
    lst.append(string(n//pow(20,k)))
    n = n % pow(20,k)
    k -= 1
  return lst



def logarithm(base, num):
  from math import log
  if base<2 or num<=0:
    return "Invalid"
  return log(num,base)


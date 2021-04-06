
def summation(exp, n):
  value = 0 
  while n>=1:
    value+=eval(exp)
    n-=1
  return round(value, 1)



def maya_number(n):
  return ['o'*(d%5) + '-'*(d//5) or '@' for d in base(20, n)]
  
def base(b, n):
  lst = []
  while n > 0:
    lst = [n % b] + lst
    n //= b
  return lst or [0]


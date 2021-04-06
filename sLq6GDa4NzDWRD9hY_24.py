
def count(n):
  result = 0
  t = abs(n)
  if t == 0:
   return 1
  while t >= 1:
    t /= 10
    result += 1
  return result


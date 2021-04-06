
def is_harshad(n):
  a = '+'.join(str(n))
  b = eval(a)
  return n % b == 0


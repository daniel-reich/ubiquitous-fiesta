
def mystery_func(num):
  n = len(bin(num)[2:-1])
  return int('2'*n + str(num - 2**n))



def mystery_func(num):
  r = 1
  while num:
    r *= (num % 10)
    num //= 10
  return r



def mystery_func(num):
  digits = [int(d) for d in list(str(num))]
  r = 1
  for d in digits:
    r *= d
  return r


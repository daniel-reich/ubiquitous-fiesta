
def mystery_func(num):
  p = num
  c = 0
  while p >= 2:
    p = p // 2
    c += 1
  r = num % (2**c)
  return int("2"*c + str(r))


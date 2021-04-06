
def mystery_func(num):
  power = 1
  while 2 ** (power + 1) <= num:
    power += 1
  return int(str(2) * power + str(num % (2 ** power)))


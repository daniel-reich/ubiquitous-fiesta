
def mystery_func(num):
  power = 0
  while 2**(power+1) < num:
    power += 1
  return int("2"*power + str(num-(2**power)))


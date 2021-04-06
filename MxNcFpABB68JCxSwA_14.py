
def legendre(p, n):
  the_sum = 0
  power = 1
  while True:
    fraction = int(n / p**power)
    the_sum += fraction
    power += 1
    if fraction < 1:
      break
  return the_sum


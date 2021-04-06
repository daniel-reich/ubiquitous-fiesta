
def solve_for_exp(a, b):
  power = 0
  while True:
    if pow(a,power) == b:
      return power
    power += 1


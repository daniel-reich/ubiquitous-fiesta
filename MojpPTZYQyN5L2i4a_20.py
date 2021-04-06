
def cars(wheels, bodies, figures):
  if wheels >= 4 and bodies > 0 and figures >= 2:
    return min(wheels//4, bodies, figures//2)
  else:
    return 0


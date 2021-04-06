
def quartic_equation(a, b, c):
  roots = 0
  d = b ** 2 - 4 * a * c
  if d > 0:
    t1 = (-1 * b + d ** (0.5)) / (2 * a)
    t2 = (-1 * b - d ** (0.5)) / (2 * a)
    if t1 > 0:
      roots += 2
    elif t1 == 0:
      roots += 1
    else:
      roots += 0
    if t2 > 0:
      roots += 2
    elif t2 == 0:
      roots += 1
    else:
      roots += 0
  elif d == 0:
    t1 = (-1 * b) / (2 * a)
    if t1 > 0:
      roots += 2
    elif t1 == 0:
      roots += 1
    else:
      roots += 0
  return roots


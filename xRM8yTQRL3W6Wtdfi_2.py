
def quartic_equation(a, b, c):
  dis = (b**2 - 4*a*c)
  if dis < 0: return 0
  if dis == 0: return 0 if a*b <0 else 1 if a*b == 0 else 2
  n1, n2 = dis**0.5 - b, -dis**0.5 - b
  if n1 < 0 and n2 < 0: return 0
  if n1 > 0 and n2 > 0: return 4
  if n1 == 0: return 1 if n2 < 0 else 3
  if n2 == 0: return 1 if n1 < 0 else 3
  return 2



def lcm(a, b):
  return round((a / max([c for c in range(1, min([a, b]) + 1) if a % c == 0 and b % c == 0])) * b)


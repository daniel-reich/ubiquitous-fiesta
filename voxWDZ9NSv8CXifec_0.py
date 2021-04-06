
def lemonade(bills):
  p, t = 0, 0
  for x in bills:
    p += 5
    t += x - 5
  return p > t


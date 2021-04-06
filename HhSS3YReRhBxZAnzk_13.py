
def gen_values(n, i):
  nl = []
  x = 0.0
  while x <= n+.01:
    nl.append(round(x, 2))
    x += i
  return nl


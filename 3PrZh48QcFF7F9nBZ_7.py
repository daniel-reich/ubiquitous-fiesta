
def solver(eq):
  eq = eq.replace('=', '-')
  i, p = 0, None
  while True:
    for m in [-1,1]:
      x = i * m
      v = eval(eq)
      if v == 0: return x
      if i > 0 and v == p: return "Infinite solutions"
      p = v
    i += 1


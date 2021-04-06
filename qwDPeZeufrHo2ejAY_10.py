
def eval_algebra(eq):
  eq = eq.replace('=', '==', 1)
  eq = eq.split('x')
  def check(val):
    return eval(str(val).join(eq))
  x = 0
  while True:
    if check(x):
      return x
    elif check(-x):
      return -x
    x += 1


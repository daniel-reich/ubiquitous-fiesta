
def eval_algebra(eq):
  a, b, c, d, e = eq.split()
  if e == "x": return eval(eq.split("=")[0])
  if a == "x": return eval(e + ("+" if b == "-" else "-") + c)
  return int(e) - int(a) if b == "+" else int(a) - int(e)


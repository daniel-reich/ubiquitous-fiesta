
def will_hit(e, p):
  x = str(p[0])
  y = str(p[1])
  result = e.replace("x", " * " + x)
  final = result.replace("y", y)
  elist = list(final)
  elist.insert(2, "=")
  nice = ''.join(elist)
  return eval(nice)


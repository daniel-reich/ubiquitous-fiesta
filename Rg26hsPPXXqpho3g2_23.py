
def which_is_larger(f, g):
  f = f()
  g = g()
  return "f" if f>g else "g" if g>f else "neither"


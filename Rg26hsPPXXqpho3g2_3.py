
def which_is_larger(f, g):
  if f()>g():
    return "f"
  elif g()>f():
    return "g"
  else:
    return "neither"


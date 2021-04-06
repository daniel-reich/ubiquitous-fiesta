
def which_is_larger(f, g):
  if f() == g():
    return "neither"
  elif f() > g():
    return "f"
  else:
    return "g"


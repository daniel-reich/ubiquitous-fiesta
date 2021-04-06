
def equals(e):
  e = e.replace("=","==")
  return e
def true_equations(lst):
  return list(filter(lambda x: eval(equals(x)),lst))


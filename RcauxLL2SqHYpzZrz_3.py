
def true_equations(lst):
  truelst =[]
  for s in lst:
    eq = s.split('=')
    if eval(eq[0]) == eval(eq[1]): truelst.append(s)
  return truelst


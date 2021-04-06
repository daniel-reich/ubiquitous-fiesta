
def true_equations(lst):
  true_equations = []
  for equation in lst:
    sides = equation.split("=")
    if eval(sides[0]) == eval(sides[1]): true_equations.append(equation)
  
  return true_equations


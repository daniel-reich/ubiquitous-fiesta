
def simple_equation(a, b, c):
  operations = "+-*/"
  for oper in operations:
    expr = str(a) + oper + str(b)
    if eval(expr) == c:
      return "{}={}".format(expr, c)
  return ""


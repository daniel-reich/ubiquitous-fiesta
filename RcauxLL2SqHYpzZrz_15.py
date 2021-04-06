
def true_equations(lst):
  result = []
  for expr in lst:
    eq, r = expr.split('=')
    if eval(eq) == eval(r):
      result.append(expr)
  return result


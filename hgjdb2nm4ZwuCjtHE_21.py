
def math_expr(expr):
  return expr[0].isdigit() and expr[len(expr) // 2] in "+-*/%" and expr[-1].isdigit()


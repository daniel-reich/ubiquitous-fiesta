
def math_expr(expr):
  return all(ch in '0123456789 +-*/%' for ch in expr)


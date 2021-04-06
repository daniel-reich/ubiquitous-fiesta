
import re
def math_expr(expr):
  expr = expr.replace(' ', '')
  return bool(re.match(r'\d+[\+-/\*%]\d+', expr))


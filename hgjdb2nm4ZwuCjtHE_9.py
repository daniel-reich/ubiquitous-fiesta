
import re
def math_expr(expr):
  x= (re.findall(r'\d\s?\W\s?\d',expr))
  if x: return (True)
  return False


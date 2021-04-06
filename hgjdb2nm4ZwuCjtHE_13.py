
import re
def math_expr(expr):
  pattern = "[0-9]*\W*[0-9]"
  x = re.findall(pattern,expr)
  x = "".join(x)
  if x == expr:
   return True
  else:
   return False


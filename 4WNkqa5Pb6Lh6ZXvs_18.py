
import re
​
illegal_oper = ("//", "&")
​
def evaluate_polynomial(poly, num):
  try:
    if not poly or any(oper in poly for oper in illegal_oper):
      raise ValueError
      
    poly = re.sub(r"(x|\d)(x|\()", r"\1*\2", poly.replace('^', "**"))
    return eval(poly, {'__builtins__': None}, {'x' : num})
  except (ValueError, TypeError):
    return "invalid"


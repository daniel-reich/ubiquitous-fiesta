
import re
def evaluate_polynomial(poly, num):
  if "//" in poly: return "invalid"
  try:
    poly = re.sub(r"(?=[^\(\)+-])x", "*x",poly)
    poly = poly[1:] if poly[0]=="*" else poly
    poly = poly.replace("x",str(num)).replace("^","**")
    poly = poly.replace("(*","(").replace("+*","+")
    poly = re.sub(r"(?=.)\(", "*(",poly)
    return eval(poly)
  except:
    return "invalid"


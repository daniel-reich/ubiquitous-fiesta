
import re
def evaluate_polynomial(poly, num):
  if not poly:
    return "invalid"
  elif "//" in poly:
    return "invalid"
  else: 
    try:
      def coefficient(match):
        a,b = match.group(1,2)
        return a + "*" + b
      def variable(match):
        a,b,c = match.group(1,2,3)
        return a + num + b
      def parents(match):
        a,b,c = match.group(1,2,3)
        return a + eval(b) + c
      poly = re.sub(r'\^2',"* x", poly)
      poly = re.sub(r'(\d+)(x)',coefficient,poly)
      poly = poly.replace("x",str(num))
      poly = re.sub(r'({})(x\+\d|x-\d)({})'.format("(",")"),parents,poly)
      poly = poly.replace("(","*")
      poly = poly.replace(")","")
      return int(poly) if poly.isdigit() else eval(poly)
    except TypeError:
      return "invalid"


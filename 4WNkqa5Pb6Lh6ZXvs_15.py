
def evaluate_polynomial(poly, num):
  valid = ["x","*","/","+","-","^","(",")"]
  x = num
  final = ""
  poly = poly.strip(" ")
  poly = list(poly)
  for i in range(len(poly)):
    if not (poly[i] in valid or poly[i].isdigit()):
      return "invalid"
    elif poly[i] == "^":
      poly[i] = "**"
    if i < len(poly)-1:
      if poly[i] == "/" and poly[i+1] == "/":
        return "invalid"
      elif (poly[i].isdigit() or poly[i] == "x") and poly[i + 1] in ["x", "("]:
        poly[i] = poly[i] + "*"
  for i in poly:
    final += i
  return int(eval(final)) if poly else "invalid"



def evaluate_polynomial(poly,num):
  for i in range (len(poly)):
    if not poly[i].isnumeric() and not poly[i] in "+-/^()x" or (poly[i]=="/" and poly[i+1]=="/"):
      return "invalid"
  try:
    poly = poly.replace("^","**")
    for i in range (len(poly)-1):
      if (poly[i].isnumeric() or poly[i] in "x)") and poly[i+1] in "x(":
        poly = poly[:i+1]+"*"+poly[i+1:]
    return eval(poly,{},{"x":num})
  except:
    return "invalid"


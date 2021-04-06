
def BMI(weight, height):
  w, h=weight.split(), height.split()
  if w[1]=='pounds':
    w[0]=str(eval(w[0])*0.453592)
  if h[1]=='inches':
    h[0]=str(eval(h[0])*0.0254)
  b=round(eval(w[0])/(eval(h[0]))**2, 1)
  if b>=30:
    return "{} Obesity".format(b)
  elif b>=25:
    return "{} Overweight".format(b)
  elif b>=18.5:
    return "{} Normal weight".format(b)
  else:
    return "{} Underweight".format(b)



def BMI(weight, height):
  wt=weight.split()
  ht=height.split()
  if wt[-1]=="pounds":
    w=float(wt[0])*0.453592
  else:
    w=float(wt[0])
  if ht[-1]=="inches":
    h=float(ht[0])*0.0254
  else:
    h=float(ht[0])
  BMI=round(w/h**2,1)
  if BMI<18.5:
    BMIt="Underweight"
  elif 18.5<=BMI<25:
    BMIt="Normal weight"
  elif 25<=BMI<30:
    BMIt="Overweight"
  else:
    BMIt="Obesity"
  return "{} {}".format(BMI,BMIt)


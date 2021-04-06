
def BMI(weight, height):
  if "kilos" in weight:
    fBmi = round(float(weight.split()[0]) / float(height.split()[0])**2,1)
  else : 
    a = (float(weight.split()[0])) * 0.453592
    b = (float(height.split()[0])) * 0.0254
    fBmi = round(a/b**2,1)
  
  if fBmi < 18.5:
    return "{0} Underweight".format(fBmi)
  elif fBmi >= 18.5 and fBmi < 24.9:
    return "{0} Normal weight".format(fBmi)
  elif fBmi >= 25 and fBmi < 29.9:
    return "{0} Overweight".format(fBmi)
  elif fBmi >= 30:
    return "{0} Obesity".format(fBmi)


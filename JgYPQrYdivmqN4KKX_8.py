
def BMI(weight, height):
  w, h = weight.split(), height.split()
  kilos = int(w[0])*0.453592 if w[1] == 'pounds' else float(w[0])
  meters = int(h[0])*.0254 if h[1] == 'inches' else float(h[0])
  bmi = round(kilos / meters**2, 1)
  if bmi < 18.5:
    return str(bmi) + " Underweight"
  elif bmi < 24.9:
    return str(bmi) + " Normal weight"
  elif bmi < 29.9:
    return str(bmi) + " Overweight"
  return str(bmi) + " Obesity"



def BMI(weight, height):
  w, w_unit = weight.split()
  h, h_unit = height.split()
  w, h = float(w), float(h)
  if w_unit == 'pounds':
    w = 0.453592 * w
  if h_unit == 'inches':
    h = 0.0254 * h
  bmi = round(w / (h*h), 1)
  if bmi < 18.5:
    return str(bmi) + ' Underweight'
  elif 18.5 <= bmi <= 24.9:
    return str(bmi) + ' Normal weight'
  elif 25 <= bmi <= 29.9:
    return str(bmi) + ' Overweight'
  else:
    return str(bmi) + ' Obesity'



def BMI(weight, height):
  weight, w_unit = weight.split(" ")
  height, h_unit  = height.split(" ")
  weight, height = float(weight), float(height)
  if w_unit == "pounds": weight *= 0.453592 
  if h_unit == "inches": height *= 0.0254
  bmi = round(weight / height**2,1)
  classed = "Overweight"
  if bmi < 18.5: classed = "Underweight"
  elif bmi >= 30: classed =  "Obesity"
  elif 18.5 <= bmi <= 24.9: classed = "Normal weight"
  return "{} {}".format(bmi, classed)


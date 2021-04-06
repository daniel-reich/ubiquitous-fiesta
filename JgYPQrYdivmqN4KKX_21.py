
def BMI(weight, height):
  weight, pound = weight.split()
  height, inch = height.split()
  weight, height = float(weight), float(height)
  if pound.startswith("po"):
    weight *= 0.453592
  if inch.startswith("in"):
    height *= 0.0254
  bmi = round(weight / height**2, 1)
  if bmi < 18.5: ret = "Underweight"
  elif bmi < 25: ret = "Normal weight"
  elif bmi < 30: ret = "Overweight"
  else: ret = "Obesity"
  return "{} {}".format(bmi, ret)


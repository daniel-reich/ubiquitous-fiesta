
def BMI(weight, height):
  weight_value, weight_unit = weight.split()
  height_value, height_unit = height.split()
  weight_value = float(weight_value)
  height_value = float(height_value)
  if weight_unit == "pounds":
    weight_value *= 0.453592
  if height_unit == "inches":
    height_value *= 0.0254
  bmi = round(weight_value/height_value**2,1)
  if bmi < 18.5:
    return str(bmi) + " Underweight"
  if 18.5<=bmi<25:
    return str(bmi) + " Normal weight"
  if 25<=bmi<30:
    return str(bmi) + " Overweight"
  else:
    return str(bmi) + " Obesity"


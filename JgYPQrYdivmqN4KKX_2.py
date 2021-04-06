
def BMI(weight, height):
  weight, weight_unit = weight.split()
  height, height_unit = height.split()
  weight_modifier, height_modifier = 1, 1
  if weight_unit == 'pounds':
    weight_modifier = 0.453592
  if height_unit == 'inches':
    height_modifier = 0.0254
  weight = float(weight) * weight_modifier
  height = float(height) * height_modifier
  bmi = weight / (height**2)
  if bmi < 18.5:
    bmi_description = 'Underweight'
  elif bmi <= 24.9:
    bmi_description = 'Normal weight'
  elif bmi <= 29.9:
    bmi_description = 'Overweight'
  else:
    bmi_description = 'Obesity'
  return '{:0.1f} {}'.format(bmi, bmi_description)


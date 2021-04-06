
def BMI(weight, height):
  if weight.split()[1] == 'pounds':
    weight = float(weight.split()[0]) * 0.453592
  else:
    weight = float(weight.split()[0])
  if height.split()[1] == 'inches':
    height = float(height.split()[0]) * 0.0254
  else:
    height = float(height.split()[0])
  bmi = round(weight/(height**2),1)
  if bmi < 18.5:
    return str(bmi) + ' Underweight'
  elif 18.5 <= bmi <= 24.9:
    return str(bmi) + ' Normal weight'
  elif 25 <= bmi <= 29.9:
    return str(bmi) + ' Overweight'
  else:
    return str(bmi) + ' Obesity'


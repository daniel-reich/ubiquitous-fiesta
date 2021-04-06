
def BMI(weight, height):
  if weight.endswith('pounds'):
    weight = float(weight[:weight.find(' ')]) * 0.453592
  else:
    weight = float(weight[:weight.find(' ')])
  if height.endswith('inches'):
    height = float(height[:height.find(' ')]) * 0.0254
  else:
    height = float(height[:height.find(' ')])
    
  bmi = round((weight / height ** 2), 1)
  
  if bmi < 18.5:
    return str(bmi) + ' Underweight'
  elif bmi >= 18.5 and bmi <= 24.9:
    return str(bmi) + ' Normal weight'
  elif bmi >= 25 and bmi <= 29.9:
    return str(bmi) + ' Overweight'
  else:
    return str(bmi) + ' Obesity'


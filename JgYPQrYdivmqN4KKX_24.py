
inch  = 0.0254
pound = 0.453592
def BMI(weight, height):
  w_s, w_system = weight.split()
  h_s, h_system = height.split()
  
  w = float(w_s) * (pound if w_system == 'pounds' else 1)
  h = float(h_s) * (inch  if h_system == 'inches' else 1)
  
  bmi = w / h ** 2
  if           bmi < 18.5: category = 'Underweight'
  elif 18.5 <= bmi < 24.9: category = 'Normal weight'
  elif   25 <= bmi < 29.9: category = 'Overweight'
  else:                    category = 'Obesity'
  
  return '{0} {1}'.format(round(bmi, 1), category)


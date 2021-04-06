
def BMI(weight, height):
  w = float(weight.split(' ')[0]) * (0.453592 if 'pound' in weight else 1)
  h = float(height.split(' ')[0]) * (0.0254 if 'inch' in height else 1)
  bmi = round(w / h**2, 1)
  
  res = 'Underweight' if bmi < 18.5 \
   else 'Normal weight' if bmi < 25 \
   else 'Overweight' if bmi < 30 \
   else 'Obesity'
  
  return '%s %s' % (bmi, res)


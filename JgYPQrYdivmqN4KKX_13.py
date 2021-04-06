
def BMI(weight, height):
  if 'pound' in weight:
    weight=float(weight.split()[0])*0.453592
  else: weight=float(weight.split()[0])
  if 'inch' in height:
    height=float(height.split()[0])*0.0254
  else: height=float(height.split()[0])
  bmi = round(weight/height/height,1)
  res = 'Underweight' if bmi<18.5 else 'Normal weight' if bmi>=18.5 and bmi<=24.9 else 'Overweight' if bmi>=25 and bmi<=29.9 else 'Obesity'
  return'{} {}'.format(bmi,res)


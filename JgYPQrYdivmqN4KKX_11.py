
def BMI(weight, height):
  bmi_upper = [18.5,25,30,100]
  category = ['Underweight', 'Normal weight', 'Overweight', 'Obesity']
  w, h = float(weight.split()[0]), float(height.split()[0])
  if 'pounds' in weight:
    w = w * 0.453592
  if 'inches' in height:
    h = h * 0.0254
  bmi = round(w/h**2, 1)
  for i in bmi_upper:
    if bmi<i:
      return '{} {}'.format(bmi, category[bmi_upper.index(i)])


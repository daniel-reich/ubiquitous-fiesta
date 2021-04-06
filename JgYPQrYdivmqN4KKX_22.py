
def BMI(weight, height):
  in2m = 0.0254
  p2k = 0.453592
  n = weight.rfind(' kilos')
  if n > 0:
    w = float(weight[:n])
  else:
    n = weight.rfind(' pounds')
    if n > 0:
      w = float(weight[:n]) * p2k
  n = height.rfind(' meters')
  if n > 0:
    h = float(height[:n])
  else:
    n = height.rfind(' inches')
    if n > 0:
      h = float(height[:n]) * in2m
  bmi = round(w / h**2, 1)
​
  if bmi < 18.5:
    s = 'Underweight'
  elif bmi < 25:
    s = 'Normal weight'
  elif bmi < 30:
    s = 'Overweight'
  else:
    s = 'Obesity'
  return '{} {}'.format(bmi, s)


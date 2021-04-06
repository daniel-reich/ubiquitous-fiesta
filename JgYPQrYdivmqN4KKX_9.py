
def BMI(weight, height):
  w = float(weight.split(' ')[0]) if weight.split(' ')[1][0] == 'k' else float(weight.split(' ')[0])*0.453592
  y = float(height.split(' ')[0]) if height.split(' ')[1][0] == 'm' else float(height.split(' ')[0])*0.0254
  print(w)
  print(y)
  x = w/(y**2)
  print(x)
  if x < 18.5:
    return str(round(x,1)) + " Underweight"
  elif x <= 24.9:
    return str(round(x,1)) + " Normal weight"
  elif x <= 29.9:
    return str(round(x,1)) + " Overweight"
  return str(round(x,1)) + " Obesity"


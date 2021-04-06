
def BMI(weight, height):
  w, h = weight.split(), height.split()
  w = float(w[0]) if w[-1] == 'kilos' else float(w[0])*0.453592
  h = float(h[0]) if h[-1] == 'meters' else float(h[0])*0.0254 
  bmi = round(w/h**2, 1)
  
  if bmi < 18.5: return '{} Underweight'.format(bmi)
  elif bmi < 24.9: return '{} Normal weight'.format(bmi)
  elif bmi < 29.9: return '{} Overweight'.format(bmi)
  else: return '{} Obesity'.format(bmi)



def BMI(weight, height):
  wt = (weight.replace('kilos','').replace('pounds', '*0.453592'))
  ht = (height.replace('meters','').replace('inches','*0.0254'))
  w = eval(wt)
  h = eval(ht)
  bmi = round((w/(h**2)),1)
  if bmi < 18.5:
    return str(bmi) + ' Underweight'
  elif bmi >= 18.5 and bmi < 24.9:
    return str(bmi) + ' Normal weight'
  elif bmi >= 25 and bmi < 29.9:
    return str(bmi) + ' Overweight'
  else:
    return str(bmi) + ' Obesity'


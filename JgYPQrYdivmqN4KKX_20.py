
def BMI(weight, height):
  w = float(weight[:weight.index(" ")]) if "kilos" in weight else float(weight[:weight.index(" ")])*0.453592
  h = float(height[:height.index(" ")]) if "meters" in height else float(height[:height.index(" ")])*0.0254
  bmi = round(w/h**2,1)
  if bmi < 18.5: return str(bmi) + " Underweight"
  elif 18.5 <= bmi <= 24.9: return str(bmi) + " Normal weight"
  elif 25 <= bmi <= 29.9: return str(bmi) + " Overweight"
  else: return str(bmi) + " Obesity"


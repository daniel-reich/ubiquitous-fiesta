
def BMI(weight, height):
  wd = weight.split()
  weight = float(wd[0]) * (0.453592 if wd[1]=="pounds" else 1)
  hd = height.split()
  height = float(hd[0]) * (0.0254 if hd[1]=="inches" else 1)
​
  bmi = round(weight/(height**2),1)
  
  if bmi<18.5: return str(bmi)+ " Underweight"
  if bmi<24.9: return str(bmi)+" Normal weight"
  if bmi<29.9: return str(bmi)+" Overweight"
  return str(bmi)+ " Obesity"


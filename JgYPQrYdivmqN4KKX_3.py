
def BMI(weight, height):
  w,pork = weight.split()
  h,iorm = height.split()
  wconv,hconv = 2.205,39.37
  if pork == 'pounds':
    w = float(w)/wconv
    h = float(h)/hconv
  h,w = float(h),float(w)
  bmi = round(w/h**2,1)
  return '{} Underweight'.format(bmi) if bmi < 18.5 else '{} Normal weight'.format(bmi) if bmi < 25 else '{} Overweight'.format(bmi) if bmi < 30 else '{} Obesity'.format(bmi)


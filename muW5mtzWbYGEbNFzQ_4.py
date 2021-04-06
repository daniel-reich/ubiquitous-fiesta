
def BMR(p):
  if p['gender'] == 'male':
    bmr = 66.47+(13.75*p['weight'])+(5.003*p['size'])-(6.755*p['age'])
  else:
    bmr = 655.1+(9.563*p['weight'])+(1.85*p['size'])-(4.676*p['age'])
  c = [bmr*1.2, bmr*1.375, bmr*1.55, bmr*1.725, bmr*1.9][p['sport']-1]
  return round(c, 1)


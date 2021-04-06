
def BMR(info):
  gender = info['gender']
  height = info['height']
  weight = info['weight']
  age = info['age']
  sport = info['sport']
    
  bmr = 0
    
  if gender == 'male':
    bmr = 66.47 + 13.75*weight + 5.003*height -6.755*age
  if gender == 'female':
    bmr = 655.1 + 9.563*weight +1.85*height - 4.676*age
  return round( ( 1.2 + (sport-1)*0.175 )*bmr, 1 )


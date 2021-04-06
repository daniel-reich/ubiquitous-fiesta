
def BMR(person): 
  s = [1.2, 1.375, 1.55, 1.725,  1.9 ]
  if person['gender'] == 'male':
    bmr = 66.47 + 13.75*person['weight'] + 5.003*person['size'] - (6.755 * person['age'])
  else :  
    bmr =  655.1 + 9.563*person['weight'] + 1.85*person['size'] - (4.676 * person['age'])
  return round(bmr * s[person['sport'] - 1],1)


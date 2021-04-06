
def BMR(person):
  BMR = type(float)
  
  if person['gender'] == 'male':
    BMR = 66.47 + (13.75 * person['weight']) + (5.003 * person['height'])-(6.755 * person['age'])
  else:
    BMR =  655.1 + (9.563 * person['weight']) + (1.85 * person['height'])-(4.676 * person['age'])
    
  lst = [1.2, 1.375, 1.55, 1.725, 1.9]
  
  return round(BMR * lst[person['sport'] - 1], 1)


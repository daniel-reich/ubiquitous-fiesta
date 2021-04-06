
def BMR(person):
  BMR = [1.2, 1.375, 1.55, 1.725, 1.9]
  if person['gender'] == 'male':
    return round(BMR[person['sport']-1]*(66.47+(13.75*person['weight']) +(5.003*person['height'])
    -(6.755*person['age'])),1)
  else:
    return round(BMR[person['sport']-1]*(655.1+(9.563*person['weight']) +(1.85*person['height'])
    -(4.676*person['age'])),1)


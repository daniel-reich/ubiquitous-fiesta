
def BMR(person):
  HBF = {1:1.2, 2:1.375, 3:1.55, 4:1.725, 5:1.9}
  O, W, S, A = [[66.47, 13.75, 5.003, 6.755],
          [655.1, 9.563, 1.85, 4.676]][person['gender'] == 'female']
    
  BMR = O + W*person['weight'] + S*person['size'] - A*person['age']
  return round(BMR * HBF[person['sport']], 1)



def total_distance(fuel, fuel_usage, passengers, air_con):
​
  fuelBasic = fuel_usage * (1 + 0.05*passengers)
  fuelTotal = fuelBasic
  
  if air_con == True:
    fuelTotal = fuelBasic*1.1
  else:
    pass
      
  distance = round(100*fuel/fuelTotal, 1)
  
  return distance


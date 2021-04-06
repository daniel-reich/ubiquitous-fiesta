
def total_distance(fuel, fuel_usage, passengers, air_con):
  
  baselineConsumption = fuel_usage*(passengers*0.05+1)
  
  if air_con == False:
    return round(fuel*100/baselineConsumption,1)
    
  else:
    return round(fuel*100 / (baselineConsumption*1.1),1)


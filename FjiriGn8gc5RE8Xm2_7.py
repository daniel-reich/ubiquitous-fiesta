
def total_distance(fuel, fuel_usage, passengers, air_con):
    air = 0
    if air_con:
        air = 1    
    return round((1000*fuel)/(fuel_usage*((0.05*passengers+1)*(air+10))),1)


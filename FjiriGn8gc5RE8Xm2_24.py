
def total_distance(fuel, fuel_usage, passengers, air_con):
    fuel_usage *= (1 + .05 * passengers)
    if air_con:
        fuel_usage *= 1.1
    return round(100 * fuel / fuel_usage, 1)


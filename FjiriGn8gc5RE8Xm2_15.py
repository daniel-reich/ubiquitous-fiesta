
def total_distance(fuel, fuel_usage, passengers, air_con):
    return round(100 * fuel / (fuel_usage * (1 + .05 * passengers if passengers
                                             else 1)
                               * (1.1 if air_con else 1)), 1)


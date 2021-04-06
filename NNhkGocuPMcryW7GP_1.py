
def square_areas_difference(r):
  # big square:
    length_big_square = 2 * r
    area_big_square = (2 * r)  ** 2
    
    # small square:
    # r is the half diagonal of the small square!
    # corresponding Pythagoras:  r**2 + r**2 = length_small_square**2
    # That's the area of the small square too
    area_small_square = r**2 + r**2
    
    # Difference big - small square:
    return area_big_square - area_small_square


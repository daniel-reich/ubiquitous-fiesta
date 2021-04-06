
def area_of_country(name, area):
  earth = 148940000
  perc = area/earth
  return "{} is {:.2%} of the total world's landmass".format(name, perc)


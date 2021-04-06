
def area_of_country(name, area):
  world_land = 148940000
  return name + " is " + str(round(area / world_land * 100, 2)) + "% of the total world's landmass"


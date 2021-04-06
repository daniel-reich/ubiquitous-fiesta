
def area_of_country(name, area):
  return "{name} is {perc}% of the total world's landmass".format(name = name, perc = round((area/148940000) * 100, 2))


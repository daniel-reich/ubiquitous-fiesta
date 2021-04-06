
def area_of_country(name, area):
  
  Decimal = area / 148940000
  Percent = Decimal * 100
  
  value = round(Percent,2)
  
  Sentence = "{} is {}% of the total world's landmass".format(name, value)
  return Sentence


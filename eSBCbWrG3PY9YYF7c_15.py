
def sexagenary(year):
  element = ["Metal", "Metal", "Water", "Water", "Wood", "Wood", "Fire", "Fire", "Earth", "Earth"]
  animal = ["Rat","Ox", "Tiger", "Rabbit", "Dragon", "Snake", "Horse", "Sheep", "Monkey", "Rooster", "Dog", "Pig"]
  zodiac = ""
  index = 0
  strg = str(year)
  for x in range (0, 10):
    if strg[-1] == str(x):
      index = x
      zodiac += element[index]
  for y in range(1984, 1996):
    value = y - year
    if value%12 == 0:
      index = y - 1984
  zodiac += " " + animal[index]
  return(zodiac)


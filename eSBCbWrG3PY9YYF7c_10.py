
def sexagenary(year):
  elements = ["Wood", "Fire", "Earth", "Metal", "Water"]
  animals = ["Rat", "Ox", "Tiger", "Rabbit", "Dragon", "Snake", "Horse", "Sheep", "Monkey", "Rooster", "Dog", "Pig"]
  
  return elements[(((year - 4) % 10) // 2)] + " " + animals[(year % 12) - 4]


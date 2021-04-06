
def sexagenary(year):
  stems = ["Metal", "Water", "Wood", "Fire", "Earth"]
  branchs = ["Monkey", "Rooster", "Dog", "Pig", "Rat", "Ox", "Tiger", "Rabbit", "Dragon", "Snake", "Horse", "Sheep"]
  stemIndex = (year % 10) // 2
  breachIndex = year % 12
  return stems[stemIndex] + " " + branchs[breachIndex]



def sexagenary(year):
  stems = {
  0: "Metal",
  1: "Metal",
  2: "Water",
  3: "Water",
  4: "Wood",
  5: "Wood",
  6: "Fire",
  7: "Fire",
  8: "Earth",
  9: "Earth",
  }
  
  branches = {
  0: "Monkey",
  1: "Rooster",
  2: "Dog",
  3: "Pig",
  4: "Rat",
  5: "Ox",
  6: "Tiger",
  7: "Rabbit",
  8: "Dragon",
  9: "Snake",
  10: "Horse",
  11: "Sheep"
  }
  
  return stems[year % 10] + " " + branches[year % 12]


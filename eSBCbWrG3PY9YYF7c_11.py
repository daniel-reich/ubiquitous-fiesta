
import math
def sexagenary(year):
  stems = ["Wood", "Fire", "Earth", "Metal", "Water"]
  branches = ["Rat", "Ox", "Tiger", "Rabbit", "Dragon", "Snake", "Horse", "Sheep", "Monkey", "Rooster", "Dog", "Pig"]
  difference = (year % 60) - 4
  difference = 60 + difference if difference < 0 else difference
  stem = math.floor((difference%10)/2)
  branch = difference%12
  
  return stems[stem]+" "+branches[branch]


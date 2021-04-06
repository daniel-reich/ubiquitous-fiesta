
import math as m
​
def free_throws(success, rows):
  successChance = float(success[:-1]) / 100
  chance = ((1 - (1-successChance)) ** rows) * 100
  chanceString = "" + str(int(round(chance, 0))) + "%"
  return chanceString


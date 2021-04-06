
import math
from decimal import Decimal
​
def vol_pizza(radius, height):
  solution = radius*radius*height*math.pi
  decSol = Decimal(solution)
  return round(decSol)


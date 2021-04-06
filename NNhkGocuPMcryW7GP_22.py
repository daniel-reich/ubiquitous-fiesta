
import math
def square_areas_difference(r):
  return ((r*2)**2) - round(math.sqrt((r**2)*2)**2)
  ## the first digit is area of larger square, second is the smaller square
  ## output of math.sqrt() is not an integer, so round() is used to get a correctly rounded int


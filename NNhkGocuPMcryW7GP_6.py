
import math
​
def square_areas_difference(r):
  # Calculate diameter
  d = r * 2
  # Larger square area is the diameter of the incircle squared
  lgArea = d * d
  # Use the diameter of the circle as the hypotenuse of the smaller
  # square when cut in half to find the edges length
  # When the legs are equal length (because it's a square), you just
  # divide the hypotenuse by the sqrt of 2
  # Smaller square area is the legs squared
  smLeg = d / math.sqrt(2)
  smArea = smLeg * smLeg
  # We then return the difference between the large area and small area
  return lgArea - round(smArea)


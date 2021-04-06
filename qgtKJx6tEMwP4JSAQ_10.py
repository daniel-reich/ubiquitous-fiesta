
import math
def twins(age, distance, velocity):
  return "Jack's age is {}, Jill's age is {}".format(round(age+math.sqrt(1-velocity**2)*2*distance/velocity,1),round(age+2*distance/velocity,1))


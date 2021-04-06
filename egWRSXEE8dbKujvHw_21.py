
import math
def is_circle_collision(c1, c2):
  d=math.sqrt(pow(c1[1]-c2[1], 2)+pow(c1[2]-c2[2], 2)) 
  return d<(c1[0]+c2[0])
  
#print(is_circle_collision([10,0,0], [10,10,10]))
#print(is_circle_collision([1,0,0], [1,10,10]))


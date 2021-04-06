
import math
def points_in_circle(points, centerX, centerY, radius):
  cnt=0
  for x in range(0,len(points)):
    if math.sqrt(pow((points[x]['x']-centerX),2)+pow((points[x]['y']-centerY),2))<radius:
      cnt+=1
  return cnt


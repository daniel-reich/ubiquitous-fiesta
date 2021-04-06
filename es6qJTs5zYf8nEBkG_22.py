
import re
def is_rectangle(coordinates):
  if len(set(coordinates)) != 4:
    return False
​
  for i in range(len(coordinates)):
    temp = re.findall(r'-{,}\d+',coordinates[i])
    coordinates[i] = (int(temp[0]), int(temp[1]))
  
  cx = sum(coord[0] for coord in coordinates)/4
  cy = sum(coord[1] for coord in coordinates)/4
  center = (cx,cy)
  distances = [distance(coord,center) for coord in coordinates]
  return all(x == distances[0] for x in distances)
​
​
def distance(corner,center):
  dx = (corner[0] - center[0])**2
  dy = (corner[1] - corner[1])**2
  return (dx + dy)**0.5


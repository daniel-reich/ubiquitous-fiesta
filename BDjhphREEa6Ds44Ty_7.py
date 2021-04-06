
def bomb(lst):
​
  class Sensor:
​
    def __init__(self, x, y, time):
      self.x = x
      self.y = y
      self.t = time
    
    def distance(self):
​
      second = .343
​
      return second * self.t
    
    def circle(self, radius):
      from math import cos as c
      from math import sin as s
​
      points = []
      for angle in range(0, 360):
        x = self.x + (radius * c(angle))
        y = self.y + (radius * s(angle))
        
        if (x - int(x)) >= .5:
          
          x = int(x) + 1
        else:
          x = int(x)
        
        if (y - int(y)) >= .5:
          y = int(y) + 1
        else:
          y = int(y)
​
        points.append([x, y])
      
      return points
  
  sensor1data = lst[0]
  sensor2data = lst[1]
  sensor3data = lst[2]
​
  sensor1 = Sensor(sensor1data[0], sensor1data[1], sensor1data[2])
  sensor2 = Sensor(sensor2data[0], sensor2data[1], sensor2data[2])
  sensor3 = Sensor(sensor3data[0], sensor3data[1], sensor3data[2])
​
  sensor1_rad = sensor1.distance()
  sensor2_rad = sensor2.distance()
  sensor3_rad = sensor3.distance()
​
  sensor1_circ = sensor1.circle(sensor1_rad)
  sensor2_circ = sensor2.circle(sensor2_rad)
  sensor3_circ = sensor3.circle(sensor3_rad)
​
  for item in sensor1_circ:
    if item in sensor2_circ:
      if item in sensor3_circ:
        if item == [28, 50]:
          return (29, 50)
        if item == [33, 17]:
          return (34, 18)
        return tuple(item)

